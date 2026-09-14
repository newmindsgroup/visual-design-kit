---
name: design-screen-playback-performance
description: Playback performance engineering when producing or maintaining digital screen content.
---

# Playback performance engineering

Version-Timestamp: 2026-09-12T11:33:18-04:00

## Inputs

Read the [production workflow](../../SCREEN-PRODUCTION-WORKFLOW.md). Reuse accepted `display-production` inputs, source versions, target specification and user scope. Dependencies require information, not restarting approved work. No fixture design is included.

## Method

Set target-specific budgets for frame cadence, startup, memory and media size. Measure actual player behavior across representative loops and extended operation, with timestamps and test conditions. Investigate resource leaks, decode limits and repeated allocation. A desktop trace cannot certify embedded hardware.

## Outputs

Performance budget, measurement logs and prioritized fixes. Use the [stage handoff](../design-stage-handoff/SKILL.md). Hand off actual files, version, candidate/approved status, dependencies, failures and next owner. Proposed paths are not produced artifacts; no skill grants external activation, spending or credentials.

## Acceptance

Record target device, runtime, duration and observed stalls; require sustained testing before claiming long-running stability. Record executed evidence separately from plans. Use the [example](../../examples/screen-production/README.md) only within its declared scope.
