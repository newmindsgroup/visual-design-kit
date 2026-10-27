# A component gallery that proves the system

Version-Timestamp: 2026-10-27 11:36:23 UTC

Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-27 11:36:23 UTC

## Set the purpose

Build a gallery from the same production components used by the product. A screenshot of a separate mock component does not verify the real implementation.
Read the project's accepted DESIGN.md, token source, existing component APIs and supported platforms first.
Extend a working Storybook, native gallery or specimen page before creating another runtime.
Keep gallery data synthetic and output in the adopting project, with the shared kit read-only.
For reference reconstruction, retain measured reference values in the candidate system and identify every deliberate adaptation.

## Separate three token layers

| Layer | Example | Consumer rule |
| --- | --- | --- |
| Primitive | Neutral ramp, accent ramp, spacing scale | Token definitions and explicit theme generation |
| Semantic | Foreground, surface, border, selected, error | Components read these roles |
| Component | Button padding or sidebar selection | Add only when a real exception needs a stable API |

Map approved project names to this model rather than renaming existing public tokens.
Keep brand and appearance overrides at the appropriate layer; a dark-mode correction should not need edits in every view.
Give motion roles a reduced-motion alternative and define icon keys through a semantic registry.
Document raw geometry exceptions such as a one-pixel hairline, optical offset or platform-required metric.
Use source searches as diagnostics. They cannot prove that every runtime value or generated asset follows the system.

## Inventory the parts before the pages

Start with the parts needed for one representative product screen, then expand from actual use.
Typical families include navigation rows, buttons, fields, checkboxes, select controls, badges, menus, list rows, dialogs and feedback.
Each family gets a stable ID and one implementation owner.
Record anatomy, content slots, public props, sizes, states, token dependencies and accessibility contract.
Reuse a native or headless control for behavior where possible. Custom drawing still needs focus, keyboard, activation and announcements.
Avoid a universal variant API that encodes every possible decoration. Keep variants tied to product meaning.
Name business composition separately from the primitive parts it contains.

## Define the state matrix

| Dimension | Required starting set | Scope condition |
| --- | --- | --- |
| Interaction | Rest, hover, pressed, focused, disabled | Hover only for pointer use |
| Selection | Off, on, mixed where supported | Only controls with a selection model |
| Operation | Idle, busy, success, error | Only asynchronous or validating components |
| Content | Empty, short, long, translated, missing | Use realistic bounded strings and actual overflow rules |
| Appearance | Light, dark, high contrast | Test every product-supported mode |
| Density | Comfortable and compact | Only if both are supported by the product |
| Window state | Active and inactive | Native chrome and selection appearance |

Not every Cartesian product needs its own card. Choose representative combinations, then explicitly cover interactions whose combinations create risk.
For example, verify a busy button cannot activate twice and an invalid field retains a visible focused error state.
A disabled specimen must actually be disabled in the interactive gallery, not merely look faded.
Record unsupported states as not applicable with a reason rather than silently omitting them.

## Provide forced visuals and real interaction

Use an explicit test-only state input for contact sheets so hover, pressed and error appearances can be captured deterministically.
Keep forced visuals separate from live controls that demonstrate real state transitions.
Do not ship a forced-state flag that can override authorization or enable a disabled production action.
In a native app use a debug gallery scene or declared snapshot route; keep production navigation unchanged unless a public component explorer is intended.
In web use a component explorer or project-local specimen page that imports actual components.
Show the semantic token names and relevant API values next to each example.
Include accessible names and keyboard instructions for interactive specimens.

## Add compositions

Place the same parts in a toolbar, a dense row, a form, a dialog and an empty/error view.
Compositions reveal issues individual cards hide: alignment, compounded spacing, focus order, clipped menus and misleading hierarchy.
Use a form with real-length labels and errors, a table with large numbers, and a narrow layout with translated text.
Test a loading region that preserves useful content and an error state with a visible recovery action.
For custom chrome, verify inactive appearance and keyboard navigation in the real native window.
A gallery remains necessary but insufficient for complete task-flow acceptance.

## Render, measure and inspect

Capture the selected matrix at actual target sizes, then create an enlarged diagnostic view only where needed.
On web start with 375, 768 and 1280 CSS px, overriding them to match the project's breakpoints and supported devices.
On macOS use minimum, preferred and wide window sizes in points, and record capture scale separately.
Inspect shared leading edges, text baselines, row pitch, insets, overflow and nested corner relationships.
Use frame probes for custom native layout and DOM bounds for web where available.
Compare light and dark using semantic-role checks rather than expecting every color to invert.
Verify visible focus, pointer feedback, keyboard activation, escape/cancel behavior and focus restoration.
Inspect contrast in the actual state, including selection, error and translucent surfaces.
Run project-specific tests and preserve screenshots for failures. A passing lint cannot replace visual inspection.

## Version the gallery with the components

Bind gallery source, component source, token build and screenshot version in one evidence record.
Retain a prior accepted baseline before changing tokens or component APIs.
For each change record intended delta, affected consumers, render checks, behavior checks and known limitations.
A new token value can affect many components even when only one source file changed; select regression specimens by dependency.
Do not update a visual baseline merely because a comparison failed. Inspect the difference and record why the new result is accepted.

## Deliverable and acceptance

Deliver the component inventory, state matrix, live gallery, token mapping and rendered evidence in the project.
Every required product part has an implementation and a gallery entry tied to the same version.
Every tested claim names its environment and actual result.
Static cards, simulated state rendering and working interactive controls are labeled separately.
Remaining runtime, assistive-technology and device checks have a next action; they are not converted into assumed passes.

## Sources

- [BAMA custom design kit](https://github.com/daveebbelaar/bama/tree/15356bd8ebff408222ad21395aea09bd74b15310/skills/design/design-kit): tokens, real controls, state gallery and measured composition methods.
- [UI system process](../../../library/draft-skills/design-ui-system/SKILL.md): existing project records and component evidence.
