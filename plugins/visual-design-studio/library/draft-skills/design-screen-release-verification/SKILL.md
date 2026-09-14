---
name: design-screen-release-verification
description: Content update and release verification when producing or maintaining digital screen content.
---

# Content update and release verification

Version-Timestamp: 2026-09-12T11:35:16-04:00

## Inputs

Read the [production workflow](../../SCREEN-PRODUCTION-WORKFLOW.md). Reuse accepted `screen-acceptance-records` inputs, source versions, target specification and user scope. Dependencies require information, not restarting approved work. No fixture design is included.

## Method

Bind an approved manifest to intended screens and activation window. Stage a complete set before activation where supported; otherwise define a safe explicit sequence and fallback. Verify exact version readback and playback. On uncertain activation inspect state before retry. Keep the previous known-good set and test restoration within authorized scope.

## Outputs

Release plan, manifest, target readback and rollback evidence. Hand off actual files, version, candidate/approved status, dependencies, failures and next owner. Proposed paths are not produced artifacts; no skill grants external activation, spending or credentials.

## Acceptance

Detect missing or mixed versions, wrong destinations and partial activation. Local hashes alone do not prove remote delivery. Record executed evidence separately from plans. Use the [example](../../examples/screen-production/README.md) only within its declared scope.

Complete the [stage handoff](../design-stage-handoff/SKILL.md) with actual files, version, checks, unknowns and next owner.
