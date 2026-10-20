# Accessibility: WCAG 2.2 AA and keyboard patterns

Version-Timestamp: 2026-10-20 02:04:32 UTC

WCAG 2.2 (W3C Recommendation, October 2023) Level AA is the kit's minimum for every interface. Design for it from the first wireframe; retrofitting costs far more. Legal regimes reference different versions (EN 301 549 under the European Accessibility Act, applied since 28 June 2025, maps to WCAG 2.1 AA in its 2021 version, with a 2.2-aligned revision in progress (verify the current edition); US ADA cases and the DOJ's 2024 Title II rule use WCAG 2.1 AA); designing to 2.2 AA covers them. Confirm requirements with counsel for the specific product and jurisdiction.

## WCAG 2.2 A and AA checklist

New in 2.2 are marked **NEW**. 4.1.1 Parsing was removed in 2.2.

### Perceivable

| SC | Level | Requirement and the numbers | Design check |
| --- | --- | --- | --- |
| 1.1.1 Non-text Content | A | Text alternative for meaningful images, icons and controls | Write alt text in the spec; decorative images `alt=""` |
| 1.2.1-1.2.3 | A | Transcripts for audio, captions and audio description (or text alternative) for prerecorded video | Budget captions in video production |
| 1.2.4 Captions (Live), 1.2.5 Audio Description | AA | Live captions; audio description for prerecorded video | |
| 1.3.1 Info and Relationships | A | Structure in markup: headings, lists, tables, labels, fieldsets | Annotate heading levels and landmarks in designs |
| 1.3.2 Meaningful Sequence | A | Reading order matches visual order | Do not reorder with CSS alone |
| 1.3.3 Sensory Characteristics | A | Instructions do not rely on shape, position or sound alone | Not "click the round button on the right" |
| 1.3.4 Orientation | AA | Works in portrait and landscape | No orientation lock unless essential |
| 1.3.5 Identify Input Purpose | AA | `autocomplete` on personal-data fields | See [forms](forms.md) |
| 1.4.1 Use of Color | A | Color is never the only cue | Add icons, text, patterns, underlines for links in text |
| 1.4.2 Audio Control | A | Audio over 3 s that plays automatically can be paused or muted | Avoid autoplay with sound |
| 1.4.3 Contrast (Minimum) | AA | Text 4.5:1; large text (24px+, or 18.66px+ bold) 3:1 | Check every text token pair, including placeholders you rely on |
| 1.4.4 Resize Text | AA | Readable and functional at 200% text size | Use rem units; no fixed-height text containers |
| 1.4.5 Images of Text | AA | Real text instead of text in images | Except logos |
| 1.4.10 Reflow | AA | No two-dimensional scrolling at 320 CSS px wide (400% zoom of 1280) or 256px tall | Tables and maps may scroll within their region |
| 1.4.11 Non-text Contrast | AA | UI component boundaries, states, focus indicators and meaningful graphics 3:1 against adjacent colors | Input borders, checkbox outlines, chart lines |
| 1.4.12 Text Spacing | AA | No loss when users set line height 1.5, paragraph spacing 2x font size, letter spacing 0.12em, word spacing 0.16em | Avoid fixed heights on text boxes |
| 1.4.13 Content on Hover or Focus | AA | Tooltips and popovers are dismissible (Esc), hoverable and persistent | |

### Operable

