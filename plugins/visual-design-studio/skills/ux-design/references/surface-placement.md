# Put each task on the right surface

Version-Timestamp: 2026-10-27 11:36:23 UTC

Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-27 11:36:23 UTC

## Begin with the action and its scope

Record who acts, what object changes, what they need to see, how long the task lasts and whether parallel work matters.
Read accepted project flows, terminology and platform conventions before selecting a new surface.
For a reconstruction, document the observed placement first. Change it only as a declared adaptation or to meet an explicit target requirement.
Do not turn every feature into a modal because that is the easiest implementation.
Use one consistent noun for each object and a verb plus object for its commands.
A glossary only needs the terms that affect the current feature; it is not a prerequisite for every small change.

## Choose the lightest sufficient container

| Situation | Starting surface | Override condition |
| --- | --- | --- |
| Change one visible value | Inline edit | A multi-field dependent task needs a larger scoped editor |
| Choose a small nearby option | Popover or anchored menu | Long content or required context needs a persistent panel |
| Inspect the current selection while continuing work | Inspector or detail pane | Independent comparison needs a separate window |
| Adjust a setting while watching its effect | Nonmodal panel or inline controls | A committed transaction needs explicit Apply/Cancel |
| Finish one bounded blocking task | Sheet or dialog | Multi-step or parallel work may need a page or window |
| Work on a durable destination | Page or sidebar destination | A temporary subtask does not need a top-level destination |
| Keep a long task beside other work | Separate window on desktop | On compact devices use a full-screen destination |
| Decide an immediate consequence | Confirmation dialog | Reversible low-consequence work may use immediate action with Undo |
| Explain a local issue | Inline message near the cause | A persistent global outage needs a banner |
| Confirm a completed transient action | Brief status with Undo when relevant | Important results need a persistent location |

Choose by task and platform. A web modal, macOS sheet and mobile bottom sheet have different navigation and sizing contracts.
Keep a maximum of one blocking modal at a time. Replace or complete the current subtask instead of nesting sheets.
A popover should not hide information required to make its choice.
Do not put a recovery action only in a disappearing toast.

## Write the minimum complete flow

List entry, prerequisite, first focus, input, validation, completion, visible result and exit.
Add alternative entry routes such as menu, toolbar, context menu and keyboard shortcut where the product supports them.
Give each transition a stable state ID so screenshots and tests can reference it.
Identify what remains visible and interactive while the surface is open.
Specify what happens if the selected object changes, disappears or becomes inaccessible during the task.
For work that changes saved data, define save timing, error recovery and duplicate-action prevention.
A fast closing animation does not prove the change was saved.

## Define focus and dismissal

A typing task opens with focus in its primary field when expected.
A choice task puts focus on a safe useful control while preserving a logical traversal order.
Specify whether Return submits, inserts a line break or performs another action; multi-line editors need an explicit rule.
Escape cancels or closes the current temporary surface where the platform expects it.
On close return focus to the triggering control, or the nearest sensible location if that control no longer exists.
On web, a modal traps focus inside while open and makes the background unavailable to interaction.
On native platforms use the system sheet or dialog behavior and verify the actual keyboard result.
Click-outside dismissal suits a disposable popover, but should not discard meaningful typed work silently.
Ask before discard only when actual unsaved work would be lost.
Do not remove focus indicators merely to make an opening screenshot look calmer.

## Specify every consequential state

| State | Required content and behavior |
| --- | --- |
| Empty | Purpose, what belongs here and a clear first action |
| Loading | Preserve useful prior content; show progress or status when delay matters |
| Invalid | Error next to the cause, retained input and a concrete correction |
| Failed operation | What failed, what remains saved and Retry or recovery |
| Partial result | What succeeded, what did not and how to continue |
| Permission denied | Why the feature is unavailable and the supported next step |
| Success | Visible result in context, with Undo or a durable result location |
| Large content | Overflow, long labels, many rows and stable selection/focus |

Use a progress indicator when the task is slow enough to need feedback; start around 400ms to 500ms, then tune from observed performance.
Known-duration operations benefit from determinate progress. Safe long tasks need Cancel or a background completion path.
Preserve typed input after an error and keep repeated activation from submitting twice.
A disabled command needs an understandable context; do not hide all affordances while loading.

## Write the interface words

Use specific actions such as "Rename project", "Export report" and "Retry upload".
Follow the platform's casing and ellipsis convention consistently instead of imposing one casing across every platform.
Use an ellipsis when a command opens a step requiring more input, if that is the platform convention.
Confirmation titles and action labels name the consequence; avoid Yes/No when Delete/Cancel is clearer.
Error text states the problem and recovery without blaming the person.
Give icon-only controls an accessible action name; tooltips add detail and shortcuts rather than carrying essential meaning.
For AI suggestions separate generated output, user edits and the action that applies a change.
Never imply that a generated preview has already changed the underlying record.

## Render and exercise the decision

Render the entry surface, open state, validation error, successful result and cancellation/recovery path.
Test narrow/short and large layouts, long translated labels, light/dark and visible focus as applicable.
Exercise the complete task with keyboard alone and with the actual pointer or touch route.
Verify focus stays visible, reaches all controls and returns sensibly after dismissal.
Inspect whether the surface obscures the content needed for its task.
Measure task completion and correction costs when usability evidence is available; AI inspection is not a user study.
For a native app capture the real surface. A browser wireframe supports a layout decision, not native-window acceptance.

## Record the handoff

Write a concise block with task, entry, surface rationale, state IDs, words, focus, commands and recovery.
Attach observed evidence or clearly labeled hypotheses to the placement decision.
Reuse accepted flows instead of asking the user to approve the same foundation repeatedly.
Keep unresolved behavior and next checks in the adopting project's work record.

## Sources

- [BAMA UX design](https://github.com/daveebbelaar/bama/tree/15356bd8ebff408222ad21395aea09bd74b15310/skills/design/ux-design): surface selection, words and state coverage.
- [Apple modality](https://developer.apple.com/design/human-interface-guidelines/modality) and [WAI-ARIA dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/): platform and web behavior to verify for the target implementation.
