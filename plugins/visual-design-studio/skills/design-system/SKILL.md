---
name: design-system
description: >-
  Build and run design systems: DTCG token architecture (primitive, semantic, component and brand tiers), light,
  dark, high-contrast and multi-brand theming, Figma variables, libraries and Code Connect, component APIs with
  accessibility contracts, documentation and Storybook, governance, semver and deprecation, and audits for
  incremental adoption. Use when creating or changing tokens, theming a product or brand, building a component
  library in code or Figma, writing component docs, or planning a design-system rollout.
license: MIT
metadata:
  version-timestamp: "2026-10-20 02:08:24 UTC"
  agent-attribution: "computer=vm; tool=Claude Code; version=2.1.304; timestamp=2026-10-20 02:08:24 UTC"
---

# Design system

A good design system makes the brand's decisions once and compiles them everywhere: one token source, components whose names, states and accessibility behave the same in Figma, web and native, docs people actually read, and releases that never surprise the products using it. It encodes a specific brand direction; it is not a neutral starter kit with a logo swapped in.

## Defaults

| Decision | Default | Change when |
| --- | --- | --- |
| Source of truth | DTCG 2025.10 JSON in the repository ([token sources](../../library/tokens/src/), documented in `library/tokens/README.md`) built by [tokens.py](../../library/scripts/tokens.py) | Client mandates another master: import it once, then keep exactly one master |
| Tiers | Primitives, semantic per mode, optional component tokens, brand overrides that remap primitives | Tiny one-off site: primitives plus semantic only |
| Naming | `category.concept.property.state` to CSS `--color-bg-surface-raised`; roles, never values | Never rename published names without a one-minor deprecation alias |
| Modes | Light, dark, high contrast; follow the OS with a user override | Fixed-environment kiosks: one tuned mode |
| Contrast floors | Text 4.5:1, UI and focus 3:1, high-contrast body 7:1, enforced by `tokens.py lint` | Never relaxed per brand |
| Space and size | 4px base (`--space-0` to `--space-24`); targets 24px minimum, 44px comfortable | Touch-first products: 44px minimum |
| Type | `--font-size-xs` to `5xl` (12-60px), line heights 1.1 / 1.25 / 1.5 / 1.65 | Editorial display sizes as component tokens |
| Radius, shadow, motion | Radius 0/4/8/12/16/full; `--shadow-sm` to `xl`; 120/200/320/480ms with `--ease-standard` | Style direction sets them through brand primitives (Swiss: 0-2px, no shadow) |
| Component vocabulary | `variant`, `size`, `tone`, `disabled`, `value`/`defaultValue`/`onValueChange`, `open`/`onOpenChange` | Follow the host framework's idiom on native |
| Primitive layer | One headless library (React Aria, Radix, Base UI, Ark or Headless UI) | Native: platform components themed with tokens |
| Figma | Variables imported from the build with scopes and code syntax; components mirror code props; Code Connect template files | Starter or Professional plans: no Code Connect, fewer modes |
| Docs | One page per component (usage, anatomy, states, accessibility, props, tokens, changelog); Storybook with the a11y addon failing CI | Very small systems: Storybook docs only |
| Versioning | Semver; deprecate with alias, remove no sooner than the next major | |

## Workflow

1. **Scope the job**: new system, extension, brand theme, or audit and migration of an existing product. For an existing product start with [audit and adoption](references/audit-and-adoption.md).
2. **Get the direction**: the tokens express a chosen visual direction. Run `python3 ../../library/scripts/atlas.py query "<brand, industry, audience, tier>"` and read the selected style entries' Token recipe tables, or take the recipe from the `design-director` skill's handoff.
3. **Define tokens** in DTCG per [token architecture](references/token-architecture.md): primitives, semantic roles per mode, component tokens only where needed. Run `tokens.py build`, `lint` and `check` from the repository root.
4. **Theme**: modes, brands and density per [theming](references/theming.md); lint every mode x brand pair.
5. **Specify components**: anatomy, props, states and accessibility contract per [component API](references/component-api.md), starting from the kit's [component specs](../../library/examples/component-specs/README.md).
6. **Mirror in Figma** per [Figma](references/figma.md): import `library/tokens/dist/figma-variables.json`, build components with matching properties, connect them with Code Connect.
7. **Implement**: web components on the chosen headless layer (the React reference system at [react-system](../../library/examples/react-system/README.md) shows the pattern: Radix primitives, token-only styling, axe-tested in every brand and mode); native themes through the `native-app-design` skill's SwiftUI and Compose handoff.
8. **Render and inspect**: a specimen page plus 4-5 reference screens (form, table, dialog, marketing section, error state) in every mode and brand. Screenshot and critique with the `design-critique` skill; run Storybook accessibility checks; fix before release.
9. **Document** per [documentation](references/documentation.md).
10. **Release and govern** per [governance and versioning](references/governance-and-versioning.md): changelog, semver, deprecations, adoption metrics.

