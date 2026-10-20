# Setting type: micro-typography

Version-Timestamp: 2026-10-20 02:07:10 UTC

Good setting is invisible: correct characters, even texture, clean line endings. Check every item below on rendered output, not in the CSS.

## Rag, line endings, widows and orphans

- Default alignment is flush-left, ragged-right. It reads best on screens and for dyslexic readers. Center only short, display-size text (up to 3 lines).
- Justify only with at least 50-60ch measure, hyphenation on, and a font with good spacing; otherwise rivers appear. Never justify narrow mobile columns.
- **Rag shaping:** avoid a stair-step or a deep notch every other line. Fix by adjusting measure or editing copy, not by squeezing tracking.
- **Headings:** no single-word last line. Use `text-wrap: balance` first; for a stubborn case, join the last two words with a no-break space (`&nbsp;`) only when both are short. Long no-break chains overflow on phones.
- **Paragraphs:** `text-wrap: pretty` reduces short last lines. It is a progressive enhancement (supported in Chromium and Safari as of 2026; verify others).
- **Balance limits:** browsers balance only short blocks (Chromium caps at 6 lines), so use it on headings, captions and pull quotes, not body text.
- **Print and PDF:** set `widows: 2; orphans: 2;` for paged CSS, keep headings with the following paragraph (`break-after: avoid`), and inspect every page. In InDesign use Keep Options and the balance ragged lines option on headings.

```css
h1, h2, h3, .card-title, figcaption { text-wrap: balance; }
p, li, dd { text-wrap: pretty; }
@media print { p { widows: 2; orphans: 2; } h2, h3 { break-after: avoid; } }
```

## Hyphenation and long strings

- `hyphens: auto` works only when the element (or an ancestor) has a correct `lang` attribute; the browser uses that language's dictionary.
- Limit it: `hyphenate-limit-chars: 6 3 2;` (words of 6+ letters, at least 3 before and 2 after the break).
- Never hyphenate headings, brand names, product names, URLs, code or numbers.
- Long URLs and IDs: `overflow-wrap: anywhere;` on the containing element so they wrap instead of overflowing.
- German, Dutch and Finnish have long compounds; turn hyphenation on for their body text even when English stays ragged without it.

```css
article { hyphens: auto; hyphenate-limit-chars: 6 3 2; }
h1, h2, h3, a[href^="http"], code { hyphens: manual; }
.break-anywhere { overflow-wrap: anywhere; }
```

## Quotes, apostrophes, dashes, primes and symbols

| Write | Not | Unicode | Use |
| --- | --- | --- | --- |
| “double” ‘single’ | "straight" 'quotes' | U+201C/U+201D, U+2018/U+2019 | English quotes |
| don’t, ’90s | don't, '90s | U+2019 | Apostrophe (the closing single quote, also before decades) |
| 10–20, Mon–Fri | 10-20 | U+2013 en dash | Ranges, connections |
| a pause—like this | a pause--like this | U+2014 em dash | US style, closed up; UK style uses a spaced en dash ( – ) |
| −12 °C, −4.5% | -12 | U+2212 minus | Negative numbers in data and finance |
| 1920 × 1080 | 1920 x 1080 | U+00D7 | Dimensions, multiplication |
| 6′ 2″, 4′ 33″ | 6' 2" | U+2032, U+2033 | Feet and inches, minutes and seconds |
| … | ... | U+2026 | Ellipsis |
| © ® ™ | (c) (r) | U+00A9, U+00AE, U+2122 | Set ® and ™ smaller or superscript in display sizes |

Language conventions: German „so“ and »so«, French « ainsi » with narrow no-break spaces (U+202F) inside the guillemets and before `; : ! ?`, Spanish ¿ ¡ at the start, Japanese 「」 and 『』, Chinese “” or 「」 by region. Set the CSS `quotes` property per `:lang()` when quotes come from `<q>`.

## Numerals

| Feature | CSS | Use |
| --- | --- | --- |
| Lining figures | `font-variant-numeric: lining-nums;` | UI, headings, all-caps settings |
| Oldstyle figures | `font-variant-numeric: oldstyle-nums;` | Running text in serif long-form, so numbers sit like lowercase |
| Tabular figures | `font-variant-numeric: tabular-nums;` | Tables, prices in columns, timers, counters, charts (no jitter when values change) |
| Proportional figures | `font-variant-numeric: proportional-nums;` | Prose and large display numbers |
| Slashed zero | `font-variant-numeric: slashed-zero;` | Codes, IDs, coupons, anything a person types back |
| Fractions | `font-variant-numeric: diagonal-fractions;` | Recipes, measurements |
| Ordinals | `font-variant-numeric: ordinal;` | 1st, 2nd where the font supports `ordn` |

Right-align numeric table columns and align on the decimal. Keep the same number of decimals within a column.

## Small caps and all caps

