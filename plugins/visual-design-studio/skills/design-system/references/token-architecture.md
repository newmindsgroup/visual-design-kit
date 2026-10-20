# Token architecture (DTCG)

Version-Timestamp: 2026-10-20 02:08:24 UTC

Design tokens are named design decisions stored once and compiled to every platform. The kit's source of truth is `library/tokens/src/*.tokens.json` in W3C Design Tokens Community Group (DTCG) format; [the tokens README](../../../library/tokens/README.md) documents the files, and [tokens.py](../../../library/scripts/tokens.py) builds, lints and checks them. Names and tiers are fixed by the kit's token contract (`.claude/skills/design-kit-authoring/references/token-contract.md` in the repository).

## The format (DTCG 2025.10)

The DTCG published its first stable specification, version 2025.10, on 28 October 2025 (W3C Community Group report; not a W3C Recommendation). Style Dictionary, Tokens Studio, Terrazzo and Figma have announced support. Core rules:

- A **token** is an object with `$value`. Optional: `$type`, `$description`, `$extensions` (vendor data, namespaced like `com.figma`), `$deprecated` (true or a message).
- A **group** is any object without `$value`. A group's `$type` is inherited by its tokens. Names must not start with `$` or contain `{`, `}` or `.`.
- An **alias** is a string reference in curly braces: `"$value": "{color.teal.600}"`. Aliases resolve through chains; cycles are errors.
- **Types**: `color`, `dimension`, `fontFamily`, `fontWeight`, `duration`, `cubicBezier`, `number`, plus composites `strokeStyle`, `border`, `transition`, `shadow`, `gradient`, `typography`.
- **Color** values are objects with a color space: `{"colorSpace": "oklch", "components": [0.52, 0.09, 195], "alpha": 1, "hex": "#..."}`. The spec covers sRGB, Display P3, OKLCH, OKLab and other CSS Color 4 spaces; add `hex` as a fallback for tools that need it.
- **Dimension** values: `{"value": 16, "unit": "px"}` (`px` or `rem`). **Duration**: `{"value": 200, "unit": "ms"}`.
- Group inheritance (`$extends`), JSON Pointer references and the separate Resolver module for themes and modes are part of the 2025.10 release set; verify their exact syntax at designtokens.org before relying on them in a build.
- File extension `.tokens.json` (or `.tokens`).

Illustrative excerpt (values are examples; the real ones live in `src/`):

```json
{
  "color": {
    "$type": "color",
    "teal": {
      "600": { "$value": { "colorSpace": "oklch", "components": [0.52, 0.09, 195], "alpha": 1 } }
    },
    "accent": {
      "default": { "$value": "{color.teal.600}", "$description": "Primary action background" }
    }
  },
  "space": {
    "$type": "dimension",
    "4": { "$value": { "value": 1, "unit": "rem" } }
  },
  "duration": {
    "$type": "duration",
    "moderate": { "$value": { "value": 200, "unit": "ms" } }
  }
}
```

## Tiers

| Tier | File(s) | Contains | Referenced by | Rule |
| --- | --- | --- | --- | --- |
| Primitives | `primitives.tokens.json` | Raw ramps and scales: `color.teal.50-950`, `color.neutral.*`, spacing steps, radii, durations | Semantic tokens and brand overrides only | Named by value or position, never by use |
| Semantic | `semantic.light.tokens.json`, `semantic.dark.tokens.json`, `semantic.high-contrast.tokens.json` | Roles: `color.bg.canvas`, `color.fg.muted`, `color.accent.hover`, `color.danger.bg` | Components and product code | Same names in every mode; only values change |
| Component | `components.tokens.json` | Optional overrides: `button.primary.bg`, `input.border.focus` | That component only | Alias semantic tokens; never primitives |
| Brand overrides | `brands/<brand>.tokens.json` | Remapped accent and neutral ramps, font families | Primitive layer | Never rename or add semantic roles |

Product code and component styles use semantic (or component) tokens. A primitive in a component file is a lint error, not a shortcut.

## Naming conventions

