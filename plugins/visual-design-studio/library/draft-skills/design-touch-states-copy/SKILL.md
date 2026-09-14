---
name: design-touch-states-copy
description: Touchscreen states and microcopy for retail screen content and related display projects.
---

# Touchscreen states and microcopy

Version-Timestamp: 2026-09-12T11:35:16-04:00

## Objective and inputs

Produce touchscreen states and microcopy within the user's screen-content scope. Read the [screen workflow](../../SCREEN-CONTENT-SKILLS.md) and reuse approved upstream files, brief, source versions and constraints. The catalog dependency `touchscreen-design` identifies required information, not a mandatory rerun. Missing inputs are explicit assumptions or scoped holds.

## Method

Use the canonical project state table owned by [touchscreen design](../design-touchscreen-design/SKILL.md). Map copy to its existing state IDs; attract, entry, loading, success, error, help, exit and idle reset are coverage examples, not a second state machine. Write short actionable copy and immediate input feedback. Warn before timeout and offer extension where required. Separate unknown transaction outcomes from failure; never encourage a blind retry.

## Output

State table with trigger, message, action, timeout, data retained and recovery. Carry source version, candidate status, editable file location, dependencies, limitations and next owner in the [handoff](../design-stage-handoff/SKILL.md). Choose an available tool suited to the artifact; a skill does not establish authentication, paid allowance or native editing capability.

## Acceptance

Walk through interrupted tasks, repeated taps, slow loading and session clearing with prior-user data absent. Record actual evidence and failures. Never label an unexecuted check passed. Maintain the approved baseline until the candidate is accepted.

## Unknown submission outcomes

Version-Timestamp: 2026-09-11T19:55:31-04:00

A dropped connection after submission means unknown, not failed. Use copy such as "We cannot confirm whether your request arrived." A user-clicked Retry is also unsafe before reconciliation; suppress repeat submission until status lookup or a verified idempotency contract makes it safe. Acknowledgment of receipt does not prove staff are on the way. Offer in-person help without inventing device dialer support. Use one coherent proposed timeout schedule, warning before reset, and retain active session data during extension. Reset must clear shopper-visible data while any required operational reconciliation stays isolated from the next session. Do not invent OS, files, versions or pass results; label proposals and untested transitions explicitly.

## Shared session and media contract

Touchscreen design owns the single project state table, its version and inactivity schedule. This skill owns messages mapped to those IDs; [touch media](../design-touch-media/SKILL.md) owns media actions mapped to the same transitions. Extend that table for a missing case rather than creating a parallel schedule or renaming states locally. Record the selected table path/hash in the handoff.

Define event ownership, cancellation, warning and extension before reset. Extension retains choices and cancels the pending reset. Reset clears shopper-visible data before attract resumes; unresolved operational actions remain isolated for reconciliation. The opening touch must not be handled twice. Verify late responses and interrupted entry using the [prepared exercises](../../examples/media-quality-recipes/README.md). Example state labels may be mapped to the project's established IDs.

Use the [display production detail checklist](../../templates/display-production-details.md) and preserve actual test evidence.
