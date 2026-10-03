"""Regression coverage for the owned showcase CI execution contract."""

from pathlib import Path
import re
import unittest


CHECKOUT = "actions/checkout@11d5960a326750d5838078e36cf38b85af677262"
GATE = "stevekkall-beansgc/gate-kit/.github/workflows/compliance.yml@v0.4.23"


def active_lines(workflow):
    """Normalize the owned plain, indented YAML; comments are not controls.

    This is a narrow source contract, not a general YAML parser. The sensitive
    mappings must retain the explicit block form below, with no extra inputs,
    duplicate keys, aliases or overrides. A format change requires review.
    """
    return [text for line in workflow.splitlines()
            if (text := re.sub(r"\s+#.*$", "", line).rstrip())
            and not text.lstrip().startswith("#")]


def mapping_block(lines, index):
    indent = len(lines[index]) - len(lines[index].lstrip())
    end = index + 1
    while end < len(lines) and len(lines[end]) - len(lines[end].lstrip()) > indent:
        end += 1
    return lines[index:end]


def workflow_boundary_errors(workflow, *, gate=False):
    lines = active_lines(workflow)
    errors = []
    if any("\t" in line for line in lines):
        errors.append("explicit space indentation required")
    # One workflow-wide read ceiling; job overrides and duplicate mappings fail.
    permissions = [index for index, line in enumerate(lines)
                   if re.match(r"\s*['\"]?permissions['\"]?\s*:", line)]
    if (len(permissions) != 1
            or mapping_block(lines, permissions[0]) != ["permissions:", "  contents: read"]):
        errors.append("explicit workflow contents: read ceiling required without overrides")
    uses = [match.group(1) for line in lines
            if (match := re.fullmatch(r"\s*(?:- )?uses:\s*(.+)", line))]
    if uses != [GATE if gate else CHECKOUT]:
        errors.append("exact reviewed action or reusable workflow identity required")
    if gate:
        # The inherited workflow remains on its authenticated existing version.
        caller = ["  compliance:", "    if: github.ref == 'refs/heads/main'",
                  f"    uses: {GATE}", "    with:", "      repo: bean-labs",
                  "      full: false"]
        if "jobs:" not in lines or lines[lines.index("jobs:") + 1:] != caller:
            errors.append("reviewed main-only caller and inputs required without overrides")
    else:
        # The owned job has only a runner and steps. A new job-level mapping
        # (including an alias merge) must not bypass the token ceiling checks.
        if "  validate:" not in lines:
            errors.append("owned validate job required")
        else:
            job = mapping_block(lines, lines.index("  validate:"))
            if any(line.startswith("    ") and not line.startswith("     ")
                   and line not in ("    runs-on: ubuntu-latest", "    steps:")
                   for line in job[1:]):
                errors.append("unexpected validate job mapping requires review")
        checkout = [f"      - uses: {CHECKOUT}", "        with:",
                    "          persist-credentials: false"]
        starts = [index for index, line in enumerate(lines)
                  if line.startswith("      - uses:")]
        if len(starts) != 1 or mapping_block(lines, starts[0]) != checkout:
            errors.append("checkout must disable credential persistence without extra inputs")
    return errors


class ShowcaseCIContract(unittest.TestCase):
    def setUp(self):
        root = Path(__file__).resolve().parents[1]
        self.instructions = (root / "AGENTS.md").read_text(encoding="utf-8")
        self.workflow = (root / ".github/workflows/validate.yml").read_text(encoding="utf-8")
        self.gate_workflow = (root / ".github/workflows/gate.yml").read_text(encoding="utf-8")
        self.active_lines = [line for line in self.workflow.splitlines()
                             if line.strip() and not line.lstrip().startswith("#")]
        self.run_commands = [match.group(1) for line in self.active_lines
                             if (match := re.fullmatch(r"\s*run:\s*(.+)", line))]

    def test_ci_runs_all_owned_fixture_tests(self):
        self.assertIn("python3 -m unittest discover -s scripts -p 'test_*.py' -v",
                      self.run_commands)

    def test_existing_artifact_check_and_job_identity_retained(self):
        self.assertIn("python3 scripts/check_showcase.py", self.run_commands)
        self.assertIn("  validate:", self.active_lines)
        self.assertIn("name: Validate showcase artifacts", self.active_lines)

    def test_test_execution_is_not_conditionally_skipped_or_soft_failed(self):
        self.assertFalse(any(re.match(r"\s*(?:if|continue-on-error):", line)
                             for line in self.active_lines))

    def test_repo_instructions_document_full_regression_command(self):
        self.assertIn("python3 -m unittest discover -s scripts -p 'test_*.py' -v",
                      self.instructions)

    def test_owned_checkout_and_read_ceiling(self):
        self.assertEqual(workflow_boundary_errors(self.workflow), [])

    def test_existing_gate_caller_and_read_ceiling(self):
        self.assertEqual(workflow_boundary_errors(self.gate_workflow, gate=True), [])

    def test_job_identity_and_independent_runs_retained(self):
        lines = active_lines(self.workflow)
        self.assertEqual([line for line in lines if re.match(r"  [\w-]+:$", line)
                          and lines.index(line) > lines.index("jobs:")], ["  validate:"])
        self.assertFalse(any(re.match(r"    name:", line) for line in lines))
        for workflow in (self.workflow, self.gate_workflow):
            self.assertFalse(any(re.match(r"\s*(?:concurrency|cancel-in-progress):", line)
                                 for line in active_lines(workflow)))


