# Legume Labs showcase review runbook

Status: **review guidance, 2026-10-02**. This runbook prepares review evidence and a proposed portfolio selection. The decision owner's provisionally accepted v1.1.0 compatible guidance for the current Legume Labs review is integrated in [QA Kit source at `d819d70cff052e7763296e5f6391065ae6ac02ec`](https://github.com/stevekkall-beansgc/qa-kit/blob/d819d70cff052e7763296e5f6391065ae6ac02ec/PORTFOLIO-READINESS.md), SHA-256 `c65bee396114b6a13ad197aee18a2b1bfb1a5927fe7305f46daa5853d2a51eb3`. The unchanged numerical rules and blockers remain those in the [earlier published v1.0.0 rulebook](https://github.com/stevekkall-beansgc/qa-kit/blob/38c7a7bfc078038cfd624ef58d24315e7230e0fe/PORTFOLIO-READINESS.md). This records source integration, not a tag/release or Health/Security runtime activation.

Original accepted provisional v1.1 candidate SHA-256: `7c88b17b296332dd9e36465a4763f76f3059d2a916320c192a971b82d5bb1a66`. The integrated guidance preserves it with two status replacements. It adds optional cold-read/risk-review methods, guarded capability-first presentation, conditional learning and material-claim traceability. Acceptance awards no points, waives no blockers and activates no Health/Security runtime.

Historical v1.0 identity at the initial October 2 audit: the canonical pin was `d452ff6c38e25d15d0767fbf1b99ccaf06eccc91`; the reviewed QA Kit release carrier was `38c7a7bfc078038cfd624ef58d24315e7230e0fe`. Both contain policy blob `7d186ff75f851302a783c74a6ab9ecbd4f51a896`. The pin is not asserted to be the adoption event; the policy file's latest change at that stage was `5a7404710db5b3f7d1e2c2778944029f2a87a7e9`.

The [public evidence baseline](SHOWCASE-EVIDENCE-BASELINE-20261002.md) records the initial release/commit observations. Keep private hiring scores and sensitive supporting records in an approved private evidence store.

## 1. Refresh scope and authority

1. Read the current adopted policy, owning repository's AGENTS guidance and intended release requirements. Record exact policy version and commit; proposed policies remain proposals until adopted.
2. Use GitHub CLI or an authorized API to observe public default branch, exact head, release tag and resolved commit, metadata, relevant issues and required workflow/job results. Record the observation time separately from source execution time.
3. Distinguish public main, released source, a proposed PR, a dirty local tree and a deployed build. Review each intended scope explicitly.
4. Prepare an isolated source snapshot for execution. Preserve concurrent primary changes.
5. Declare audience, supported mode, central journey, important failure modes, data/privilege/effect boundaries, builder contribution, inherited parts and material AI assistance.

Finish this stage with an evidence manifest naming the reviewed versions, required checks and unknowns. A repository name, tag, green badge or existing receipt alone does not establish current coverage.

## 2. Review publication and hiring evidence

Use the canonical audit template and its ten P categories, five H dimensions, floors, blockers and decision rules. Give every category a rationale and exact evidence identifiers. Score each hiring audience separately. Keep points, unknowns and disposition together; never normalize over missing categories.

Inspect the core implementation and meaningful failure paths. Reproduce safe documented setup and the representative journey, then execute the checks required for the reviewed scope. Record runtime, environment, commands, exit/result, skipped checks and retained outputs. If a prerequisite is unavailable, record the failed or blocked setup and dependent checks separately.

Minimize data at collection and redact when possible. Do not retain live secrets, credentials or unnecessary personal/private data, even privately. Prefer sanitized excerpts, hashes or safe evidence IDs. Essential raw sensitive evidence requires a specifically approved restricted store with access and retention controls; never copy it, private paths or unreviewed transcripts into the public repository.

Inspect actual CI jobs and steps on the evaluated commit. A successful aggregate can contain skipped work; a failed job can be denied before executing any code. Record those distinctions. Preserve native, browser, deployment and operational acceptance as independent evidence where claimed.

