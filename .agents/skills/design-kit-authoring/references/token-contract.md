# Token contract

Version-Timestamp: 2026-10-20 01:42:00 UTC

Source of truth: `plugins/visual-design-studio/library/tokens/src/*.tokens.json` in W3C Design Tokens Community Group (DTCG) format (`$value`, `$type`, `$description`, aliases as `{group.token}`). Built outputs live in `library/tokens/dist/`. Every consumer (React reference system, stylescapes, examples, skills) uses the CSS custom property names below. Renaming a published name requires a deprecation alias for one minor version.

## Tiers

1. **Primitives** (`primitives.tokens.json`): raw ramps and scales. Never referenced directly by components.
2. **Semantic** (`semantic.light|dark|high-contrast.tokens.json`): roles that change per mode. Components use these.
3. **Component** (`components.tokens.json`): optional per-component overrides that alias semantic tokens.
4. **Brand overrides** (`brands/<brand>.tokens.json`): remap primitive accent/neutral/font references per brand.

## CSS output

- `:root` holds primitives and the light semantic set.
- `[data-theme="dark"]` and `[data-theme="high-contrast"]` override semantic values. `@media (prefers-color-scheme: dark)` applies dark when `data-theme` is not set to `light`. `@media (prefers-contrast: more)` applies high-contrast when no theme is forced.
- `[data-brand="<name>"]` overrides brand primitives.
- `@media (prefers-reduced-motion: reduce)` sets every `--duration-*` except `--duration-instant` to `0.01ms`.

## Semantic CSS variable names (stable API)

| Group | Variables |
| --- | --- |
| Background | `--color-bg-canvas`, `--color-bg-surface`, `--color-bg-surface-raised`, `--color-bg-sunken`, `--color-bg-inverse` |
| Foreground | `--color-fg-default`, `--color-fg-muted`, `--color-fg-subtle`, `--color-fg-inverse`, `--color-fg-on-accent` |
| Border | `--color-border-subtle`, `--color-border-default`, `--color-border-strong` |
| Accent | `--color-accent-default`, `--color-accent-hover`, `--color-accent-active`, `--color-accent-subtle`, `--color-accent-fg` |
| Status | `--color-{success,warning,danger,info}-{fg,bg,border}` |
| Other color | `--color-focus-ring`, `--color-overlay-scrim` |
| Font family | `--font-family-display`, `--font-family-body`, `--font-family-mono` |
| Font size | `--font-size-{xs,sm,md,lg,xl,2xl,3xl,4xl,5xl}` = 0.75, 0.875, 1, 1.25, 1.5, 1.875, 2.25, 3, 3.75 rem |
| Line height | `--line-height-{tight,snug,normal,relaxed}` = 1.1, 1.25, 1.5, 1.65 |
| Font weight | `--font-weight-{regular,medium,semibold,bold}` = 400, 500, 600, 700 |
| Letter spacing | `--letter-spacing-{tight,normal,wide,caps}` = -0.02em, 0, 0.01em, 0.06em |
| Measure | `--measure-{narrow,body,wide}` = 45ch, 66ch, 75ch |
| Space (4px base) | `--space-{0,1,2,3,4,5,6,8,10,12,16,20,24}` = n x 0.25rem |
| Size | `--size-target-min` 24px, `--size-target-comfortable` 44px, `--size-icon-{sm,md,lg}` 16, 20, 24px |
| Radius | `--radius-{none,sm,md,lg,xl,full}` = 0, 4, 8, 12, 16px, 9999px |
| Border width | `--border-width-{thin,thick}` = 1px, 2px |
| Elevation | `--shadow-{sm,md,lg,xl}` |
| Duration | `--duration-{instant,fast,moderate,slow,slower}` = 0ms, 120ms, 200ms, 320ms, 480ms |
| Easing | `--ease-standard` cubic-bezier(0.2, 0, 0, 1); `--ease-decelerate` cubic-bezier(0, 0, 0, 1); `--ease-accelerate` cubic-bezier(0.3, 0, 1, 1); `--ease-emphasized-decelerate` cubic-bezier(0.05, 0.7, 0.1, 1); `--ease-emphasized-accelerate` cubic-bezier(0.3, 0, 0.8, 0.15); `--ease-linear` linear |
| Z-index | `--z-{base,dropdown,sticky,overlay,modal,toast}` = 0, 1000, 1100, 1200, 1300, 1400 |
| Layout | `--container-{sm,md,lg,xl}` = 640, 768, 1024, 1280px; `--gutter` clamp(1rem, 4vw, 2rem) |

Breakpoints (JSON and Tailwind only, since CSS variables cannot drive media queries): sm 640, md 768, lg 1024, xl 1280, 2xl 1536 px.

## Default reference brands

- **Meridian** (default): deep teal accent, OKLCH hue about 195, cool neutral ramp. Chosen to avoid the generic indigo/purple default.
- **Ember** (`data-brand="ember"`): warm vermilion accent, OKLCH hue about 35, warm neutral ramp. Demonstrates multi-brand theming.

## Implementation details (0.5.0)

- Brand-level primitive groups `color.neutral`, `color.accent` and `font.family` are marked brandable and are the only groups a `brands/<name>.tokens.json` file may override. `[data-brand="meridian"]` is also emitted so nested scopes can switch back.
- Shadow sets live in primitives as `elevation.soft`, `elevation.firm` and `elevation.deep`; the semantic files map `shadow.sm|md|lg|xl` to them per mode, because dark mode uses borders and lighter surfaces more than shadows.
- Component tokens (`components.tokens.json`) alias semantic or public scale tokens only and are re-declared on `:root`, `[data-theme]` and `[data-brand]` so nested scopes resolve.
- Dark and high-contrast media queries apply only to `:root:not([data-theme])`, so an explicit `data-theme` always wins.
- Values a single page or brand needs beyond this contract use a `--brand-` prefix (for example `--brand-brass`) and never shadow contract names.
- `library/tokens/README.md` is the generated, user-facing API reference; keep it in sync when this contract changes.

## Contrast guarantees (enforced by `tokens.py lint`)

In every mode and brand: `fg-default`, `fg-muted` on `bg-canvas`, `bg-surface` and `bg-surface-raised` at 4.5:1 or more; `fg-subtle` 3:1 or more (decorative, non-essential text only; placeholders map to `fg-muted` at 4.5:1); `fg-on-accent` on `accent-default`, `accent-hover` and `accent-active` 4.5:1; `accent-fg` on `accent-subtle` 4.5:1; each status `fg` on its `bg` 4.5:1; `border-strong` and `focus-ring` on `bg-canvas` 3:1; each status `border` on `bg-canvas` and `bg-surface` 3:1 so it can mark an invalid input (WCAG 1.4.11). High-contrast mode raises body text to 7:1. The kit adds further pairs the components rely on; `tokens.py lint` reports all of them (336 pairs in 0.5.0).
