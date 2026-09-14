---
name: design-touch-media
description: Interactive media behavior for retail screen content and related display projects.
---

# Interactive media behavior

Version-Timestamp: 2026-09-12T11:35:16-04:00

## Objective and inputs

Produce interactive media behavior within the user's screen-content scope. Read the [screen workflow](../../SCREEN-CONTENT-SKILLS.md) and reuse approved upstream files, brief, source versions and constraints. The catalog dependency `touchscreen-design` identifies required information, not a mandatory rerun. Missing inputs are explicit assumptions or scoped holds.

## Method

Define which media responds to input and which is decorative. User actions take precedence over attract animation. Specify interruption, cancellation and return states; avoid hover dependencies. Provide reduced-motion alternatives and static fallback without losing meaning.

## Output

Interaction storyboard, media event contract and prototype specification. Carry source version, candidate status, editable file location, dependencies, limitations and next owner in the [handoff](../design-stage-handoff/SKILL.md). Choose an available tool suited to the artifact; a skill does not establish authentication, paid allowance or native editing capability.

## Acceptance

Test rapid taps, interrupted transitions, loading failure and motion preference without trapping navigation. Record actual evidence and failures. Never label an unexecuted check passed. Maintain the approved baseline until the candidate is accepted.

## Attract-to-interaction and media failure

Version-Timestamp: 2026-09-11T21:22:42-04:00

Make the first meaningful touch give immediate feedback and transition into usable navigation without waiting for a promotional clip to finish. State explicitly whether that first touch only dismisses the attract screen or also selects a visible control; do not accidentally activate a destination hidden beneath it. Cancel attract timers/media on entry, and suppress late load callbacks so they cannot overwrite the active task. Keep navigation usable when media fails; show a reviewed still or concise unavailable state that preserves the message. Avoid restarting attract mode merely because a clip ended.

On session end, coordinate with [touchscreen design, the session-state owner](../design-touchscreen-design/SKILL.md): clear shopper data and selections, cancel work tied to that session, then return to the correct attract state. Test repeated touches, slow media, touch during transition, reset during loading and an old response arriving after reset. Associate response/session IDs so old results cannot appear for a new shopper. Define reduced-motion behavior without disabling access to the underlying task.

Use the [display production detail checklist](../../templates/display-production-details.md) and preserve actual test evidence.
