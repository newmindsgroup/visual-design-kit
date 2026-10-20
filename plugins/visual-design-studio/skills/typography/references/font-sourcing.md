# Font sourcing, licensing and loading

Version-Timestamp: 2026-10-20 02:07:10 UTC

A font is software with a license. Confirm the license for every use before a client sees the work, then load the files so text appears fast and does not jump.

## License types

| License | Typical source | Allows | Watch for |
| --- | --- | --- | --- |
| SIL Open Font License 1.1 (OFL) | Google Fonts, Velvetyne, The League of Moveable Type, many foundry libre releases | Use in any project including commercial, embed in web, apps and PDFs, modify, redistribute with the license | Cannot sell the font file on its own; a modified version must not use a Reserved Font Name; ship `OFL.txt` with the files |
| Apache 2.0 | Some Google Fonts (for example Permanent Marker) | Similar freedoms to OFL | Keep the license and notices |
| Ubuntu Font Licence | Ubuntu family | Use and redistribute | Modified versions must be renamed |
| Free-for-commercial proprietary (for example the ITF Free Font License used by Fontshare) | Fontshare and similar | Free use under the terms | Not open source; redistribution and modification are restricted; read the full license |
| Commercial EULA | Foundries and resellers | What you buy: desktop seats, web (by monthly pageviews or domains), app embedding, ePub, broadcast and video, server or dynamic generation | Each use is a separate license; logo use and trademark registration can need an extended license; variable fonts are sometimes priced separately |
| Subscription (for example Adobe Fonts) | Adobe Fonts | Desktop use and web use through the provider's hosted kits while subscribed | Self-hosting the files is not allowed; check app embedding and client handover terms before using it for a client brand |

Rules:

- A free download is not a license. Read the license file inside the exact package you ship.
- Client brands need fonts the client can license themselves. Record who holds each license.
- Using a font to draw a logo is allowed under OFL and most desktop EULAs; outlining type for a logo does not remove the need to license the font for the designer's desktop use.
- Server-side image generation (social cards, PDFs, OG images) is "server use" in many commercial EULAs. OFL allows it.

## Where to find type

- **Open and libre:** Google Fonts and its GitHub repository (`github.com/google/fonts`), Fontsource (npm packages of open fonts), Velvetyne, Collletttivo, The League of Moveable Type, Omnibus-Type, Production Type's libre releases (Newsreader, Spectral), Adobe's open families (Source Serif, Source Sans, Source Code, Source Han), IBM Plex.
- **Commercial foundries:** Klim Type Foundry, Commercial Type, Grilli Type, Dinamo, Colophon, Sharp Type, Pangram Pangram, Displaay, Production Type, Hoefler&Co., Monotype (Linotype, ITC, Fontsmith), Swiss Typefaces, Lineto, OH no Type Co, Darden Studio.
- **Multiscript specialists:** Rosetta Type, Typotheque, TypeTogether, Indian Type Foundry, and the Noto project for open coverage. See [multiscript](multiscript.md).

## Self-host Google Fonts

Self-host instead of linking `fonts.googleapis.com`:

- **Privacy:** loading fonts from Google's servers sends each visitor's IP address to Google. In January 2022 the Munich Regional Court (LG München I, 3 O 17493/20) held that doing so without consent violated the GDPR and awarded damages to the visitor. EU and UK sites should self-host. Confirm requirements with counsel for the specific product and jurisdiction.
- **Performance:** browsers partition their caches per site, so a shared CDN gives no cross-site cache benefit; a third-party origin adds a connection.
- **China:** Google services are generally unreachable from mainland China; self-host on infrastructure that serves the market.

How:

1. Download the family from the Google Fonts repository or a Fontsource package (`npm install @fontsource-variable/<family>`), keeping `OFL.txt`.
2. Convert or subset to woff2 (below), place files in `/fonts/`, write `@font-face` rules.
3. Commit `OFL.txt` next to the files.

## Subsetting

Ship only the characters and features the content needs.

```sh
pip install fonttools brotli
pyftsubset Fraunces.ttf \
  --output-file=fraunces-latin.woff2 --flavor=woff2 \
  --layout-features='kern,liga,calt,case,lnum,onum,tnum,pnum,frac,ss01' \
  --unicodes='U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD'
```

