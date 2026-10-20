# Auditing an existing product and adopting a system incrementally

Version-Timestamp: 2026-10-20 02:08:24 UTC

Most design-system work starts from an existing product with years of drift. Audit what exists, consolidate it into tokens and a short component list, then migrate in slices that ship. Never pause product work for a "big bang" rebuild.

The kit's deeper process material applies here: the [reusable system inventory](../../../library/SYSTEM-INVENTORY.md) (193 concepts across foundations, UI, patterns, templates, assets and governance, with scoping profiles), [discovering and adopting a UI system](../../../library/SYSTEM-ADOPTION.md) (layer-by-layer comparison and reversible adoption decisions), and [starting a component task](../../../library/COMPONENT-START.md) (the prompt and records for component work).

## Audit workflow

1. **Scope**: which products, platforms and flows; who owns them; what decision the audit must support (rebuild, consolidate, adopt a vendor system).
2. **Interface inventory**: screenshot every distinct screen of the top flows on each platform. Cut out and group instances by type (buttons, inputs, cards, modals, tables, navigation, alerts). Count variants per type.
3. **Code inventory**: count unique values and component implementations (commands below).
4. **Design-file inventory**: Figma local styles and variables, library analytics (insertions, detachments), duplicate components across files.
5. **Accessibility baseline**: automated scan (axe) of the top 10 screens plus a manual keyboard and screen-reader pass of the top 3 flows; contrast of every text and UI color pair found.
6. **Consolidate**: cluster the values (below) and propose the token set and component list.
7. **Prioritize**: score each component by frequency x inconsistency x risk (accessibility or revenue impact).
8. **Plan adoption**: slices, owners, metrics, deprecation dates.

## Code inventory commands

Run from the product repository root; adjust globs to the stack.

```sh
# Unique hex colors and how often each appears (CSS, SCSS, JS/TS, Vue, Svelte)
rg -o --no-filename -i '#[0-9a-f]{3,8}\b' -g '*.{css,scss,less,ts,tsx,js,jsx,vue,svelte}' . \
  | tr 'A-F' 'a-f' | sort | uniq -c | sort -rn | head -50

# rgb()/hsl()/oklch() literals
rg -o --no-filename -i '(rgba?|hsla?|oklch)\([^)]*\)' -g '*.{css,scss,ts,tsx,vue}' . | sort | uniq -c | sort -rn | head -30

# Font sizes, spacing and radius literals
rg -o --no-filename 'font-size:\s*[^;]+' -g '*.{css,scss}' . | sort | uniq -c | sort -rn
rg -o --no-filename '(margin|padding|gap)[a-z-]*:\s*[^;]+' -g '*.{css,scss}' . | sort | uniq -c | sort -rn | head -40
rg -o --no-filename 'border-radius:\s*[^;]+' -g '*.{css,scss}' . | sort | uniq -c | sort -rn

# Native apps: hardcoded colors in Swift and Kotlin
rg -n 'Color\(red:|UIColor\(red:|Color\(0x[0-9A-Fa-f]{8}' -g '*.{swift,kt}' .

# Competing component implementations (example: buttons)
rg -l -i 'function \w*button|const \w*button\s*=|class \w*Button' -g '*.{tsx,jsx,vue,svelte,swift,kt}' .
```

Report findings as numbers: near-duplicate grays, distinct font sizes against the kit's 9-step scale, spacing values that are not multiples of 4, and how many button implementations exist with different focus behavior.

## Consolidation rules

- **Color**: convert every found color to OKLCH, cluster by hue and lightness, and collapse near-duplicates (differences you cannot see side by side) into ramp steps. Then name roles: which ones are canvas, surface, text, border, accent, status. Check each role pair for contrast before finalizing. The `color` skill covers ramp building.
- **Type**: map found sizes to the nearest step of the kit scale (`--font-size-xs` to `5xl`: 12 to 60px) and list the outliers that need a design decision.
- **Space**: snap to the 4px scale (`--space-1` to `--space-24`); values like 13px or 22px become 12 or 24 after a visual check.
- **Components**: one implementation per component type; pick the most accessible existing version as the starting point, or rebuild from the kit's component specs.
- Record each mapping (old value, new token, decision, owner) so the migration is mechanical.

## Incremental adoption

| Phase | What ships | How |
| --- | --- | --- |
| 1. Tokens under the hood | New token CSS file loaded first; legacy variables aliased to tokens | `--legacy-brand-blue: var(--color-accent-default);` so old code inherits new values without edits |
| 2. Leaf components | Button, link, icon, input, checkbox, badge | Replace usages screen by screen; codemods for prop renames |
| 3. Composite components | Dialog, menu, select, tabs, table, toast | Behind feature flags where behavior changes |
| 4. Patterns and templates | Forms, empty and error states, navigation shells | Rebuild one flow end to end as the showcase |
| 5. Cleanup | Remove legacy CSS and aliases | Only after usage scans show zero references |

- **New work rule**: from day one, new screens use the system; legacy screens migrate when touched.
- **Ratchet lint**: enable stylelint or ESLint rules that forbid raw colors, spacings and unapproved imports in new or changed files; tighten the allow-list each release.
- **Coexistence**: use CSS cascade layers (`@layer legacy, system, overrides;`) so the system wins predictably while old styles still exist.
- **Vertical slice first**: before migrating everything, prove the system on one real flow with all states (error, empty, loading, keyboard, narrow screens), as the adoption guide above recommends.
- **Native apps**: introduce the generated color and type files first, then replace view styles component by component; keep system chrome native.

## Audit deliverables

1. One-page summary: the counts, the top 5 problems, the recommendation.
2. Value tables: found vs proposed tokens, with frequency.
3. Component matrix: type, implementations found, recommended source, priority.
4. Accessibility findings with severity and the components they trace to.
5. Adoption roadmap: phases, owners, dates, metrics (coverage, token adherence, version lag; see [governance and versioning](governance-and-versioning.md)).

## Common failures

- An audit deck with screenshots and no numbers or decisions.
- Rebuilding all components before any product screen uses one.
- Migrating visuals and behavior in the same change, so regressions are hard to trace.
- Treating the vendor system's defaults as the brand: adopting Material or a UI kit unchanged makes the product look like everyone else's. Map the brand onto its tokens.
