---
name: design-stage-handoff
description: Assemble a bounded AI design-stage instruction or resumable handoff from existing briefs, evidence, personas and baselines. Use for full-workflow sequencing, stage-only tasks and precise revisions; it does not execute production merely by preparing a packet.
---

# Design stage instructions and handoffs

Version-Timestamp: 2026-09-12T11:36:30-04:00

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
