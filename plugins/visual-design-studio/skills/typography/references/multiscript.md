# Multiscript and RTL typography

Version-Timestamp: 2026-10-20 02:07:10 UTC

Each script has its own structure, rhythm and conventions. Choose a family per script, size scripts to look equal rather than measure equal, and never carry Latin habits (tracking, italics, all caps) into scripts that do not use them. Every family named here is OFL unless marked; confirm the shipped version's license.

## Principles

1. **One font does not cover the world.** Noto is a project of per-script families (Noto Sans JP, Noto Sans Arabic, Noto Sans Devanagari...). List the scripts first, then choose families.
2. **Match visual size, not font-size.** Arabic, Devanagari and Thai look smaller than Latin at the same px; CJK looks larger and denser. Adjust per script.
3. **More line-height for tall marks.** Stacked vowels, tone marks and matras need 1.6-1.9.
4. **No tracking on connected or ideographic scripts** unless a native typographer asks for it.
5. **No synthetic italics.** CJK, Arabic, Hebrew and Indic scripts have no true italic tradition; emphasize with weight, color or script-specific marks.
6. **Set `lang` on every element whose language differs.** Hyphenation, line breaking, quotes, font selection (`:lang()`) and screen readers depend on it.
7. **Native-speaker review** of shaping, line breaks and tone is required before launch. A specimen that renders is not a validated one.

## Families and adjustments by script

Body size is relative to a 16px Latin body. Atlas market entries hold the local conventions; read them with `python3 ../../../library/scripts/atlas.py show <id>`.

| Script | Sans / Gothic | Serif / traditional | Size vs Latin | Line-height | Atlas market |
| --- | --- | --- | --- | --- | --- |
| Japanese | Noto Sans JP, M PLUS 1p, M PLUS 2, Zen Kaku Gothic New, BIZ UDPGothic | Noto Serif JP, Zen Old Mincho, Shippori Mincho | 16px body (same px; looks larger) | 1.7-1.9 | `market.japan` |
| Chinese, Simplified | Noto Sans SC (Source Han Sans), system PingFang SC / Microsoft YaHei | Noto Serif SC; LXGW WenKai (kai-style, OFL on GitHub) | 14-16px body | 1.6-1.8 | `market.china-mainland` |
| Chinese, Traditional | Noto Sans TC | Noto Serif TC, LXGW WenKai TC | 15-16px | 1.7-1.8 | none in the atlas yet |
| Korean | Pretendard (OFL, GitHub), Noto Sans KR, IBM Plex Sans KR, Nanum Gothic, Gowun Dodum | Noto Serif KR, Nanum Myeongjo, Gowun Batang | 15-16px | 1.6-1.7 | `market.korea` |
| Arabic | Noto Sans Arabic, IBM Plex Sans Arabic, Cairo, Tajawal, Readex Pro, Almarai, Vazirmatn (Persian focus) | Noto Naskh Arabic, Amiri; Noto Kufi Arabic for display | +10-20% (17-19px) | 1.6-1.9 | `market.middle-east-north-africa-arabic` |
| Hebrew | Heebo, Assistant, Rubik, IBM Plex Sans Hebrew, Noto Sans Hebrew | Frank Ruhl Libre, Noto Serif Hebrew | +5-10% | 1.5-1.6; 1.7+ with niqqud | `market.israel-hebrew` |
| Devanagari (Hindi, Marathi, Nepali) | Noto Sans Devanagari, Mukta, Hind, Poppins (includes Devanagari) | Noto Serif Devanagari, Tiro Devanagari Hindi, Martel | +10-15% | 1.6-1.8 | `market.india-south-asia` |
| Bengali, Tamil, Telugu, Gujarati, Gurmukhi, Kannada, Malayalam | Noto Sans Bengali / Tamil / Telugu / Gujarati / Gurmukhi / Kannada / Malayalam | Noto Serif equivalents | +10-15% | 1.6-1.9 | `market.india-south-asia` |
| Thai | Noto Sans Thai (loopless), IBM Plex Sans Thai, Prompt, Kanit, Anuphan | Noto Sans Thai Looped, Sarabun (looped, formal and long text) | +10-15% | 1.6-1.8 | `market.southeast-asia` |
| Khmer, Lao, Myanmar | Noto Sans Khmer / Lao / Myanmar | Noto Serif equivalents | +10-20% | 1.8-2.0 (Myanmar is very tall) | `market.southeast-asia` |
| Vietnamese (Latin with stacked diacritics) | Families with full Vietnamese support: Noto Sans, Source Sans 3, IBM Plex Sans, Inter | Noto Serif, Source Serif 4 | same | 1.5+ | `market.southeast-asia` |
| Cyrillic, Greek | Noto Sans, Source Sans 3, IBM Plex Sans, Inter, Manrope, Rubik | Noto Serif, Source Serif 4, Literata | same | same as Latin | none in the atlas yet |
| Ethiopic (Amharic, Tigrinya) | Noto Sans Ethiopic | Noto Serif Ethiopic | +10% | 1.6-1.8 | `market.sub-saharan-africa` |

## CJK specifics

