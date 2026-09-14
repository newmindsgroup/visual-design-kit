# AI-ready UX deliverable record

Version-Timestamp: 2026-09-08 08:57:40 AST

Authoring extension to [design-work.md](design-work.md), not a new validator schema. Use the existing work record as the authoritative container; insert the selected sections below. Replace placeholders and timestamp before use. JSON/CSV tables are optional machine-readable companions, not automatic proof of correctness. Keep one canonical representation and identify any derived diagram/view by source version.

## Identity and decision

- Deliverable ID and UXD contract ID from [the catalog](../UX-DELIVERABLES.md):
- Version, owner, date, project/use and intended consumer:
- Selection: create / reuse / omit / hold, with rationale:
- Decision this artifact supports and question it answers:
- Actual status: proposed / authored / reviewed, with readiness and approval separately:
- Inputs: IDs, paths, versions/hashes as applicable, authority and freshness:
- Existing baseline, allowed changes and preserved invariants, or no-baseline reason:
- Evidence classification per material assertion: observed / supplied / inferred / proposed / unknown. Unknown includes consequence, owner and next action:

## Shared vocabulary and IDs

These are field conventions for this authoring extension, not new validator enums. Selection, lifecycle, validity, readiness, approval and check results are different facts; never collapse them into one status.

| Field | Values and meaning |
| --- | --- |
| selection | create / reuse / omit / hold, with decision rationale |
| lifecycle | proposed / authored / reviewed; reviewed does not imply approval |
| validity | current / stale / unknown, against the named inputs and intended use |
| evidence_class | observed / supplied / inferred / proposed / unknown. A participant-reported statement is supplied evidence, not direct observation of their inner state |
| readiness | ready for named next use / needs revision / held, with affected use and reason |
| approval | actual approval reference and scope, or not approved / unknown; reuse existing project approval conventions |
| check_result | passed / failed / not run / not applicable; passed needs actual method/version/evidence |

Use the adopting project's existing IDs where available. Otherwise use stable project-scoped IDs such as `PROJECT-JOURNEY-001`, `PROJECT-STATE-001` and `PROJECT-REQ-001`, with a separate version field. Uniqueness applies across that project; references crossing projects include project identity and version. A `UXD-09` is a reusable contract type, while `PROJECT-JOURNEY-001` is one actual artifact instance. Never reuse a retired ID for a different item. Resolve references by ID plus version rather than a display label or a mutable filename.

Record missing facts once in the existing work record:

| Hold ID | Missing fact or conflict | Affected item IDs and action/use | Owner | Resolution needed | Review trigger | State |
| --- | --- | --- | --- | --- | --- | --- |
| [project-scoped ID] | [fill] | [exact initiation/retry/delivery scope] | [fill] | [evidence or decision needed] | [date/event] | [open/resolved with evidence] |

Independent work can continue outside a hold. On changed inputs, mark affected records' validity stale and reassess readiness/check applicability; preserve historical results and their tested versions. In the detail tables below, Status means lifecycle plus validity, not approval.

## Common traceability table

| Item ID | Need/requirement ID | Input evidence ID and locator | Assertion or design choice | Evidence classification | Downstream ID | Check ID |
| --- | --- | --- | --- | --- | --- | --- |
| [fill] | [fill] | [source, page/section/session locator] | [fill] | [fill] | [fill] | [fill] |

Use stable IDs throughout. Do not renumber unrelated records on revision. Proposed facts are not made observed by repeated reuse. Reference private evidence with approved access controls; no participant data is needed in a reusable pack.

## Select the relevant detail block

### Sitemap, content and navigation (UXD-13 to 18)

| Node/content ID | Label/type/purpose | Parent ID | Need ID | Content/model reference | Access and locale | Navigation inclusion | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [fill] | [fill] | [root or ID] | [fill] | [fill] | [fill] | [fill] | [fill] |