class WorkflowBoundaryNegatives(unittest.TestCase):
    workflow = ("permissions:\n  contents: read\njobs:\n  validate:\n"
                "    steps:\n" + f"      - uses: {CHECKOUT}\n"
                "        with:\n          persist-credentials: false\n")
    gate_workflow = ("permissions:\n  contents: read\njobs:\n  compliance:\n"
                     "    if: github.ref == 'refs/heads/main'\n" + f"    uses: {GATE}\n"
                     "    with:\n      repo: bean-labs\n      full: false\n")

    def test_reviewed_fixture_passes_with_provenance_comment(self):
        self.assertEqual(workflow_boundary_errors(self.workflow.replace(
            CHECKOUT, CHECKOUT + " # v4.4.0")), [])
        self.assertEqual(workflow_boundary_errors(self.gate_workflow, gate=True), [])

    def test_mutable_or_different_checkout_pin_rejected(self):
        for ref in ("actions/checkout@v4", "actions/checkout@" + "0" * 40):
            with self.subTest(ref=ref):
                self.assertTrue(workflow_boundary_errors(self.workflow.replace(CHECKOUT, ref)))

    def test_persistence_missing_true_or_commented_rejected(self):
        control = "          persist-credentials: false\n"
        for replacement in ("", "          persist-credentials: true\n",
                            "          # persist-credentials: false\n"):
            with self.subTest(replacement=replacement):
                self.assertTrue(workflow_boundary_errors(self.workflow.replace(control, replacement)))

    def test_credential_or_checkout_input_override_rejected(self):
        for extra in ("          token: unexpected\n", "          ref: main\n",
                      "          persist-credentials: true\n", "          <<: *inputs\n"):
            with self.subTest(extra=extra):
                self.assertTrue(workflow_boundary_errors(self.workflow + extra))

    def test_read_ceiling_missing_commented_or_widened_rejected(self):
        for workflow in (self.workflow, self.gate_workflow):
            for replacement in ("", "# permissions:\n#   contents: read\n",
                                "permissions: write-all\n", "permissions:\n  contents: write\n",
                                "permissions:\n  contents: read\n  id-token: write\n"):
                with self.subTest(gate=workflow == self.gate_workflow, replacement=replacement):
                    changed = workflow.replace("permissions:\n  contents: read\n", replacement)
                    self.assertTrue(workflow_boundary_errors(changed, gate=workflow == self.gate_workflow))

    def test_job_permission_or_duplicate_ceiling_override_rejected(self):
        for workflow in (self.workflow, self.gate_workflow):
            for extra in ("    permissions: write-all\n", "    permissions:\n      contents: write\n",
                          '    "permissions": write-all\n', "    <<: *job\n"):
                with self.subTest(extra=extra, gate=workflow == self.gate_workflow):
                    changed = workflow.replace("jobs:\n", "permissions:\n  contents: read\njobs:\n")
                    self.assertTrue(workflow_boundary_errors(changed, gate=workflow == self.gate_workflow))
                    changed = workflow.replace("  validate:\n", "  validate:\n" + extra).replace(
                        "  compliance:\n", "  compliance:\n" + extra)
                    self.assertTrue(workflow_boundary_errors(changed, gate=workflow == self.gate_workflow))

    def test_gate_upgrade_or_input_override_rejected(self):
        for old, new in (("@v0.4.23", "@main"), ("full: false", "full: true"),
                         ("repo: bean-labs", "repo: other"),
                         ("      full: false", "      full: false\n      runner: beans-mac")):
            with self.subTest(new=new):
                self.assertTrue(workflow_boundary_errors(self.gate_workflow.replace(old, new), gate=True))


if __name__ == "__main__":
    unittest.main()
