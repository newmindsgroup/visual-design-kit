# Dark mode

Version-Timestamp: 2026-10-20 02:07:10 UTC

Dark mode is a second palette designed for low light, not an inversion. Surfaces get lighter as they rise, text is off-white, accents are lighter and calmer, and shadows give way to borders and lightness steps.

## Defaults

| Decision | Default | Change when |
| --- | --- | --- |
| Canvas | OKLCH L 0.18-0.20, tinted chroma 0.005-0.012 | OLED media and video apps may use true black #000000 for the canvas only |
| Elevation | +0.03 L per level: canvas 0.18, surface 0.21, raised 0.24, overlay 0.27 | Dense tools can compress to +0.02 |
| Primary text | L 0.93-0.95 (off-white), never pure #FFFFFF on large areas of text | High-contrast mode: pure white allowed |
| Secondary text | L 0.74-0.78 | |
| Accent | Raise L to 0.72-0.80, cut chroma 10-30% from the light-mode fill | Brand insists on its exact hue: keep the hue, adjust L and C |
| Text on accent | Dark text (canvas color) on the light accent | |
| Shadows | Replace with 1px borders (`--color-border-subtle`) plus a lighter surface; keep shadows only under overlays, darker and larger | |
| Images | Dim bright photos 5-15%, swap illustrations with light backgrounds, provide dark logo variants | |

## Worked dark token set (Meridian-style teal, hue 195)

All values computed; ratios are WCAG 2.2.

| Token | OKLCH | Hex |
| --- | --- | --- |
| `--color-bg-sunken` | 0.15 0.008 195 | #070C0C |
| `--color-bg-canvas` | 0.18 0.008 195 | #0E1313 |
| `--color-bg-surface` | 0.21 0.008 195 | #141919 |
| `--color-bg-surface-raised` | 0.24 0.008 195 | #1B2020 |
| `--color-bg-inverse` | 0.94 0.006 195 | #E7ECEC |
| `--color-border-subtle` | 0.30 0.008 195 | #292F2F |
| `--color-border-default` | 0.37 0.008 195 | #3B4141 |
| `--color-border-strong` | 0.54 0.008 195 | #6A7070 |
| `--color-fg-default` | 0.94 0.006 195 | #E7ECEC |
| `--color-fg-muted` | 0.76 0.006 195 | #ADB2B2 |
| `--color-fg-subtle` | 0.62 0.006 195 | #828787 |
| `--color-fg-on-accent` | 0.18 0.008 195 | #0E1313 |
| `--color-accent-default` | 0.75 0.11 195 | #43C3C3 |
| `--color-accent-hover` | 0.80 0.10 195 | #65D2D2 |
| `--color-accent-active` | 0.85 0.09 195 | #82E1E0 |
| `--color-accent-subtle` | 0.29 0.045 195 | #073232 |
| `--color-accent-fg` | 0.80 0.10 195 | #65D2D2 |
| `--color-focus-ring` | 0.78 0.11 195 | #4FCDCD |

Pairs: fg-default on canvas 15.70:1 and on raised 13.82:1; fg-muted on canvas 8.73:1 and on raised 7.68:1; fg-subtle on raised 4.52:1; on-accent text on accent default, hover, active 8.77, 10.44, 12.30:1; accent-fg on accent-subtle 7.74:1; border-strong on canvas 3.71:1; focus ring on raised 8.59:1. Border-default on canvas is 1.80:1, fine for decoration, not for input outlines.

Why not reuse the light accent: `#047879` on the dark canvas is only 3.54:1, so it fails as link text and looks muddy as a fill.

### Dark status colors

| Status | fg | bg | border | fg on bg | border on canvas |
| --- | --- | --- | --- | --- | --- |
| Success | #7CD591 (0.80 0.13 150) | #152D1A (0.27 0.045 150) | #579766 (0.62 0.10 150) | 8.29:1 | 5.37:1 |
| Warning | #EEB154 (0.80 0.13 75) | #33230A (0.27 0.045 75) | #A97D3A (0.62 0.10 75) | 7.98:1 | 5.07:1 |
| Danger | #FFA098 (0.80 0.15 25) | #3A1D1B (0.27 0.045 25) | #BB6D67 (0.62 0.10 25) | 7.83:1 | 4.90:1 |
| Info | #89C3FE (0.80 0.12 250) | #14283C (0.27 0.045 250) | #558AC0 (0.62 0.10 250) | 8.08:1 | 5.16:1 |