Complete the publication safety/provenance review proportionate to the actual artifacts: reuse rights, inherited assets, dependency exposure, data boundaries, intended publication history/artifacts, and contact instructions. Missing clearance stays unknown. Select existing qualified tools through the owning tooling process before adding a scanner or changing configuration.

Finish with the canonical publication/demo/portfolio dispositions, three strongest proofs and up to three required fixes with clearance evidence. A review disposition prepares a decision; publishing, merging, deployment and external communication retain their own authority.

## 3. Build the material-claim ledger

Inventory every material status, maturity, deployment, quantitative, comparative, authorship and adoption claim, plus every featured proof or starting promise. Include claims in captions, diagrams and screenshots.

For each claim record:

| Field | Content |
|---|---|
| Claim ID | Stable identifier |
| Location | File/section plus a short quotation; line numbers are supplemental |
| Reviewed version | Repository commit, release or demo build |
| Claim | Exact assertion, including scope |
| Evidence | Immutable public URL or safe private evidence ID |
| Evidence class | D / I / V / U from the adopted policy |
| Observation | Reviewer and checked date, separately from execution date |
| Disposition | Supported / qualified / unsupported / unknown |
| Follow-up | Clearance criterion, owner and re-audit trigger |

An evidence link must substantiate the assertion. Runtime/performance claims require actual matching execution. A public page declaring a service is live verifies that the claim was made; it does not verify the customer journey. An owner statement can establish work-state intent when its source and date are recorded.

Complete mapping for every material claim in the edited scope. Qualify or remove unsupported affirmative claims before promotion. Preserve historical register observations; append current observations instead of changing an old date to imply a new review.

Automation may inventory claims/IDs and validate file, anchor or reachability errors. Human review checks meaning, version compatibility and sufficient proof.

## 4. Prepare the entry page

State the practical capability and strongest relevant proof early. Offer a clear starting artifact that currently works. Distinguish project capability, release version, demonstrated behavior, public access and active/frozen/planned work state.

For each proposed featured example, present problem, demonstration, builder contribution, consequential decisions, evidence and material limitations. Select a small complementary set; the most familiar project is not automatically the strongest candidate.

Keep limitations beside the affected claim when omission could lead a reader to trust an estimate, deploy unsupported code, misunderstand payment mode or disclose data. Move supporting provenance detail into the ledger while retaining an accurate status and evidence link.

First-screen word budgets and Start-here tables are editing aids. Word bans, negation quotas, commit counts and screenshots are not scoring gates. Preserve meaningful accessible image descriptions and existing incoming links when reorganizing files.

## 5. Record consequential learning

Where the project claims learning/iteration or seeks the corresponding higher rating, identify a substantive decision, defect, negative/inconclusive result or correction. Record:

1. Prior design or belief, if evidenced.
2. Discovery method and version-linked evidence.
3. Consequence to correctness, safety, reproducibility, product direction or user outcome.
4. Actual response or recorded decision.
5. Verification, recurrence prevention where applicable and remaining limitations.
6. Evidence that would change the decision.

"None evidenced" or "unknown" is a valid assessment result. Do not invent an original hypothesis, stage a synthetic failure as a historical incident, or claim prevention merely because a test file exists.

## 6. Challenge a proposed flagship claim

For a proposed Legume Labs flagship-selection packet, an independent risk review of a central consequential claim is recommended. This evidence procedure feeds the existing rubric and blockers; it is not an additional eligibility gate. Canonical thresholds continue to determine eligibility.

Predeclare the claim and highest-risk behavior. Give the reviewer an exact commit and safe isolated environment. Ask them to try to falsify the claim and inspect the mechanism. Execute a relevant version-matched check where the claim is runnable and safe; record inaccessible or unexecuted coverage.

Retain the brief, reviewer/context independence, inspected files, commands, outputs, evidence-backed findings, severity and owner disposition. Reconcile model findings with artifacts before treating them as defects or opening issues.

Apply the collection-minimization rule above to reviewer outputs: retain sanitized findings and safe evidence identifiers, not unnecessary secrets or personal data. Essential raw sensitive evidence requires the specifically approved restricted store; only reviewed sanitized findings and safe evidence identifiers belong in a public packet.

