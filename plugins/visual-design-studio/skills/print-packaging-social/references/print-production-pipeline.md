# Print production pipeline

Version-Timestamp: 2026-10-23 20:38:00 UTC

How the kit turns a token-driven HTML layout into finished files: a screen PDF and PNGs for email, web and social, a print master for the printer, and an editable twin for the client's team. Use it with the [collateral templates](../../../library/examples/collateral/README.md). Tool facts were checked on 2026-10-23 against package registries, vendor source and a local run of WeasyPrint 70.0 and Chromium 141; re-check versions before quoting them to a client.

## Three files, three jobs

| File | Made with | Color | Goes to | It is not |
| --- | --- | --- | --- | --- |
| Screen PDF + PNGs | `scripts/render_collateral.mjs` (Playwright, Chromium) | RGB | Email, web, social, slide leave-behind | A print file: no bleed, no trim box, no output intent, variable fonts become Type 3 |
| Print master | WeasyPrint 70 CLI, `--pdf-variant pdf/x-4` (or `pdf/x-1a`) | CMYK via `device-cmyk()` and CMYK images | The printer, after preflight | A validated PDF/X: WeasyPrint writes the markers and output intent, nothing checks conformance |
| Editable twin | Canva brand template or import ([Canva handoff](canva-handoff.md)) | Canva's | The client's team for edits | The master: re-export with PDF Print settings and preflight before it goes to press |

Keep the HTML source as the master of record. When the twin and the master drift, the HTML wins unless the client signs off the Canva version.

## Defaults

| Decision | Default | Change when |
| --- | --- | --- |
| Source | A template from `library/examples/collateral/`, tokens copied from `library/tokens/dist/` | The client already has InDesign masters: match them, use this only for the screen versions |
| Page size | `@page { size: <trim>; margin: 0; }`; never include bleed in the size | Imposed or multi-up files: the printer imposes; you supply single pages |
| Bleed | `bleed: 3mm` (ISO) or `0.125in` (US); bleed art positioned with `inset: calc(-1 * var(--bleed))` | Packaging, large format, die-cuts: the converter's figure |
| Marks | `marks: none` when the printer adds its own; `marks: crop` for desktop proofs | The printer asks for marks in the file |
| Safe zone | 3-5mm (0.125-0.1875in) inside trim for text and logo | Folds, spines, perfect binding: 6mm+ |
| Color | `device-cmyk()` overrides for every color token in a per-job `print-cmyk.css` | No CMYK builds from the printer yet: send RGB only to a printer who confirms PDF/X-4 with RGB is accepted |
| Profile | The printer's ICC profile through `@color-profile device-cmyk` | Never guess: ask which profile, and do not commit vendor ICC files (their licenses are unverified) |
| Images | CMYK JPEG, 300 ppi at placed size, converted by the photographer or retoucher to the printer's profile | Large format viewed from 1m+: 100-150 ppi |
| Fonts | OFL families, embedded (WeasyPrint subsets them as CID TrueType) | Client fonts: confirm the license allows PDF embedding |
| Screen PDF | `tagged: true`, `outline: true`, `preferCSSPageSize: true`, `printBackground: true` | Archival: WeasyPrint `--pdf-variant pdf/ua-1` or `pdf/a-2b`, then veraPDF |
| Gate | `preflight_pdf.py` with no findings, then the printer's preflight and a hard proof | Never skip the proof on a first run, a new stock or a brand-critical color |

## 1. Author