- Pattern: `category.concept.property.variant.state`, dropping levels you do not need: `color.bg.surface-raised`, `color.accent.hover`, `font.size.lg`, `space.4`, `radius.md`, `shadow.lg`, `duration.fast`.
- CSS output joins with hyphens and keeps the contract names: `--color-bg-surface-raised`, `--space-4`, `--radius-md`.
- Semantic names describe the job (`accent`, `danger`, `fg-muted`), never the value (`teal`, `light-gray`). Primitive names describe the value.
- States are suffixes in a fixed order: `default`, `hover`, `active`, `selected`, `disabled`, `focus`.
- Scales: numeric for ramps (50-950, where 500 is mid lightness), t-shirt for steps (`xs` to `5xl`), multiples of 4px for space (`space.4` = 1rem).
- Never put a mode in a name (`bg-dark`) or a platform (`ios-accent`). Modes and platforms are contexts.
- Pick American or British spelling once (`color`, not both) and keep it everywhere.

## Aliasing rules

1. Direction: component → semantic → primitive. Depth of three hops or fewer.
2. Two semantic tokens that share a value today stay separate (`fg-muted` and `border-strong` may match in one brand and diverge in another).
3. An alias is a relationship, not evidence: when importing someone else's tokens, record which values were declared and which were inferred (see the UI system's [portability method](../../../library/draft-skills/design-ui-system/references/system-portability.md)).
4. Resolve aliases at build time for platforms that cannot reference (iOS asset catalogs, email), but keep references in CSS where custom properties allow runtime theming.

## Modes

The kit stores one semantic file per mode with identical names. The build emits:

- `:root` with primitives and the light set; `[data-theme="dark"]` and `[data-theme="high-contrast"]` overrides; `@media (prefers-color-scheme: dark)` when no theme is forced; `@media (prefers-contrast: more)` for high contrast; `@media (prefers-reduced-motion: reduce)` setting every non-instant duration to 0.01ms.
- Figma: one variable collection per tier, with modes Light, Dark and High contrast on the semantic collection (see [Figma](figma.md)).

Add a mode only when every semantic token has a deliberate value in it. Density, brand and platform are separate axes; do not multiply them into one giant mode list.

## Multi-brand

- A brand file remaps the primitive references behind accent, neutral and font-family roles (the accent ramp, the neutral ramp's temperature, the display and body families). Semantic tokens keep their names and structure, so every component re-themes without code changes. The exact primitive paths are in `library/tokens/src/brands/`.
- The kit ships Meridian (default, teal accent, OKLCH hue about 195, cool neutrals) and Ember (`data-brand="ember"`, vermilion accent, hue about 35, warm neutrals) to prove the mechanism.
- Lint every brand in every mode: a brand that fails contrast does not ship. If a brand's accent cannot reach 4.5:1 for `fg-on-accent`, give that brand a darker `accent-default` step rather than weakening the rule.
- Keep brand-specific components out of the shared system; a sub-brand that needs a new component contributes it through governance or keeps it local.

## Build, lint and check

Run from the repository root:

```sh
python3 plugins/visual-design-studio/library/scripts/tokens.py build   # src -> dist: tokens.css, tailwind.css, tokens.resolved.json, figma-variables.json (see the tokens README)
python3 plugins/visual-design-studio/library/scripts/tokens.py lint    # schema, aliases, tier direction, contrast guarantees per mode and brand
python3 plugins/visual-design-studio/library/scripts/tokens.py check   # dist is up to date with src (CI gate)
```

Lint enforces the contract's contrast guarantees: `fg-default` and `fg-muted` at 4.5:1 on canvas, surface and raised surface; `fg-subtle` at 3:1; `fg-on-accent` 4.5:1 on accent default, hover and active; status `fg` on status `bg` 4.5:1; `border-strong` and `focus-ring` 3:1 on canvas; high-contrast body text 7:1.

Other tools that read DTCG: Style Dictionary (v4 and later read DTCG natively; v5.3 added the 2025.10 structured color format per its release notes), Terrazzo (formerly Cobalt UI), and Tokens Studio for Figma. Use one build tool per repository; two generators produce drift.

## Common failures

- Semantic layer missing, so components reference `teal-600` directly and rebranding means a rewrite.
- Hundreds of one-off component tokens that duplicate semantic ones: create component tokens only where a component genuinely diverges.
- Token names that leak values (`blue-button`) or modes (`text-dark`).
- Editing generated CSS or Figma variables by hand: the next build overwrites it, or worse, the two drift.
- Renaming a published token without a deprecation alias for one minor version (contract rule; see [governance and versioning](governance-and-versioning.md)).
