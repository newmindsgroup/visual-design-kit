# Stylescapes: calibration set and template

Version-Timestamp: 2026-10-20 02:56:57 UTC

Twelve fictional brands, each rendered as one stylescape page in a deliberately different direction, plus the reusable template the `design-director` skill uses to present competing directions. The set exists for two jobs:

1. **Calibration.** Show Claude (and people) what excellent, distinct work looks like across the design space, from neo-brutalist fintech to an Arabic-first luxury storefront. The kit's earlier examples were all quiet editorial cream-and-serif; this set spans styles, industries, markets, audiences, archetypes, price tiers and channels.
2. **Format.** Every page uses the same ten sections, so two or three candidate directions for one brief can be compared side by side and scored.

All brands, people, addresses and data are invented. All artwork is CSS, inline SVG and self-hosted fonts; pages make no network requests.

## View locally

```sh
cd plugins/visual-design-studio/library
python3 -m http.server 8000
# open http://localhost:8000/examples/stylescapes/
```

Opening the files directly (`file://`) also works in most browsers; a local server avoids font-loading restrictions.

## Page format

Every page, and the template, has these sections in this order, with these `id`s:

| # | id | Contents |
| --- | --- | --- |
| 1 | `direction` | Brand, direction name, atlas ID chips, one-line brief |
| 2 | `hero` | Key visual for the main channel: landing hero, poster, app screen, packaging front or dashboard. The showpiece. |
| 3 | `palette` | 5-8 swatches with role, hex, OKLCH and computed contrast against the intended background |
| 4 | `type` | Display, body and caption specimens with family, size, line-height and real copy in the brand's language |
| 5 | `components` | Primary, secondary, disabled and focused buttons; input with label, hint and error; card or list item; badges |
| 6 | `applications` | One or two touchpoints relevant to the channel |
| 7 | `imagery` | Imagery direction, 4-6 inline SVG icons drawn to the direction's rules, an illustration or texture sample |
| 8 | `motion` | Durations and easing plus one CSS demo that respects `prefers-reduced-motion` |
| 9 | `voice` | Headline, CTA and error message |
| 10 | `rationale` | Why it fits, what it risks, the category-expected alternative |

Shared rules: CSS custom properties use the token contract names (`--color-bg-canvas`, `--color-accent-default`, `--font-family-display`, `--space-4`, `--radius-md`, `--duration-moderate`, `--ease-standard` and the rest of `.claude/skills/design-kit-authoring/references/token-contract.md`), so each page doubles as a token example; brand-only extras use a brand prefix (for example `--vibra-ease-pop`). WCAG 2.2 AA throughout (4.5:1 text, 3:1 large text and UI, visible focus, 24px minimum targets, correct `lang`/`dir`). Layouts are checked at 390 and 1440 px.

## How design-director uses `_template/`

