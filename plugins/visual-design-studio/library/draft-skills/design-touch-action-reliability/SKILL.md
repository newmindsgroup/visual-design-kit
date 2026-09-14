---
name: design-touch-action-reliability
description: Reliable touchscreen actions for screen-content projects when this specialized workflow is required.
---

# Reliable touchscreen actions

Version-Timestamp: 2026-09-11T20:08:06-04:00

## Inputs and scope

Read the [advanced workflow](../../DISPLAY-ADVANCED-SKILLS.md). Reuse accepted `touchscreen-design` inputs, source versions, objective and constraints. Dependencies express information needs, not mandatory repeated work. Scope is screen content and interaction, not fixture design. Unknown facts remain unknown.

## Method

Define not-started, submitting, received, completed, failed and unknown separately. A timeout is not proof of failure. Suppress manual and automatic duplicate submission until authoritative reconciliation or verified idempotency makes retry safe. Elapsed time alone never makes retry safe. Receipt does not prove fulfillment. Isolate unresolved operational records from the next shopper.

## Deliverable and handoff

Action lifecycle, reconciliation contract and honest status copy. Include exact files actually created, candidate status, assumptions, failed checks and next owner through the [handoff](../design-stage-handoff/SKILL.md). Proposed paths are not produced files. No installed tool, publication authority or provider access is implied by this skill.

## Acceptance

Inject response loss after accepted submission; repeated taps and session reset must not create another action or reveal prior data. Record observations separately from expected behavior. Missing runtime evidence remains pending; do not label plans or descriptions tested. Keep prior approved versions recoverable.
