#!/usr/bin/env python3
"""Check local files, ordinary Markdown heading anchors and SVG XML.

This is an offline artifact check, not a complete Markdown renderer, remote
link checker or claim verifier. ATX headings and explicit HTML IDs are covered;
other renderer-generated anchors need separate review.
"""

from html.parser import HTMLParser
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import unquote, urlparse
import xml.etree.ElementTree as ET


class HTMLIDs(HTMLParser):
    """Read real attributes, not data-id or id-shaped text in another value."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()

    def handle_starttag(self, tag, attrs):
        self.ids.update(value for name, value in attrs if name == "id" and value)


def markdown_anchors(content: str) -> set[str]:
    """Collect simple GitHub-style ATX slugs outside fenced code blocks."""
    anchors: set[str] = set()
    visible: list[str] = []
    fence: str | None = None
    for line in content.splitlines():
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if marker:
            run = marker.group(1)
            if fence is None:
                fence = run
            elif run[0] == fence[0] and len(run) >= len(fence) and not line[marker.end():].strip():
                fence = None
            continue
        if fence is not None:
            continue
        visible.append(line)
    # Comments can span lines. Keep their IDs and headings out of both paths.
    rendered = re.sub(r"<!--.*?(?:-->|$)", "", "\n".join(visible), flags=re.S)
    html = HTMLIDs()
    # Inline-code examples are text, not real HTML elements. Heading slugs below
    # retain their code text, whereas the HTML path must omit those spans.
    html.feed(re.sub(r"(?<!`)(`+)(?!`)(.*?)(?<!`)\1(?!`)", "", rendered, flags=re.S))
    for line in rendered.splitlines():
        heading = re.match(r"^ {0,3}#{1,6}\s+(.+?)\s*$", line)
        if not heading:
            continue
        title = re.sub(r"\s+#+\s*$", "", heading.group(1))
        title = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", title)
        title = re.sub(r"<[^>]+>", "", title).lower()
        slug = "".join(char for char in title if char in "-_ " or unicodedata.category(char)[0] not in "PS").replace(" ", "-")
        unique = slug
        counter = 1
        while unique in anchors:
            unique = f"{slug}-{counter}"
            counter += 1
        anchors.add(unique)
    anchors.update(html.ids)
    return anchors


def check(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []

    for source in sorted(root.rglob("*.md")):
        if ".git" in source.parts:
            continue
        if not source.resolve().is_relative_to(root):
            errors.append(f"{source.relative_to(root)}: Markdown source escapes repository")
            continue
        content = source.read_text(encoding="utf-8")
        for destination in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            destination = destination.strip().strip("<>")
            parsed = urlparse(destination)
            if parsed.scheme or parsed.netloc or destination.startswith("//"):
                continue
            target = unquote(parsed.path)
            local = (source.parent / target).resolve() if target else source.resolve()
            if not local.is_relative_to(root):
                errors.append(f"{source.relative_to(root)}: local target escapes repository {destination}")
                continue
            if not local.is_file():
                errors.append(f"{source.relative_to(root)}: missing local target {destination}")
                continue
            if parsed.fragment and local.suffix.lower() == ".md":
                anchor = unquote(parsed.fragment)
                if anchor not in markdown_anchors(local.read_text(encoding="utf-8")):
                    errors.append(f"{source.relative_to(root)}: missing Markdown anchor {destination}")

    for diagram in sorted(root.rglob("*.svg")):
        if not diagram.resolve().is_relative_to(root):
            errors.append(f"{diagram.relative_to(root)}: SVG source escapes repository")
            continue
        try:
            ET.parse(diagram)
        except ET.ParseError as exc:
            errors.append(f"{diagram.relative_to(root)}: invalid SVG XML: {exc}")

    return errors


def main() -> int:
    errors = check(Path(__file__).resolve().parents[1])

    if errors:
        print("\n".join(errors))
        return 1
    print("Local Markdown targets, supported heading anchors and SVG XML are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