- The unicode list above is the common "Latin" range Google Fonts uses. Add Latin Extended (`U+0100-024F`, `U+1E00-1EFF`) for Central European and Vietnamese text.
- Keep layout features needed for shaping. Never strip features from Arabic, Indic or other complex scripts; subset by script, not by glyph list.
- Split files with `unicode-range` so the browser downloads a subset only when a page uses it.
- Commercial EULAs differ on whether subsetting counts as modification; most web licenses allow it. Check.

## Formats and budget

- Serve woff2 only. Every current browser supports it; woff and ttf fallbacks add bytes for no users.
- A common budget for the first view: 2-4 font files, under about 150 KB of woff2 in total. Latin text families subset to 20-50 KB per style. CJK fonts are megabytes and need the strategies in [multiscript](multiscript.md).
- Load only weights and styles in use. One variable file usually beats 3+ static files; 1-2 statics can be smaller than a variable file.

## @font-face and font-display

```css
@font-face {
  font-family: "Fraunces";
  src: url("/fonts/fraunces-latin.woff2") format("woff2");
  font-weight: 100 900;            /* variable range */
  font-style: normal;
  font-display: swap;
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+2000-206F, U+20AC, U+2122, U+2212;
}
```

| `font-display` | Behavior | Use |
| --- | --- | --- |
| `swap` | Fallback text immediately, swaps when the font arrives | Brand text and headings, with a metric-matched fallback so the swap does not shift layout |
| `fallback` | About 100ms invisible, then fallback; swaps only if the font arrives within about 3s | Body text on slower audiences |
| `optional` | About 100ms invisible; uses the font only if already available, otherwise keeps the fallback for this page view | Performance-first pages and `audience.low-bandwidth-entry-devices`; best Cumulative Layout Shift |
| `block` | Up to about 3s invisible text | Avoid; only icon fonts, which you should replace with SVG |

## Preload

Preload the 1-2 files used above the fold, never every weight:

```html
<link rel="preload" href="/fonts/fraunces-latin.woff2" as="font" type="font/woff2" crossorigin>
```

`crossorigin` is required even for same-origin fonts; without it the browser downloads the file twice.

## Fallback metrics: stop the layout shift

Make the fallback font occupy the same space as the web font with `size-adjust` and the metric override descriptors.

```css
@font-face {
  font-family: "Fraunces Fallback";
  src: local("Georgia");
  size-adjust: 105%;          /* example values: compute for your exact pair */
  ascent-override: 92%;
  descent-override: 24%;
  line-gap-override: 0%;
}
:root { --font-family-display: "Fraunces", "Fraunces Fallback", Georgia, serif; }
```

How to get the numbers:

- `size-adjust` = web font average character width / fallback average character width (both normalized to their em).
- `ascent-override` = web font ascender / units per em / size-adjust. Same for descender and line gap.
- Tools compute this from the font files: Fontaine and Capsize (open source), and framework font loaders such as `next/font`, which generate the fallback automatically.
- Verify: block the font request in DevTools and compare screenshots; line breaks should barely move.

## Fallback stacks

- System UI: `system-ui, -apple-system, "Segoe UI", Roboto, "Noto Sans", "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";`
- Serif: `"Iowan Old Style", "Palatino Linotype", Palatino, Georgia, "Noto Serif", serif;`
- Mono: `ui-monospace, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;`
- Map the brand stacks to the tokens `--font-family-display`, `--font-family-body` and `--font-family-mono`.

## Other destinations

- **iOS:** add font files to the app bundle and list them under `UIAppFonts` in Info.plist; scale custom fonts with `UIFontMetrics` so Dynamic Type still works.
- **Android:** place files in `res/font/` or use downloadable fonts; set sizes in sp.
- **Email:** custom web fonts render in Apple Mail and some other clients but not in Gmail or most Outlook versions; always design the fallback and test it.
- **PDF:** embed fonts (OFL allows it); check commercial EULAs for embedding rules.
- **Figma:** use the organization's shared fonts or local fonts; record exact family and version in handoff.

## Sourcing checklist

- License file present for every family, and the license covers every planned use.
- Self-hosted woff2, subset to required languages, total under budget.
- `font-display` chosen per role; 1-2 preloads with `crossorigin`.
- Metric-matched fallback; layout shift checked with fonts blocked.
- Exact family, version, weights and source recorded in handoff (the `design-system` skill holds token builds).
