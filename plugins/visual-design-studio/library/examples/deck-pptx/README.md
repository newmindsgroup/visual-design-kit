# Token-driven PPTX deck

Version-Timestamp: 2026-10-23 20:10:44 UTC

A Node 22 example that turns the kit's resolved tokens into an editable 10-slide sales deck with a slide master. It writes two versions of the same deck: a PowerPoint-native one with native charts and tables, and a Canva-safe one built only from text boxes, images and simple shapes. All content is fictional placeholder copy ("Northwind Field Ops"); every slide's speaker notes say so. Replace every name, number, quote and price with approved facts before use.

Dependency: [PptxGenJS](https://www.npmjs.com/package/pptxgenjs) 4.0.1 (MIT), pinned exactly, checked with `npm view pptxgenjs version` on 2026-10-23. Nothing else is installed; the tests use Node's built-in test runner and `node:zlib`.

## Run

```sh
npm ci --ignore-scripts
npm run build          # both decks into out/ (gitignored)
npm test               # node --test: slide count, master, chart/table presence per mode, token use
```

To use it on a project, copy this folder outside the installed plugin and point it at the project's tokens.

| Option | Effect |
| --- | --- |
| *(none)* | PowerPoint-native: native column chart, native tables. Writes `out/deck-<brand>-native.pptx` |
| `--canva-safe` | Text boxes, PNG chart with editable text labels, shape-and-text grids instead of tables. Writes `out/deck-<brand>-canva-safe.pptx` and `out/chart-<brand>-metric.png` |
| `--brand=<id>` `--mode=<light\|dark\|high-contrast>` | Pick a brand and mode from the token file (default: the file's `defaultBrand` and `defaultMode`) |
| `--tokens=<file>` or `TOKENS_RESOLVED=<file>` | Read another `tokens.resolved.json` (default `../../tokens/dist/tokens.resolved.json`) |
| `--system-fonts` | Name the stack's Office-safe fallback (Arial, Georgia) instead of the brand fonts, for decks sent to machines you do not control |
| `--out=<dir>` | Output folder |

## Slides

Title, agenda, problem, solution, three-column proof, metric (chart plus headline number), case study (quote plus results), team (initials, no photos), pricing and next steps, closing. Two masters: `KIT_DARK` for title and closing, `KIT_CONTENT` with a title placeholder, footer rule, footer text and slide number.

## How tokens map to slides

Defaults live in `src/tokens.mjs` (`DECK_SCALE`). Change them there, not per slide.

| Token | Slide value | Change when |
| --- | --- | --- |
| `font.size.*` (rem) | 1rem = 16pt: body `lg` 20pt, title `3xl` 36pt, hero `5xl` 60pt, metric `5xl` x 1.5 = 90pt, caption `sm` 14pt | Decks read on laptops only (sales calls): keep. Large rooms: raise `ptPerRem` to 18-20 |
| `space.*` (rem) | 1rem = 0.2in: margin `space.12` 0.6in, gutters `space.6` 0.3in | Dense analyst decks: 0.16in per rem |
| `card.radius`, `radius.*` (px) | 96px per inch: 12px = 0.125in | |
| `color.bg.*`, `color.fg.*`, `color.accent.*`, `table.*` | HEX without `#` | Dark mode deck: `--mode=dark` |
| `font.family.display`, `font.family.body` | First family named in every text run; theme heading and body fonts set to the same | `--system-fonts` |
| `line-height.*`, `letter-spacing.*` | `lineSpacingMultiple`; tracking in points = em x font size | |

## Fonts

The default `meridian` brand names Schibsted Grotesk and Source Sans 3; `ember` names Fraunces and Figtree. All four are SIL Open Font License 1.1 families; the license files ship with the kit's collateral example (`library/examples/collateral/fonts/`). Confirm each family's license file before bundling a font (see [asset licenses](../../knowledge/ASSETS-LICENSES.md)). This example bundles no font files.

PPTX does not embed fonts reliably. PptxGenJS writes font names only, never font files. Embedding through PowerPoint's save options depends on the app version and the font's embedding permissions (verify in the target app), and a machine without the font substitutes one silently. Defaults:

- Internal decks and decks you present yourself: brand fonts, installed on every presenting machine.
- Decks sent to clients or edited by others: `--system-fonts`, or send a PDF alongside the PPTX.
- Canva: upload the brand fonts to the Canva brand kit before importing (font upload needs a paid Canva plan; verify on the current plan page).

## Open in PowerPoint, Keynote and Canva

- **PowerPoint**: open the native deck. Charts are editable (right-click, Edit Data) and tables are real tables. Check that the masters show under View > Slide Master.
- **Keynote**: open either deck. Keynote converts PPTX on import, so masters, charts and tables may shift. Not tested for this example: verify before sending a Keynote file to anyone.
- **Canva**: import the Canva-safe deck (Create a design > Import file, or the Canva connector's import tool). Per Canva Help [search summary, research 2026-10-23, https://www.canva.com/help/upload-formats-requirements/]:
  - PPTX charts, SmartArt, 3D models and WordArt are ignored on import. That is why this mode has none.
  - Limits: up to 300 slides and 300 MB per file.
  - Native tables are not listed as ignored, but their import fidelity is unverified, so the Canva-safe mode draws them as shapes and text.
- In Canva, re-check fonts, line breaks and the chart labels (they are separate text boxes over the chart image; move them with the image).

Test both versions in the target app before claiming fidelity. LibreOffice 7+ renders both decks for a quick visual check (`soffice --headless --convert-to pdf out/*.pptx`), but it is not PowerPoint, Keynote or Canva.

## Known limits

- **No SVG charts.** PptxGenJS 4.0.1 writes SVG images with a PNG fallback that it rasterizes through a browser canvas (`createSvgPngPreview` in the package source). In Node there is no canvas, so the fallback is broken. This example rasterizes the chart itself (`src/png.mjs`) and keeps the labels as text.
- **npm audit** reports a high-severity denial-of-service advisory in `image-size` 1.x, a PptxGenJS dependency (GHSA-5p2g-fcmc-qvqq, GHSA-w3rx-r6r6-pgpr). The ES module build of PptxGenJS 4.0.1 does not call it; the deck only embeds images this script generates. Re-check on each PptxGenJS upgrade and do not feed it untrusted image files.
- The native chart highlights no single bar; the Canva-safe chart highlights the latest one. Highlighting one point natively needs a second series.

## Files

- `src/build-deck.mjs`: CLI and `buildDeck()`; one block per slide.
- `src/tokens.mjs`: token loading and unit mapping.
- `src/png.mjs`: PNG encoder and bar-chart rasterizer (`node:zlib` only).
- `src/content.mjs`: the fictional placeholder copy. Replace this file first.
- `tests/deck.test.mjs`, `tests/zip.mjs`: tests and a 37-line ZIP reader.
