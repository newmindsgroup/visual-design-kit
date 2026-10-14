---
name: design-stage-handoff
description: Assemble a bounded AI design-stage instruction or resumable handoff from existing briefs, evidence, personas and baselines. Use for full-workflow sequencing, stage-only tasks and precise revisions; it does not execute production merely by preparing a packet.
---

# Design stage instructions and handoffs

Version-Timestamp: 2026-10-03T12:31:00.335655-04:00

Project-local draft entry point for manual use in Codex or Claude Code. Tool execution, automatic discovery and host portability are unverified.

## Contract

Input: requested outcome/stage/scope, canonical current-state reference, relevant research/actor/persona/requirement IDs, baseline status, operation boundary and next consumer. Read [stage-execution.md](../../templates/stage-execution.md), [lifecycle contracts](../../DESIGN-PROCESS.md) only for the selected stage, and [continuity routines](../../WORKFLOW.md) when resuming.

Fill role, objective, selected context, permissions/runtime checks, concrete task, output schema/path/limit and evidence-based evaluation. Select audience inputs under the [shared rule](../../CAPABILITY-CONTRACTS.md#audience-input-selection); retain justified bounded actors and their evidence limits when applicable. Refer to full personas via [their canonical contract](../../templates/persona.md); do not replace them with generated summaries. Preserve the complete need/use-case/requirement/decision/criterion chain, including IDs.

Verify prerequisite files and their status. Full-project packets sequence stages; stage-only packets reuse valid predecessors; precise-change packets include exact baseline/version or hash, actual approval reference, delta and invariants. Distinguish the approved baseline from the new candidate: the candidate may remain unapproved while being compared. Request approval evidence for the baseline only when that claim depends on it; do not demand candidate approval merely to prepare a comparison. Missing approval must not become implicit approval. If only an approved-baseline-dependent edit is blocked, return its comparison plan and missing input while completing independent packet preparation.

Reassess the receiving task through the shared model governor and fill the template receiving-stage route. Verify the exact capability entry fits the available inputs and intended output. Preserve completion/review gates, privacy and unresolved holds. Record recommended and actual model/effort separately; no automatic model switch is implied. Reuse a prior route only after confirming unchanged conditions. Discover the destination routing method and record its version, supported operations and limits; historical authoring-host checks do not transfer.

Keep one canonical truth. Load relevant sections just in time; do not paste the whole library or duplicate host memories. Check actual tools, formats and data permissions before claiming executability. A Markdown instruction does not grant access. Store concise rationale and evidence, not hidden chain-of-thought.

Output: ready/provisional/blocked-for-named-use packet or filled handoff, with exact output versions, sources/actors/personas used, decisions, actual checks, remaining gaps and next owner/action. On resume, inspect partial actions before repetition; external effects must not be replayed from a stale handoff. Do not call a design validated because its prompt passed a check.

Acceptance: Verify the recorded audience selection, rationale, evidence limits and named use under the shared audience input rule. Reassess affected audience inputs on scope, evidence or intended-use changes; preserve historical results and hold dependent use until required conditions are resolved. Audience records alone never prove usability or production acceptance. Selected inputs resolve; all six template sections exist; IDs and unknowns survive; permissions and output scope match the request; readiness and approval are separate. Shared acceptance and schema rules: [CAPABILITY-CONTRACTS.md](../../CAPABILITY-CONTRACTS.md). Machine-readable handoffs follow the existing [subject contract](../../HANDOFF-CONTRACT.md), with the [persona template](../../templates/handoff-record.json) or [bounded-actor template](../../templates/handoff-actor-record.json) selected under that contract.


## Context and creative continuity

Version-Timestamp: 2026-09-09 10:35:51 AST

Use [context readiness](../../AI-DESIGN-CONTEXT.md) and [creative continuity](../../CREATIVE-CONTINUITY.md) for ambiguous feedback, exact revisions, asset retrieval or task resume. Reuse this skill's baseline/delta and approval rules; do not create a second authority.


## Reviewed learning checkpoint

Version-Timestamp: 2026-09-09 10:43:00 AST

At a meaningful feedback or failure checkpoint, select [skill improvement](../../SKILL-IMPROVEMENT.md) only if there is a reusable lesson. Keep project-specific feedback with its project, preserve baselines and do not adopt an untested candidate merely to finish the handoff.

## Historical evidence boundary

Keep superseded evidence and prior results in the project history, with version links from the handoff. The validated active evidence register accepts current sources only. Do not put historical sources into active support or relabel them current to pass validation. Preserve history outside that active register.

The comparison CLI treats lists and empty objects as whole values. It cannot verify an invariant such as frames.0.label inside a list. Declare the whole list invariant, use stable object keys where appropriate, or run a separate element-level check; never claim element preservation from the list-level result alone.


## Recoverable revision and activity history

Version-Timestamp: 2026-10-02 21:02:25 AST

For every produced design revision, fill the [immutable revision/activity fields](../../templates/design-work.md#immutable-revision-and-activity-record) in the authoritative project version index; the work record links to that owner. Persist all produced native/artwork/render/export bytes under a new sequence ID and real timestamp with numeric UTC offset or IANA timezone before overwrite or another review; bind parent, source hash, actual verified tool/model/effort, drawing hypothesis and visual delta, review input/output versions, feedback, four acceptance states and measured outcome. A hash without preserved bytes is not recovery. Append activity/decision/outcome events, including failed methods and missing evidence; never store hidden reasoning, secrets or private book text. Historical reconstruction is labeled as such and cannot replace missing originals. Keep confidential history in the authorized project workspace. The project executor owns that index; kit maintenance does not modify client revisions or create a duplicate ledger.


## Incremental preview checkpoint

Version-Timestamp: 2026-10-02 21:05:13 AST

For visual work, show the actual versioned preview at a meaningful drawing checkpoint before expensive finalization. State the stage and status (generated sketch, native study, review candidate or accepted-for-stated-scope), one or two concrete visual hypotheses and a focused steering question when needed. Bind feedback to the shown revision and append the response/changed decision to the existing activity record; do not overwrite history or present a generated preview as native proof. Keep one authoritative current-working pointer to immutable revisions. Continue unrelated authorized work while a dependent decision is pending.

Reuse the receiving-stage route in stage-execution.md when stage, inputs, risk, actual failure or capacity changes; do not reroute every tool call or infer a permanent best model. Record recommended versus verified actual runtime, approach, acceptance, repair count and measured elapsed/outcome limits in the existing work packet. A recommendation or prose statement does not switch models. Keep checkpoint overhead proportional; no new dashboard, plugin or background loop is implied.

Produced revisions include saved native/artwork files, exports, previews shown to a user/reviewer, and artifacts cited by a decision. Transient unsaved viewport redraws are not separate revisions. Record omitted artifacts and missing bytes explicitly.

Version-Timestamp: 2026-10-03T12:28:38.580424-04:00

## Progression review site

For requested logo redesign or new identity collaboration, use the [progression-site output contract](../../templates/design-progression-site.md) to present the existing authoritative revision/activity history as a website-format review artifact. This is a presentation of evidence, not a second version authority or automatic publication. Default to a local/draft hub; hosting/sharing requires the authorized destination, verified access and appropriate project/Sites workflow. A selected/accepted logo does not establish completion of the identity system.
