---
name: brand-identity
description: >-
  Builds brand strategy, positioning, names, logos and identity systems with construction-level craft: three distinct
  territories, unit grids, optical corrections, 16px and one-color tests, clear space, minimum sizes, file sets, brand
  architecture and guidelines. Use when asked for a brand, rebrand or refresh, a logo, wordmark, monogram or symbol, a
  name or naming screen, a positioning statement or brand platform, an archetype, an identity system, a brand portal
  or a brand book and handoff file set.
license: MIT
metadata:
  version-timestamp: "2026-10-27 12:00:00 UTC"
  agent-attribution: "computer=vm; tool=Claude Code; version=2.1.309; timestamp=2026-10-23 20:10:44 UTC"
---

# Brand identity

Excellent identity work starts from a position a competitor could not sign, turns it into one memorable idea, and draws that idea precisely enough to survive a 16px favicon, a one-color rubber stamp and a ten-meter sign. The logo is one asset in a system; the system is what people recognize.

## Defaults

| Decision | Default | Change when |
| --- | --- | --- |
| Strategy before drawing | One-sentence positioning, 3-5 attributes written as "X, not Y", one primary archetype (one secondary at most) | Client supplies an approved platform: reuse it and list the gaps |
| Territories | 3 distinct ideas, each with 1 hero mark and 2 alternates; every pair differs in idea and in 2+ of: logo type, shape language, type genre | Refresh with strong equity: 1 faithful evolution plus 2 bolder steps |
| First presentation | Black on white, equal optical size, same name, no mockups; then 1-color reversed; then 3 real applications | Never skip the flat view: mockups hide weak silhouettes |
| Construction | Base unit = main stroke weight; radii, gaps and counters as multiples of it; Bezier points on extrema; circle-quadrant handles about 0.552 of the radius | Calligraphic or hand-lettered marks: construction notes replace the grid |
| Optical corrections | Round overshoot 1-3% of cap height; pointed overshoot 2-5%; horizontals 5-12% thinner than verticals; visual center 2-5% above geometric center | Large display-only marks: lower end; small sizes and ink spread: upper end |
| Small-size test | Symbol reads at 16x16 and 32x32 px; wordmark reads at 80-100px wide | Fails: draw a small-size master (open counters, heavier hairlines, +2-5% tracking) |
| Color test | Works in 1-color black, 1-color white on black, and on a mid-tone photo before any brand color is added | Gradient or multicolor marks: a flat fallback for every version |
| Clear space | 1x a named element of the mark (cap height, or symbol width) on all sides | Tight UI headers: 0.5x, documented as the exception |
| Minimum size | Wordmark 80px / 20mm wide; horizontal combination 100-120px / 25-30mm; symbol 16px / 6mm; drop the tagline below 150px / 35mm | Final values come from render and print tests of the actual mark |
| Palette | 1-2 brand colors, 2 neutrals, 1 accent; each in HEX (sRGB), CMYK coated and uncoated, Pantone C and U, RAL or NCS for signage | Value tier and kids: up to 4 brights; luxury: 1 color plus black, white and a metallic |
| File set | SVG, PDF, PNG @1x/2x/3x, favicon set, 1024px app-icon master, native source; EPS only on request | Scale the whole package by tier: [identity deliverables](references/identity-deliverables.md) |
| Brand book | Screen PDF (16:9) plus PDF/X-4 print master rendered by the kit, Canva editable twin, 1-2 page quick reference; every value generated from tokens and a print spec file | No print run: skip the print master. See [brand book production](references/brand-book-production.md) |
| Third-party assets | Default licensed stack (Lucide, Phosphor or Tabler icons, OFL fonts, CC0 or Pixabay audio) with a provenance record per asset; never NC licenses or scraped images | Client owns a paid library: use it and record the license tier |
| Naming | 200-400 raw candidates over 4-6 typologies, 30 shortlisted, 10 screened, 3-5 presented in context | Naming a feature or sub-brand: architecture rules first, then 20-50 candidates |
| Trademark | Knockout screen recorded with date, database, Nice classes and query; never called clearance | Always route adoption through a qualified trademark attorney |