| SC | Level | Requirement and the numbers | Design check |
| --- | --- | --- | --- |
| 2.1.1 Keyboard | A | Everything works with a keyboard | Specify keys per component (below) |
| 2.1.2 No Keyboard Trap | A | Focus can always move away | Modals trap intentionally but close with Esc |
| 2.1.4 Character Key Shortcuts | A | Single-key shortcuts can be turned off, remapped, or only work on focus | |
| 2.2.1 Timing Adjustable | A | Time limits can be turned off, adjusted or extended (warn with at least 20 s to extend) | Session timeouts, auto-advancing toasts with actions |
| 2.2.2 Pause, Stop, Hide | A | Moving or auto-updating content lasting over 5 s can be paused | Carousels, marquees, animated backgrounds need a pause control |
| 2.3.1 Three Flashes | A | Nothing flashes more than 3 times per second | |
| 2.4.1 Bypass Blocks | A | Skip link or landmarks | "Skip to main content" |
| 2.4.2 Page Titled | A | Unique, descriptive `title` | "Invoices - Acme" |
| 2.4.3 Focus Order | A | Logical focus order | Annotate tab order on complex screens |
| 2.4.4 Link Purpose (In Context) | A | Link text plus context explains the destination | No bare "Read more" lists |
| 2.4.5 Multiple Ways | AA | More than one way to find pages (nav, search, sitemap) | |
| 2.4.6 Headings and Labels | AA | Headings and labels describe topic or purpose | |
| 2.4.7 Focus Visible | AA | Keyboard focus is visible | 2px `--color-focus-ring`, 2px offset |
| 2.4.11 Focus Not Obscured (Minimum) | AA **NEW** | A focused element is not entirely hidden by author content (sticky headers, footers, cookie banners, chat widgets) | `scroll-padding-top` / `-bottom` equal to sticky UI height; non-modal banners must not cover focus |
| 2.5.1 Pointer Gestures | A | Multipoint or path gestures (pinch, swipe paths) have a single-pointer alternative | Buttons for zoom and carousel |
| 2.5.2 Pointer Cancellation | A | Actions fire on up-event, with a way to abort | No actions on pointer-down |
| 2.5.3 Label in Name | A | Accessible name contains the visible label text | Speech users say what they see |
| 2.5.4 Motion Actuation | A | Shake or tilt features have a UI alternative and can be disabled | |
| 2.5.7 Dragging Movements | AA **NEW** | Anything done by dragging can be done with single-pointer clicks or taps | Sortable lists get move up/down buttons or a menu; sliders accept clicks on the track; kanban cards get "Move to" |
| 2.5.8 Target Size (Minimum) | AA **NEW** | Targets at least 24x24 CSS px, unless spaced so a 24px-diameter circle centered on each does not overlap another target or circle; exceptions for inline links in text, equivalent controls elsewhere, user-agent controls, and essential presentation | `--size-target-min`; use 44x44 (`--size-target-comfortable`) for touch-first UI |

### Understandable

| SC | Level | Requirement and the numbers | Design check |
| --- | --- | --- | --- |
| 3.1.1 Language of Page, 3.1.2 Language of Parts | A, AA | `lang` on `html` and on passages in other languages | |
| 3.2.1 On Focus, 3.2.2 On Input | A | Focus or changing a value does not trigger unexpected context changes | No auto-submit on select change without warning |
| 3.2.3 Consistent Navigation | AA | Repeated navigation in the same order | |
| 3.2.4 Consistent Identification | AA | Same function, same label and icon | |
| 3.2.6 Consistent Help | A **NEW** | Help mechanisms (contact details, chat, help link, self-help) appear in the same relative order on every page where they appear | Fix the help link's position in header or footer |
| 3.3.1 Error Identification, 3.3.2 Labels or Instructions | A | Errors described in text; labels and instructions provided | |
| 3.3.3 Error Suggestion | AA | Suggest a correction when known | "Did you mean gmail.com?" |
| 3.3.4 Error Prevention (Legal, Financial, Data) | AA | Reversible, checked or confirmed submissions for legal, financial or data-changing transactions | Review step before payment |
| 3.3.7 Redundant Entry | A **NEW** | Information already entered in the same process is auto-populated or selectable, unless re-entry is essential (security, memory exercises) or the data is no longer valid | "Same as delivery address"; carry data across steps |
| 3.3.8 Accessible Authentication (Minimum) | AA **NEW** | No cognitive function test (memorizing, transcribing, puzzles) for sign-in unless there is an alternative, a helping mechanism (paste, password managers), or it is object recognition or personal-content recognition | Allow paste and autofill; offer passkeys or email links; avoid text CAPTCHAs |

### Robust

| SC | Level | Requirement | Design check |
| --- | --- | --- | --- |
| 4.1.2 Name, Role, Value | A | Custom controls expose name, role, state | Prefer native elements; follow ARIA patterns below |
| 4.1.3 Status Messages | AA | Status messages are announced without moving focus | `role="status"` for toasts and result counts; `role="alert"` for urgent errors |

