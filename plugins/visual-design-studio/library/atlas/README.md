# Design Space Atlas

Version-Timestamp: 2026-10-20 02:05:00 UTC

The atlas maps the design space so Claude can design for any style, industry, market, audience, brand personality, price position and channel, and combine them on purpose. Each entry is a compact, opinionated brief with concrete values: fonts, colors, scales, conventions, clichés, regulation and reference anchors.

## Axes

| Axis | Entries | Directory | What an entry gives you |
| --- | --- | --- | --- |
| Style | 37 | `styles/` | Visual signature, token recipe (fonts, palette, scale, radius, motion), composition, clichés and AI tells, accessibility notes |
| Industry | 32 | `industries/` | Audience jobs, trust signals, conventions vs differentiation, clichés, regulation, key screens, three recommended directions |
| Market | 17 | `markets/` | Script and fonts, layout direction, color meaning, formats, platforms and payments, regulation, localization pitfalls |
| Audience | 10 | `audiences/` | A table of design defaults that override the general ones (text size, targets, reading level, density, motion) |
| Archetype | 12 | `archetypes/` | Visual translation and voice for a brand personality |
| Price tier | 5 | `tiers/` | Signals and token recipe that position a brand from value to ultra-luxury |
| Channel | 12 | `channels/` | Formats and specs, structure, craft defaults, production and QA |

`registry.json` lists every ID. `index.json` is generated from the entries' frontmatter for fast search.

## Use it

```sh
# Find what is relevant to a brief (top 3 per axis)
python3 ../scripts/atlas.py query "premium skincare for men in korea, minimalist, instagram launch"

# Read one entry
python3 ../scripts/atlas.py show style.quiet-minimal

# Check a combination for tensions and get suggestions
python3 ../scripts/atlas.py combine style.neo-brutalist industry.fintech-banking audience.older-adults

# Browse an axis
python3 ../scripts/atlas.py list --axis industry
```

Add `--json` for machine-readable output. Paths are printed absolute so they can be read directly.

## How to combine entries

1. Start from the **industry** entry's *Recommended directions* (category-expected, adjacent, category-breaking) and *Category clichés*.
2. Apply the **market** entry's script, format and regulatory rules. They are requirements, not style.
3. Apply the **audience** entry's design defaults. They override style defaults (for example, older adults get larger text even in a minimal style).
4. Express the **archetype** and **tier** through type classification, palette, density, imagery and motion pace.
5. Choose a **style** (or two) that serves all of the above, then constrain it to the **channel** specs.
6. Resolve every conflict that `combine` reports deliberately and say how.

The `design-director` skill runs this as a full workflow with divergent directions and weighted scoring.

## Entry structure

Every entry has YAML frontmatter (`id`, `axis`, `name`, `aliases`, `summary`, `tags`, `pairs_with`, `avoid_with`, `version_timestamp`) and fixed H2 sections per axis:

- **Style:** Essence, Visual signature, Token recipe, Composition and layout, Imagery and iconography, Motion, Fits and risks, Do and don't, Clichés and AI tells, Accessibility notes, Reference anchors.
- **Industry:** Audience and jobs to be done, Trust signals, Category conventions, Where to differentiate, Category clichés, Regulatory and compliance notes, Key deliverables and screens, Voice and content, Recommended directions, Metrics that matter, Reference anchors.
- **Market:** Language and script, Typography and layout, Color and symbolism, Imagery and representation, Formats and conventions, Platforms, devices and payments, Regulatory and compliance notes, Localization pitfalls, Reference anchors.
- **Audience:** Who and what they need, Design defaults, Interaction and content, Visual tone, Pitfalls, Regulatory and compliance notes, Reference anchors.
- **Archetype:** Essence, Visual translation, Voice and tone, Fits and tensions, Clichés to avoid, Reference anchors.
- **Tier:** Signals, Token recipe, Imagery and copy, Pitfalls, Reference anchors.
- **Channel:** Formats and specs, Structure and hierarchy, Craft defaults, Production and handoff, QA checklist, Reference anchors.

`python3 ../scripts/atlas.py validate --complete` checks every entry against this structure.

## Limits

- Regulatory notes describe what typically affects design; they are not legal advice. Confirm requirements with counsel for the specific product and jurisdiction.
- Platform specs and trends change. Entries are dated; verify volatile specs (social formats, app store assets, platform UI conventions) before production.
- Reference anchors name public work for orientation. Never copy another brand's assets.
- Cultural guidance is a starting point for research with people from that market, not a substitute for it.
