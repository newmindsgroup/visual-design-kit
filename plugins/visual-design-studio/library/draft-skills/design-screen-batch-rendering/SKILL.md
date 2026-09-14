---
name: design-screen-batch-rendering
description: Automated campaign rendering when producing or maintaining digital screen content.
---

# Automated campaign rendering

Version-Timestamp: 2026-09-12T11:33:18-04:00

## Inputs

Read the [production workflow](../../SCREEN-PRODUCTION-WORKFLOW.md). Reuse accepted `screen-templates` inputs, source versions, target specification and user scope. Dependencies require information, not restarting approved work. No fixture design is included.

## Method

Validate all records before rendering. Give every variant a stable identifier and explicit format. Preserve source versions and output hashes. Reject unsafe filenames, invalid fields and existing destinations. Record failed variants rather than replacing them with guessed values. Keep full output sets versioned for review; batch generation does not imply approval.

## Outputs

Repeatable renderer, data fixture, export manifest and failure report. Use the [stage handoff](../design-stage-handoff/SKILL.md). Hand off actual files, version, candidate/approved status, dependencies, failures and next owner. Proposed paths are not produced artifacts; no skill grants external activation, spending or credentials.

## Acceptance

Rebuild identical input and compare hashes; inject invalid input, missing assets and changed files. The linked example implements an SVG subset, not video or arbitrary layouts. Record executed evidence separately from plans. Use the [example](../../examples/screen-production/README.md) only within its declared scope.
