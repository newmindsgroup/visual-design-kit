# Theming: modes, brands, density and platform outputs

Version-Timestamp: 2026-10-20 02:08:24 UTC

A theme is a set of values for the same semantic token names. Components never know which theme is active. The kit's themes are light, dark and high contrast, crossed with brands (Meridian default, Ember), built from `library/tokens/src/` by `library/scripts/tokens.py`.

## Defaults

| Axis | Default | Change when |
| --- | --- | --- |
| Modes | Light, dark, high contrast; follow the OS unless the user chooses | Kiosk or signage with fixed lighting: one mode tuned to the environment |
| Selection | `prefers-color-scheme` and `prefers-contrast` first; `data-theme` attribute for a user override stored per device | Product has accounts: store the override in the profile too |
| Brand | `data-brand` on `html` (or a subtree for co-branded areas) | White-label products: set at build time per tenant to avoid shipping every brand |
| Density | Comfortable; compact as an opt-in for data-heavy views | Touch-first products: comfortable only |
| Reduced motion | Durations collapse to 0.01ms except instant (contract rule) | Keep essential progress indicators but stop decorative motion |

## CSS output pattern (from the token contract)

```css
:root { /* primitives + light semantic set */ color-scheme: light dark; }
[data-theme="dark"] { /* dark semantic overrides */ }
[data-theme="high-contrast"] { /* high-contrast overrides */ }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { /* dark */ } }
@media (prefers-contrast: more) { :root:not([data-theme]) { /* high contrast */ } }
[data-brand="ember"] { /* brand primitive remaps */ }
@media (prefers-reduced-motion: reduce) { :root { /* --duration-* except instant = 0.01ms */ } }
```

- Set `color-scheme` so native form controls and scrollbars match.
- Apply the stored override before first paint (a tiny inline script that sets `data-theme` from storage) to avoid a flash of the wrong theme; wrap storage access in try/catch.
- Windows forced-colors mode (`@media (forced-colors: active)`) replaces your palette. Use real borders and outlines (not background-only states), keep focus as an outline, and use system color keywords (`CanvasText`, `Highlight`) for custom-drawn parts.

## Dark mode craft

Dark mode is a second design, not an inversion.

- **Surfaces**: raise lightness as elevation rises (canvas darkest, raised surfaces lighter) instead of relying on shadows, which barely read on dark backgrounds. A common starting point: canvas OKLCH L 0.16-0.20, surface 0.20-0.24, raised 0.24-0.28, with a slight hue tint from the neutral ramp.
- **Text**: default text around L 0.92-0.95, not pure white; muted text still at 4.5:1.
- **Accent**: raise lightness and lower chroma slightly versus light mode so it does not vibrate; re-check `fg-on-accent` contrast (often flips from white text to dark text).
- **Status colors**: re-tune each; saturated red on near-black is hard to read.
- **Images and illustration**: dim large bright images slightly or provide dark variants; never invert photos; logos need a dark-background version.
- **Pure black**: reserve `#000` for an optional true-black OLED theme or media viewers.

## High contrast

- Body text 7:1 (contract lint), all text at least 4.5:1, UI boundaries 3:1 against both neighbors.
- Every interactive element gets a visible border; selected and hover states change more than a subtle fill (add border weight, underline or an icon).
- Focus ring 2-3px with a contrasting offset, never removed.
- Remove translucency, glass and low-opacity overlays; increase scrim opacity.
- Test with OS high-contrast settings (macOS and iOS Increase Contrast, Android contrast levels, Windows contrast themes).

## Brand theming

| A brand may change | A brand must not change |
| --- | --- |
| Accent ramp and accent role values | Semantic token names and structure |
| Neutral ramp temperature (cool, warm) | Spacing scale and layout breakpoints |
| Display and body font families | Minimum target sizes and minimum text sizes |
| Radius character (via primitives) if the system allows it | Contrast guarantees |
| Illustration, imagery and motion personality in content | Component behavior, keyboard and ARIA contracts |

- Co-branding: scope `data-brand` to a subtree (partner page, embedded widget) and keep the host's chrome.
- Generate each brand's ramps in OKLCH so steps are perceptually even; check the 500-700 steps carry text contrast. The `color` skill covers ramp construction.
- Name brands by brand, not by color (`ember`, not `orange`).

## Density

- Density changes spacing and component heights, not type below minimums or targets below 24x24 CSS px (44px for touch).
- Implement as component-tier tokens switched by `[data-density="compact"]`: for example control height 32 / 40 / 48px and table row height 32 / 40 / 52px for compact / comfortable / spacious, and section spacing scaled about 0.75x / 1x / 1.25x. These density tokens are not in the current token contract; propose them through governance before shipping.
- Offer compact only where people scan many rows (tables, inboxes, admin); keep forms comfortable.

## Platform outputs

| Target | Output | Notes |
| --- | --- | --- |
| Web (CSS) | `dist/tokens.css` custom properties | Runtime theming via attributes; no JS theme provider needed |
| Tailwind 4 | `dist/tailwind.css` (`@theme` mapping) | Utilities read the same variables; breakpoints live here (CSS variables cannot drive media queries) |
| Any tool | `dist/tokens.resolved.json` | Every alias resolved per mode and brand; feed native generators from this |
| Figma | `dist/figma-variables.json` | Import into variable collections with modes; see [Figma](figma.md) |
| iOS | Asset catalog color sets (Any, Dark, High Contrast) plus a Swift constants file | Generated; see the `native-app-design` skill's SwiftUI and Compose handoff |
| Android | Compose `ColorScheme`, `Typography`, `Shapes` plus extended tokens | Generated; dynamic color is an option, not a replacement |
| Email | Inlined hex values, light theme plus a limited dark-mode block | Many clients ignore custom properties |
| Print | Separate CMYK and spot conversions | Screen tokens do not convert reliably; see the `print-packaging-social` skill |

## Testing matrix

Render a fixed set of reference screens (a form, a table, a dialog, a marketing section, an error state) in every mode x brand combination, plus compact density where offered. Run `tokens.py lint` in CI; review screenshots by eye for contrast that passes numerically but looks wrong (vibrating accents, muddy dark surfaces, unreadable status chips).