`_template/stylescape.html` is a neutral, fully working page (the kit's default Meridian slate and teal tokens, system fonts) that looks finished even when unfilled.

1. Copy it once per candidate direction, for example to `<project>/stylescapes/direction-a.html`, `direction-b.html`, `direction-c.html`.
2. Replace the **BRAND TOKENS** block in `:root`; keep the variable names.
3. Add `@font-face` rules for self-hosted OFL fonts (license file beside the woff2). Subset CJK or Arabic fonts to the glyphs used.
4. Fill every element marked `data-slot="..."`; text in `[square brackets]` is placeholder. Delete every `.guide` note.
5. Replace the whole `.kv` block in `#hero` with the real key visual.
6. List 5-8 palette roles as `.swatch` elements with `data-hex` and `data-on`; the small script at the end of the template computes OKLCH and the WCAG 2 ratio into the `[data-out]` cells (same math as the kit's `colorcheck.py`). Delete the script if the values are hardcoded.
7. Optionally fill the weighted scorecard in `#rationale`, or delete it if scores live elsewhere.
8. Render each page at 1440 and 390 px, inspect the screenshots, fix clipped text, orphans, overflow and missing glyphs, then present the directions side by side.

The brand pages in this folder are worked examples of step 5: each one replaces the placeholder with a full composition.

## Brands

| # | Page | Direction | Brief | Atlas IDs | Author |
| --- | --- | --- | --- | --- | --- |
| 1 | [`vibra-neobank`](vibra-neobank/index.html) | Loud and Honest | No-fee, Pix-first neobank for Gen Z in Brazil, Portuguese copy | style.neo-brutalist, industry.fintech-banking, market.brazil-portuguese, audience.teens-gen-z, archetype.everyperson, tier.value, channel.native-app | A |
| 2 | [`little-harbor-health`](little-harbor-health/index.html) | Night Light | Pediatric telehealth for parents of young kids | style.playful-bubbly, style.clinical-calm, industry.digital-health-wellness, audience.children-under-13, archetype.caregiver, tier.mid-market, channel.marketing-website | A |
| 3 | [`kiyomi-house`](kiyomi-house/index.html) | Light Through Paper | Eight-room boutique inn in Kyoto, bilingual JA/EN | style.quiet-minimal, industry.hotels-travel, market.japan, archetype.innocent, tier.luxury, channel.marketing-website | A |
| 4 | [`gridline-ops`](gridline-ops/index.html) | Quiet Until It Matters | Industrial IoT monitoring for plant operators | style.data-dense-utilitarian, industry.industrial-manufacturing-construction, audience.expert-power-users, archetype.sage, channel.web-app | A |
| 5 | [`static-drop`](static-drop/index.html) | Photocopy Chrome | Limited streetwear drops for teens, released online | style.grunge-punk-zine, style.y2k-cyber, industry.fashion-apparel, audience.teens-gen-z, archetype.outlaw, channel.ecommerce-store | A |
| 6 | [`finca-alba`](finca-alba/index.html) | Carved at Dawn | Single-origin Puerto Rican coffee, bilingual ES/EN packaging | style.vintage-heritage-americana, style.handcrafted-organic, industry.food-beverage-cpg, market.us-hispanic-puerto-rico-caribbean, archetype.creator, tier.premium, channel.packaging | A |
| 7 | [`harlow-vance`](harlow-vance/index.html) | The Record | Litigation and appeals law firm | style.classic-luxury-serif, industry.legal-professional-services, archetype.ruler, tier.premium, channel.marketing-website | B |
| 8 | [`tidewater-collective`](tidewater-collective/index.html) | Field Report | Coastal climate-resilience nonprofit raising donations | style.eco-natural-sustainable, style.editorial-magazine, industry.nonprofit-ngo, industry.energy-climate, archetype.hero, channel.marketing-website | B |
| 9 | [`apex-wolves`](apex-wolves/index.html) | Hunt As One | An esports team's season launch | style.bold-geometric-sport, style.dark-tech-developer, industry.gaming-esports, audience.teens-gen-z, archetype.hero, channel.social-media | B |
| 10 | [`carefill`](carefill/index.html) | Plain and Sure | Prescription refills and reminders for adults 65+ | style.civic-plain, style.clinical-calm, industry.healthcare-provider, audience.older-adults, archetype.caregiver, channel.native-app | B |
| 11 | [`noor-atelier`](noor-atelier/index.html) | Quiet Light | Arabic-first modest-fashion e-commerce in the UAE, RTL | style.classic-luxury-serif, industry.fashion-apparel, market.middle-east-north-africa-arabic, tier.luxury, channel.ecommerce-store | B |
| 12 | [`forge-cli`](forge-cli/index.html) | Shop Drawing | CLI and cloud for deploying AI agents, for developers | style.dark-tech-developer, industry.developer-tools, audience.expert-power-users, archetype.magician, channel.marketing-website | B |

Machine-readable data (slug, name, direction, brief, atlas IDs, key visual, palette, fonts, author, note): [`brands.json`](brands.json). Gallery: [`index.html`](index.html).

## Font licensing

Every font is bundled under the SIL Open Font License 1.1, with its `OFL.txt` (copyright line plus the full license) in the same folder: `fonts/<family-slug>/`. Latin files come from the Fontsource npm packages (`@fontsource/*`, `@fontsource-variable/*`), which repackage the Google Fonts releases; only the needed woff2 subsets were copied. The OFL allows bundling and modification (subsetting counts) as long as the fonts are not sold on their own and the license travels with them. None of the bundled `OFL.txt` files declares a Reserved Font Name, so subset files may keep their family names; check this again before subsetting any newly added family.

| Family | Folder | Used by | Notes |
| --- | --- | --- | --- |
| Bricolage Grotesque | `bricolage-grotesque` | Vibra, gallery | Variable: wght, wdth, opsz |
| Fredoka | `fredoka` | Little Harbor, gallery | Variable wght |
| Atkinson Hyperlegible Next | `atkinson-hyperlegible-next` | Little Harbor | Variable wght |
| Shippori Mincho | `shippori-mincho` | Kiyomi House, gallery | Subset to the page's glyphs with fontTools from the Google Fonts TTF |
| Zen Kaku Gothic New | `zen-kaku-gothic-new` | Kiyomi House | Subset to the page's glyphs |
| IBM Plex Sans Condensed | `ibm-plex-sans-condensed` | Gridline, gallery | 400, 500, 600 |
| IBM Plex Mono | `ibm-plex-mono` | Gridline | 400, 500 |
| Anton | `anton` | STATIC | 400 |
| Unbounded | `unbounded` | STATIC, gallery | Variable wght |
| Courier Prime | `courier-prime` | STATIC | 400, 700 |
| Young Serif | `young-serif` | Finca Alba, gallery | 400 |
| Big Shoulders Display | `big-shoulders-display` | Finca Alba | Variable wght |
| Libre Franklin | `libre-franklin` | Finca Alba | Variable wght |
| La Belle Aurore | `la-belle-aurore` | Finca Alba | 400 |
| Libre Caslon Display, Libre Caslon Text | `libre-caslon-display`, `libre-caslon-text` | Harlow & Vance, gallery | |
| Newsreader, Archivo | `newsreader`, `archivo` | Tidewater Collective, gallery | |
| Saira | `saira` | Apex Wolves, gallery | |
| Public Sans | `public-sans` | CareFill, gallery | |
| Amiri, IBM Plex Sans Arabic, Bodoni Moda | `amiri`, `ibm-plex-sans-arabic`, `bodoni-moda` | Noor Atelier, gallery | Arabic subsets |
| Instrument Sans, Martian Mono | `instrument-sans`, `martian-mono` | Forge, gallery | |

Font budget for the whole set is 4 MB; the folder is about 2 MB. When Japanese or Arabic copy changes, re-subset from the full TTF, for example:

```sh
pyftsubset ShipporiMincho-Regular.ttf --text-file=chars.txt --layout-features='*' \
  --flavor=woff2 --output-file=fonts/shippori-mincho/shippori-mincho-kiyomi-subset-400.woff2
```

`--layout-features='*'` keeps the vertical-writing alternates (`vert`, `vrt2`) that tategaki punctuation needs.

## Adding a brand

1. Copy `_template/stylescape.html` to `<slug>/index.html`, fill it, keep the ten section ids.
2. Put fonts in `fonts/<family-slug>/` with `OFL.txt`; reuse an existing folder when the family is already there.
3. Compute every palette value with `colorcheck.py` (or the template script), never by eye.
4. Render at 1440 and 390 px and review the screenshots.
5. Add the brand to `brands.json`, this table and a preview card in `index.html`.
