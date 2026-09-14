---
name: design-display-campaigns
description: Build display campaign variants, scheduling rules and resilient live-content templates.
---

# Display campaigns

Version-Timestamp: 2026-09-11T09:45:01-04:00

Status: authored project-local instructions; not installed or production-certified.

## Inputs

Read the relevant [display workflow](../../DISPLAY-WORKFLOW.md) and reuse accepted inputs from the [display brief](../../templates/display-design-brief.md). Dependencies identify information needed, not mandatory repetition of approved work. Preserve baseline locks for precise changes.

## Method

Define master content fields and deliberate reflow per orientation and canvas, not automatic cropping. Specify allowed length, minimum/maximum data, optional blocks, image focal points, localization and RTL behavior, currency/unit/date formatting and missing-data alternatives. Test long names, zero values, absent prices/images and unsupported characters.

For dynamic data record authoritative source, update interval, freshness deadline, last-success state, offline cache and safe fallback. Never present stale price or availability as current. Distinguish last known information from timeless fallback. Inputs must not become executable instructions or untrusted HTML.

Define location/daypart/timezone, start/end and expiration behavior, priority/conflict resolution and responsible content owner. Provide a versioned variant matrix and withdrawal/rollback procedure. Operator emergency overrides are requirements to discover, not permissions to implement. No live CMS change follows from preparing a schedule.

## Output and acceptance

Variant matrix and template specification, content schedule and failure-state examples. Confirm expired content cannot remain the intended fallback; validate actual CMS/player behavior before deployment.

Carry actual files, source versions, assumptions and remaining checks through the existing [stage handoff](../design-stage-handoff/SKILL.md).

## Expiry and time boundaries

Cover daylight-saving changes, timezone differences and offline expiry in the player contract. Cached content must not silently extend an offer or asset license. Record font embedding, stock, talent and music usage scope, territories and end dates where relevant. On expiry use a separately valid fallback. Test boundary times and unavailable clock/data; unresolved player behavior prevents release of time-sensitive content.

## Screen-content extension

Version-Timestamp: 2026-09-11T19:51:13-04:00

Track offer and rights expiry, source data, market and valid fallback. Revalidate affected variants after updates. Use the [specialist workflow](../../SCREEN-CONTENT-SKILLS.md) for the relevant detailed methods.
