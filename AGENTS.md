# Repository guidance

This is a static public portfolio made of Markdown and SVG. Keep every project
claim tied to a public source or clearly labeled as owner-confirmed. Distinguish
current capability from planned work and proposed demonstrations.

Private agent-system names and high-level roles are approved for this overview.
Keep private source links, code, prompts, credentials, personal data, and
operational details out of the public repository. Do not imply system integration
or automation where a person carries context between systems.

There is no application runtime. The CI workflow checks local Markdown targets
and SVG XML, then runs the offline checker and CI-contract regression suite.

## Test commands

Run `python3 scripts/check_showcase.py` for the repository-owned static check.
The QA manifest and CI workflow use the same command.

Run `python3 -m unittest discover -s scripts -p 'test_*.py' -v` for all offline
regression fixtures. The same command is required in the artifact-validation CI
job; fixture success does not verify remote links, product claims or live services.