- **Measure:** 30-40 full-width characters per line for body text.
- **Spacing:** keep body tracking at 0 (Japanese web often uses 0 to +0.05em). Tighten headings with proportional alternates: `font-feature-settings: "palt" 1;`.
- **Punctuation and spacing between scripts:** `text-spacing-trim` trims full-width punctuation and `text-autospace` adds space between ideographs and Latin or numbers; both are newer properties (Chromium as of 2026; verify others). Otherwise insert a thin space manually only in display text.
- **Line breaking:** Japanese line-start and line-end rules (kinsoku) prevent closing brackets and small kana from starting a line: `line-break: strict;`. Korean breaks by word: `word-break: keep-all;` so words stay whole.
- **Emphasis:** bold, color, or emphasis dots: `text-emphasis: filled sesame;` (Japanese) or `text-emphasis: dot;` (Chinese). Never italics.
- **Vertical text:** `writing-mode: vertical-rl;` for Japanese and Traditional Chinese editorial, with `text-combine-upright: all;` for 2-digit numbers.
- **Ruby:** `<ruby>漢字<rt>かんじ</rt></ruby>` for Japanese furigana and Chinese pinyin annotations.
- **Font weight of files:** a full CJK family is several MB per weight. Options: rely on system fonts (PingFang, Hiragino, Yu Gothic, Microsoft YaHei, Apple SD Gothic Neo, Malgun Gothic) with a web font only for headings; use services or builds that slice the font into many `unicode-range` files; or subset to the exact characters for fixed display text.

## Arabic specifics

- Never letter-space Arabic; it breaks the joins between letters. Justification uses kashida (tatweel) elongation, which the renderer or font applies; do not insert tatweel characters by hand in UI text.
- No italics or all-caps equivalents; emphasize with weight, size or color.
- Diacritics (harakat) need line-height 1.8+ in educational and religious text.
- Numerals: Western Arabic digits (0-9) are standard in the Maghreb and common across the Gulf in digital products; Eastern Arabic digits (٠-٩) are common in Egypt, the Levant and the Gulf in print and formal contexts. Persian and Urdu use their own Extended Arabic-Indic digits. Pick per market (confirm in the market entry and with native reviewers) and keep one system per surface.
- Pair Arabic with a Latin face of similar weight and color: IBM Plex Sans Arabic with IBM Plex Sans, Noto Sans Arabic with Noto Sans, Readex Pro with Lexend.

## Indic and Thai specifics

- Devanagari words hang from the headline (shirorekha); check that conjuncts and matras shape correctly in the exact font and renderer. Missing shaping shows as dotted circles.
- Do not stretch, track or synthesize bold. Mixed Hindi and English is common; match the Latin weight to the Devanagari weight.
- Thai has no spaces between words; browsers break lines with dictionaries. Never insert line breaks by character count. Prefer looped Thai faces for long and formal reading, loopless for headlines and modern brands.

## RTL layout (Arabic, Hebrew, Persian, Urdu)

- Set `<html lang="ar" dir="rtl">` (or `he`, `fa`, `ur`). Use logical CSS: `margin-inline-start`, `padding-inline-end`, `inset-inline-start`, `text-align: start`, `border-start-start-radius`.
- Mirror: navigation order, back and forward arrows, progress direction, sliders, carousels, breadcrumbs, icons that show direction.
- Do not mirror: logos, media playback controls, clocks, checkmarks, numbers and phone numbers, embedded Latin words, code, images of real objects.
- Charts: time axes are often kept left-to-right even in RTL products; decide per product and test with native readers (see the `data-visualization` skill).
- Isolate user-generated or mixed-direction strings: `<bdi>` or `unicode-bidi: isolate;`, and `dir="auto"` on inputs.

```css
:lang(ar) { font-family: "IBM Plex Sans Arabic", "Noto Sans Arabic", sans-serif; font-size: 1.125em; line-height: 1.8; letter-spacing: 0; }
:lang(ja) { font-family: "Noto Sans JP", "Hiragino Sans", "Yu Gothic", sans-serif; line-height: 1.8; line-break: strict; }
:lang(ko) { word-break: keep-all; }
[dir="rtl"] .icon-arrow { transform: scaleX(-1); }
```

## Mixed-script setting

- Order the stack Latin first, then the script font: `font-family: "Inter", "Noto Sans JP", sans-serif;` so Latin and numbers use the Latin face. Reverse it if the script font's Latin is designed to match (many Japanese fonts include good Latin).
- Match apparent size with `size-adjust` on a script-specific `@font-face`, or with `font-size-adjust` (supported in all major browsers since 2024).
- Align baselines and check that line-height accommodates the tallest script in the line.
- Keep the same weight color across scripts: a 400 Latin next to a 400 Arabic may not match; compare and adjust.

## Text expansion

Plan layouts for translation before it arrives. These are typical ranges from localization practice, not guarantees:

| Source string (English) | Typical expansion in European languages |
| --- | --- |
| Up to 10 characters (button labels) | Can double or triple |
| 11-40 characters | +40-80% |
| Paragraphs | +20-35% (German, French, Finnish at the high end) |

CJK usually needs fewer characters but taller lines. Design buttons and nav to grow, avoid fixed-width labels, and test with pseudo-localized strings (accented and lengthened text) before real translations exist. The `ux-design` skill covers content design.

## Multiscript checklist

- Every required script has a named family, weight set and license.
- `lang` and `dir` set; logical properties used; mirrored icons reviewed.
- Size, line-height and line breaking adjusted per script; no tracking or faux italics.
- Long translations and pseudo-localization rendered at 360px and desktop.
- Native-speaker review recorded before launch.
- Deep method for client projects: [localization and resilient content](../../../library/draft-skills/design-content-writing/references/localization.md) and [advanced typesetting](../../../library/draft-skills/design-typography/references/advanced-typesetting.md).
