# AI tells, fixed

Version-Timestamp: 2026-10-20 02:27:13 UTC

[Open the gallery](index.html). One self-contained page: inline CSS and SVG, no scripts, no network requests, nine OFL fonts in [fonts/](fonts/).

Eighteen generic-AI design tells, each rendered twice at realistic size: the default a model reaches for first ("Generic") and a version built for a specific fictional brief ("Better"), with a short caption on what changed. The catalog behind it, with causes and fixes for every tell, is [ai-tells.md](../../../skills/design-critique/references/ai-tells.md). Score whole designs with the [critique rubric](../../../skills/design-critique/references/rubric.md).

## How to use it

- **Calibrate before critiquing.** Open the page at the width you are reviewing and compare your artifact with the matching pair. If your design resembles a Generic panel and the brief did not ask for it, log the tell by its ID.
- **Steal the move, not the look.** Each Better panel shows a mechanism (domain palette, data as decoration, one primary action, a named AI action). Apply the mechanism in your client's style.
- **Show clients the contrast.** The pairs explain in one glance why a "clean" first draft is not finished.

## Index

| # | Tell (catalog ID) | Better version: industry / atlas style |
| --- | --- | --- |
| 01 | Default indigo-to-pink gradient (AT-01) | Freight dispatch / `style.data-dense-utilitarian` |
| 02 | One sans for everything (AT-02) | Wood-fired trattoria / `style.mid-century-modern` |
| 03 | Centered hero and three icon cards (AT-03) | Architects for schools / `style.swiss-international` |
| 04 | Emoji as icons (AT-04) | Family dental practice / `style.clinical-calm` |
| 05 | Icons in pastel circles (AT-05) | Council service page / `style.civic-plain` |
| 06 | Uniform soft cards everywhere (AT-06) | Neobank account / `style.quiet-minimal` |
| 07 | Glassmorphism on everything (AT-07) | Mountain lodge / `style.scandinavian-nordic` |
| 08 | Gradient text headline (AT-08) | Running club / `style.bold-geometric-sport` |
| 09 | Glowing orbs and blobs (AT-09) | Energy co-op / `style.eco-natural-sustainable` |
| 10 | Fake dashboard hero (AT-10) | Invoicing for freelancers / `style.flat-material` |
| 11 | Sparkles for anything AI (AT-11) | Support tool / `style.corporate-modern` |
| 12 | Blob-people illustration (AT-12) | Bike repair co-op / `style.risograph-print-texture` |
| 13 | Meaningless metrics (AT-14) | Home insurer / `style.editorial-magazine` |
| 14 | Vague promise copy (AT-15, AT-24) | Clay studio course / `style.handcrafted-organic` |
| 15 | Low-contrast gray body text (AT-17) | Litigation firm / `style.classic-luxury-serif` |
| 16 | Too many calls to action (AT-18) | 1930s mansion flat / `style.art-deco` |
| 17 | Badge and pill overload (AT-19) | Silk scarves / `style.fashion-editorial-didone` |
| 18 | Dark mode with neon glow (AT-20) | Deploy CLI and cloud / `style.dark-tech-developer` |

Catalog tells not shown here (stock-photo smiles AT-13, flat hierarchy AT-16, symmetry AT-21, identical section rhythm AT-22, fake testimonials AT-23, motion on everything AT-25, logo-soup proof bars AT-26) are described in the catalog; they need photography, full pages or motion to demonstrate honestly.

## Build rules this page follows

- Generic panels use the reader's Inter or system sans and stock Tailwind-like values on purpose. They are marked `data-variant="generic"` and contain no real links or buttons.
- Better panels use only the tokens they declare, drawn SVG, and fonts from `fonts/`. Every text color on a solid background meets WCAG 2.2 AA (4.5:1 body, 3:1 for 24px+ or 18.66px+ bold).
- Each mini-render is a CSS size container, so it reflows at 390 px instead of scaling down.
- No emoji, arrows or symbols outside the bundled Latin subsets appear in Better panels, so nothing falls back to a system font.

## Verification

Rendered with [render_review.mjs](../../../skills/design-critique/scripts/render_review.mjs) at 390, 768 and 1440 px, full page, with axe-core 4.10.2:

```sh
node plugins/visual-design-studio/skills/design-critique/scripts/render_review.mjs \
  plugins/visual-design-studio/library/examples/ai-tells/index.html \
  --full-page --exclude '[data-variant="generic"]'
```

Result on 2026-10-20 (Chromium 141): no horizontal overflow, no clipped text, 0 contrast failures among 418-424 measured text elements, 0 axe violations, no failed or external requests, no fallback glyphs in Better panels (the only fallback font is Noto Color Emoji inside Generic panels). Remaining review items, checked by eye:

- Two single-word last lines are intentional: "River / loop" (a forced poster break) and "Le Carré / Nocturne" (a three-word product name).
- Seven text elements sit over SVG or glass and are reported as unmeasured. Computed by hand: lodge nav white on the 72% tint over the sky is about 8.6:1; lodge headline #14232A on the lightest sky (#C6D5DC) is about 11:1 and stays above the mountains at every width; chart labels #10261D and #3D5A4C on the yellow band (#F0D884 after blending) are about 10.7:1 and 5.3:1.
- axe lists color-contrast "needs review" for the same SVG-backed nodes.

Every screenshot was inspected at 390 and 1440 px, and the stacked layout at 768 px, before acceptance.

## Fiction and licensing

Every brand, person, address, price and statistic is invented for teaching; UK phone numbers use the Ofcom 01632 960xxx drama range. No third-party logos, photographs or illustrations are used. Fonts are Anton, Archivo, Bodoni Moda, Bricolage Grotesque, Fraunces, JetBrains Mono, Newsreader, Public Sans and Space Grotesk, Latin subsets from Fontsource 5.3.0 packages, each under the SIL Open Font License 1.1 with its `OFL.txt` beside the font file.
