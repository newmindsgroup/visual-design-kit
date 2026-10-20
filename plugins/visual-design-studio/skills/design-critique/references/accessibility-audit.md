# 15-minute accessibility audit

Version-Timestamp: 2026-10-20 02:29:27 UTC

A quick, repeatable pass that catches most blocking problems in a web page, app screen or HTML artifact before a design review or delivery. It is not a full WCAG 2.2 conformance audit, does not replace testing with disabled people, and does not certify anything. Record what you ran, on which build, and what you could not test.

Standard: W3C WCAG 2.2 level AA. Success-criterion numbers are given so findings can be traced; read the W3C "Understanding" page for any criterion you are unsure of.

## Before you start (1 minute)

- Pick the 1-3 core tasks for this artifact (read the article, submit the form, complete checkout, find opening hours).
- Open the build you are reviewing, not a mock-up of it. Note the URL or file and the commit or version.
- Have [render_review.mjs](../scripts/render_review.mjs) ready, or the axe DevTools browser extension.

## 1. Automated pass (minutes 0-2)

```sh
node ../scripts/render_review.mjs <file-or-url> --widths 320,390,1440 --full-page
```

- axe-core runs when `axe-core` resolves or `AXE_SCRIPT` points at `axe.min.js`. Log every violation with its rule ID, impact and target.
- The report's own contrast sampling covers text on solid backgrounds; anything listed under `unmeasured` (text over images, gradients, glass) goes to step 5.
- Automated tools catch only part of real issues (published estimates run from about 30% to 57%, depending on how issues are counted). A clean report means "nothing obvious", not "accessible".

## 2. Keyboard-only pass (minutes 2-5)

Put the mouse away. Use Tab, Shift+Tab, Enter, Space, arrow keys and Esc only.

| Check | Pass when | WCAG |
| --- | --- | --- |
| Reach everything | Every link, button, field and custom control is reachable and operable | 2.1.1 |
| No trap | Focus can always leave a widget, embed or dialog | 2.1.2 |
| Order | Focus follows the visual reading order | 2.4.3 |
| Skip link | First Tab reveals a "Skip to content" link on pages with repeated navigation | 2.4.1 |
| Dialogs | Focus moves into a dialog on open, stays inside, Esc closes it, focus returns to the trigger | 2.1.2, 2.4.3 |
| Not obscured | Sticky headers, cookie bars and chat bubbles never fully cover the focused element | 2.4.11 |
| Hover content | Tooltips and menus that open on hover also open on focus, can be dismissed with Esc and stay while hovered | 1.4.13 |

Complete each core task by keyboard. If you cannot, that is a blocker (Accessibility score 1).

## 3. Focus visibility (minute 5-6)

- Every focused element shows a visible indicator (2.4.7). Browser defaults removed with `outline: none` and no replacement is a failure.
- Aim for a 2px or thicker outline with 3:1 contrast against the colors next to it, offset 2px from the element. That meets most of the AAA Focus Appearance criterion (2.4.13) and survives on both light and dark surfaces.
- Use `:focus-visible` so mouse clicks do not show rings while keyboard focus always does.

## 4. Zoom, reflow and text spacing (minutes 6-9)

| Check | How | Pass when | WCAG |
| --- | --- | --- | --- |
| 200% zoom | Browser zoom to 200% at 1280px wide | No text cut off, overlapping or hidden; all functions still available | 1.4.4 |
| 400% reflow | Browser zoom to 400% at 1280px wide (equals 320 CSS px), and `render_review.mjs --widths 320` as a second view | Content reads in one column with no horizontal scrolling, except data tables, maps and diagrams | 1.4.10 |
| Text spacing | Inject: `*{line-height:1.5!important;letter-spacing:.12em!important;word-spacing:.16em!important} p{margin-bottom:2em!important}` | No clipped or overlapping text; fixed-height boxes grow | 1.4.12 |

A narrow viewport is not identical to browser zoom (fixed pixel media queries and `vw` type behave differently). Record both results separately.

## 5. Contrast spot checks (minutes 9-11)

