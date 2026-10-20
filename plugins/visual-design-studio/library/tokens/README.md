# Design tokens

Version-Timestamp: 2026-10-20 02:32:45 UTC

The kit's reference token system: W3C Design Tokens Community Group (DTCG) JSON in `src/`, built into CSS custom properties, a Tailwind CSS v4 theme, resolved JSON and Figma variables in `dist/`. Names follow the token contract (`.claude/skills/design-kit-authoring/references/token-contract.md` in the source repository); `scripts/tokens.py` encodes it and fails lint on any missing or renamed name. Two reference brands ship: **Meridian** (default, deep teal on cool slate) and **Ember** (`data-brand="ember"`, warm vermilion on sand).

Open [specimen.html](specimen.html) to see every role, scale and component in each brand and mode.

## Files

| Path | What it is |
| --- | --- |
| `src/primitives.tokens.json` | Raw OKLCH ramps (slate, sand, teal, vermilion, green, amber, red, blue), alpha blacks, font stacks, type sizes, line heights, weights, letter spacing, measure, space, sizes, radius, border widths, shadow sets (`elevation.soft|firm|deep`), durations, easings, z-index, containers, gutter, breakpoints. Brand-level groups `color.neutral`, `color.accent` and `font.family` are marked `brandable`. |
| `src/semantic.light.tokens.json` | Default mode. Every semantic color role plus `shadow.*` (aliasing `elevation.soft`), all aliasing primitives. |
| `src/semantic.dark.tokens.json` | Dark mode, designed rather than inverted (see below). |
| `src/semantic.high-contrast.tokens.json` | Light-based high contrast: body and secondary text at 7:1 or more. |
| `src/components.tokens.json` | Button, input, card, dialog, badge, table and focus tokens. Alias semantic roles or public scale tokens only. |
| `src/brands/ember.tokens.json` | Ember: remaps `color.accent.*` to vermilion, `color.neutral.*` to sand, fonts to Fraunces / Figtree / IBM Plex Mono. |
| `dist/tokens.css` | The CSS API. Import it everywhere. |
| `dist/tailwind.css` | Tailwind v4 `@theme inline reference` mapping to short utility names. |
| `dist/tokens.resolved.json` | Every token fully resolved for each brand x mode (for native apps, charts, email, tests). |
| `dist/figma-variables.json` | Collections `Primitives` (modes Meridian, Ember) and `Semantic` (modes Light, Dark, High contrast) with alias references. |
| `figma-import.js` | Plugin API script that imports `figma-variables.json` through the Figma MCP `use_figma` tool. |
| `specimen.html` | Visual specimen with a brand and mode switcher. |

Never edit `dist/` by hand. Scripts live in `../scripts/` (standard library Python 3.9+).

## Build, lint, check

Run from `plugins/visual-design-studio/library/`:

```sh
python3 scripts/tokens.py build    # write the four dist/ files (byte-for-byte deterministic)
python3 scripts/tokens.py lint     # structure, aliases, contract names and values, tiers, ramps, contrast
python3 scripts/tokens.py check    # exit 1 if dist/ is missing or stale (use in CI)
python3 scripts/tokens.py ramps --write   # regenerate ramp hex values from their OKLCH recipes
python3 -m unittest discover -s tests     # includes test_tokens, test_color_tools, test_type_scale
```

`lint` reports one line per problem with a category: `[structure]`, `[alias]` (unresolved or circular), `[contract]` (missing, renamed or changed names and values), `[tier]`, `[brand]`, `[ramp]`, `[contrast]` (theme, pair, both hex values, ratio and required minimum).

## How the CSS cascades

```text
:root                                  primitives (raw ramps, scales) + brand-level aliases
:root, [data-theme="light"]            light semantic roles (var() references into primitives)
[data-theme="dark"] / ["high-contrast"]  semantic overrides
@media (prefers-color-scheme: dark)    :root:not([data-theme]) gets dark
@media (prefers-contrast: more)        :root:not([data-theme]) gets high contrast (wins over system dark)
[data-brand="meridian" | "ember"]      brand-level primitives only (accent, neutral, font families)
:root, [data-theme], [data-brand]      component tokens, re-declared so nested scopes resolve correctly
@media (prefers-reduced-motion)        every --duration-* except instant becomes 0.01ms
```