Represent hierarchy separately from cross-links and redirects. Include empty/missing content implications, navigation labels and intentional exclusions. Check duplicate IDs, missing parents, cycles in the hierarchy, orphaned destinations, ambiguous labels and content coverage. Record cross-links in a separate edge table. A Mermaid or visual sitemap must agree with these IDs and hierarchy; a picture alone is insufficient for implementation. XML sitemap generation is a separate technical task.

### Task/user flow and state model (UXD-11/17/21)

| State ID | Actor/goal | Entry/precondition | Visible content/feedback | Permitted action | Data or service effect | Screen ID |
| --- | --- | --- | --- | --- | --- | --- |
| [fill] | [fill] | [fill] | [fill] | [fill] | [none or contract reference] | [fill] |

| Transition ID | From | Trigger | Guard/condition | To | Failure/cancel/back/recovery | Criterion ID |
| --- | --- | --- | --- | --- | --- | --- |
| [fill] | [ID] | [fill] | [explicit or unconditional] | [ID] | [state ID or justified N/A] | [fill] |

Declare start and terminal states. Check reachable success, invalid/unavailable branches, loops, abandoned sessions and transitions to missing states. Each decision must cover its relevant outcomes. For uncertain remote mutation, initiation and retry remain held until the actual recovery contract exists. A flow diagram cannot supply that contract. Include focus, reading order and input effects in the linked interaction specification. Happy-path-only output is incomplete when other outcomes can occur.

### Journey or service blueprint (UXD-08 to 10)

Actor/persona and scenario; current observed / reconstructed / proposed future state; start/end boundaries; channel/context; evidence coverage and sampling limits:

| Stage/step ID | Goal/action | Touchpoint/channel | Evidence ID | Barrier or need | Emotion and its evidence status | Opportunity/requirement | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [fill] | [fill] | [fill] | [fill] | [fill] | [unknown if unsupported] | [fill] | [fill] |

For a service blueprint, add frontstage action, backstage action, supporting system/team, dependency, handoff, failure and recovery to each relevant step. Explicitly mark customer-visible versus internal work. Check timing/order, actual actor differences, unknown ownership and consistency with the linked journey. Do not fill an emotion curve for visual effect.

### Research, requirements, screens and evaluation (other selected UXD contracts)

Use each selected catalog row's fields in an ID-keyed table or named section. Research preserves observation versus interpretation and session/source references. Requirements link needs to explicit criteria. Screens link to flow states and content. Evaluation lists planned methods separately from actual observations/results. Reuse the complete [persona](persona.md), [research brief](research-brief.md) and [specimen record](specimen-record.md) where applicable rather than inventing smaller replacements.

## Handoff and acceptance

| Check ID | Requirement and method | Result: passed / failed / not run / not applicable | Actual evidence/version or reason | Owner/next step |
| --- | --- | --- | --- | --- |
| [fill] | [fill] | [fill] | [fill] | [fill] |

Check referential integrity, source traceability, selected-contract completeness, baseline preservation and consistency between tables and visual views. Distinguish structural checks from semantic review, real-user evidence, accessibility, platform/device checks and approval. A successful render or model critique is not a usability study. No automated validator for these new table blocks exists yet; report manual checks honestly.

Finish with the existing [stage-execution packet](stage-execution.md) and [handoff record](handoff-record.json): actual artifacts produced versus proposed paths; next consumer; accepted inputs; remaining holds; exact next action; change dependencies to revisit; and refresh trigger. If a requirement, flow edge or source changes, mark affected screens/tests/results stale until reassessed. Do not silently propagate stale approval.

## JSON handoff subject compatibility

The shared handoff format now supports an explicit bounded-actor route. Follow the [subject contract and migration guidance](../HANDOFF-CONTRACT.md). Omitted subject_type retains legacy persona traces; subject_type bounded_actor requires actual role, goal, context and evidence classification plus actor-linked traces. Never relabel an actor as a full persona. The original actor-only incompatibility is preserved as historical exercise evidence; the new route has separate current validation. Map readable not run to JSON pending and not applicable to not_applicable without changing the result. Selecting a persona still requires its complete canonical record upstream; handoff validation alone does not validate that record.