## Off-black and off-white reference values

| Background | White text | #F2F2F2 text | #E8E8E8 text | Notes |
| --- | --- | --- | --- | --- |
| #000000 | 21.00:1 | 18.76:1 | 17.14:1 | Maximum glare and halation for some readers; OLED power savings |
| #09090B | 19.90:1 | 17.77:1 | 16.24:1 | Near-black, neutral |
| #121212 | 18.73:1 | 16.73:1 | 15.29:1 | Material Design's dark-theme baseline surface |
| #18181B | 17.72:1 | 15.83:1 | 14.46:1 | Common zinc near-black |
| #1C1C1E | 17.01:1 | 15.20:1 | 13.89:1 | Apple's elevated dark background (system gray 6) |
| #2C2C2E | 13.94:1 | 12.45:1 | 11.37:1 | Apple's tertiary dark background |

Pure white on pure black can cause halation (a glow around letters), especially for readers with astigmatism; off-white on off-black reads calmer while still exceeding 15:1.

## Rules

- **Elevation by lightness:** higher surfaces are lighter. Shadows are barely visible on dark backgrounds; keep `--shadow-lg` and `--shadow-xl` for menus and dialogs (darker, larger blur) and rely on lightness plus a subtle border for cards.
- **Desaturate:** saturated colors vibrate on dark backgrounds. Lower chroma 10-30% and raise lightness; keep hue.
- **Weight:** light text on dark looks bolder. Use weight 400 for body (not 300), reduce variable weight 20-50 units or use a grade axis, and consider `-webkit-font-smoothing: antialiased` on macOS (see the `typography` skill).
- **Borders over fills:** use `--color-border-subtle` to separate regions instead of many surface shades.
- **Selected and hover:** lighten (step up in L) rather than darken.
- **Charts:** use a dark-tuned data palette (lighter, slightly lower chroma); see the `data-visualization` skill.
- **Never just invert:** inverted photos, inverted brand colors and pure white text on pure black are the common failures.

## Images, illustration and brand assets

- **Photos:** keep them; dim very bright images with `filter: brightness(0.9)` or a 5-15% scrim when they sit beside text.
- **Illustrations:** provide dark variants, or place light illustrations on a contained light card. Swap white backgrounds in PNGs for transparent ones.
- **Logos:** ship a reversed (light) version; never apply CSS `invert()` to a logo.
- **Icons:** SVG with `currentColor` adapts automatically; check two-tone icons.
- **Screenshots of light UI:** frame them in a device or a neutral card so they do not glare.
- **Code blocks and embeds:** use a dark syntax theme and dark third-party embed modes (maps, video players).

```css
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) img:not([data-keep-bright]) { filter: brightness(0.92); }
}
[data-theme="dark"] img:not([data-keep-bright]) { filter: brightness(0.92); }
```

```html
<picture>
  <source srcset="/img/hero-dark.avif" media="(prefers-color-scheme: dark)">
  <img src="/img/hero-light.avif" alt="..." width="1600" height="900">
</picture>
```

## Theming mechanics

- The token contract applies dark values under `[data-theme="dark"]` and under `@media (prefers-color-scheme: dark)` when no theme is forced to light. Components use semantic tokens only, so they switch automatically.
- Set `color-scheme: light dark;` on `:root` so form controls and scrollbars follow the theme.
- Provide a user toggle (light, dark, system) and persist it; default to system.
- Email: Apple Mail and some clients apply their own dark mode; test logos and dark text on transparent images. Use `@media (prefers-color-scheme: dark)` where supported and transparent PNGs with a light outline for dark-on-transparent logos.

## Testing dark mode

1. Render every key screen in dark mode at real brightness, ideally on a phone at night brightness and on an OLED screen.
2. Run the contrast matrix for the dark set (see [contrast](contrast.md)); token lint covers token pairs.
3. Check APCA for body and thin text: dark mode is where WCAG 2 and perception diverge most.
4. Check elevation: can you tell canvas, surface, raised and overlay apart in a grayscale screenshot?
5. Check images, logos, illustrations, embeds, charts, focus rings and selection states.
6. Check the transition: no white flash on load (set the theme before first paint).
