# Contrast

Version-Timestamp: 2026-10-20 02:07:10 UTC

WCAG 2.2 contrast is the compliance baseline: it is what accessibility law and procurement reference (for example EN 301 549 in the EU and Section 508 in the US both reference WCAG 2.x). APCA is a newer perceptual model, useful as an advisory second opinion, especially in dark mode. Pass WCAG first; use APCA to tune.

## WCAG 2.2 math

1. Convert each sRGB channel (0-255) to 0-1, then linearize: `c <= 0.04045 ? c / 12.92 : ((c + 0.055) / 1.055) ^ 2.4`.
2. Relative luminance: `Y = 0.2126 R + 0.7152 G + 0.0722 B`.
3. Contrast ratio: `(Y_lighter + 0.05) / (Y_darker + 0.05)`, from 1:1 to 21:1.

(The WCAG text uses 0.03928 as the threshold; the difference from 0.04045 never changes a result at two decimals.)

Worked example: `#767676` on white. Linear channel value 0.1812, so Y = 0.1812; ratio = 1.05 / 0.2312 = 4.54:1. It is the lightest neutral gray that passes 4.5:1 on white.

Reference grays on white (computed): `#595959` 7.00:1, `#767676` 4.54:1, `#949494` 3.03:1, `#999999` 2.85:1, `#AAAAAA` 2.32:1.

## WCAG 2.2 thresholds

| Success criterion | Level | Requirement |
| --- | --- | --- |
| 1.4.3 Contrast (Minimum) | AA | Text 4.5:1; large text 3:1 |
| 1.4.6 Contrast (Enhanced) | AAA | Text 7:1; large text 4.5:1 |
| 1.4.11 Non-text Contrast | AA | 3:1 for UI component boundaries and states, and graphics needed to understand content |
| 1.4.1 Use of Color | A | Color is not the only way to convey information |
| 2.4.7 Focus Visible | AA | A visible keyboard focus indicator |
| 2.4.11 Focus Not Obscured (Minimum) | AA | The focused element is not entirely hidden by sticky headers, banners or overlays |
| 2.4.13 Focus Appearance | AAA | Indicator at least as large as a 2 CSS px perimeter, with 3:1 between focused and unfocused states |

- **Large text** is 18pt (24 CSS px) regular or 14pt (about 18.66 CSS px) bold, at the rendered size.
- **Exempt:** logos and brand names in logos, purely decorative text, text in inactive (disabled) components, and incidental text in photos. Disabled controls still need to look disabled by more than color, and their text should stay legible (aim for 3:1).
- Contrast applies in every state: default, hover, focus, active, selected, error, visited, and in every theme.

## Opacity and overlays

Compute contrast on the composited color, not the token before opacity.

| Text | On | Composited | Ratio |
| --- | --- | --- | --- |
| Black at 87% | White | #212121 | 16.10:1 |
| Black at 60% | White | #666666 | 5.74:1 |
| Black at 54% | White | #757575 | 4.61:1 |
| Black at 38% (typical disabled) | White | #9E9E9E | 2.68:1 |
| White at 87% | #121212 | #E0E0E0 | 14.19:1 |
| White at 60% | #121212 | #A0A0A0 | 7.16:1 |
| White at 38% | #121212 | #6C6C6C | 3.57:1 |

**Text over photos:** test the lightest area under the text. White text over a white sky needs a black scrim of at least 60% (5.74:1); 50% gives only 3.95:1, enough for large text. Prefer a gradient scrim behind the text block, a solid caption bar, or a crop that puts text over a dark area. Video: test the brightest frame.

## Non-text contrast (3:1)

Needs 3:1 against adjacent colors:

- Input borders when the border is what identifies the field (use `--color-border-strong`, not `--color-border-default`).
- Checkbox, radio and toggle outlines and their checked states; slider tracks and thumbs.
- Icons that carry meaning without a text label.
- Focus indicators against the background and against the component.
- Chart lines, bars, points and the boundaries that separate adjacent segments (see the `data-visualization` skill).

Does not need it: decorative dividers, card outlines on cards that are also separated by space or fill, disabled controls, and components whose look is set by the browser and left unmodified.

## Focus indicators