## Workflow

1. **Extract the variables.** Industry, markets and scripts, audience, archetype, price tier, channels, existing equity, media budget. Run the atlas query below and read the 3-5 entries it returns. When the brief is thin ("design us a logo"), ask at most 4 questions, each with options and a recommendation (name and what you do, audience, personality versus competitors, main use), state the rest as assumptions, and offer to proceed on them.
2. **Strategy.** Competitor audit (8-15 brands), perceptual map, positioning statement, platform and an attribute-to-design translation table. See [strategy and positioning](references/strategy-and-positioning.md).
3. **Name**, if needed: territories, generation, linguistic and trademark knockout screens. See [naming](references/naming.md).
4. **Explore.** 50-100 thumbnails, cluster them, pick 3 territories that differ in idea. See [concept exploration](references/logo-design.md#concept-exploration-to-three-territories).
5. **Construct.** Vectorize the chosen territory on a unit grid, customize letterforms instead of typing a font, apply optical corrections.
6. **Render and inspect.** Export PNGs at 16, 32, 64, 200 and 1000px; view at 100% on light and dark; blur test; line up against 8-12 competitor logos in grayscale at equal height. Fix, re-export, compare. Use `design-critique` for the scored loop.
7. **System.** Color, type, graphic device, imagery, motion, voice and templates, stress-tested across 6 applications. See [identity system](references/identity-system.md).
8. **Deliver.** Pick the tier's package from [identity deliverables](references/identity-deliverables.md), write the book with [guidelines](references/guidelines.md), then produce it with [brand book production](references/brand-book-production.md): print master from the kit's collateral templates, screen PDF, Canva twin, approvals per section. Decks come from the [PPTX deck example](../../library/examples/deck-pptx/README.md). Record every third-party asset in a [provenance record](../../library/knowledge/ASSETS-LICENSES.md#provenance-record).
9. **Existing brand?** Run the equity audit before drawing and decide evolve or replace. See [refresh vs rebrand](references/refresh-vs-rebrand.md).

## Decisions that change the answer

- **Tier.** Value: larger marks, bold sans, high-contrast primaries, symbol-led for shelf impact. Premium and luxury: wordmark-led, 1.5-2x clear space, refined serif or sans, one color plus black, foil or blind emboss in print. Ultra-luxury: monogram plus wordmark, almost no color.
- **Archetype.** Sets shape language and voice. Ruler and Sage lean on symmetry, rational type and restraint; Jester and Creator on irregular shapes and color; Outlaw on rough edges and hard contrast. Read the entry, for example `python3 ../../library/scripts/atlas.py show archetype.ruler`.
- **Industry code.** Decide which category codes are entry tickets (keep) and which are clichés (break). The industry entry's "Recommended directions" gives the expected, adjacent and breaking positions.
- **Market and script.** Arabic, Hebrew, CJK, Devanagari or Thai lockups need native type design, not a font swap. Check color and gesture meanings and screen the name in every language.
- **Channel mix.** App-first or social-first: a symbol or monogram is mandatory for icons and avatars. Retail: shelf legibility at 2-3m. Signage: counters and strokes at large scale and in fabricated materials.
- **Name length.** Over 10-12 letters or 3+ words: pair the wordmark with a monogram or symbol for small spaces.
- **Media budget.** Abstract symbols need sustained exposure before they carry meaning alone; small budgets favor wordmarks and descriptive combination marks.

## Common failures

- Three territories that are one idea in three fonts → change the source of the idea (name, product, place, metaphor, gesture), not the styling.
- Untouched Montserrat, Inter or Poppins as the wordmark → custom spacing plus one distinctive letter, terminal or ligature, or a licensed distinctive face.
- Category-cliché symbols (swoosh, globe, lightbulb, connected dots, leaf in hand, shield with check, gradient blob, letter in a circle) → push past the first 20 sketches; reverse-image-search the finalists.
- Golden-ratio circles drawn over a finished mark → show only the construction that drove decisions.
- Hairlines and counters that close at 16px → a small-size master, or strokes of at least 1.5px at 16px.
- Mathematically centered mark in a circle or app tile that looks low or left-heavy → shift by eye using the optical-centering values.
- Raster AI output presented as the logo → treat it as a sketch; redraw in vector, check distinctiveness, record provenance.
- Gradient-only or color-dependent mark → a one-color version for stamps, embroidery, etching and partner lockups.
- Guidelines PDF without assets or templates → ship a portal or package with files, templates and a one-page quick reference.
- Canva design sent to the printer as the master → print from the kit's PDF/X master; Canva holds the editable twin.

Single-context fallback: every step above runs in one context. Where review-panel subagents are not loaded (Codex, claude.ai chat), run the `design-critique` rubric yourself in steps 6 and 8, one lens at a time.

## References

- [Strategy and positioning](references/strategy-and-positioning.md): positioning statement, brand platform, perceptual mapping, archetypes, brief-to-strategy workflow.
- [Naming](references/naming.md): typologies, generation techniques, linguistic screening, domains and handles, trademark knockout searches.
- [Logo design](references/logo-design.md): logo types, territories, construction grids, optical corrections, scalability tests, clear space, minimum sizes, file set, lockups.
- [Identity system](references/identity-system.md): elements beyond the logo, flexible and dynamic identities, brand architecture.
- [Guidelines](references/guidelines.md): brand book structure, must-have contents, digital brand portal, AI handoff.
- [Brand book production](references/brand-book-production.md): page-by-page book, editions, sources of truth for HEX, CMYK and Pantone, print master and Canva twin, who approves.
- [Identity deliverables](references/identity-deliverables.md): deliverable checklist for startup, mid-market and enterprise or rebrand, formats, file naming, handoff checks.
- [Collateral templates](../../library/examples/collateral/README.md): token-driven brand guidelines book (logo, clear space, color with HEX/RGB/CMYK/Pantone slots, type, imagery, voice, do and don't), business card, one-pager; render with `../print-packaging-social/scripts/render_collateral.mjs`.
- [Asset licenses](../../library/knowledge/ASSETS-LICENSES.md): licensed icon, font and audio stack, provenance record, never-use list.
- [Refresh vs rebrand](references/refresh-vs-rebrand.md): equity audit, evolution vs revolution, migration plan.
- Atlas, whenever style, industry, market, archetype or tier matters:
  - `python3 ../../library/scripts/atlas.py query "boutique hotel brand japan luxury"`
  - `python3 ../../library/scripts/atlas.py show archetype.explorer`
  - `python3 ../../library/scripts/atlas.py combine style.classic-luxury-serif archetype.lover tier.luxury`
- Deep process for client projects with approvals and records: [brand strategy](../../library/draft-skills/design-brand-strategy/SKILL.md), [naming](../../library/draft-skills/design-brand-naming/SKILL.md), [logo concepts](../../library/draft-skills/design-logo-concepts/SKILL.md), [logo refinement](../../library/draft-skills/design-logo-refinement/SKILL.md), [logo variants](../../library/draft-skills/design-logo-variants/SKILL.md), [logo evaluation](../../library/draft-skills/design-logo-evaluation/SKILL.md), [identity system](../../library/draft-skills/design-identity-system/SKILL.md), [identity refresh](../../library/draft-skills/design-identity-refresh/SKILL.md), [identity delivery](../../library/draft-skills/design-identity-delivery/SKILL.md), [brand guidelines](../../library/draft-skills/design-brand-guidelines/SKILL.md), the [identity workflow](../../library/IDENTITY-WORKFLOW.md) and the [logo study template](../../library/templates/logo-study.md).

Catalog IDs covered: brand-strategy, brand-naming, identity, logo-concepts, logo-refinement, logo-variants, logo-evaluation, identity-refresh, identity-delivery, brand-guidelines
