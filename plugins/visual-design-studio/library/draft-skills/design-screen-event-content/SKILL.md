---
name: design-screen-event-content
description: Event-driven display content when producing or maintaining digital screen content.
---

# Event-driven display content

Version-Timestamp: 2026-09-12T11:33:18-04:00

## Inputs

Read the [production workflow](../../SCREEN-PRODUCTION-WORKFLOW.md). Reuse accepted `screen-playlists` inputs, source versions, target specification and user scope. Dependencies require information, not restarting approved work. No fixture design is included.

## Method

Define supported event source, payload, freshness, priority, interruption, cooldown and return-to-loop. Debounce repeated signals and reject stale/invalid events. Never assume a sensor exists or collect identifying data by default. Specify conflict and offline behavior. Keep unverified external events from triggering actions.

## Outputs

Event contract, state machine and simulated-event tests. Use the [stage handoff](../design-stage-handoff/SKILL.md). Hand off actual files, version, candidate/approved status, dependencies, failures and next owner. Proposed paths are not produced artifacts; no skill grants external activation, spending or credentials.

## Acceptance

Test duplicates, conflicting priorities, disconnect, stale events and return to the base loop. Simulation does not certify physical sensors. Record executed evidence separately from plans. Use the [example](../../examples/screen-production/README.md) only within its declared scope.
