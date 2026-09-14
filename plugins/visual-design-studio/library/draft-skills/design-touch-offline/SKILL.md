---
name: design-touch-offline
description: Offline and slow-network interaction for screen-content projects when this specialized workflow is required.
---

# Offline and slow-network interaction

Version-Timestamp: 2026-09-11T20:08:06-04:00

## Inputs and scope

Read the [advanced workflow](../../DISPLAY-ADVANCED-SKILLS.md). Reuse accepted `touchscreen-design` inputs, source versions, objective and constraints. Dependencies express information needs, not mandatory repeated work. Scope is screen content and interaction, not fixture design. Unknown facts remain unknown.

## Method

Classify each feature as local, cached or network-required. Display freshness where it changes decisions. Distinguish unavailable from empty results. Define loading cancellation and bounded recovery; do not queue actions for later submission without explicit requirements and duplicate protection.

## Deliverable and handoff

Connectivity matrix, stale-data rules and recovery states. Include exact files actually created, candidate status, assumptions, failed checks and next owner through the [handoff](../design-stage-handoff/SKILL.md). Proposed paths are not produced files. No installed tool, publication authority or provider access is implied by this skill.

## Acceptance

Exercise startup offline, mid-task disconnect, stale cache, reconnect and unavailable dependencies. Record observations separately from expected behavior. Missing runtime evidence remains pending; do not label plans or descriptions tested. Keep prior approved versions recoverable.
