"""Offline regressions for the bounded static artifact checker."""

from pathlib import Path
import tempfile
import unittest

from check_showcase import check, markdown_anchors


class ShowcaseChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def test_valid_same_and_cross_file_anchors(self):
        self.write("README.md", "# Start here\n[here](#start-here)\n[other](docs/guide.md#usage-1)\n")
        self.write("docs/guide.md", "# Usage\n# Usage\n")
        self.assertEqual(check(self.root), [])

    def test_missing_same_file_anchor(self):
        self.write("README.md", "# Start\n[broken](#missing)\n")
        self.assertIn("missing Markdown anchor", check(self.root)[0])

    def test_missing_cross_file_anchor(self):
        self.write("README.md", "[broken](guide.md#wrong)\n")
        self.write("guide.md", "# Correct\n")
        self.assertIn("missing Markdown anchor", check(self.root)[0])

    def test_encoded_path_and_fragment(self):
        self.write("README.md", "[guide](<guide%20one.md#caf%C3%A9>)\n")
        self.write("guide one.md", "# Café\n")
        self.assertEqual(check(self.root), [])

    def test_fences_not_headings_or_html_ids(self):
        content = "# Real\n```md\n# Fake\n<a id='fake'></a>\n```\n~~~\n# Also fake\n~~~\n"
        self.assertEqual(markdown_anchors(content), {"real"})

    def test_formatting_duplicates_and_explicit_id(self):
        content = "# **Use** `CLI`!\n# **Use** `CLI`!\n<a id='custom'></a>\n"
        self.assertEqual(markdown_anchors(content), {"use-cli", "use-cli-1", "custom"})

    def test_data_id_and_attribute_text_are_not_real_ids(self):
        self.write("README.md", '[bad](#not-an-id)\n<a data-id="not-an-id" title="id=decoy"></a>\n')
        self.assertEqual(markdown_anchors('<a data-id="not-an-id" title="id=decoy"></a>'), set())
        self.assertIn("missing Markdown anchor", check(self.root)[0])
        self.assertEqual(markdown_anchors('<span id="actual"></span><!-- <a id="comment"> -->'), {"actual"})

    def test_multiline_comments_and_inline_code_are_not_anchors(self):
        hidden = '<!--\n<a id="hidden"></a>\n# Hidden heading\n-->\n`<a id="inline"></a>`\n'
        self.write("README.md", "[bad](#hidden)\n" + hidden)
        self.assertEqual(markdown_anchors(hidden), set())
        self.assertIn("missing Markdown anchor", check(self.root)[0])
        self.assertEqual(markdown_anchors('<a\n id="actual"></a>\n# `CLI`\n'), {"actual", "cli"})

    def test_remote_links_not_claimed_verified(self):
        self.write("README.md", "[remote](https://example.invalid/a#missing)\n[relative](//example.invalid/b)\n")
        self.assertEqual(check(self.root), [])

    def test_missing_target(self):
        self.write("README.md", "[broken](missing.md)\n")
        self.assertIn("missing local target", check(self.root)[0])

    def test_outside_target_and_symlink_refused(self):
        outside = self.root.parent / (self.root.name + "-outside.md")
        outside.write_text("# Outside\n", encoding="utf-8")
        self.addCleanup(outside.unlink)
        (self.root / "alias.md").symlink_to(outside)
        self.write("README.md", f"[outside](../{outside.name})\n[alias](alias.md)\n")
        errors = check(self.root)
        self.assertEqual(sum("local target escapes repository" in error for error in errors), 2)
        self.assertTrue(any("Markdown source escapes repository" in error for error in errors))

    def test_svg_xml_failure(self):
        self.write("assets/map.svg", "<svg>")
        self.assertIn("invalid SVG XML", check(self.root)[0])


if __name__ == "__main__":
    unittest.main()
