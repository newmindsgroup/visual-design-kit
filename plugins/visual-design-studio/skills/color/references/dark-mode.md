# Dark mode

Version-Timestamp: 2026-10-20 02:07:10 UTC

Dark mode is a second palette designed for low light, not an inversion. Surfaces get lighter as they rise, text is off-white, accents are lighter and calmer, and shadows give way to borders and lightness steps.

## Defaults

| Decision | Default | Change when |
| --- | --- | --- |
| Canvas | OKLCH L 0.15-0.20, tinted chroma 0.005-0.015 (Meridian: slate 950, L 0.165) | OLED media and video apps may use true black #000000 for the canvas only |
| Elevation | About +0.045 L per level above the canvas: canvas 950 (0.165), surface 900 (0.210), raised 850 (0.256); sunken 975 (0.143) sits below | Dense tools can compress to +0.02-0.03 |
| Primary text | L 0.92-0.95 (off-white), never pure #FFFFFF on large areas of text | High-contrast mode: pure white allowed |
| Secondary text | L 0.72-0.78 | |
| Accent | A light step (300 in the kit, L about 0.75) instead of the light-mode 600; avoid the most saturated midtones (400-500) for large fills | A fill still vibrates: lower its chroma 10-20% at the same L |
| Text on accent | Dark text (the canvas color) on the light accent | |
| Shadows | Replace with 1px borders (`--color-border-subtle`) plus a lighter surface; keep shadows only under overlays, darker and larger | |
| Images | Dim bright photos 5-15%, swap illustrations with light backgrounds, provide dark logo variants | |

## Worked example: the kit's Meridian dark set

Values from the shipped tokens (`semantic.dark.tokens.json` with Meridian's slate and teal); ratios are WCAG 2.2, computed.

| Token | Primitive | Hex | OKLCH |
| --- | --- | --- | --- |
| `--color-bg-sunken` | neutral 975 | #070A0D | 0.143 0.009 246 |
| `--color-bg-canvas` | neutral 950 | #0B0F12 | 0.165 0.009 241 |
| `--color-bg-surface` | neutral 900 | #14191D | 0.210 0.011 242 |
| `--color-bg-surface-raised` | neutral 850 | #1E2429 | 0.256 0.013 243 |
| `--color-bg-inverse` | neutral 100 | #E2E9EF | 0.930 0.011 244 |
| `--color-border-subtle` | neutral 800 | #282F35 | 0.301 0.015 244 |
| `--color-border-default` | neutral 700 | #3E464D | 0.390 0.016 245 |
| `--color-border-strong` | neutral 500 | #6F7982 | 0.571 0.018 245 |
| `--color-fg-default` | neutral 100 | #E2E9EF | 0.930 0.011 244 |
| `--color-fg-muted` | neutral 300 | #A6AFB8 | 0.750 0.016 248 |
| `--color-fg-subtle` | neutral 400 | #8A949D | 0.661 0.018 245 |
| `--color-fg-on-accent` | neutral 950 | #0B0F12 | 0.165 0.009 241 |
| `--color-accent-default` | accent 300 | #4FC2C2 | 0.749 0.103 195 |
| `--color-accent-hover` | accent 200 | #88DCDB | 0.841 0.082 195 |
| `--color-accent-active` | accent 100 | #C3F3F2 | 0.931 0.049 195 |
| `--color-accent-subtle` | accent 900 | #001D1D | 0.209 0.036 195 |
| `--color-accent-fg` | accent 300 | #4FC2C2 | 0.749 0.103 195 |
| `--color-focus-ring` | accent 300 | #4FC2C2 | 0.749 0.103 195 |

Pairs: fg-default on canvas 15.70:1 and on raised 12.79:1; fg-muted on canvas 8.66:1 and on raised 7.05:1; fg-subtle on raised 5.08:1; on-accent text on accent default, hover, active 9.01, 12.19, 15.97:1; accent-fg on accent-subtle 8.23:1; border-strong on canvas 4.34:1; focus ring on raised 7.34:1. Border-default on canvas is 2.01:1: fine for card edges, not for input outlines.

Why not reuse the light accent: teal 600 `#006C6C` on the dark canvas is only 3.08:1, so it fails as link text and looks muddy as a fill.

### Dark status colors

| Status | fg (300) | bg (900) | fg on bg |
| --- | --- | --- | --- |
| Success | #6DC582 | #001F09 | 8.30:1 |
| Warning | #DEA137 | #281200 | 7.87:1 |
| Danger | #FF8382 | #350206 | 7.59:1 |
| Info | #73B1FF | #021835 | 7.99:1 |

The dark status `border` tokens (700 steps) are about 2:1 on the canvas: decorative edges only. An invalid field's border uses `--color-danger-fg` so it clears 3:1.

## Off-black and off-white reference values

| Background | White text | #F2F2F2 text | #E8E8E8 text | Notes |
| --- | --- | --- | --- | --- |
| #000000 | 21.00:1 | 18.76:1 | 17.14:1 | Maximum glare and halation for some readers; OLED power savings |
| #09090B | 19.90:1 | 17.77:1 | 16.24:1 | Near-black, neutral |
| #121212 | 18.73:1 | 16.73:1 | 15.29:1 | Material Design's dark-theme baseline surface |
| #18181B | 17.72:1 | 15.83:1 | 14.46:1 | Common zinc near-black |
| #1C1C1E | 17.01:1 | 15.20:1 | 13.89:1 | Apple's secondary dark background (system gray 6) |
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
