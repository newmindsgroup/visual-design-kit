---
name: design-screen-multiscreen
description: Multiple-screen coordination for retail screen content and related display projects.
---

# Multiple-screen coordination

Version-Timestamp: 2026-09-11T19:51:13-04:00

## Objective and inputs

Produce multiple-screen coordination within the user's screen-content scope. Read the [screen workflow](../../SCREEN-CONTENT-SKILLS.md) and reuse approved upstream files, brief, source versions and constraints. The catalog dependency `display-discovery` identifies required information, not a mandatory rerun. Missing inputs are explicit assumptions or scoped holds.

## Method

Map content to supplied screen IDs and dimensions only. Decide complementary versus synchronized messages. Use synchronization only when the player contract supports it; specify drift and independent fallback behavior. Avoid splitting essential words or product information across screens.

## Output

Content screen map, per-screen exports and synchronization assumptions. Carry source version, candidate status, editable file location, dependencies, limitations and next owner in the [handoff](../design-stage-handoff/SKILL.md). Choose an available tool suited to the artifact; a skill does not establish authentication, paid allowance or native editing capability.

## Acceptance

Test one screen absent and unsynchronized playback; coordinated art is not proof of synchronized hardware. Record actual evidence and failures. Never label an unexecuted check passed. Maintain the approved baseline until the candidate is accepted.