- Real small caps come from the font's `smcp` and `c2sc` features: `font-variant-caps: all-small-caps;` for acronyms in running text (NASA, UNESCO) so they do not shout. Add `font-synthesis-small-caps: none` (or `font-synthesis: none`) to prevent fake, scaled-down capitals.
- All-caps labels: +0.05 to +0.12em tracking (`--letter-spacing-caps`), line-height about 1.2, and the `case` feature so hyphens, brackets and colons rise to cap height: `font-feature-settings: "case" 1;`.
- Keep all caps to labels, overlines, buttons and short headings. Never set paragraphs in caps.
- Type the source text in sentence case and apply `text-transform: uppercase`. Copy-paste, translation and some screen readers handle it better than typed capitals.

## OpenType features in CSS

Prefer the high-level properties; they compose. Use `font-feature-settings` only for stylistic sets and character variants, and declare every feature you need in one declaration because it does not merge with inherited values.

| Need | High-level property | Low-level tag |
| --- | --- | --- |
| Kerning | `font-kerning: normal` | `kern` |
| Standard ligatures | `font-variant-ligatures: common-ligatures` | `liga`, `clig` |
| Discretionary ligatures (display only) | `font-variant-ligatures: discretionary-ligatures` | `dlig` |
| Contextual alternates | `font-variant-ligatures: contextual` | `calt` |
| Superscript, subscript | `font-variant-position: super` | `sups`, `subs` |
| Case-sensitive forms | none | `case` |
| Stylistic set | `font-variant-alternates` with `@font-feature-values` | `ss01` to `ss20` |
| Character variant | none | `cv01` to `cv99` |
| Swashes | `font-variant-alternates: swash(name)` | `swsh` |

```css
:root { --features: "ss01" 1, "cv11" 1; }      /* document which glyph each one changes */
.brand-text { font-feature-settings: var(--features); }
.table-num { font-variant-numeric: tabular-nums lining-nums slashed-zero; }
```

Check that the font actually has a feature before relying on it: render a test string and compare it with the feature on and off.

## Optical sizes and variable fonts

- Optical sizing adjusts stroke contrast, spacing and x-height for the size in use. Browsers apply the `opsz` axis automatically (`font-optical-sizing: auto` is the default). Families with `opsz`: Fraunces, Newsreader, Literata, Source Serif 4, Bodoni Moda, Bricolage Grotesque, Roboto Flex, Inter (version 4+).
- Declare ranges in `@font-face` so the browser knows the file covers them: `font-weight: 100 900; font-stretch: 75% 125%;`.
- Set registered axes with normal properties (`font-weight`, `font-stretch`, `font-style`); use `font-variation-settings` only for custom axes such as Fraunces `SOFT` and `WONK` or Roboto Flex `GRAD`.
- A grade axis (`GRAD`) changes stroke weight without changing width, so dark mode and hover states can thicken or thin text without reflow.
- A variable file is not automatically smaller: one variable file usually beats 3+ static weights, but 1-2 static weights can be lighter. Compare byte sizes.

```css
.display { font-variation-settings: "SOFT" 100, "WONK" 0; font-weight: 650; }
@media (prefers-color-scheme: dark) { body { font-variation-settings: "GRAD" -25; } }  /* only if the font has GRAD */
```

## Kerning and spacing

- Leave kerning on (`font-kerning: normal`). Text sizes use the font's metric kerning.
- Display headlines and wordmarks need optical review: check pairs such as AV, To, Ty, LT, r., f) and quotes next to capitals. Fix with local `letter-spacing` on spans in code, or optical kerning in design tools, and only at display sizes.
- Word spacing matters in condensed display type: if words run together at tight tracking, add `word-spacing: 0.05em`.
- Paragraph separation: either a first-line indent of 1em with no space between paragraphs (books, long reports) or a space of 0.75-1em with no indent (screens). Never both.

## Hanging punctuation and optical margins

- `hanging-punctuation: first allow-end last;` hangs opening quotes and bullets into the margin, but only Safari supports it as of 2026. Fallback for pull quotes: `text-indent: -0.45em` on the quote paragraph (tune per font).
- Print: turn on Optical Margin Alignment in InDesign for body text and pull quotes.
- Bulleted lists: hang the bullet so text aligns with the paragraph edge above.

## Links and underlines

```css
a { text-decoration-thickness: 0.08em; text-underline-offset: 0.18em; text-decoration-skip-ink: auto; }
```

Keep underlines on links in body text; color alone does not identify a link (WCAG 2.2 SC 1.4.1).

## Rendering notes

- Light text on dark backgrounds looks heavier on macOS. `-webkit-font-smoothing: antialiased;` thins it, on macOS only; apply it to dark surfaces, not globally.
- Do not use `text-rendering: optimizeLegibility` globally; it can slow long pages on some platforms and kerning is already on by default.

## Setting checklist

- Curly quotes and apostrophes, real dashes, minus signs and multiplication signs.
- Tabular figures in every column of numbers and every changing number.
- No faux bold, italic or small caps (`font-synthesis: none`).
- Headings balanced, no single-word last lines, no stranded headings at page bottoms.
- Hyphenation only where `lang` is set and never in headings.
- Caps labels tracked and using `case`.
- Features verified by rendering with the shipped font file.
