# Legume Labs: inspect the work

Legume Labs explores small developer tools and local-AI product decisions. This focused portfolio shows a check runner, an estimate's limits, and a concrete correction to the checks behind this site.

**Start with the evidence:** [run this site's offline checks](docs/showcase-start.md#run-the-showcase-checks), [inspect the QA runner result](assets/qa-quickstart-output.txt), or [read the before/after lesson](docs/what-i-learned.md). No account, private service or model inference is needed for the offline checks.

**Source publication approved, October 4, 2026.** Independent review accepted this bounded static case study. The complete QA quickstart passes in an exact-source Ubuntu CI run; its regression test is now merged. The earlier failed macOS replay remains documented, with its cause unresolved. Review acceptance is not fleet health, hiring qualification or deployment. [Exact evidence and disposition](docs/showcase-evidence.md).

## Check orchestration: QA Kit

QA Kit runs repository-selected checks and records JSON results. Its disposable synthetic quickstart calls the real runner for a passing case, a failed documentation check and a failed unit test.

At [merged source `595812b2`](https://github.com/stevekkall-beansgc/qa-kit/tree/595812b22269527dfad3952b1739eba7a36ad1ba), the [Ubuntu CI test run](https://github.com/stevekkall-beansgc/qa-kit/actions/runs/37214014615) executes the real CLI with sample verification. The passing case, both meaningful failure cases and final sample comparison pass, with driver and child Python 3.12.14. [PR #11](https://github.com/stevekkall-beansgc/qa-kit/pull/11) adds only a regression test; the runner and sample are unchanged from v0.7.5. Versioned publication is recorded separately in [QA Kit Releases](https://github.com/stevekkall-beansgc/qa-kit/releases). [Actual results](assets/qa-quickstart-output.txt) and [reproduction instructions](docs/showcase-start.md#qa-kit-reproduction-status) include the preserved earlier failure. These are synthetic runner results, not fleet health, arbitrary-command sandboxing or security certification.

## A lesson: test the failure your check claims to catch

The original showcase checker discarded a link's heading fragment. A file could exist while its target section did not. The correction added bounded anchor checks and negative fixtures; a follow-up made CI execute those fixtures.

[Inspect the change and its limits](docs/what-i-learned.md). The source establishes the mechanism and correction, not measured visitor impact or who personally implemented each part. This is an artifact-level review story, not a recorded integration of private agent systems. [Agent-workflow boundary](AGENT-SYSTEMS.md).

## Product judgment: BeanFit

BeanFit estimates whether a model/runtime combination may fit a device. Its [version-bound README](https://github.com/stevekkall-beansgc/beanfit/blob/1d5d960c9d94436e46f74247ef53d24d7fad4634/README.md) exposes assumptions alongside recommendations. Speed bands are assumed, quality numbers editorial, and the shared MoE speed formula is not architecture-calibrated. This candidate includes no new benchmark, catalog refresh or BeanFit execution. It is supporting source to inspect, not a verified flagship recommendation.

## Contribution and contact

Stephen Kall identifies the design of QA Kit and the checker correction as his work. This is owner-confirmed design attribution, not a claim that he personally wrote or ran every part. Implementation, test work, drafting and review involved material AI assistance; the linked history does not establish a complete person-by-person implementation or validation account.

For showcase questions or problem reports, Stephen's nominated contact is [beanscg@gmail.com](mailto:beanscg@gmail.com). Send sensitive reports privately rather than posting credentials, personal data or vulnerabilities in public Issues. No response-time commitment is made. QA Kit also documents [private vulnerability reporting](https://github.com/stevekkall-beansgc/qa-kit/blob/29f4d08911eed530cf09c855306b145078de8805/SECURITY.md); this pass does not verify monitoring of that separate route.

Stephen permits the retained showcase diagrams/assets to be publicly reused. That permission is not a new repository-wide license or exhaustive third-party provenance clearance. The scoped publication review and its limits are recorded in the evidence ledger.

## Further reading

- [Current candidate evidence](docs/showcase-evidence.md) — exact sources, checks, claims and unresolved blockers.
- [Historical source register](SOURCE-REGISTER.md) — dated observations, not current product status.
- [Delivery guide](DELIVERY.md) and [review runbook](docs/SHOWCASE-REVIEW-RUNBOOK.md) — existing process context, not proof that every repository follows every stage.
- [Editing and verification commands](AGENTS.md).

Older portfolio diagrams and evidence indexes remain historical artifacts. This candidate does not re-qualify other products, hosted services, private systems, rights or the entire repository history. Passing static checks cannot clear those matters.