Measure with a picker (the DevTools color picker or the report's `contrast.failures`). To check a whole palette's token pairs at once, use `library/scripts/craft_tools.py`, which audits opaque sRGB pairs from a JSON palette. Check these places first, because they fail most often:

| Element | Minimum | WCAG |
| --- | --- | --- |
| Body text and labels | 4.5:1 | 1.4.3 |
| Large text (24px+, or 18.66px+ bold) | 3:1 | 1.4.3 |
| Muted text, captions, placeholder text that carries information | 4.5:1 | 1.4.3 |
| Text over photos, video, gradients or glass: test the lightest (or darkest) spot behind the glyphs | 4.5:1 | 1.4.3 |
| Input borders, checkbox and radio outlines, icon-only buttons, chart lines that carry meaning | 3:1 against adjacent colors | 1.4.11 |
| Links inside body text distinguished only by color | 3:1 against the surrounding text, or add an underline | 1.4.1 |
| Error, success and required states | Never color alone: add text or an icon with a text alternative | 1.4.1 |

Disabled controls and pure decoration are exempt from 1.4.3, but a disabled primary button should still look deliberately disabled, not broken.

## 6. Target sizes (minute 11-12)

- WCAG 2.2 AA (2.5.8): pointer targets at least 24x24 CSS px, or spaced so a 24px circle around each does not overlap another target. Inline text links are exempt.
- Recommended for touch: 44x44 (WCAG 2.5.5 AAA; Apple HIG 44pt) or 48x48dp (Material Design 3). Check icon buttons, close buttons, pagination, carousel dots and footer link lists at 390px.

## 7. Motion and flashing (minute 12-13)

- Emulate reduced motion: DevTools, Rendering panel, "Emulate CSS media feature prefers-reduced-motion: reduce", or `render_review.mjs --reduced-motion`. Large movement, parallax and autoplaying motion should stop or become opacity-only.
- Anything that moves, blinks or auto-updates for more than 5 seconds needs a pause or stop control (2.2.2).
- Nothing flashes more than three times per second (2.3.1).

## 8. Screen reader smoke test (minutes 13-15)

Test one desktop screen reader; add mobile when the artifact is mobile-first.

| Reader | Start | Useful keys |
| --- | --- | --- |
| VoiceOver (macOS, Safari) | Cmd+F5 | VO = Control+Option. VO+U opens the rotor (headings, landmarks, links, form controls); VO+Right Arrow reads next; VO+Space activates |
| NVDA (Windows, Firefox or Chrome) | Ctrl+Alt+N | H next heading, D next landmark, K next link, F next form field, B next button, NVDA+F7 elements list, NVDA+Space toggles browse and focus mode |
| VoiceOver (iOS) | Settings, Accessibility, VoiceOver (or the Accessibility Shortcut) | Swipe right for next item, double-tap to activate, rotor with a two-finger twist |

Listen for:

- **Page title and language:** the title names the page; `lang` is set (and `dir="rtl"` for Arabic or Hebrew).
- **Headings:** one H1, a logical outline in the rotor or elements list (1.3.1).
- **Landmarks:** header, nav, main and footer present; one main.
- **Names:** every button and link says what it does out of context ("Download floor plan (PDF)", not "Click here"); icon-only buttons have accessible names (4.1.2).
- **Images:** informative images have alt text that says what matters; decorative images are silent (`alt=""` or `aria-hidden`) (1.1.1).
- **Forms:** each field announces its label, required state and hint; errors are announced and say how to fix them (3.3.1, 3.3.2).
- **Dynamic updates:** toasts, cart counts and validation messages are announced (status messages, 4.1.3).

## Record

| # | Finding | Where (width, element) | WCAG | Severity | Fix |
| --- | --- | --- | --- | --- | --- |
| 1 | | | | Blocker / Major / Minor | |

- **Blocker:** a core task cannot be completed by keyboard or screen reader, or core content fails contrast. Delivery stops.
- **Major:** an AA failure on secondary content or a workaround exists.
- **Minor:** best-practice issues (verbose alt text, redundant ARIA).

Add a line for what you did not test (for example "No Windows machine: NVDA not run"; "Native app: tested in simulator only"). Score Accessibility in the [rubric](rubric.md) from this record: any Blocker or Major caps it at 2.

## Common design-side fixes

- Raise muted text to 4.5:1 rather than enlarging it; enlarge only when the role allows.
- Replace placeholder-as-label with a visible label above the field.
- Give focus rings a two-color treatment (for example a 2px dark ring with a 2px light offset) so they work on any background.
- Put text over images on a scrim or plate, or move it beside the image.
- Add text to status colors ("Overdue", "Paid") and patterns or labels to chart series.
