# Legume Labs

Legume Labs is Stephen Kall's portfolio of separate software products and
experiments. The projects solve different problems; QA Kit and Gate Kit provide
reusable delivery tools for repositories that adopt them.

This overview explains what each project helps with, how the tools fit together,
and where to inspect the work. Project releases belong to their individual
repositories; a release of this overview does not release the products.

## At a glance

![Portfolio and delivery map: four separate product projects, QA Kit and Gate Kit as shared developer tools, and a conditional review path from product code to a versioned release and public evidence.](assets/system-map.svg)

[Open the full-size portfolio map](assets/system-map.svg). The map explains
roles and a reusable process, not deployed services or universal adoption.

## Public products

| Project | What it helps with | What to inspect |
| --- | --- | --- |
| [Bean Counter](https://github.com/stevekkall-beansgc/bean-counter) | Keep billing records through a local SQLite command-line workflow. | [Version-bound billing quickstart](https://github.com/stevekkall-beansgc/bean-counter/blob/2487dcfa9333b54c8622fd826e289fcaccb7ee22/docs/billing-quickstart.md). The older v0.3.0 synthetic walkthrough is historical; no hosted billing or payment processing is implied. |
| [BeanFit](https://github.com/stevekkall-beansgc/beanfit) | Estimate which local models and runtimes may fit a device's memory budget. | [CLI and assumptions at reviewed source](https://github.com/stevekkall-beansgc/beanfit/blob/1d5d960c9d94436e46f74247ef53d24d7fad4634/README.md). Recommendations are estimates, not measured inference benchmarks; quality ratings are editorial. |
| [BeanFit App](https://github.com/stevekkall-beansgc/beanfit-app) | Keep an account-linked device profile and recommendation snapshot. | [Account and pairing flow](https://github.com/stevekkall-beansgc/beanfit-app/blob/e9e68ce0819e0ea98947ace49f894353391e80b9/README.md). Snapshot storage is distinct from automatic refresh and delivered update alerts, which are not demonstrated here. |
| [Jumping Beans](https://github.com/stevekkall-beansgc/jumping-beans) | Explore a conversational shopping journey designed for participating storefronts. | [Project overview](https://github.com/stevekkall-beansgc/jumping-beans). Prototype demonstrations do not establish live partner commerce or operational delivery and analytics. |

The links describe source and demonstrations, not a promise that every project
is deployed or production-ready. The [delivery guide](DELIVERY.md) explains
product boundaries; the [source register](SOURCE-REGISTER.md) preserves dated
observations rather than asserting current operational status.

## Shared developer tools

Product code and behavior tests stay in the owning repository. The shared tools
run or assess that repository's declared checks; inspect its manifest and CI
workflow to confirm adoption.

| Tool | Role | Where to start |
| --- | --- | --- |
| [QA Kit](https://github.com/stevekkall-beansgc/qa-kit) | Runs repository-selected checks and records passing, failing or unusable-configuration outcomes. | [Disposable synthetic quickstart](docs/showcase-start.md#qa-kit-reproduction-status): one passing run, one failed documentation check and one failed unit test. |
| [Gate Kit](https://github.com/stevekkall-beansgc/gate-kit) | Applies a documentation and check contract in configured local and CI workflows. | [Repository and synthetic demo](https://github.com/stevekkall-beansgc/gate-kit). A verdict is not independent security certification. |

## Agent systems

![Historical agent capability map: BeanMind for context, Agency for approved execution and Beanstalk for offline evaluation, with human handoffs and separate support for scheduling, tool selection, model experiments and shared contracts.](assets/agent-systems.svg)

[Open the full-size capability map](assets/agent-systems.svg). This restores the
September 25 role overview: **BeanMind** supplies context, **Agency** executes
approved work, and **Beanstalk** compares judgments and records lessons offline.
People carry context and results between them; automatic transfer is not
established here. These are historical roles and proposed demonstrations, not
current runtime qualification or a recorded connected demo.

The supporting roles are separate: **Bean Sched** owns recurring-work timing;
**Bean Skillz** curates tools and keeps context focused; **Model Harness** supports
model-quality experiments; **Bean Commons** supplies shared structures and
contracts. [The agent guide](AGENT-SYSTEMS.md) distinguishes this role map from
the narrower correction story that can actually be inspected here.

## How changes reach a release

![Five-stage delivery path: product-owned code and tests, QA Kit where configured, Gate Kit where configured, reviewed versioned release, then inspection of public evidence. The diagram lists how to confirm adoption and what a release alone cannot prove.](assets/release-flow.svg)

[Open the full-size release path](assets/release-flow.svg). To check whether a
project follows it, inspect the repository's manifest, workflow and source-bound
release records. Notes, demos, CI results and artifacts establish only what they
actually show—not customer adoption, fleet health or deployment.
[The delivery guide](DELIVERY.md) explains these checks.

## Start with QA Kit

The simplest complete example needs no account, private service or model.
[Inspect the captured output](assets/qa-quickstart-output.txt), then
[reproduce the quickstart](docs/showcase-start.md#qa-kit-reproduction-status).
The complete Ubuntu run passed; the earlier failed macOS replay remains
documented. These are synthetic check-runner results, not fleet-health proof.

## What the work taught us

The original link checker confirmed that a file existed but ignored its heading
fragment. The correction added anchor checks and negative fixtures, then made
CI execute those fixtures. [Inspect the before and after](docs/what-i-learned.md).

## Contribution and contact

Stephen designed QA Kit and the checker correction. Implementation,
validation, drafting and review involved material AI assistance; this is not
a claim that he personally wrote every line or ran every check.

Questions or problem reports: [beanscg@gmail.com](mailto:beanscg@gmail.com).
Send sensitive reports privately. QA Kit's separate security reporting route
is documented in its repository.

## Further reading

- [Exact sources, results and publication limits](docs/showcase-evidence.md).
- [Detailed case study and asset reuse terms](README-REFERENCE.md).
- [Historical source register](SOURCE-REGISTER.md).
- [Delivery guide](DELIVERY.md) and [editing instructions](AGENTS.md).
