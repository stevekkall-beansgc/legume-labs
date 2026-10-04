# Start with bounded evidence

The local checks below exercise this static portfolio's checker and regression fixtures. QA Kit's separate full CLI/sample journey now passes in the version-bound supported CI environment. Neither route proves fleet health or publication clearance.

## Run the showcase checks

Prerequisites: an inspected copy of this showcase source candidate and Python 3.12. No package installation, model download, credential or service is required. From the repository root:

```sh
python3.12 -B scripts/check_showcase.py
python3.12 -B -m unittest discover -s scripts -p 'test_*.py' -v
```

Expected: the checker exits 0; the fixture suite exits 0. The fixtures include rejected missing anchors, misleading HTML IDs, escaped paths and malformed SVG, plus CI-contract checks. Test-owned temporary fixtures are removed by the suite. Do not run unfamiliar code or manifests merely because a check passed elsewhere.

[The candidate check record](../assets/showcase-check-results.txt) records actual results for this candidate. It does not show a newly published CI run. The [lesson](what-i-learned.md) connects these checks to their historical correction.

The checker intentionally skips remote destinations and supports a bounded subset of local Markdown anchors. Success means the checks it implements passed; it does not mean all links are available, every renderer agrees, or the prose, privacy, rights and security claims are valid.

## QA Kit reproduction status

Selected merged source: [QA Kit `595812b22269527dfad3952b1739eba7a36ad1ba`](https://github.com/stevekkall-beansgc/qa-kit/tree/595812b22269527dfad3952b1739eba7a36ad1ba), [test-only PR #11](https://github.com/stevekkall-beansgc/qa-kit/pull/11), merged October 4. Versioned publication is recorded separately in [QA Kit Releases](https://github.com/stevekkall-beansgc/qa-kit/releases). Its runner, quickstart and committed sample are byte-identical to base v0.7.5, `29f4d089`. The [contribution guide](https://github.com/stevekkall-beansgc/qa-kit/blob/595812b22269527dfad3952b1739eba7a36ad1ba/CONTRIBUTING.md) documents Ubuntu/Python 3.12. In an inspected checkout of that source, with `python3` resolving to Python 3.12, run:

```sh
python3 -B examples/synthetic_quickstart.py --verify-sample examples/synthetic_quickstart_report.json
```

Expected overall exit: 0, with all three scenario PASS lines, `PASS  sample report verified: examples/synthetic_quickstart_report.json` and final `synthetic quickstart OK (3/3 scenarios, all output in disposable dirs)`. No account, package installation, model, paid service or private fleet manifest is required. Run only inspected code: QA manifests can execute commands, and are not an arbitrary-command sandbox.

The [normal Ubuntu CI job](https://github.com/stevekkall-beansgc/qa-kit/actions/runs/37214014615) passed 160 tests and the stdlib check on this exact commit. The new test invokes the real CLI with sample verification, checks overall exit 0 and empty stderr, and requires all five exact result lines. Its successful output records driver/child Python 3.12.14 on Linux. The PR gate passed too; the main-only self-hosted job did not run on the PR. No workflow, runner, product or sample was changed, and no manual dispatch or CI retry occurred.

The scenarios use synthetic repositories and call the real runner; they are not real customer failures. The committed sample normalizes fields. The [transcript](../assets/qa-quickstart-output.txt) distinguishes actual failed and successful results. Temporary directories/reports are cleaned up automatically; no persistent configuration or service is installed. Underlying raw JSON reports are not separately retained. A missing scenario line, nonzero overall exit or sample mismatch is a failed run; preserve it rather than dropping the flag or rewriting the expected sample.

### Preserved earlier observations

An earlier October 4 macOS replay of base `29f4d089` used driver Python 3.12.14 but did not retain the child interpreter's version. All three scenario assertions passed, then sample verification failed and the overall exit was 1. In a separate passing-case-only diagnosis, driver 3.12.14/child 3.9.6 matched the sample; the mismatch was not reproduced. Earlier [Ubuntu CI](https://github.com/stevekkall-beansgc/qa-kit/actions/runs/37129167180) verified the passing case/sample only. A later complete local 3.12.14 replay and the new supported CI result add distinct evidence; none establishes the original failure's cause or retroactively changes it into a pass.

If a new replay fails, record source, driver and child versions and actual output. Stop that proof until the failure is understood; the successful named CI environment is not a promise of support for every interpreter or platform.

## Inspect instead of running

- [Before/after checker lesson](what-i-learned.md): exact public source, negative fixtures and CI follow-through.
- [Candidate claims and evidence](showcase-evidence.md): what is observed, synthetic, inferred or still unknown.
- [BeanFit source](https://github.com/stevekkall-beansgc/beanfit/blob/1d5d960c9d94436e46f74247ef53d24d7fad4634/README.md): estimated fit and its explicit assumptions; no new execution here.
