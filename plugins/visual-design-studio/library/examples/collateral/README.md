# Collateral templates

Version-Timestamp: 2026-10-23 20:38:00 UTC

Token-driven HTML/CSS templates for finished sales, marketing and brand-identity files. Every color, family, weight, line height and letter spacing comes from `styles/tokens.css`, so one attribute (`data-brand` on `<html>`) switches the whole set between the kit's two reference brands, Meridian and Ember, and a client's tokens switch it to their brand. The `print-packaging-social` skill points here when a brief asks for finished files rather than direction.

All content is fictional and marked on the page with a `SAMPLE:` line: company, people, client, quote, phone numbers (555-01xx range), addresses and every figure. Replace each `data-field` before anything leaves the studio, and delete the sample line last.

## Templates

| File | Size | Pages | Use |
| --- | --- | --- | --- |
| `brand-guidelines.html` | 11 x 8.5in landscape | 9: cover, contents, logo, clear space and size, color, type, imagery, voice, do and don't | Brand book PDF; the color page carries HEX, RGB, CMYK and Pantone slots |
| `one-pager.html` | US Letter | 1 | Sell sheet for email and office printing (white margin, no bleed) |
| `case-study.html` | US Letter | 2 | Challenge, approach, quote, results, call to action |
| `proposal-cover.html` | US Letter | 1 | Cover with reference, date, parties and confidentiality line |
| `business-card.html` | 3.5 x 2in, 0.125in bleed, crop marks | 2: front, back | Press file through WeasyPrint; the screen view shows trim and safe zone |
| `social-carousel.html` | 1080 x 1350px (4:5) | 5 frames | Hook, three points, call to action; export the PNGs |
| `capabilities-deck.html` | 1920 x 1080px (16:9) | 4: cover and 3 slides | Leave-behind PDF; rebuild in Canva or PowerPoint for an editable deck |

Shared files: `styles/tokens.css` (copy of `../../tokens/dist/tokens.css`, never edit), `styles/fonts.css` and `fonts/` (OFL fonts for both brands, license next to each family), `styles/collateral.css` (print type scale, page frame, logo mark, placeholders), `assets/brand.js` (browser preview only).

## Render

Screen PDF and PNGs (Chromium through Playwright; tagged PDF with outline, CSS page size, RGB, no bleed):

```sh
node ../../../skills/print-packaging-social/scripts/render_collateral.mjs one-pager.html --brand meridian,ember --out renders/one-pager
```

It writes `<name>-<brand>.pdf`, one PNG per page or frame and `report.json` (overflow, clipped text, single-word last lines, brand fonts loaded, axe-core summary when axe resolves). Look at every PNG. Playwright and Chromium come from your own QA environment (`PLAYWRIGHT_MODULE`, `PLAYWRIGHT_CHROMIUM`, `AXE_SCRIPT`), never from this folder.

Print master (WeasyPrint 70 as an optional external CLI; it needs Python 3.10+ and Pango):

```sh
weasyprint --pdf-variant pdf/x-4 -s print-cmyk.css business-card.html business-card-x4.pdf
python3 ../../../skills/print-packaging-social/scripts/preflight_pdf.py business-card-x4.pdf
```

`print-cmyk.css` is yours to write per job: an `@color-profile device-cmyk` rule pointing at the printer's ICC profile and `device-cmyk()` overrides for the color tokens, each marked `!important` because a `-s` stylesheet is a user stylesheet and otherwise loses to the template. Command lines, the X-1a variant and limits: [print production pipeline](../../../skills/print-packaging-social/references/print-production-pipeline.md).

In a browser, `?brand=ember` previews the other brand. For WeasyPrint, which runs no JavaScript, edit `data-brand` on `<html>`.

## Token and font wiring

1. `styles/tokens.css` must match `library/tokens/dist/tokens.css` byte for byte; `library/tests/test_collateral_templates.py` fails when it is stale. After `tokens.py build`, copy it again: `cp ../../tokens/dist/tokens.css styles/tokens.css`.
2. Templates use semantic tokens (`--color-fg-default`, `--color-accent-default`, `--color-bg-inverse`) and the accent and neutral ramps. The only literal color values are the HEX and RGB labels on the guidelines color page, and the test checks them against `tokens.resolved.json`.
3. Brand-specific text (the name in the lockup, font names on the type page) uses `.only-meridian` and `.only-ember`, hidden with `display: none` so neither the PDF text nor the accessibility tree carries the other brand.
4. The logo mark is drawn with CSS borders, not inline SVG, because WeasyPrint 70 paints inline-SVG `currentColor` as black. A real identity replaces `.mark` and the live-text wordmark with the client's outlined artwork.
5. In a client project, replace `fonts.css` and `fonts/` with the client's licensed fonts and confirm the license allows PDF embedding.

## Field names for the editable twin

Replaceable text carries `data-field="name"` (`headline`, `lede`, `stat_1`, `cta`, `email`, `person_name`). Use the same names for the fields of a Canva brand template so autofill maps one to one; see [Canva handoff](../../../skills/print-packaging-social/references/canva-handoff.md).

## Engine differences seen while building (Chromium 141, WeasyPrint 70.0)

| Behavior | Chromium (screen PDF) | WeasyPrint (print master) |
| --- | --- | --- |
| `@page` bleed and marks | Ignored; page is the trim size | TrimBox and BleedBox written; marks drawn inside the bleed in DeviceRGB |
| Variable OFL fonts | Embedded as Type 3 fonts | Embedded as CID TrueType subsets; `font-weight` ranges in `@font-face` ignored with a warning, weights still render |
| Auto margins in flex columns | Work | Ignored; the templates use grid rows instead |
| `text-wrap: balance / pretty`, `print-color-adjust` | Applied | Ignored with a warning |
| `prefers-*` media queries in tokens.css | Applied | Whole rules skipped with a warning (harmless for print) |
| Repeating gradients on image placeholders | Drawn | Not drawn |