A finding invalidating the central claim, breaking the supported core journey or activating an existing safety blocker requires verified correction or explicitly narrowed promoted scope. Documentation alone cannot clear an active correctness/safety blocker. Record accepted noncritical risks and their re-audit triggers.

## 7. Run a fresh cold read

Prepare an answer key against the reviewed entry-page version: intended audience/problem, practical outcome, starting artifact, strongest proof, contribution and consequential lesson where claimed. Freeze it before reviewer answers.

Give an unfamiliar reviewer only the public or approved sanitized entry URL and this prompt:

> Review this repository as a hiring manager for the named audience. Spend up to two minutes on its entry page and up to five minutes following its strongest evidence. State what the builder makes, the best evidence and its exact location, the builder's contribution, one evidenced consequential decision or lesson, and what you still need to verify. Identify any ambiguity about deployment, payment mode, simulation, authorship or practical benefit. Describe what you actually inspected; do not assume linked claims were executed.

Record the exact prompt, audience, artifact commit, reviewer/model, observed timebox and limitations, navigation, answers and material mismatches. An agent estimate of reading speed is diagnostic; it is not human usability validation. Review-efficiency evidence should reflect observed navigation, not an unsupported timing claim.

Keep unreviewed reviewer transcripts private; publish only approved sanitized excerpts or safe evidence IDs, without personal data or private paths.

Check whether the reader identifies relevance quickly, finds the intended starting artifact and strongest proof, and can explain the evidence's scope. A material safety/deployment/authorship misread needs correction. One reviewer is diagnostic; reconcile two independent reads when they will materially affect the efficiency rating. Do not import informal /10 ratings as canonical assessments.

## 8. Reconcile, verify and prepare publication

1. Reconcile reviewer findings against artifacts and record supported/qualified/unsupported/unresolved dispositions.
2. Complete selected local improvements, preserving links, evidence history and private boundaries.
3. Run the owning repository's required checks and repeat affected verification after changes. For this static showcase candidate, run `python3 scripts/check_showcase.py` and `python3 -m unittest discover -s scripts -p 'test_*.py'`. The checker covers local files, ordinary ATX heading anchors, explicit HTML IDs, path confinement and SVG XML. It is not a full renderer; inspect unsupported Markdown forms, remote evidence and claim meaning separately.
4. Append a new assessment for the changed source with policy identity, source/demo versions, checks, blockers/floors and proposed decision. Old results retain their original dates and scopes.
5. Present concrete reviewed changes and remaining blockers to the decision owner. Obtain any publication/release authority required by the owning repository before external writes.

## Initial execution record

- October 2 public scope inventory completed for Legume Labs, BeanFit, BeanFit App, Bean Counter, Jumping Beans, QA Kit and Gate Kit.
- At the initial stage, public canonical portfolio policy was verified as v1.0.0 and the newer Health/Security scorecard candidate remained disabled. The decision owner subsequently provisionally accepted a focused v1.1 compatible-guidance candidate for this review; canonical merge was pending at that stage. Later source integration is recorded above. Reconciled scores carry forward unchanged.
- Isolated exact public snapshots prepared; static showcase checker replayed successfully.
- Detailed repository assessments are retained privately. Selection and first-screen edits follow assessment reconciliation.
- A frozen-key, fresh-context Senior AI cold-read diagnostic completed on the existing public entry page. The reader found the intended engineering route and deeper decision evidence, while repeating a stale App-URL claim. This is not human usability validation or publication clearance; transcripts and hiring judgments remain private.
- The later October 2 source candidate reconciled this runbook with an [evidence index of earlier October 2 observations](CURRENT-PUBLIC-EVIDENCE-20261002.md), pinned entry routes and qualified App/estimate wording. The source evidence refresh establishes no deployment, promotion or rights clearance of the listed projects; GitHub Releases records release identity.
- Next: close remaining publication-evidence gaps and repeat affected assessments and cold reads against the frozen candidate before promoting flagship claims.

No recurring job, model route, score storage, cloud integration or automatic remediation is enabled by this document.
