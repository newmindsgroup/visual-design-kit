---
name: design-screen-executable-tests
description: Executable content and interaction tests for screen-content projects when this specialized workflow is required.
---

# Executable content and interaction tests

Version-Timestamp: 2026-09-11T20:08:06-04:00

## Inputs and scope

Read the [advanced workflow](../../DISPLAY-ADVANCED-SKILLS.md). Reuse accepted `display-evaluation` inputs, source versions, objective and constraints. Dependencies express information needs, not mandatory repeated work. Scope is screen content and interaction, not fixture design. Unknown facts remain unknown.

## Method

Choose actual artifacts or executable behavior to exercise. Specify stimulus, expected result and evidence before running. Inject disconnects, duplicate input, missing data and expiry. Keep fixtures isolated and never call live services from tests. Record exit status, actual results and skipped checks.

## Deliverable and handoff

Runnable test suite for the chosen implementation and evidence report. Include exact files actually created, candidate status, assumptions, failed checks and next owner through the [handoff](../design-stage-handoff/SKILL.md). Proposed paths are not produced files. No installed tool, publication authority or provider access is implied by this skill.

## Acceptance

Tests must fail on a known broken case and pass the corrected case. A prose state table is not execution. Record observations separately from expected behavior. Missing runtime evidence remains pending; do not label plans or descriptions tested. Keep prior approved versions recoverable.