## Decisions that change the answer

- **Scale**: one product and a small team favors a light process and possibly copy-in components; many products need a versioned package, RFCs and adoption metrics.
- **Brands**: white-label and multi-brand products need the brand tier from day one, brand-scoped contrast lint and Figma brand modes or extended collections.
- **Platforms**: web-only systems can lean on CSS variables at runtime; web plus native needs build-time generation and naming parity tables.
- **Style direction**: Swiss and data-dense directions mean small radii, no shadows and compact density options; playful or soft directions mean larger radii and springier motion. Change primitives, not component code.
- **Audience**: accessibility-first and older audiences raise minimum text and target sizes and may make high contrast a first-class default.
- **Existing vendor system** (Material, Fluent, Carbon, a UI kit): map the brand onto its tokens when speed matters; replace components only where the brand or accessibility demands it.
- **Client tooling**: Figma plan decides mode counts, branching and Code Connect availability; check before promising a workflow.

## Common failures

- A palette, not a system: tokens named by color with no semantic roles, so dark mode and rebrands mean rewrites. Add the semantic tier.
- Two masters: values edited in Figma and in code separately. Generate Figma variables and platform files from the DTCG source.
- The generic default look shipped as a brand: stock shadcn/ui styling, Inter everywhere, slate grays, 8px radius and the same shadow on every card. Derive every primitive from the brand direction.
- Prop sprawl and inconsistent names (`isOpen`, `visible`, `show`) across components. Fix the vocabulary.
- Components without an accessibility contract: missing focus return, unlabeled icon buttons, keyboard traps.
- Docs made of screenshots that drift from the code. Render real components.
- Dark mode by inversion; brand themes that pass in light and fail in dark.
- Breaking changes released as minors, and deprecations that never finish.

## References

- [Token architecture](references/token-architecture.md): DTCG format, tiers, naming, aliasing, modes, multi-brand, build and lint.
- [Theming](references/theming.md): light, dark, high contrast, brands, density, platform outputs.
- [Figma](references/figma.md): variables, styles, auto layout, component properties, publishing, Dev Mode, Code Connect, Figma MCP and the figma skills.
- [Component API](references/component-api.md): props, variants, composition, controlled state, polymorphism, accessibility contracts, headless libraries, shadcn/ui.
- [Documentation](references/documentation.md): doc site structure, component page template, Storybook with the a11y addon.
- [Governance and versioning](references/governance-and-versioning.md): contribution, RFCs, semver, deprecation, changelog, adoption metrics.
- [Audit and adoption](references/audit-and-adoption.md): auditing a product, consolidation, incremental migration.
- Atlas: `python3 ../../library/scripts/atlas.py query "..."` for the direction behind the tokens.
- Native platforms: the [native-app-design skill](../native-app-design/SKILL.md).
- Deep process (client projects): [UI system](../../library/draft-skills/design-ui-system/SKILL.md) and its [system portability](../../library/draft-skills/design-ui-system/references/system-portability.md); [Figma production](../../library/draft-skills/design-production-interface/references/figma.md); [website system assembly](../../library/draft-skills/design-web-system-assembly/SKILL.md); [system inventory](../../library/SYSTEM-INVENTORY.md), [system adoption](../../library/SYSTEM-ADOPTION.md) and [component start](../../library/COMPONENT-START.md).

Catalog IDs covered: ui, web-system-assembly, production
