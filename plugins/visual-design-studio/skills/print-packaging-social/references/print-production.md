# Print production

Version-Timestamp: 2026-10-20 02:07:10 UTC

Print is unforgiving: what leaves as a PDF is what comes back on paper, multiplied by the run. Set the file up correctly at the start, design with the stock and process in mind, and preflight before every send. The printer's specification sheet overrides every value here. For the channel overview (hierarchy, structure, QA) see the atlas entry [print collateral](../../../library/atlas/channels/print-collateral.md).

## Document setup

| Setting | Default | Notes |
| --- | --- | --- |
| Page size | Trim size exactly | Never include bleed in the page size; set it as the bleed box |
| Bleed | 3mm (Europe, ISO) or 0.125in (3.175mm, US) on every trimmed edge | 5mm for large format, die-cuts or if the printer asks |
| Safe zone | 3-5mm (0.125-0.2in) inside trim | 6mm+ near folds and spines; more on the outer edge of thick saddle-stitched booklets because of creep |
| Margins for reading | 10-20mm on A4 and Letter; inside margin 3-6mm larger than outside for bound documents | |
| Folds | Roll folds: inside panels 1.5-3mm narrower than outer panels | Get a folding dummy from the printer |
| Page count | Saddle stitch in multiples of 4; perfect binding usually from about 48 pages | Spine width from the printer (sheets × caliper) |
| Grid | Columns and baseline set in the document; see the layout skill for print grids | |

## Resolution

- **Effective resolution** = image ppi ÷ scale. A 300ppi image placed at 150% is 200ppi effective.
- 300ppi effective at final size for photos in offset and quality digital print (about 2x a 150 lpi screen).
- 600-1200ppi for 1-bit line art and scanned signatures; vector for logos, type and charts.
- Large format: 100-150ppi at final size when viewed from a meter or more; billboards are often supplied at 1:10 scale at higher ppi (check the template).
- Upscaling low-resolution images does not add real detail; replace them.

## Color

- Work in RGB for photography masters, convert to CMYK at the end with the **printer's** profile and rendering intent (relative colorimetric with black point compensation is a common default; perceptual for out-of-gamut-heavy photos).
- Common output profiles:

| Region and stock | Profile | Notes |
| --- | --- | --- |
| Europe, coated sheetfed | PSO Coated v3 (FOGRA51) | Current ISO 12647-2:2013 standard; total ink 300% |
| Europe, coated (legacy) | ISO Coated v2 (FOGRA39) | Still widely requested; 330% version and a 300% variant |
| Europe, uncoated | PSO Uncoated v3 (FOGRA52) | Expect duller, darker colors |
| US, premium coated sheetfed | GRACoL 2013 (CRPC6) | Ask for the printer's ink limit |
| US, publication web offset | SWOP 2013 (CRPC5) or the publication's spec | Magazines publish their own specs |
| Japan | Japan Color 2011 Coated | |
| Newsprint | The newspaper's profile (for example ISOnewspaper26v4) | Ink limit around 240% |

- **Total area coverage (TAC):** stay under the profile or printer limit, typically 300-330% coated, 260-300% uncoated, about 240% newsprint. Excess ink causes drying problems, set-off and muddy shadows.
- **Rich black** for large solid areas: C60 M40 Y40 K100 (240%) is a common default; cool black C60 M0 Y0 K100; warm black C0 M60 Y30 K100. Never use registration black (400%).
- **100K for small text and fine lines:** body text, anything under about 12pt and lines under 1pt in 100% K only, set to overprint, so misregistration cannot create colored halos.
- **Reversed type** (white out of a color or rich black): 8pt minimum, medium weight or heavier, no fine serifs; 10pt+ on uncoated stock.
- **Minimum line weight:** 0.25pt (0.09mm) positive, 0.5pt reversed.
- **Screen tints:** avoid tints under 3-5% (they may disappear) or over 95% (may fill in).

## Overprint and knockout

- 100K black text overprints by default in most layout apps; keep it that way.
- Set white objects to knock out. A white object set to overprint disappears on press.
- Put die lines, varnish, foil and white ink on their own spot-color layers (named "Die", "SpotUV", "Foil", "White") set to overprint, so they do not knock holes in the art.
- Check with Acrobat's Output Preview (separations and overprint simulation) before sending.

## Spot colors

- Pantone Solid **Coated (C)** and **Uncoated (U)** are the same ink on different paper; U looks lighter and duller. Specify both, and approve color on the actual stock.
- Use spot colors when the brand color is outside the CMYK gamut (vivid oranges, greens, blues, purples, fluorescents, metallics), when color must match across runs and vendors, or for 1-2 color jobs where spots are cheaper than four-color.
- Each spot adds a plate and press cost in offset; digital presses usually simulate spots in CMYK (or use extended gamut such as CMYK plus orange, green and violet).
- Use the Pantone CMYK equivalent (Color Bridge) only as a simulation; tell the client it will not match the spot exactly.
- Name spot swatches exactly as the printer expects; convert unintended spots to process before export.

## Paper

Weight conversions: gsm ≈ text lb × 1.48; gsm ≈ cover lb × 2.708; gsm ≈ bond lb × 3.76.

