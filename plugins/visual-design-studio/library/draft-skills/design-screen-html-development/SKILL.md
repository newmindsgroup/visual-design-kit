---
name: design-screen-html-development
description: HTML signage development when producing or maintaining digital screen content.
---

# HTML signage development

Version-Timestamp: 2026-09-12T11:33:18-04:00

## Inputs

Read the [production workflow](../../SCREEN-PRODUCTION-WORKFLOW.md). Reuse accepted `screen-data-content` inputs, source versions, target specification and user scope. Dependencies require information, not restarting approved work. No fixture design is included.

## Method

Build local-first fixed-canvas content using the verified target browser engine. Bundle licensed fonts/media locally. Define loading, missing-asset and static fallback states. Avoid external font/CDN dependencies. Manage animation start, pause, visibility changes and cleanup; do not assume desktop APIs exist on a player. Escape untrusted content, validate URLs and avoid embedding secrets.

## Outputs

Offline package, runtime compatibility contract and runnable preview. Use the [stage handoff](../design-stage-handoff/SKILL.md). Hand off actual files, version, candidate/approved status, dependencies, failures and next owner. Proposed paths are not produced artifacts; no skill grants external activation, spending or credentials.

## Acceptance

Cold-start offline, missing assets, reduced motion, aspect changes and intended player compatibility. Use the example as a bounded starting point, not a universal player framework. Record executed evidence separately from plans. Use the [example](../../examples/screen-production/README.md) only within its declared scope.
