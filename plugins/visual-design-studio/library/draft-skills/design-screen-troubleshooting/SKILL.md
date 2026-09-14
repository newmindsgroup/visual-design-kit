---
name: design-screen-troubleshooting
description: Display content troubleshooting when producing or maintaining digital screen content.
---

# Display content troubleshooting

Version-Timestamp: 2026-09-12T11:35:16-04:00

## Inputs

Read the [production workflow](../../SCREEN-PRODUCTION-WORKFLOW.md). Reuse accepted `display-evaluation` inputs, source versions, target specification and user scope. Dependencies require information, not restarting approved work. No fixture design is included.

## Method

Preserve failing file and environment evidence. Compare working source, encoded export, player preview and physical screen in that order. Isolate scaling, fonts, decode, network and capture artifacts one at a time. Use a known-good file to separate player failures from artwork failures. Record exact reproduction and avoid broad resets.

## Outputs

Diagnostic record, isolated cause or hypotheses, bounded fix and retest. Hand off actual files, version, candidate/approved status, dependencies, failures and next owner. Proposed paths are not produced artifacts; no skill grants external activation, spending or credentials.

## Acceptance

Reproduce the original failure and verify correction without changing approved unrelated design. Record executed evidence separately from plans. Use the [example](../../examples/screen-production/README.md) only within its declared scope.

Complete the [stage handoff](../design-stage-handoff/SKILL.md) with actual files, version, checks, unknowns and next owner.
