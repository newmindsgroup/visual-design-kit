---
name: design-screen-cms-integration
description: CMS and player integration when producing or maintaining digital screen content.
---

# CMS and player integration

Version-Timestamp: 2026-09-12T11:33:18-04:00

## Inputs

Read the [production workflow](../../SCREEN-PRODUCTION-WORKFLOW.md). Reuse accepted `display-production` inputs, source versions, target specification and user scope. Dependencies require information, not restarting approved work. No fixture design is included.

## Method

Read the selected system contract and verify authentication through supported methods. Map screen IDs, editable fields, upload constraints, preview transformations and content expiry. Separate local packaging from upload and activation. Inspect returned IDs/readback after uncertain mutations rather than blindly retry. Add vendor adapters only when that system is required and verified.

## Outputs

Integration mapping, local package and explicitly scoped activation/readback plan. Use the [stage handoff](../design-stage-handoff/SKILL.md). Hand off actual files, version, candidate/approved status, dependencies, failures and next owner. Proposed paths are not produced artifacts; no skill grants external activation, spending or credentials.

## Acceptance

Check transformed preview versus source, exact target/version and expiry; a successful upload is not playback acceptance. Record executed evidence separately from plans. Use the [example](../../examples/screen-production/README.md) only within its declared scope.