- Put `data-theme` and `data-brand` on `<html>`. For a nested preview (a card showing Ember dark inside a Meridian page), set **both** attributes on the wrapper: semantic roles are recomputed only where `data-theme` is set.
- `data-theme="light"` opts out of system dark; omit the attribute to follow the OS.
- High contrast is light-based. A user with OS dark mode plus "increase contrast" gets the light high-contrast theme; add a dark high-contrast mode if your audience needs it (see "Add a mode").

## CSS variable API

| Group | Variables |
| --- | --- |
| Background | `--color-bg-canvas`, `--color-bg-surface`, `--color-bg-surface-raised`, `--color-bg-sunken`, `--color-bg-inverse` |
| Foreground | `--color-fg-default`, `--color-fg-muted`, `--color-fg-subtle`, `--color-fg-inverse`, `--color-fg-on-accent` |
| Border | `--color-border-subtle`, `--color-border-default`, `--color-border-strong` |
| Accent | `--color-accent-default`, `--color-accent-hover`, `--color-accent-active`, `--color-accent-subtle`, `--color-accent-fg` |
| Status | `--color-{success,warning,danger,info}-{fg,bg,border}` |
| Other color | `--color-focus-ring`, `--color-overlay-scrim` |
| Font family | `--font-family-display`, `--font-family-body`, `--font-family-mono` |
| Font size | `--font-size-{xs,sm,md,lg,xl,2xl,3xl,4xl,5xl}` = 0.75, 0.875, 1, 1.25, 1.5, 1.875, 2.25, 3, 3.75rem |
| Line height | `--line-height-{tight,snug,normal,relaxed}` = 1.1, 1.25, 1.5, 1.65 |
| Weight | `--font-weight-{regular,medium,semibold,bold}` = 400, 500, 600, 700 |
| Letter spacing | `--letter-spacing-{tight,normal,wide,caps}` = -0.02em, 0, 0.01em, 0.06em |
| Measure | `--measure-{narrow,body,wide}` = 45ch, 66ch, 75ch |
| Space | `--space-{0,1,2,3,4,5,6,8,10,12,16,20,24}` = n x 0.25rem |
| Size | `--size-target-min` 24px, `--size-target-comfortable` 44px, `--size-icon-{sm,md,lg}` 16, 20, 24px |
| Radius | `--radius-{none,sm,md,lg,xl,full}` = 0, 4, 8, 12, 16, 9999px |
| Border width | `--border-width-{thin,thick}` = 1px, 2px |
| Elevation | `--shadow-{sm,md,lg,xl}`: soft set in light, deep in dark, firm in high contrast |
| Duration | `--duration-{instant,fast,moderate,slow,slower}` = 0, 120, 200, 320, 480ms |
| Easing | `--ease-{standard,decelerate,accelerate,emphasized-decelerate,emphasized-accelerate,linear}` |
| Z-index | `--z-{base,dropdown,sticky,overlay,modal,toast}` = 0, 1000 ... 1400 |
| Layout | `--container-{sm,md,lg,xl}` = 640, 768, 1024, 1280px; `--gutter` clamp(1rem, 4vw, 2rem) |
| Components | `--button-*`, `--input-*`, `--card-*`, `--dialog-*`, `--badge-*`, `--table-*`, `--focus-ring-{color,width,offset}` |

Ramps (`--color-teal-600`, `--color-neutral-850` ...) are emitted so brands can remap them, but they are private: use semantic roles in product code. Breakpoints (640, 768, 1024, 1280, 1536px) exist only in JSON and Tailwind.

## Resolved role values

