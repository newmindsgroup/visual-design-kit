# Design Space Atlas entry schema

Version-Timestamp: 2026-10-20 01:42:00 UTC

The atlas maps the design space so Claude can design for any style, industry, market, audience, brand archetype, price tier and channel, and combine them deliberately. Entries live in `plugins/visual-design-studio/library/atlas/<axis-dir>/<slug>.md`. Every ID must already exist in `library/atlas/registry.json`.

| Axis | ID prefix | Directory |
| --- | --- | --- |
| style | `style.` | `styles/` |
| industry | `industry.` | `industries/` |
| market | `market.` | `markets/` |
| audience | `audience.` | `audiences/` |
| archetype | `archetype.` | `archetypes/` |
| tier | `tier.` | `tiers/` |
| channel | `channel.` | `channels/` |

## Frontmatter

Strict subset of YAML: one `key: value` per line; lists use `[a, b, c]` on one line; no nesting; no multi-line values. Colons inside a value are fine (only the first colon separates key and value); surrounding quotes are optional and stripped.

```yaml
---
id: style.swiss-international
axis: style
name: Swiss / International Typographic Style
aliases: [swiss style, international typographic style, grid modernism]
summary: Objective, grid-driven typography with asymmetric layouts, sans-serif type and flat color; clarity as the aesthetic.
tags: [grid, sans-serif, typographic, objective, modernist, flat]
pairs_with: [industry.fintech-banking, industry.saas-b2b, channel.presentation]
avoid_with: [audience.children-under-13]
version_timestamp: 2026-10-20 01:42:00 UTC
---
```

- `summary`: one sentence, at most 200 characters. It is what Claude sees in query results.
- `tags`: 4-10 lowercase search terms a person might type in a brief.
- `pairs_with`: 3-10 registry IDs from other axes that combine well. `avoid_with`: 0-6 IDs where it usually fails. Explain the reasons in the body.

## Required H2 sections, exact text, in this order

### style
`Essence`, `Visual signature`, `Token recipe`, `Composition and layout`, `Imagery and iconography`, `Motion`, `Fits and risks`, `Do and don't`, `Clichés and AI tells`, `Accessibility notes`, `Reference anchors`

- **Token recipe** must be a table with concrete values for: display font options (2-3, prefer OFL/Google Fonts plus one commercial alternative), body font options, type scale ratio, body size and line-height, letter-spacing for display and caps, weight usage, palette (5-8 roles with hex and OKLCH), radius, border usage, shadow/elevation, spacing density, grid, motion duration and easing.

### industry
`Audience and jobs to be done`, `Trust signals`, `Category conventions`, `Where to differentiate`, `Category clichés`, `Regulatory and compliance notes`, `Key deliverables and screens`, `Voice and content`, `Recommended directions`, `Metrics that matter`, `Reference anchors`

- **Recommended directions** must list three directions with atlas IDs: *Category-expected* (safe, fits norms), *Adjacent* (borrowed from a neighboring category), *Category-breaking* (deliberately different, with the risk stated).

### market
`Language and script`, `Typography and layout`, `Color and symbolism`, `Imagery and representation`, `Formats and conventions`, `Platforms, devices and payments`, `Regulatory and compliance notes`, `Localization pitfalls`, `Reference anchors`

### audience
`Who and what they need`, `Design defaults`, `Interaction and content`, `Visual tone`, `Pitfalls`, `Regulatory and compliance notes`, `Reference anchors`

- **Design defaults** must be a table of concrete values (minimum text size, target size, contrast, reading level, session length, motion, density) that differ from the general defaults.

### archetype
`Essence`, `Visual translation`, `Voice and tone`, `Fits and tensions`, `Clichés to avoid`, `Reference anchors`

### tier
`Signals`, `Token recipe`, `Imagery and copy`, `Pitfalls`, `Reference anchors`

### channel
`Formats and specs`, `Structure and hierarchy`, `Craft defaults`, `Production and handoff`, `QA checklist`, `Reference anchors`

- **Formats and specs** is a table with dimensions, resolution, color space, file types and safe areas. Date volatile platform specs ("as of 2026") and say where to confirm them.

## Reference anchors

3-8 bullets naming real public references: designers, movements, publications, public design systems, brands, books or standards. Link URLs only when you are confident they are stable and correct (official sites, Wikipedia, W3C, Apple, Google). Never embed or copy their assets.

## Validation

```sh
python3 plugins/visual-design-studio/library/scripts/atlas.py validate            # entries present so far
python3 plugins/visual-design-studio/library/scripts/atlas.py validate --complete # every registry ID has a file
python3 plugins/visual-design-studio/library/scripts/atlas.py build              # regenerate index.json
```