| Use | Metric | US equivalent |
| --- | --- | --- |
| Letterhead, copier | 90-120gsm | 24-32lb bond (60-80lb text) |
| Flyers, inner pages | 115-170gsm | 80-115lb text |
| Brochure covers, posters | 200-300gsm | 75-110lb cover |
| Business cards, postcards | 350-450gsm (duplexed 600gsm+ for luxury) | 130lb cover and up, or 14-16pt caliper |

- **Coated** (gloss, silk or satin, matte): sharp detail, vivid color, lower dot gain.
- **Uncoated:** warmer, tactile, absorbs ink: higher dot gain, duller and darker colors, softer detail. Design and proof with uncoated swatches and profiles.
- **Recycled and FSC-certified** stocks are widely available; texture and tint vary, so proof.
- Grain direction affects folding and curl; ask the printer for folded pieces.

## Finishes

| Finish | Design notes |
| --- | --- |
| Lamination (gloss, matte, soft-touch) | Protects and changes feel; soft-touch scuffs and complicates recycling |
| Aqueous or UV varnish | Overall or spot; spot UV on separate layer, avoid fine detail under about 0.5mm |
| Foil (hot or cold) | Separate vector layer; fine lines and small type fill in; ask the finisher for minimums |
| Emboss and deboss | Separate layer; simple shapes and lines over about 0.5-1mm read best; affects the reverse side |
| Letterpress | Deep impression on soft cotton stock, 1-2 spot colors, no large solids |
| Die-cut | Vector path on a die layer; keep art 3mm from cuts; minimum internal radii per die maker |
| Edge painting, gilding | Thick or duplexed stock only |

## PDF/X preflight checklist

Export **PDF/X-4** (live transparency, ICC color, optional layers) unless the printer requires **PDF/X-1a** (CMYK and spot only, flattened). Then check:

1. Output intent matches the printer's profile.
2. Trim box equals the finished size; bleed box includes the full bleed on every edge.
3. Crop marks offset at least the bleed distance, so they sit outside the bleed.
4. All fonts embedded (subset is fine) or outlined; no missing glyphs.
5. Images 300ppi effective (warn under 250); no RGB or Lab left if the printer requires CMYK.
6. Total ink under the limit (Acrobat Output Preview, Total Area Coverage).
7. Black text 100K and overprinting; white objects not overprinting.
8. Only the intended spot colors exist, named correctly; die, varnish and foil on overprinting spot layers.
9. No hairlines under 0.25pt; reversed type 8pt+.
10. Page count and order match the imposition (multiples of 4 for saddle stitch).
11. No transparency or blend issues in overprint preview; no low-resolution placeholders.
12. Run Acrobat Preflight with the printer's profile (or Enfocus PitStop), then reopen the PDF and view every page at 100%.

## Proofing

- **Soft proof** on a calibrated display using the output profile and paper simulation.
- **Contract proof** (calibrated inkjet to FOGRA or GRACoL with a control strip) for color-critical jobs; this is what the press matches.
- **Press check** for brand-critical or high-run jobs.
- **Physical dummy** for folds, binding, die-cuts and finishes.

## Common sizes

| Format | Size |
| --- | --- |
| A0 / A1 / A2 / A3 | 841x1189 / 594x841 / 420x594 / 297x420mm |
| A4 / A5 / A6 | 210x297 / 148x210 / 105x148mm |
| DL flyer (1/3 A4) | 99x210mm (DL envelope 110x220mm) |
| B1 / B2 (ISO) | 707x1000 / 500x707mm |
| US Letter / Legal / Tabloid (Ledger) | 8.5x11 / 8.5x14 / 11x17in (215.9x279.4 / 215.9x355.6 / 279.4x431.8mm) |
| US Half Letter | 5.5x8.5in |
| Business card US and Canada | 3.5x2in (88.9x50.8mm) |
| Business card Europe and UK | 85x55mm |
| Business card Japan / China / Australia | 91x55 / 90x54 / 90x55mm |
| Postcard US | 4x6in; USPS postcard rate allows 3.5x5 to 4.25x6in (verify current USPS rules) |
| Postcard Europe | A6 105x148mm |
| Posters US | 11x17, 18x24, 24x36in; 27x40in film one-sheet |
| Posters Europe | A2, A1, A0; 50x70cm and 70x100cm |
| Roll-up banner | 850x2000mm common (check the stand) |

## Typography for print

- Body 9-11pt for reading documents; 12pt+ for older audiences and public information.
- Legal and fine print 6-7pt minimum, never reversed.
- Avoid text over busy photography; if necessary, use a scrim or a solid panel.
- QR codes: at least 20x20mm for close scanning, roughly 1/10 of the expected scanning distance as a rule of thumb, with a 4-module quiet zone, dark on light, and a short URL printed beside it.

## Common failures

- Bleed missing or only on some edges → bleed box on all trimmed edges, backgrounds extended.
- Text in the trim danger zone → safe zone respected.
- Colors approved on screen only → contract proof on the real stock.
- 400% black backgrounds → rich black recipe under the ink limit.
- Thin serif text reversed out of a four-color image → bolder sans, larger size, or a solid panel.
- Placed PDFs carrying RGB and stray spots → convert or remove before export.
