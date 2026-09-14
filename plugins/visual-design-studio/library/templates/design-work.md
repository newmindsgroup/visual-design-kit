# Selected design work record

Version-Timestamp: 2026-09-08 18:04:08 AST

Replace this template timestamp with the actual revision time when creating a record.

## Scope and state

Record ID, capability ID, owner, requested outcome, intended use, phase/full-project/precise-change scope, current candidate version, readiness and approval status separately.

## Selected inputs

Declare the workspace root and how to locate it from this record, the project output folder and the read-only reference-library folder. State the base for relative paths explicitly; do not infer it from the current shell directory. Relocation requires a new mapping and source-version checks, not permission to write into the library.

Exact brief, evidence/persona/requirement IDs, file paths and hashes where needed. List which existing prerequisites are accepted and why they remain current. Do not copy whole source libraries.

## Decisions and work

Keep each fact, decision and check in one authoritative section with stable IDs; receiving packets can cite that section. Scale prose and tables to the selected work, and mark irrelevant sections briefly with a reason. Preserve required contract fields and full persona structures when selected. Concision does not waive evidence, change boundaries or unresolved holds.

For each decision: ID, need/use-case IDs, requirement, alternatives, chosen proposal, rationale, evidence or hypothesis, consequences and acceptance criterion ID. Insert capability-specific outputs from the selected skill here.

## Medium and consumption conditions

Record only applicable conditions: live presentation, independent reading, interactive screen, print or unattended viewing; expected viewing distance and pace; aspect/size; speaker notes versus on-page explanation; online/offline assets; export format and intended viewer. Defaults remain unselected until the brief resolves them. A live deck and a standalone document may need different content density and evidence placement. Keep approved brand rules consistent while adapting the composition.

## Production specification, when selected

- Route/app and control mechanism, actual version/environment, status (`authored`, `blocked`, `experimental`, `route-verified`), date and evidence reference. Route status is distinct from manifest structure or candidate approval.
- Required native master and exports, units/dimensions, selected medium requirements, font/asset dependencies, conversion losses and canonical editable source.
- Action-specific account/permission and entitlement findings, no-extra-charge boundary, authorized destination/data scope. Record unresolved access as a dependent hold.
- Actual local source/export paths; cloud design/node ID and version where applicable, with approved access scope. A cloud URL does not replace required local manifest bytes.
- Native save/reopen/editability and export/viewer results, evidence references and remaining limits. Link to Checks and limits rather than duplicating test results.

For example, a missing Figma connection records `status: blocked`, no produced source/export, the required file/edit/export operations and next access-discovery action. Do not report a screenshot or alternate format as fulfillment of the native deliverable. This example is a recording pattern, not an executed test.

## Criterion basis

| Criterion ID | Basis | Source/version and applicability | Project target | Verification method | Exception/owner |
| --- | --- | --- | --- | --- | --- |
| [fill] | [normative standard / platform guidance / project requirement / heuristic] | [fill] | [fill or pending] | [fill] | [fill] |

Distinguish a source requirement from its explanation and from a project's stricter target. Record success-criterion level, units and exceptions where relevant. Do not promote an attractive ratio, word count, timing estimate or brand example to a universal standard. Use existing decision records to resolve conflicts; this table does not create a new approval mechanism.

## Change boundary

Baseline reference/hash and its actual approval status; allowed delta; preserved invariants; current candidate approval status. For new work state no baseline, with reason. Do not invent a baseline.

## Checks and limits

Reference the Criterion basis ID and its method; record actual result, evidence path/hash, reviewer/date and open gap here. Author each method once in Criterion basis. If it changes, revise that authoritative row and identify which earlier results need rerunning. Separate machine structure, content/factual, creative, accessibility, usability, legal, native/runtime/device and independent review. Mark irrelevant checks with reasons.

## Handoff

For a delivery candidate, use [delivery preflight](../DELIVERY-PREFLIGHT.md) to reconcile this record with actual source/export versions and recipient instructions. Keep applicable checks and failures in Checks and limits; preparing this section does not send files.

Actual outputs and versions, manifest, remaining risks, next action/owner, refresh trigger and recovery instructions. Preparing a handoff does not send it.
