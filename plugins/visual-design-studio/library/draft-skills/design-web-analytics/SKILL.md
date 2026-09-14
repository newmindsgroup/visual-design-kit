---
name: design-web-analytics
description: Website analytics and measurement for scoped website projects and revisions.
---

# Website analytics and measurement

Version-Timestamp: 2026-09-12T11:35:16-04:00

## Inputs and scope

Read the [website workflow](../../WEBSITE-WORKFLOW.md). Reuse accepted `web-discovery` inputs and the relevant [website work sections](../../templates/website-work.md). Record intended outcome, audience evidence, exact source versions, platform constraints and allowed change. Dependencies express information needs, not a compulsory restart of approved work.

## Method

Define questions, outcomes and event semantics before instrumenting. Avoid personal data in URLs or event properties. Separate event firing, receipt and meaningful outcomes. Respect the selected consent rules and authorization for collection.

## Deliverable

Measurement plan and verified event contract. Attach to the existing design-work record with stable page/component/content IDs. Hand off actual file paths, candidate status, assumptions, unexecuted checks and next owner. Proposed filenames are not produced files. Missing tools hold dependent execution only.

## Acceptance

Test duplicates, denied consent and missing events with synthetic data; no invented metrics or causal lift. Preserve prior approved work. A specification, sample or simulated interaction is not proof of production behavior. Use [acceptance scenarios](../../examples/website-workflow/README.md) and project-specific checks; no external changes or installation are implied.

Complete the [stage handoff](../design-stage-handoff/SKILL.md) with actual files, version, checks, unknowns and next owner.

Resolve consent requirements through [web privacy](../design-web-privacy/SKILL.md) before enabling tracking; retain the applicable decision and permission evidence.