1. Copy a template and its `styles/`, `fonts/` and `assets/` folders into the project. Set `data-brand` (or replace `tokens.css` with the client's built tokens).
2. Replace every `data-field` and image slot. Delete the `SAMPLE` lines last.
3. Keep text 3-5mm inside trim; extend any color or image that touches the edge into the bleed.
4. For print, write `print-cmyk.css` next to the HTML. Values come from the printer's proof or the brand's approved CMYK builds, never from a HEX conversion:

```css
/* print-cmyk.css: per job. Profile from the printer; values from an approved proof. */
@color-profile device-cmyk {
  src: url("printer-profile.icc");
  components: cyan, magenta, yellow, black;   /* comma-separated; without it WeasyPrint 70 records N=1 */
}

html[data-theme] {
  --color-accent-default: device-cmyk(C M Y K) !important;   /* replace C M Y K with 0-1 values */
  --color-fg-default: device-cmyk(0 0 0 1) !important;       /* 100K text */
  --color-bg-surface: device-cmyk(0 0 0 0) !important;
  /* ...every color token the template uses */
}
```

`!important` is needed because a `-s` stylesheet is a user stylesheet and loses to the template's author styles without it. Alternatively link the file in the HTML after `collateral.css`.

## 2. Screen PDF and PNGs

```sh
node scripts/render_collateral.mjs path/to/one-pager.html --brand meridian,ember --out renders/one-pager
python3 scripts/preflight_pdf.py --intent screen renders/one-pager/one-pager-meridian.pdf
```

Playwright resolves from `PLAYWRIGHT_MODULE` or the working folder, a browser from `PLAYWRIGHT_CHROMIUM` or Playwright's own install, axe-core from `AXE_SCRIPT`. Look at every PNG for overflow, single-word last lines, contrast and leftover sample text. The report lists the same checks, but the PNG is the evidence.

Chromium facts (Playwright `page.pdf`, checked 2026-10-23): options cover size, margins, `preferCSSPageSize`, `printBackground`, `outline` and `tagged` (default `false`). There is no option for bleed, crop marks, color space, output intent or PDF/X, and the output is RGB. Tagged output is not certified PDF/UA.

## 3. Print master with WeasyPrint

WeasyPrint 70.0 is BSD-3-Clause and needs Python 3.10+ and system Pango, so the kit treats it as an optional external command (pipx, uv or a container), never an import:

```sh
uv tool install weasyprint==70.0          # or: pipx install weasyprint==70.0
weasyprint --pdf-variant pdf/x-4 -s print-cmyk.css business-card.html business-card-x4.pdf
weasyprint --pdf-variant pdf/x-1a -s print-cmyk.css business-card.html business-card-x1a.pdf   # if the printer asks
python3 scripts/preflight_pdf.py business-card-x4.pdf
```

Observed on 2026-10-23 with WeasyPrint 70.0 and the kit's business card:

- `bleed: 0.125in` gives a 270 x 162pt MediaBox and BleedBox with a 252 x 144pt TrimBox (9pt, 3.175mm, each side).
- The output intent is written only when an `@color-profile` exists; with a 4-component profile the file reports `GTS_PDFX`, N=4.
- `device-cmyk()` colors, including through `var()`, are written as DeviceCMYK.
- `marks: crop` draws the marks inside the bleed area in DeviceRGB black, so full-bleed art covers them and a PDF/X-1a check flags RGB. With `marks: none` and CMYK overrides, the card preflights with DeviceCMYK only.
- `font-weight` ranges in `@font-face` and the `prefers-*` media queries in `tokens.css` are ignored with warnings; weights still render.

Limits from the WeasyPrint source (research 2026-10-23): the PDF/X variants set metadata and the output intent only; they do not convert content. RGB images stay DeviceRGB; only CMYK JPEGs go in as DeviceCMYK. WeasyPrint does not validate conformance.

## 4. Preflight

`scripts/preflight_pdf.py` (standard library, Python 3.9+) reports page count, MediaBox, CropBox, BleedBox and TrimBox with the bleed on each side, fonts and embedding, images with pixel size and effective ppi at the placed size (or "unknown"), color spaces (DeviceRGB, DeviceCMYK, DeviceGray, ICCBased, Separation and DeviceN names), output intents, PDF/X and PDF/A markers, tagging and outline.

| Flag | Default | Use |
| --- | --- | --- |
| `--intent print` | print | Trim, bleed, output intent, DeviceRGB and low ppi are findings |
| `--intent screen` | | Only unembedded fonts are findings; the rest are notes |
| `--min-bleed` | `3mm` (0.125in = 3.175mm passes) | `5mm` for packaging |
| `--min-ppi` | 300 | 150 for large format viewed from a distance |
| `--allow-rgb` | off | The printer confirmed RGB with a PDF/X-4 output intent |
| `--require-pdfx` | off | The printer's spec requires PDF/X |
| `--json` | off | Machine-readable report for a handoff record |

Exit 0 means no findings, 1 findings, 2 an error (not a PDF, encrypted, unreadable). A pass means the file is ready to send to the printer's preflight, not that it conforms to PDF/X.

## 5. Optional external checks

- **veraPDF** (GPLv3+ or MPLv2+, user-installed) validates PDF/A and PDF/UA. It does not validate PDF/X.
- **Ghostscript** is AGPL-3.0 or commercial. Document it, never bundle, link or wrap it in a client-facing web service: Artifex reads the AGPL to cover network access. For a one-off local conversion of an RGB-only PDF, a common pattern is `gs -dPDFX -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sColorConversionStrategy=CMYK -sOutputFile=out.pdf PDFX_def.ps in.pdf`, where `PDFX_def.ps` is edited to point at the printer's ICC profile. Verify the options against the documentation of the version you install (the current release number was unverified on 2026-10-23), then preflight the result.
- **Acrobat Preflight** or the printer's own preflight is the real PDF/X check. No free PDF/X validator was verified.

## Honest limits

- No automated, color-managed RGB-to-CMYK conversion of images in the clean pipeline. Supply CMYK images or accept the printer's conversion.
- No PDF/X validation in the kit. Markers are claims.
- Spot colors (Pantone) are not authored by the templates; the guidelines page leaves Pantone and CMYK as slots to fill from a bridge guide or press proof.
- Screen color is not press color. A hard proof on the job's paper is required before the run, and again for any brand-critical color.

## Common failures

- Chromium PDF sent to press → it has no bleed, no TrimBox and Type 3 fonts; make the master with WeasyPrint.
- `-s print-cmyk.css` without `!important` → nothing changes; preflight still shows DeviceRGB only.
- `components: cyan magenta yellow black` without commas → output intent reports N=1.
- CMYK values typed from a HEX converter → colors shift on press; use the printer's builds or a proof.
- Marks left on with full-bleed art for a PDF/X-1a job → RGB marks fail the check; set `marks: none`.
- Text at the trim edge → move it inside the 3-5mm safe zone; trimming tolerance is about 1mm.