```css
:where(a, button, input, select, textarea, [tabindex]):focus-visible {
  outline: 2px solid var(--color-focus-ring);
  outline-offset: 2px;
}
.on-varied-backgrounds:focus-visible {          /* double ring survives light and dark surfaces */
  outline: 2px solid transparent;               /* still shows in forced-colors mode */
  box-shadow: 0 0 0 2px var(--color-bg-canvas), 0 0 0 4px var(--color-focus-ring);
}
```

- 2px or thicker, 3:1 against what is next to it. Never `outline: none` without a replacement.
- `box-shadow` disappears in Windows forced-colors mode; keep a transparent `outline` so the system draws one.
- Sticky headers must not cover the focused element: use `scroll-padding-top` equal to the header height.

## High contrast and forced colors

- `@media (prefers-contrast: more)` applies the high-contrast token set: body text 7:1, borders darker, subtle tints removed.
- `@media (forced-colors: active)` hands colors to the system palette. Use system keywords (`CanvasText`, `Canvas`, `LinkText`, `Highlight`, `ButtonText`, `ButtonFace`) for custom controls and keep borders on elements that rely on background color alone.
- Test in Windows Contrast themes, or emulate both features in Chrome DevTools (Rendering panel).

## APCA (advisory)

APCA (Accessible Perceptual Contrast Algorithm) models perceived contrast from text size, weight and polarity. It was proposed for WCAG 3, which is still a working draft whose contrast method is not final as of 2026. Treat APCA as advisory; it never replaces a WCAG 2.2 result in a compliance claim.

- Output is Lc (lightness contrast), roughly 0-106 for dark text on light and 0 to about -108 for light text on dark. Compare absolute values; polarity matters because the same pair reversed scores differently.
- Commonly cited APCA "Bronze simple mode" levels:

| Lc | Use |
| --- | --- |
| 90 | Preferred for body text; columns of reading text |
| 75 | Minimum for body text (about 18px at 400, 16px at 500, 14px at 700) |
| 60 | Minimum for other content text people must read (about 24px at 400, 16px at 700), UI labels |
| 45 | Large and heavy text: headlines (about 36px at 400, 24px at 700), large icons |
| 30 | Minimum for any text: placeholders, disabled text, fine print that is not essential |
| 15 | Minimum for non-text that must be discernible: dividers, focus-adjacent outlines |

- Where APCA helps most: dark mode (WCAG 2 tends to overrate dark-on-black pairs and underrate some light-on-saturated pairs) and thin or small type.
- Compute it with `python3 ../../../library/scripts/color_tools.py apca '<text>' '<background>'` (text color first). Read the current guidance at the APCA project before relying on exact thresholds.

## Testing workflow

1. **Tokens:** run the token linter (`tokens.py lint`, see the `design-system` skill); it enforces the contract's guarantees in every mode and brand.
2. **Pairs outside tokens** (illustration, campaign art, charts): `python3 ../../../library/scripts/color_tools.py contrast '<fg>' '<bg>'`.
3. **Rendered UI:** Chrome DevTools color picker shows the ratio and AA/AAA lines; axe DevTools or Lighthouse flags failing text; Stark or a similar Figma plugin checks design files.
4. **States and themes:** check hover, focus, selected, error and disabled in light, dark and high contrast.
5. **Images and gradients:** sample the worst-case pixels under text.
6. **Vision simulation:** Chrome DevTools Rendering, "Emulate vision deficiencies" (protanopia, deuteranopia, tritanopia, achromatopsia, blurred vision). Simulation is an inspection aid, not proof.
7. **Record** the contrast matrix for handoff: foreground token, background token, ratio, target, pass.

## Contrast matrix template

| Foreground | Background | Ratio | Target | Pass |
| --- | --- | --- | --- | --- |
| `--color-fg-default` | `--color-bg-canvas` | | 4.5 (7 in high contrast) | |
| `--color-fg-muted` | `--color-bg-surface-raised` | | 4.5 | |
| `--color-fg-subtle` | `--color-bg-canvas` | | 3.0 | |
| `--color-fg-on-accent` | `--color-accent-active` | | 4.5 | |
| `--color-accent-fg` | `--color-accent-subtle` | | 4.5 | |
| `--color-danger-fg` | `--color-danger-bg` | | 4.5 | |
| `--color-border-strong` | `--color-bg-canvas` | | 3.0 | |
| `--color-focus-ring` | `--color-bg-canvas` | | 3.0 | |