AAA criteria worth adopting where feasible: 2.4.13 Focus Appearance (focus indicator at least as large as a 2 CSS px perimeter with 3:1 change in contrast), 2.3.3 Animation from Interactions (honor `prefers-reduced-motion`), 1.4.6 Contrast Enhanced (7:1, the kit's high-contrast mode).

## ARIA Authoring Practices keyboard patterns

From the W3C WAI-ARIA Authoring Practices Guide (APG). Use native HTML first (`button`, `a`, `input`, `select`, `details`, `dialog`); add ARIA only to build what HTML lacks. No ARIA is better than wrong ARIA.

| Pattern | Keys |
| --- | --- |
| Button | Enter and Space activate |
| Link | Enter activates |
| Checkbox | Space toggles |
| Radio group | Tab enters the group at the checked radio; arrow keys move and select; Tab leaves the group |
| Switch | Space toggles (Enter optional) |
| Disclosure (show/hide, site nav submenus) | Enter or Space toggles; `aria-expanded` on the button |
| Accordion | Enter or Space toggles a section; optional Up/Down, Home/End between headers |
| Tabs | Left/Right move between tabs (Up/Down if vertical); Home/End; Tab moves into the panel; automatic or manual activation |
| Menu button and menu | Enter, Space or Down opens and focuses the first item; Up opens at the last; arrows move; Home/End; type-ahead; Esc closes and returns focus; Tab closes and moves on |
| Listbox | Up/Down move; Home/End; type-ahead; multi-select: Space toggles, Shift+arrows extend |
| Combobox (autocomplete, command palette) | Down opens and moves into the list; Up moves up; Enter accepts; Esc closes (second Esc clears); Alt+Down opens without moving; focus stays in the input with `aria-activedescendant` |
| Dialog (modal) | Focus moves inside on open (first field, or the least destructive action); Tab and Shift+Tab cycle within; Esc closes; focus returns to the trigger |
| Slider | Left/Down decrease, Right/Up increase; Page Up/Down larger steps; Home/End min and max |
| Toolbar | One tab stop for the whole toolbar; arrows move between controls |
| Grid (editable tables, spreadsheets) | Arrows move between cells; Home/End row ends; Ctrl+Home/End grid ends; Enter or F2 edits a cell |
| Tree view | Up/Down move; Right expands or moves to first child; Left collapses or moves to parent; Home/End; type-ahead |
| Tooltip | Appears on focus and hover; Esc dismisses |
| Carousel | Rotation pauses on hover and focus; a visible Pause control; previous and next buttons |

**Focus management techniques:** a roving `tabindex` (the active item has `tabindex="0"`, others `-1`) for composite widgets such as tabs, toolbars and radio groups; `aria-activedescendant` when focus must stay in an input (combobox). Use the `inert` attribute on background content behind modals.

## Testing routine

1. **Automated:** axe-core (browser extension or CI) on every template and state. Deque's own analysis reports axe finds about 57% of issues by volume; the rest need people.
2. **Keyboard only:** unplug the mouse; complete every key task; check visible focus at every step, logical order, no traps, nothing hidden under sticky UI.
3. **Screen readers:** VoiceOver with Safari (macOS and iOS), NVDA with Firefox or Chrome (Windows), TalkBack with Chrome (Android). Check names, roles, states, headings, landmarks and announcements.
4. **Zoom and reflow:** 200% text resize, 400% browser zoom at 1280px (equals 320px), and the text-spacing bookmarklet.
5. **Preferences:** `prefers-reduced-motion`, `prefers-contrast: more` (the kit's high-contrast theme), Windows forced-colors mode (`forced-colors: active`), dark mode.
6. **Color:** check every text and UI token pair; simulate common color-vision deficiencies.
7. **Content:** alt text, link text, headings outline, reading level.

Record each failure with the SC number, the element, and the fix, and rate severity with the scale in `ux-design` [heuristics and laws](../../ux-design/references/heuristics-and-laws.md); any failure that blocks a task for a group of users is severity 4.
