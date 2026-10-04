# Lesson: test the failure your check claims to catch

The consequential change here is small: a portfolio link checker moved from checking whether a file existed to checking a bounded set of section targets, then its regression fixtures became part of CI. The public source supports that change. It does not establish a user incident, personal implementation credit or measured impact.

## Before: a weaker passing result

The [original checker](https://github.com/stevekkall-beansgc/legume-labs/blob/4ae9f0184322614f5e6b008207a6961d0fa86f1c/scripts/check_showcase.py) split a destination at `#` and kept only the file path. A same-file fragment became an empty target and was skipped; a cross-file target only needed the file to exist.

Consequently, an example such as a page with a `Start` heading and a link to a missing section could pass. That is an inference from the inspected old source, not a newly executed historical incident or evidence that a visitor encountered it.

Keeping a file-only check would have been simpler, but its pass could not support a section-navigation claim. A complete Markdown renderer would offer broader compatibility but add scope and dependencies. The implemented correction chose bounded offline checks; these alternatives are present-day analysis, not a reconstructed historical debate.

## Correction: exercise the negative cases

The [correction diff](https://github.com/stevekkall-beansgc/legume-labs/compare/4ae9f0184322614f5e6b008207a6961d0fa86f1c...5e161327a9b4ad3760174a1e47fd1fabd94c7398) added checks for ordinary ATX-heading slugs and actual HTML ID attributes, confined local paths and parseable SVG.

Its [negative fixtures](https://github.com/stevekkall-beansgc/legume-labs/blob/5e161327a9b4ad3760174a1e47fd1fabd94c7398/scripts/test_check_showcase.py) include missing same-file and cross-file anchors, misleading `data-id` attributes, IDs inside comments/code, escaped paths and malformed SVG. These are synthetic tests of a mechanism, not historical production failures.

## Follow-through: run the fixtures where the verdict is produced

At the first correction, CI still invoked only the artifact checker. The [follow-up diff](https://github.com/stevekkall-beansgc/legume-labs/compare/5e161327a9b4ad3760174a1e47fd1fabd94c7398...474a186fb12cd332d1680777d8a259ff42f33e73) added unittest fixture discovery to the normal validate job and tests of that workflow contract.

The selected base source, [`b4c703878f777f366540572546af666e832227c4`](https://github.com/stevekkall-beansgc/legume-labs/tree/b4c703878f777f366540572546af666e832227c4), retains the checker correction and fixture execution. Its [existing validate run](https://github.com/stevekkall-beansgc/legume-labs/actions/runs/37129166772) was observed through GitHub's API on October 4 as successful, including the artifact-check and fixture steps. That is base-source CI evidence, not proof of this later documentation/assets revision. [New local candidate checks](../assets/showcase-check-results.txt) are separate.

## What to carry forward

A validator's pass is only as strong as the failure cases it checks and the workflow that actually executes them. Put a meaningful negative case beside each consequential claim, and preserve the difference between source inspection and observed execution.

This parser is not a full Markdown renderer and skips remote links. The change cannot establish claim truth, privacy, asset rights, deployment, reviewer accuracy, customer benefit or long-term recurrence prevention. The earlier QA replay remains a failed observation. A later full CLI/sample pass is [separately evidenced](showcase-start.md#qa-kit-reproduction-status), not a causal explanation or repair of that old failure.

Stephen identifies the checker correction's design as his work. Implementation, tests and review involved material AI assistance; this declaration does not establish that he personally wrote or executed each part. No personal learning chronology is invented. Return to the [entry](../README.md) or [evidence ledger](showcase-evidence.md).
