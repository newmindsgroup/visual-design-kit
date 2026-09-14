---
name: design-web-integrations
description: Website integration experience for scoped website projects and revisions.
---

# Website integration experience

Version-Timestamp: 2026-09-12T11:35:16-04:00

## Inputs and scope

Read the [website workflow](../../WEBSITE-WORKFLOW.md). Reuse accepted `web-forms` inputs and the relevant [website work sections](../../templates/website-work.md). Record intended outcome, audience evidence, exact source versions, platform constraints and allowed change. Dependencies express information needs, not a compulsory restart of approved work.

## Method

Define external request/response contracts, authentication ownership and minimal data. Map loading, cancellation, confirmed, failed and unknown outcomes. Reconcile uncertain mutations before retry and isolate failures from unrelated content. Keep credentials server-side.

## Deliverable

Integration state contract and synthetic acceptance cases. Attach to the existing design-work record with stable page/component/content IDs. Hand off actual file paths, candidate status, assumptions, unexecuted checks and next owner. Proposed filenames are not produced files. Missing tools hold dependent execution only.

## Acceptance

Test malformed responses, timeouts and duplicate input locally; real service changes need authorized scope. Preserve prior approved work. A specification, sample or simulated interaction is not proof of production behavior. Use [acceptance scenarios](../../examples/website-workflow/README.md) and project-specific checks; no external changes or installation are implied.

Complete the [stage handoff](../design-stage-handoff/SKILL.md) with actual files, version, checks, unknowns and next owner.
