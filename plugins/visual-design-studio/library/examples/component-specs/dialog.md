# C-051 Dialog: filled modal specification example

Version-Timestamp: 2026-09-10 20:21:45 AST

## Identity and scope

Record DLG-EX-01, candidate 1.0; inventory [C-051 Dialog](../../inventory/ui.md#c-051), family [overlay](../../inventory/families.md#overlay). Owner Codex; document review checks (historical source-version evidence, not bundled or inherited); work [WORK-EX-01](work-record.md). Optional item selected for a bounded informational interruption on web. This example contains read-only task information with a Close action. It has no form, irreversible confirmation, asynchronous save or unsaved edits.

Use when this temporary information must be read without interacting with the underlying view. Prefer inline content or a full page when interruption adds no value. Nonmodal panels, alerts, nested dialogs and C-052 Sheet and side panel are not this variant. In particular, a sheet can be nonmodal: shape or placement cannot establish modality.

## Select core and conditional behavior

This example's core is a read-only **web modal**, not every kind of overlay. This table owns applicability.

| Section | Activation condition and dependencies | Included states and criteria | Omission or hold |
| --- | --- | --- | --- |
| DLG-CORE | Every use of this modal example: naming, actual modality, initial/contained/return focus and reachable dismissal | DLG-S1 to DLG-S5; DLG-01 core and DLG-02; SH-01/SH-02 | Never omit modality or dismissal access. Missing configuration/fallback remains held; do not open a broken modal |
| DLG-OVERFLOW | Content overflows at any supported size or user setting, including a short V1 after enlargement | V1 or V2, existing open states; DLG-01 overflow branch and SH-02 | Mandatory when condition occurs. Never mark overflow safety omitted merely because the initial desktop sample fits; test the condition for both variants |
| DLG-CONSEQUENTIAL | Form edits, unsaved data, destructive effects or work continuing after dismissal | Outside this read-only example; retain core requirements but hold task-specific close/escape/save rules for an approved extension and criterion mapping | Reachable dismissal remains mandatory; the effect of requesting dismissal (save, discard, confirm or cancel) is what needs a task-specific contract. Do not reuse unconditional Close/Escape as permission to discard work. No completed consequential-close spec is supplied |
| DLG-NATIVE | A native presentation is requested | Outside detailed web scope; DEC-03 and separate C-052 selection if a sheet is appropriate | Held for platform/version and native semantics. Selecting this row does not turn ARIA/focus-loop instructions into a native implementation |

Long content is an optional content choice; accessible overflow handling is conditional safety, not an optional feature. Native adaptation and consequential workflows remain separate scoped work.

## Anatomy and content

DLG-V1 contains a modal surface, visible title “Details,” short structured body, visible Close button, background scrim and focusable title anchor for long content. Both V1 and V2 provide a named, keyboard-focusable scrolling body region whenever content overflows, with a persistent reachable Close control outside that region. V2 supplies the long-content fixture; V1 can also overflow after accessibility or viewport changes. The region has an accessible name such as “Details content” and tabindex=0 while scrolling is needed. Evaluate overflow after initial layout and again after content, font loading, viewport/zoom, text-size, spacing, forced-colors, user stylesheet or orientation changes. Update the region name/focusability before the next keyboard traversal. If overflow disappears while that region has focus, retain current focus with tabindex=-1 until the user leaves; do not pull focus elsewhere. Nonoverflowing bodies are not extra tab stops. It supports ordinary keyboard scrolling (arrows/Page Up/Page Down) while focused, without hijacking keys elsewhere. This is the same modal behavior, not a different modal contract. Tokens request surface.dialog, text.primary, border.dialog, overlay.scrim, space.dialog, type.heading/body and focus.indicator; map to approved roles and values. C-001 supplies the Close action; F-001/F-002/F-003/F-009 support presentation and focus.

Data is a title, read-only body content and invoker reference, all required before opening. Plain text and authored safe structure only; no arbitrary HTML injection. Missing title/body is a configuration failure: keep closed and expose a local visible unavailable reason at the trigger, not an empty modal. Long fixture: 20 numbered short paragraphs and a 120-character heading. These are stress cases, not product limits. No confidential payload or external data request is assumed.

## State catalog for selected sections

| State ID | Trigger and visible result | Input/focus/assistive result | Recovery and criterion |
| --- | --- | --- | --- |
| DLG-S1 closed/default | Initial or dismissed; surface absent from visual and focus interaction | Invoker available in normal page order | Valid activation opens S2. DLG-01 |
| DLG-S2 opening/open | Render surface/title and make background noninteractive for all input | Move focus inside to Close for short V1; to title anchor (tabindex=-1, programmatic only) for V2 or any overflowing V1 so beginning stays visible; Tab then reaches the overflowing body region and Close. Expose dialog role and name | Settles S3. DLG-01 |
| DLG-S3 focus within | Tab/Shift+Tab traverse contained controls and wrap; background stays inert | No positive tabindex ordering; assistive browsing cannot operate background. Dialog has modal semantics only while behavior is modal | Close button or Escape to S4. DLG-01 |
| DLG-S4 closing | Close/Escape removes modal and scrim | Restore invoker focus if still present and usable; otherwise the predeclared fallback section heading | S1. DLG-02 |
| DLG-S5 invalid configuration/unavailable | Missing required content before activation; remain closed with reason | Do not move focus to a nonexistent surface | Owner supplies complete content before retry. DLG-02 |

Backdrop activation does not dismiss in this teaching choice; pointer-down must not trigger a background action. A visible Close control is always reachable. The scrim is not itself a hidden focus target. Default hover/pressed states belong to C-001, not the modal container. Loading/error after opening, empty data, selected/mixed, busy saving and dirty-edit warnings are excluded because content is preloaded and read-only. Changing that assumption requires new states and acceptance methods first.

## Web and native contract

For web, prefer the platform dialog primitive where supported by the selected browser matrix; this is a semantic option, not a selected framework. Opening by a modal API and closing by the corresponding lifecycle must be tested. Coordinate the selected initial target with native dialog focusing/autofocus behavior so competing handlers do not move focus twice. Every close route, including a browser cancel/Escape close, runs the same DLG-S4 restoration path. Do not approximate modality by adding aria-modal to an interactive background. Name the dialog from its visible title. Rich structured bodies should be read in structure, not flattened into an enormous accessible description. Sources SRC-DIALOG and SRC-HTML-DIALOG guide this web example.

A native sheet is a separate C-052 choice. DEC-03 holds platform presentation until a real brief names OS, version, modality and content needs. iOS/iPadOS dismissal gestures, presentation sizes, accessibility focus and underlying navigation require current native guidance and device checks. The Apple source body could not be read with the text fetch in this milestone; no Apple-specific behavior is asserted as verified. Android's inspected Compose page describes sheet state/lifecycle, but no Compose runtime is chosen or copied. Android Back, predictive Back, keyboard handling, outside dismissal and system sheet lifecycle must be resolved for the actual version. Never port a DOM focus trap into a native sheet.

For narrow web layouts, allow surface and body to grow/scroll within available viewport; keep title context and a reachable Close control, including after virtual keyboard or zoom changes if future content introduces input. Do not clip body behind fixed actions. Restore prior page scroll after dismissal. RTL preserves semantic reading order and logically positioned controls. Long headings wrap; reduced motion removes nonessential opening movement without delaying focus or dismissal. SH-01/SH-02 apply.

Handoff: DLG-01/DLG-02 procedures, DLG-SP-01 specimen and DEC-03. Before project adoption specify the fallback focus target ID, supported browser matrix and actual interruption rationale. Destructive operations, unsaved edits, asynchronous work or native sheets require separate scoped refinements. No rendered or accessibility behavior has been tested here.