| Theme | canvas | surface / raised | fg default / muted | accent default / hover / active | accent fg | on accent |
| --- | --- | --- | --- | --- | --- | --- |
| Meridian light | #f2f7fc | #ffffff / #ffffff | #14191d / #565f67 | #006c6c / #005050 / #003636 | #005050 | #ffffff |
| Meridian dark | #0b0f12 | #14191d / #1e2429 | #e2e9ef / #a6afb8 | #4fc2c2 / #88dcdb / #c3f3f2 | #4fc2c2 | #0b0f12 |
| Meridian high contrast | #ffffff | #ffffff / #ffffff | #070a0d / #3e464d | #003636 / #001d1d / #071010 | #003636 | #ffffff |
| Ember light | #faf6f2 | #ffffff / #ffffff | #1b1813 / #645c54 | #a72800 / #7e1c00 / #571000 | #7e1c00 | #ffffff |
| Ember dark | #100e0b | #1b1813 / #27221d | #ece7e1 / #b4ada4 | #ff8769 / #ffb6a3 / #ffe0d8 | #ff8769 | #100e0b |
| Ember high contrast | #ffffff | #ffffff / #ffffff | #0c0907 / #4a443d | #571000 / #320600 / #170b08 | #571000 | #ffffff |

Dark mode is not an inversion: the canvas is a tinted near-black (`neutral.950`, OKLCH L 0.165, never #000), surfaces get lighter as they rise (900, then 850) so elevation reads without shadows, text is off-white (`neutral.100`), and accents move to step 300, which is lighter and lower in saturation (C/L) than the light-mode step 600, with dark text on them.

## Color system

`color_tools.py ramp` generates every ramp. OKLab lightness is linear in the step number, `L = 1.02 - 0.0009 x step` (50 = 0.975, 500 = 0.57, 950 = 0.165), so a step has the same lightness in every hue and swapping a brand's hue keeps contrast close. Chroma follows a sine taper peaking at 500 and falls to 12% of peak at 50 and 950 (45% for neutrals); colors outside sRGB are mapped by reducing chroma at constant L and H. Each ramp group stores its recipe in `$extensions["com.github.newmindsgroup.vdk"].ramp` and each token its `oklch`; lint fails if a hex no longer matches its recipe.

| Ramp | Hue | Peak C | Use |
| --- | --- | --- | --- |
| slate | 245 | 0.018 | Meridian neutral (extra steps 850, 975) |
| sand | 70 | 0.016 | Ember neutral (extra steps 850, 975) |
| teal | 195 | 0.12 | Meridian accent; sRGB caps teal chroma below step 400 |
| vermilion | 35 | 0.19 | Ember accent |
| green / amber / red / blue | 150 / 72 (rotating 84 to 60) / 22 / 255 | 0.15 / 0.16 / 0.2 / 0.16 | success / warning / danger / info |

Ember's vermilion sits 13 degrees from danger red. Danger UI must always carry an icon and text, never color alone.

```sh
python3 scripts/color_tools.py convert "#a72800" "oklch(0.62 0.12 195)"
python3 scripts/color_tools.py ramp --hue 150 --chroma 0.14 --name pine --format css
python3 scripts/color_tools.py contrast "#565f67" "#f2f7fc"     # WCAG 2.x ratio, AA/AAA verdicts
python3 scripts/color_tools.py apca "#565f67" "#f2f7fc"         # APCA-W3 0.1.9 Lc (advisory)
python3 scripts/color_tools.py check-palette palette.json       # ramps monotonic, pairs pass
python3 scripts/type_scale.py --fluid --min-vw 360 --max-vw 1440 --min-base 16 --max-base 18 \
  --min-ratio 1.2 --max-ratio 1.333 --format css                 # clamp() with the math in comments
```

## Tailwind CSS v4

```css
@import "tailwindcss";
@import "../tokens/dist/tokens.css";
@import "../tokens/dist/tailwind.css";
```

`tailwind.css` uses `@theme inline reference`: utilities compile straight to the token variables (so `data-theme` and `data-brand` switch them at runtime) and Tailwind emits no duplicate variables. It resets Tailwind's default palette, type scale, leading, tracking, weights, radii, shadows, easings, containers and breakpoints, so `bg-purple-500` or `text-7xl` do not compile. It also redefines `dark:` to follow `data-theme="dark"` or the system setting, and adds `hc:` for high contrast. Verified with Tailwind CSS 4.1.

| Utility | Token |
| --- | --- |
| `bg-canvas`, `bg-surface`, `bg-surface-raised`, `bg-sunken`, `bg-inverse` | `--color-bg-*` |
| `bg-accent`, `bg-accent-hover`, `bg-accent-active`, `bg-accent-subtle` | `--color-accent-{default,hover,active,subtle}` |
| `bg-success`, `bg-warning`, `bg-danger`, `bg-info`, `bg-scrim` | `--color-*-bg`, `--color-overlay-scrim` |
| `text-default`, `text-muted`, `text-subtle`, `text-inverse`, `text-on-accent` | `--color-fg-*` |
| `text-accent`, `text-success`, `text-warning`, `text-danger`, `text-info` | `--color-accent-fg`, `--color-*-fg` |
| `border-subtle`, `border-default`, `border-strong`, `border-accent`, `border-focus`, `border-success` ... (also `divide-*`) | `--color-border-*`, `--color-accent-default`, `--color-focus-ring`, `--color-*-border` |
| `ring-focus`, `ring-accent`, `outline-focus` | `--color-focus-ring`, `--color-accent-default` |
| `fill-accent`, `stroke-danger`, `caret-accent`, `accent-accent` ... | `--color-accent-default`, `--color-*-fg` |
| `font-display`, `font-body`, `font-mono` (`font-sans` = body) | `--font-family-*` |
| `text-xs` ... `text-5xl`, `text-md` (= `text-base`) with matching leading | `--font-size-*`, `--line-height-*` |
| `leading-{tight,snug,normal,relaxed}`, `tracking-{tight,normal,wide,caps}` | `--line-height-*`, `--letter-spacing-*` |
| `font-regular` (= `font-normal`), `font-medium`, `font-semibold`, `font-bold` | `--font-weight-*` |
| `p-4`, `gap-6`, `mt-12`, `w-64` ... (n x `--space-1`) | `--space-*` |
| `rounded-sm` ... `rounded-xl` (`rounded-none`, `rounded-full` built in) | `--radius-*` |
| `shadow-sm` ... `shadow-xl` | `--shadow-*` (mode-aware) |
| `ease-standard`, `ease-decelerate`, `ease-accelerate`, `ease-emphasized-decelerate`, `ease-emphasized-accelerate`, `ease-linear` | `--ease-*` |
| `duration-instant`, `duration-fast`, `duration-moderate`, `duration-slow`, `duration-slower` | `--duration-*` |
| `z-base`, `z-dropdown`, `z-sticky`, `z-overlay`, `z-modal`, `z-toast` | `--z-*` |
| `max-w-sm` ... `max-w-xl`, `@sm:` ... `@xl:`; `sm:` ... `2xl:` | containers 640-1280px; breakpoints 40-96rem |

Note: `max-w-md` is 768px here (Tailwind's default is 28rem). Use `max-w-(--measure-body)` for text columns.

## Add a brand

1. Generate ramps: `python3 scripts/color_tools.py ramp --hue <H> --chroma <C> --name <name> --format json`. Add the group to `color` in `primitives.tokens.json` with the recipe under `$extensions["com.github.newmindsgroup.vdk"].ramp`, then run `tokens.py ramps --write` to fill the steps. Neutral ramps need steps 50-950 plus 850 and 975.
2. Add any font stacks under `font.stack` (OFL or licensed for the client; ship the license with self-hosted files).
3. Create `src/brands/<brand>.tokens.json` that remaps only brandable tokens: `color.accent.<step>` to `{color.<ramp>.<step>}`, `color.neutral.<step>`, `font.family.{display,body,mono}`. Give the file `$extensions["com.github.newmindsgroup.vdk"].name`.
4. `tokens.py build && tokens.py lint`. Lint checks every contrast guarantee for the new brand in every mode. Accents whose step 600 is too light for white text (yellow, lime, cyan, bright orange) fail here: pick a lower chroma, shift the hue, or make `fg-on-accent` dark for that brand by adding a brandable on-accent primitive.
5. Apply with `<html data-brand="<brand>">`. Figma gets a new mode in `Primitives`.

## Add a mode

1. Copy `semantic.light.tokens.json` to `semantic.<mode>.tokens.json` (lowercase, hyphenated), set `$extensions[...].name` and `colorScheme`, and remap every role. Lint fails on any missing role.
2. Build: the mode is emitted as `[data-theme="<mode>"]` and as a Figma `Semantic` mode (Professional plans allow 4 modes per collection; verify your plan).
3. To follow a system setting (for example dark high contrast), add the media block in `build_css` in `scripts/tokens.py` and a guarantee override in `GUARANTEES`, then add the mode to the specimen's `THEMES`.

## Figma variables

`dist/figma-variables.json` holds two collections. `Primitives` has modes Meridian and Ember (raw ramps hidden from pickers and publishing; brand-level `font/family/*`, `space/*`, `radius/*`, `font/size/*` and others scoped to the right fields). `Semantic` has modes Light, Dark and High contrast and aliases Primitives. Values: COLOR as 0-1 RGBA, FLOAT in px (rem x 16), STRING for the first family name, TIMING in seconds, EASING as cubic-bezier objects. Each variable carries `codeSyntax.WEB` (`var(--color-bg-canvas)`). Line height, letter spacing, measure, gutter, z-index, breakpoints, shadows and elevation sets are listed in `notExported` with the reason; build shadows as effect styles from `tokens.resolved.json`.

To import with the Figma MCP server:

1. Load the `figma-use` skill (required before any `use_figma` call) and open or create a design file.
2. `python3 scripts/tokens.py figma-script > /tmp/vdk-figma.js` prints `const DATA = ...;` plus `figma-import.js`.
3. Pass the file's contents as the `use_figma` code. The script is idempotent: it matches collections, modes and variables by name, creates what is missing, updates values in place and returns `{collections, created, updated, skipped}`.
4. Switch brand by setting the Primitives mode on a frame and theme by setting the Semantic mode.

## Consume elsewhere

- **React / Next.js:** import `tokens.css` once in the root layout; set `data-theme` on `<html>` from a cookie or localStorage before paint to avoid a flash. Style with `var(--...)` or the Tailwind utilities; never import hex values into components.
- **Astro:** import `tokens.css` in the base layout frontmatter (`import "../tokens/dist/tokens.css"`); put the theme script inline in `<head>`. Works with the Tailwind setup above (see `library/examples/astro-motion/`).
- **SwiftUI:** generate an asset catalog or a `Color` extension from `tokens.resolved.json` (`values.meridian.light` and `values.meridian.dark` become the Any/Dark appearances; high contrast maps to the "High Contrast" appearance variants). Convert rem to points 1:1 with a 16pt base and use Dynamic Type styles rather than fixed sizes for text.
- **Jetpack Compose:** generate a `ColorScheme` per mode from `tokens.resolved.json` (`bg.canvas` to `background`, `bg.surface` to `surface`, `accent.default` to `primary`, `fg.on-accent` to `onPrimary`) and a `Typography` from the font-size tokens in sp. Keep the semantic names in a `CompositionLocal` for roles Material does not cover.

## What the contrast lint guarantees

Checked with the WCAG 2.x formula in every brand x mode (Meridian and Ember x light, dark, high contrast):

- `fg-default` and `fg-muted` on `bg-canvas`, `bg-surface`, `bg-surface-raised`: 4.5:1; 7:1 in high contrast.
- `fg-subtle` on the same three: 3:1. Use it for placeholders and non-essential text only.
- `fg-on-accent` on `accent-default`, `accent-hover`, `accent-active`: 4.5:1. `accent-fg` on `accent-subtle`: 4.5:1.
- Each status `fg` on its `bg`: 4.5:1. `border-strong` and `focus-ring` on `bg-canvas`: 3:1.
- Kit additions: `accent-fg` and status `fg` on canvas and surface 4.5:1 (links and inline status text); `fg-inverse` on `bg-inverse` 4.5:1; `fg-default` and `fg-muted` on `bg-sunken` 4.5:1; `border-strong` and `focus-ring` on surfaces 3:1.
- Component rules declared in `components.tokens.json` (`$extensions...contrast`), such as table text on selected rows and badge text on badge backgrounds.

Not guaranteed: translucent colors (the scrim, shadows), text over images or gradients, colors you add outside the tokens, and APCA levels (`color_tools.py apca` is advisory; WCAG 2.2 conformance uses the 2.x ratio). Windows forced-colors mode replaces these colors with system colors; test it separately.
