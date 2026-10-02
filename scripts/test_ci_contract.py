"""Regression coverage for the owned showcase CI execution contract."""

from pathlib import Path
import re
import unittest


class ShowcaseCIContract(unittest.TestCase):
    def setUp(self):
        root = Path(__file__).resolve().parents[1]
        self.instructions = (root / "AGENTS.md").read_text(encoding="utf-8")
        self.workflow = (root / ".github/workflows/validate.yml").read_text(encoding="utf-8")
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


if __name__ == "__main__":
    unittest.main()
