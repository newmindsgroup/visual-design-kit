---
name: design-display-production
description: Prepare editable display and motion deliverables for a specific player and installation.
---

# Display production

Version-Timestamp: 2026-09-11T09:45:01-04:00

Status: authored project-local instructions; not installed or production-certified.

## Inputs

Read the relevant [display workflow](../../DISPLAY-WORKFLOW.md) and reuse accepted inputs from the [display brief](../../templates/display-design-brief.md). Dependencies identify information needed, not mandatory repetition of approved work. Preserve baseline locks for precise changes.

## Method

Select an available authorized tool from the required editable source and output, not habit. A timeline deliverable requires an editable project with media/font dependencies; a rendered video is not an editable animation. Verify app/tool capability locally before claiming support. Reuse motion instructions when animation is selected.

Bind source version to exports and record resolution, orientation, pixel aspect, frame rate, codec/container/profile, bitrate/file limit, color interpretation, audio requirement, transparency and duration from operator specifications. Mark irrelevant fields not applicable. Test whether the actual player supports transparency, web runtime, live fonts or external network requests rather than assuming desktop-preview support.

Inspect full playback and loop seam, dropped frames, text hold times, scaling/cropping, color and multi-screen sync. Verify offline startup and recovery where relevant. Preserve source assets, font licenses and rendered/static fallback. Export a dependency manifest and rollback version; publish only within an authorized release scope.

## Output and acceptance

Editable project, bound exports, dependency manifest and recorded player checks. Missing target player keeps playback acceptance pending while local artifact checks remain useful.

Carry actual files, source versions, assumptions and remaining checks through the existing [stage handoff](../design-stage-handoff/SKILL.md).

## Screen-content extension

Version-Timestamp: 2026-09-11T19:51:13-04:00

Preserve editable sources, fonts and dependency manifests. Bind exports to screen IDs and versions; verify actual player specifications. Use the [specialist workflow](../../SCREEN-CONTENT-SKILLS.md) for the relevant detailed methods.

## Delivery format selection

Version-Timestamp: 2026-09-11T20:19:25-04:00

Compare still, rendered video, HTML and interactive application against message, update frequency, offline needs, target player support and editable-source requirements. Prefer the simplest format that meets the brief. Record why richer runtime is needed; do not default every campaign to an app. See [production workflow](../../SCREEN-PRODUCTION-WORKFLOW.md).

## Approved fallback and optimization manifest

Version-Timestamp: 2026-09-11T21:22:42-04:00

For every moving asset, associate a separately reviewed static fallback with the same message, current offer validity and required disclosures. Define missing/corrupt media, startup delay, decode failure and reduced-motion behavior where relevant. Distinguish a player-level fallback from one an interactive app implements; do not assume the player supports either. Test failure injection on the selected runtime and ensure a stale fallback cannot revive an expired promotion.

Record the actual player/container/codec/profile, dimensions, frame rate, bitrate or file-size budget, color expectations, audio policy and alpha support from verified specifications. Keep master and optimized delivery derivatives separate. Compare quality after resizing/compression, including small type, gradients, motion edges and transparency halos. If alpha is unsupported, composite against the intended background rather than export broken transparency. Avoid arbitrary universal bitrate/FPS defaults. Measure loading, decoding and sustained playback on the target hardware; missing hardware remains a delivery acceptance hold. Bind each export and fallback to hashes and a recoverable prior approved version.

Use the [display production detail checklist](../../templates/display-production-details.md) and preserve actual test evidence.
