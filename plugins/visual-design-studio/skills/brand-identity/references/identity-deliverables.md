# Identity deliverables by tier

Version-Timestamp: 2026-10-23 20:10:44 UTC

What to hand over at the end of an identity project, scaled to the client. Pick the tier from the client's size and channel mix, then add or drop rows for what the brief actually needs. Every file must open, be named by the convention below, and be listed in the handoff readme.

## Choose the tier

| Tier | Typical client | Default package | Move up when |
| --- | --- | --- | --- |
| Startup | Under 50 people, one product, digital-first | Logo pack, palette, type, quick reference, 24-32 page book, 6-10 templates | Physical retail, packaging or signage is planned in the next year |
| Mid-market | 50-1,000 people, several channels, an in-house marketer or small team | Startup package plus print specs, full book, Canva editable twin, 15-30 templates, motion logo | Several regions, sub-brands or outside agencies produce work |
| Enterprise or rebrand | Multiple brands or regions, agencies, a migration from an old identity | Mid-market package plus brand architecture, portal, channel playbooks, migration plan, sonic logo, training | |

## Checklist

`S` = startup, `M` = mid-market, `E` = enterprise or rebrand. A mark means included by default.

### Logo

| Deliverable | Formats | S | M | E |
| --- | --- | --- | --- | --- |
| Primary, horizontal, stacked and symbol lockups | SVG, PDF, PNG @1x/2x/3x | x | x | x |
| Color versions: full color, black, white, on brand color | Same, per lockup | x | x | x |
| Print versions in CMYK and spot | PDF/X-4 (CMYK), PDF with spot colors | | x | x |
| Favicon and app icon set | `favicon.ico`, `icon.svg`, 180 px touch icon, 192 and 512 px manifest icons, 1024 px app icon master | x | x | x |
| Social avatars and covers | PNG at each platform's current size | x | x | x |
| Native master files | AI, Figma or Affinity with construction layers | x | x | x |
| EPS | Only on a vendor's request | | | |
| Co-brand and sub-brand lockups | SVG, PDF, PNG | | | x |

File specs per format: [logo deliverable file set](logo-design.md#deliverable-file-set).

### Color, type and graphic elements

| Deliverable | Formats | S | M | E |
| --- | --- | --- | --- | --- |
| Design tokens | DTCG JSON plus CSS variables (the kit's token pipeline) | x | x | x |
| Color spec sheet: HEX, RGB, CMYK coated and uncoated, Pantone C and U | PDF, one page | x | x | x |
| Print spec data with ICC profile, proof date and approver | CSV or JSON next to the tokens | | x | x |
| RAL or NCS for signage | Added to the spec sheet | | | x |
| Font list with licenses and download sources; font files only where the license allows redistribution (OFL files with `OFL.txt`) | Readme, license files | x | x | x |
| Graphic device and patterns | SVG, PDF, PNG tiles | x | x | x |
| Icon set (one family, licensed) | SVG, plus the license notices | | x | x |
| Photography and illustration library with provenance records | JPG or PNG, `licenses/` folder | | x | x |

### Guidelines and templates

| Deliverable | Formats | S | M | E |
| --- | --- | --- | --- | --- |
| Quick reference | 1-2 page PDF and PNG | x | x | x |
| Brand book | Screen PDF; print master PDF/X-4 when printed. See [brand book production](brand-book-production.md) | x | x | x |
| Editable twin of the book and templates | Canva (or Figma) shared with editors | | x | x |
| Presentation master | PPTX (editable, token-driven; see the [deck example](../../../library/examples/deck-pptx/README.md)), Google Slides or Keynote on request, Canva twin | x | x | x |
| Stationery: business card, letterhead, compliments slip | Print PDF/X-4 with bleed and crop marks; DOCX letterhead | x | x | x |
| Email signature | HTML plus a 2x PNG logo hosted by the client | x | x | x |
| Social templates: feed 1080x1350, story 1080x1920, link preview 1200x630 | Canva templates, PNG examples | x | x | x |
| Document templates: report, one-pager, proposal | DOCX or Google Docs, Canva | | x | x |
| Signage, packaging, merchandise specs | PDF with dimensions and materials | | x | x |
| AI handoff file | Markdown plus tokens; see [guidelines](guidelines.md#ai-handoff-file) | | x | x |
| Brand portal | Web portal with downloads and changelog | | | x |
| Channel playbooks | PDF or portal sections, 10-30 pages each | | | x |

### Motion, sound and rollout

| Deliverable | Formats | S | M | E |
| --- | --- | --- | --- | --- |
| Logo animation | Lottie JSON plus MP4 (H.264) and a reduced-motion still; 1.5-3 s | | x | x |
| Video end card and lower third | MP4 or MOV with alpha, plus source | | | x |
| Sonic logo | WAV 48 kHz 24-bit plus MP3, with provenance record | | | x |
| Migration plan and asset inventory | Spreadsheet: touchpoint, owner, priority, replace-by date | | | x |
| Training session and recording | Slides plus a 30-60 min recording | | x | x |

## Naming and folders

File names: `brand-asset-[variant]-[color]-[space].[ext]`, all lowercase, hyphens, no spaces, the same pattern as the logo file set. Examples:

- `ledgerly-logo-horizontal-fullcolor-rgb.svg`
- `ledgerly-symbol-white-cmyk.pdf`
- `ledgerly-businesscard-front-cmyk-bleed3mm.pdf`
- `ledgerly-guidelines-v1.2-screen.pdf`, `ledgerly-guidelines-v1.2-print.pdf`
- `ledgerly-deck-master-v1.0.pptx`

Color space tag: `rgb` for screen, `cmyk` for process print, `spot` for Pantone, `mono` for single-color art. Size tag for raster: `@2x` or the pixel width (`-1000w`).

Folder tree, one per version:

```text
ledgerly-brand-v1.0/
  README.md            # what is inside, fonts and licenses, contacts, version and date
  01-logo/             # svg/ pdf/ png/ favicon/ app-icon/ social/ source/
  02-color/            # spec sheet, tokens, print spec data
  03-type/             # font list, license files, OFL font files where allowed
  04-graphics/         # device, patterns, icons
  05-imagery/          # library and licenses/
  06-templates/        # deck, stationery, social, documents (with Canva links in README)
  07-guidelines/       # quick reference, book screen and print PDFs
  08-motion-sound/     # Lottie, MP4, sonic logo
  licenses/            # one license file per third-party asset plus the provenance record
```

## Handoff checks

- Open every file in a different app than the one that exported it.
- Vector logos: text outlined, no hidden layers or stray points, artboard trimmed to the art (clear space is a rule in the book, not padding in the file).
- PDFs for print: PDF/X-4, fonts embedded or outlined, bleed present where required, spot colors named as in the spec sheet.
- PNGs: transparent where they should be, sRGB, no color profile surprises in Office.
- Templates: give one to someone outside the project and have them make one piece without help.
- Licenses: every third-party asset has a provenance record and a saved license file ([asset licenses](../../../library/knowledge/ASSETS-LICENSES.md)).
- README lists the version, date, owner and the approver of each section.

## Common failures

- Logo pack with only PNGs → vector SVG and PDF for every lockup.
- Font files shipped without the right to redistribute them → ship the license record and download source instead.
- Canva templates handed over without the print master → print always comes from the PDF/X master.
- Different names for the same lockup in the book and the files → name lockups once and use the name everywhere.
- Enterprise rebrand without a migration inventory → old assets stay live for years.
