# Selected design work record

Version-Timestamp: 2026-10-03T12:31:00.335655-04:00

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


## Immutable revision and activity record

Version-Timestamp: 2026-10-02 21:02:25 AST

Use the existing authoritative project version index (such as VERSION-INDEX) with this record, not a parallel workflow. Every produced design revision gets a never-reused sequence ID plus real timestamp with numeric UTC offset or IANA timezone and parent revision (or explicit root). Preserve all native masters, artwork, renders and exports actually produced at versioned paths before any overwrite; verify readable bytes and hashes. Do not overwrite a revision snapshot. Missing originals stay missing; a regenerated or historical reconstruction has a new ID and an explicit reconstruction label, not an original-byte claim. Hashes alone do not recover lost images.

| Revision ID/time/parent | Source version/hash and preserved artifact paths/hashes | Actual tool/version/model/effort (verified or unknown) | Hypothesis, strategy and visual delta | Review input/output revision IDs | Feedback event and acceptance states | Outcome metric/result and limits |
| --- | --- | --- | --- | --- | --- | --- |

Append activity events with timestamp, actor/tool, action/strategy, input/output versions, concise rationale, review/feedback, failed methods and actual check results. Update the current index through new status events while keeping historical artifact bytes and prior events intact. Record elapsed time, repair/iteration count, remaining criterion failures and observed outcome where measured; unknown metrics stay unknown. Separate critique completion, criteria evidence, user visual acceptance and production readiness. Store no hidden chain-of-thought, credentials, private books or bulk context. Keep confidential artifacts/logs local to their authorized project; versioning is not publishing or permission to export to a new service. Native/Git history may supplement this index but cannot substitute for recovery evidence for ignored or overwritten renders.


## Preview and current-working checkpoint

Version-Timestamp: 2026-10-02 21:05:13 AST

- One authoritative current-working pointer/index location and exact revision; stage/status: generated sketch/native study/review candidate/accepted-for-stated-scope. Link here if another existing record owns the pointer; do not create a duplicate authority.
- Actual versioned preview/evidence path, one or two visual hypotheses, intended observable effect, checkpoint before costly finalization and focused steering question/decision if needed:
- User feedback event ID, shown revision/hash, actual response/evidence pointer, changed decision/next revision or unresolved dependent hold. Feedback and status changes append to history; immutable artifact bytes stay unchanged.
- Receiving-stage route reference and change trigger (stage/input/risk/failure/capacity); recommendation versus actual verified runtime/approach, acceptance/outcome, repairs and measured elapsed time/limits. Do not measure quality by model-call volume.

Version-Timestamp: 2026-10-03T12:28:38.580424-04:00

When a progression/review website is requested, fill [design-progression-site.md](design-progression-site.md) from this record and the authoritative version index. Record audience/access, included revision/event IDs, excluded confidential material, actual interaction persistence, site artifact version, and local/share status. The hub does not replace this history or imply publication permission.
