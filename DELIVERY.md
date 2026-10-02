# Product and Delivery Guide

This guide describes four separate products, two shared developer tools, and a reusable release path. It is a portfolio and delivery overview, not a map of deployed services or direct technical dependencies.

![Review path from product-owned code through configured checks to a versioned release and its public evidence](assets/release-flow.svg)

## 1. Product boundaries

The products address different jobs. Their public repositories and release pages are separate, and one product's evidence should not be read as evidence for another.

- **Bean Counter** is a local SQLite billing CLI. Its [v0.9.0 release](https://github.com/stevekkall-beansgc/bean-counter/releases/tag/v0.9.0) records platform-specific native qualification and limitations. The original v0.3.0 walkthrough remains historical. No hosted billing or payment processing is implied.
- **BeanFit** estimates model and runtime fit for a device and makes uncertainty visible. Its sample output is an estimate, not a performance benchmark.
- **BeanFit App** provides an account and device registration flow for BeanFit recommendations. GitHub metadata lists a public service URL, but this evidence refresh did not qualify the hosted customer journey. Registration saves a snapshot; automatic refresh and delivered update alerts are not demonstrated here.
- **Jumping Beans** presents a shopper-controlled offer journey. The September 25 overview recorded owner-confirmed frozen status; current work-state intent was not reconfirmed in this refresh. Its public showcase does not imply active storefront partnerships or live commerce operations.

## 2. Shared developer tools

These public developer tools can provide shared checks, but project-by-project use must be verified from each repository:

1. **QA Kit** reads a repository-owned manifest to select checks and record results.
2. **Gate Kit** applies a documentation and check contract in workflows configured to use it.
3. Product repositories keep the tests that exercise their behavior beside the product code.

These descriptions explain what the tools do. They do not assert that every product repository has adopted the same manifest or gate.

## 3. Reusable release path

Where a repository configures the shared tools, the review path is:

1. Product code and its tests live in the product repository.
2. QA Kit runs the checks selected by that repository's manifest.
3. Gate Kit applies the declared documentation and check contract in the configured local or CI workflow.
4. A reviewed change may be published as a versioned release tied to source.
5. Release notes, demos, CI results, binaries, checksums, and build records provide evidence when supplied.

To confirm adoption for a particular product, inspect its manifest and CI workflow. A release of QA Kit or Gate Kit proves the tools exist; it does not prove every product uses them.

## 4. Status labels

| Label | Meaning here |
| --- | --- |
| **Public source** | A public repository can be inspected. This does not mean its service is publicly accessible. |
| **Released** | A versioned public release exists. This alone says nothing about production use. |
| **Demonstrated** | A public showcase, walkthrough, or reproducible local demo exists. It is not customer adoption evidence. |
| **Deployed · owner-confirmed** | Deployment status comes from the owner's workspace, not a public service URL. It does not imply public visitor access. |
| **Service URL listed** | Public metadata declares a URL. Its presence does not verify reachability, deployed build identity or customer-journey acceptance. |
| **Unreleased source candidate** | A local proposed change, not merged source, a published release or a deployed correction. |
| **Ongoing / frozen / planned** | Work-state labels are owner-confirmed or explicitly documented; they are not inferred from a release date. |

## 5. Evidence route

- [Bean Counter v0.9.0](https://github.com/stevekkall-beansgc/bean-counter/releases/tag/v0.9.0) → [version-bound billing quickstart](https://github.com/stevekkall-beansgc/bean-counter/blob/2487dcfa9333b54c8622fd826e289fcaccb7ee22/docs/billing-quickstart.md).
- [BeanFit five-minute showcase at reviewed source](https://github.com/stevekkall-beansgc/beanfit/blob/9a9dc02fb297a5c4ba3fe8938c96084f18adb7fb/README.md#five-minute-showcase). Assumed bands and editorial quality are not measured calibration.
- [QA Kit showcase at reviewed source](https://github.com/stevekkall-beansgc/qa-kit/blob/38c7a7bfc078038cfd624ef58d24315e7230e0fe/README.md#five-minute-public-showcase) → [Gate Kit synthetic demo at reviewed source](https://github.com/stevekkall-beansgc/gate-kit/blob/38741affd2034f9b110b4a302ecfc08c4046f722/README.md#2-run-the-synthetic-demo).
- [Jumping Beans public showcase](https://devpost.com/software/jumping-beans) → [v0.11.0 release](https://github.com/stevekkall-beansgc/jumping-beans/releases/tag/v0.11.0).

The [current evidence index](docs/CURRENT-PUBLIC-EVIDENCE-20261002.md) records exact sources, material claims and unresolved limits. The [source register](SOURCE-REGISTER.md) retains its September 25 history. Neither index promotes local candidate patches into released capabilities.
