---
id: market.japan
axis: market
name: Japan
aliases: [Japanese market, ja-JP, Nihon, Japanese typography, kanji kana, keigo]
summary: Japanese-language market with three scripts, polite register, information-rich layouts, iPhone-heavy mobile use, LINE, PayPay, konbini payments and tax-inclusive pricing under APPI and commerce law.
tags: [japan, japanese, ja-jp, kanji, kana, keigo, line, paypay, konbini, vertical text]
pairs_with: [industry.ecommerce-dtc, industry.food-beverage-cpg, industry.gaming-esports, industry.fashion-apparel, industry.automotive-mobility, industry.hotels-travel, style.quiet-minimal, style.playful-bubbly, style.illustrative-narrative, channel.native-app]
avoid_with: []
version_timestamp: 2026-10-20 02:17:13 UTC
---

# Japan

## Language and script

- Japanese (`ja-JP`) mixes kanji (borrowed Han characters; roughly 2,100 in everyday use), hiragana (grammar and native words), katakana (loanwords, emphasis, brand names) and Latin (rōmaji, acronyms). Always set `lang="ja"`, or the browser may select a Chinese or Korean glyph variant for shared Han characters.
- Furigana (ruby, `<ruby>` markup) shows kanji readings for children, learners and uncommon words. Use it in kids' products, public service and education.
- **Keigo (honorific speech):** UI and marketing copy uses the polite です/ます form; formal contexts add respectful (尊敬語) and humble (謙譲語) forms. Address customers as お客様. Apologize in error states (申し訳ございません) and avoid blunt imperatives. Casual (だ/である) tone fits only youth or character-driven brands. Pick one register per product.
- Writing conventions: no spaces between words; full-width punctuation 。、「」『』…… 〜 ・; half-width digits and Latin; katakana long-vowel mark ー; avoid half-width katakana. The wave dash 〜 has two Unicode variants (U+301C and U+FF5E) that cause garbled data between systems; standardize.
- Input: IME composition is a major form pitfall. Do not submit on Enter while composing (check `event.isComposing`/`compositionend`). Users may type full-width digits (０１２); normalize with NFKC before validating phone, postal code and card fields.
- Names: family name first (山田 太郎). Forms usually ask for kanji name plus katakana reading (セイ/メイ) in separate fields for sorting and calls. Honorific さん (neutral) and 様 (formal) follow names.
- Text expansion: Japanese uses roughly 20-40% fewer characters than English, but every character is full-width and taller line-height is needed, so area is similar; polite phrasing can lengthen button labels. Test with real strings.
- Eras: Reiwa (令和) year counting is used in government, finance and forms (2026 is Reiwa 8). Offer the Gregorian year by default and show the era where documents require it.

## Typography and layout

| Item | Default | Override when |
| --- | --- | --- |
| Gothic (sans) | Noto Sans JP, Source Han Sans JP, BIZ UDPGothic (universal design), IBM Plex Sans JP, M PLUS 1p/2, Zen Kaku Gothic New, LINE Seed JP (OFL) | Brand voice; UD fonts for accessibility |
| Rounded | M PLUS Rounded 1c, Zen Maru Gothic, Kiwi Maru (OFL) | Friendly, kids, food |
| Mincho (serif) | Noto Serif JP, Shippori Mincho, Zen Old Mincho, Kaisei family (OFL) | Editorial, luxury, tradition |
| Display / hand | Dela Gothic One, RocknRoll One, Reggae One, Yusei Magic (OFL) | Campaigns |
| Commercial | Morisawa (Shin Go, Ryumin, UD Shin Go), Fontworks (Rodin, Tsukushi), Adobe Fonts | Large programs |
| System stack | "Hiragino Sans", "Hiragino Kaku Gothic ProN", "Yu Gothic", "Meiryo", "Noto Sans JP", sans-serif | Windows Yu Gothic thin weight renders weakly; use 500+ |
| Body size | 14-16px (modern sites 16px; older sites 12-14px); secondary 12px minimum | Elders: 16-18px |
| Line-height | 1.7-2.0 body, 1.3-1.5 headings | Tight UI lists 1.5 |
| Letter-spacing | 0.02-0.08em on body (a common practice); headlines with `font-feature-settings: "palt"` for proportional kana | Small UI labels 0 |

- **Line breaking (kinsoku shori):** certain characters cannot start a line (。、」）ー small kana ぁぃ ゃゅょっ) or end it (「（). Use `line-break: strict`, `word-break: auto-phrase` (Chromium 119+) or the BudouX library to break at phrase boundaries, and `text-wrap: balance` for headlines. Do not break inside katakana loanword compounds when avoidable.
- CSS punctuation spacing: `text-spacing-trim` (Chrome 123+) trims full-width punctuation; add about 0.25em between Japanese and Latin/digits (`text-autospace` where supported).
- **Vertical text (tategaki):** `writing-mode: vertical-rl; text-orientation: mixed;` columns run right to left; punctuation shifts to the upper right; one or two digits use `text-combine-upright: digits 2` (tate-chu-yoko); long Latin runs rotate sideways. Use for novels, manga, newspapers, poetry, restaurant menus, traditional packaging and seals; rarely for UI. Books and manga bind on the right; page turn is right to left.
- Italics: do not slant Japanese; use bold, color, or emphasis dots (傍点, `text-emphasis: filled sesame`). Underline sparingly.
- Layout: Japanese commerce pages are information-rich by design: ranking labels, points (ポイント), coupons, reviews and spec tables build trust (Rakuten, Yahoo! Japan, Amazon.co.jp). Long vertical landing pages (縦長LP) with testimonials, FAQ and urgency are standard for DTC. Minimal, ma (間) negative-space design (MUJI, Kenya Hara) is respected for premium and design-led brands. Match density to category; avoid an empty Western-style hero for mass-market retail.
- Mascots (yuru-chara, Kumamon), manga and anime-style illustration are mainstream even in public service and finance communication.

## Color and symbolism

- Red and white: the national flag (Hinomaru) and the celebratory kōhaku (紅白) pairing. Red with gold signals festivity; white with black signals funerals (black-and-white striped curtains). Avoid white flowers (chrysanthemum) and white-black pairings in celebration campaigns.
- Number taboos: 4 (shi, "death") and 9 (ku, "suffering") are avoided in gift sets, room and floor numbers; 8 (八, widening) is auspicious.
- Seasonal palettes matter: spring sakura pink (April starts the school and fiscal year), summer blues and whites, autumn red/orange (kōyō), winter whites; limited editions (季節限定) are central in food and beauty. Traditional color names (藍 indigo, 朱 vermilion, 桜色, 抹茶) carry cultural meaning.
- Stock and finance charts typically show red for rising and blue/green for falling (confirm per platform), opposite of the US. Green traffic lights are called "blue" (青信号).
- Pastels and cute (kawaii) palettes suit youth; muted earth tones, indigo and neutral greys suit premium and wellness; high-saturation primaries suit games and entertainment.
- Meet WCAG contrast: thin Mincho and pale pastels fail quickly at 12-14px.

## Imagery and representation

- Japan has a rapidly aging population (about 29% aged 65+; verify) and growing foreign-resident communities. Show active older adults, multigenerational families, working women and mixed-heritage people, not only young urban professionals.
- Avoid stereotypes: geisha, samurai, ninja, sushi-only, Mt. Fuji and cherry blossoms for every context. Use real neighborhoods, trains, konbini, izakaya, schools, local festivals (matsuri).
- Casting celebrities (tarento) is a standard ad strategy; local talent builds recognition and trust. Retouching norms are heavy; avoid body-shame messaging.
- Packaging and gift culture (omiyage, ochūgen, oseibo, noshi paper) shape visuals: wrap, seasonal sets and presentation matter. Design for gifting.
- Rising Sun flag (旭日旗) motifs read as controversial in Korea and China; if the product is sold regionally, avoid 16-ray sunbursts.
- Sensitive topics: religion (Shinto and Buddhism are folk-integrated; avoid trivializing shrines and temples), World War II history, territorial names. Use neutral maps and terminology.
- Pet, food and nature imagery is popular; show seasons accurately.

## Formats and conventions

| Item | Convention | Example |
| --- | --- | --- |
| Date | YYYY年M月D日 or YYYY/MM/DD; weekday in parentheses | 2026年10月20日(火) |
| Time | 24-hour; 午前/午後 | 15:30 |
| Number | Comma thousands; large numbers in 万 (10^4) and 億 (10^8) | 1,234万円 |
| Currency | JPY, no decimals; ¥ or 円; consumption tax 10% (8% reduced rate for food) | ¥1,100(税込) |
| Price display | Tax-inclusive total (総額表示) required | ¥1,100 (税込) |
| Address | Postal code, prefecture, city/ward, town, block-building number (large to small); 47 prefectures | 〒100-0001 東京都千代田区千代田1-1 |
| Phone | +81, mobile 070/080/090; landline with area code | 090-1234-5678 |
| Name | Family name first; kanji + kana reading | 山田 太郎 / ヤマダ タロウ |

- Postal code lookup (7 digits) should auto-fill prefecture and city; keep a free text for building and room.
- Bank transfer names use half-width/full-width katakana; validate carefully.
- Public holidays cluster in Golden Week (late April-early May), Obon (mid-August) and year-end/New Year; deliveries and campaigns pause.

## Platforms, devices and payments

- iOS leads: iPhone holds roughly 60-70% of smartphones (StatCounter; verify). Android devices from Sony, Sharp, Google Pixel, Samsung also appear. Mobile networks are fast; many users still use desktop for some tasks. Keep Safari/WebKit behavior in your test matrix.
- **LINE** is the dominant messaging and notification platform (also used in Thailand and Taiwan); LINE official accounts, LINE login and LIFF mini apps are common marketing channels. X (Twitter) is unusually popular in Japan; Instagram, YouTube, TikTok and Niconico complement.
- Payments: cards (JCB is a domestic brand; Visa/Mastercard), **PayPay** (QR wallet leader), Rakuten Pay, d払い, au PAY, Merpay, transit IC cards (Suica/PASMO via Apple Pay), **konbini payment** (pay at convenience store with a code, deadline-limited), bank transfer (振込), cash on delivery (代金引換), carrier billing, and Amazon Pay. Cashless share is rising (around 40% of consumption; METI, verify). Points programs (Rakuten, T-Point, Ponta, PayPay Points) influence platform choice. LINE Pay Japan merged into PayPay in 2025 (verify).
- Marketplaces: Rakuten Ichiba, Amazon.co.jp, Yahoo! Shopping, ZOZOTOWN, Mercari (C2C), Uber Eats, Demae-can; Tabelog and Gurunavi for restaurants.
- From December 2025 the Mobile Software Competition Act lets Apple/Google platforms support alternative app stores and external payments in Japan; check current terms before designing purchase flows (verify with the JFTC).
- Delivery culture: time-slot selection (午前中, 14-16時), re-delivery requests via LINE and carriers (Yamato, Sagawa, Japan Post).

## Regulatory and compliance notes

- **APPI** (Act on the Protection of Personal Information, amended 2022): specify and notify the purpose of use, consent for third-party provision and overseas transfers (with information about the destination), breach reporting to the PPC, and rules on "personally referable information" such as cookie IDs shared with third parties. The Telecommunications Business Act's external transmission rule (2023) requires notice or opt-out for certain operators sending user data (cookies, SDKs) to third parties.
- **Act on Specified Commercial Transactions (特定商取引法):** online sellers must publish a seller information page (特定商取引法に基づく表記: operator, address, phone, price, payment, delivery, returns) and show an accurate final confirmation screen; misleading subscription (定期購入) flows are penalized.
- **Advertising:** Premiums and Representations Act (景品表示法) prohibits misleading superiority or price claims; stealth-marketing rules (since October 2023) require ads by influencers to be identifiable (#PR, 広告). The Pharmaceutical and Medical Device Act (薬機法) strictly limits claims for cosmetics, supplements and health products.
- **Accessibility:** Act for Eliminating Discrimination against Persons with Disabilities (private businesses must provide reasonable accommodation since April 2024); JIS X 8341-3:2016 (aligned with WCAG 2.0 AA) is the reference; many companies target WCAG 2.1/2.2 AA.
- **Platforms:** the Mobile Software Competition Act (full effect December 2025) and the Act on Improving Transparency of Digital Platforms.
- **Consumer:** online sales have no general cooling-off period, but if return terms are not clearly stated buyers may return goods within a statutory window (8 days; verify); show tax-inclusive prices and clear return terms.
- Confirm requirements with counsel for the specific product and jurisdiction.

## Localization pitfalls

- Ignoring `lang="ja"`: wrong glyph shapes. Missing Japanese fonts cause tofu boxes; Latin-only fallback fonts look off.
- Submitting forms on IME confirm Enter; not accepting full-width input; rejecting katakana readings; forcing Western name order or a single Latin "first name".
- Prices shown pre-tax; missing 特商法 page; casual tone in support; omitting furigana for kids.
- Line breaks that split words or leave punctuation at line start; justified text with awkward gaps.
- Sparse Western-style pages for mass-market retail; or flashy overload for premium brands.
- Using 4s in gifts and 9s in rooms; white-and-black celebration visuals.
- Treating Japan as only Tokyo: Kansai (Osaka) has different humor and consumer tastes; Hokkaido and Okinawa differ.
- Not planning for LINE, PayPay or konbini payment; no tracking number in delivery flow.

## Reference anchors

- W3C Requirements for Japanese Text Layout (JLReq), JIS X 4051 composition rules
- Japan Digital Agency Design System and Digital Agency design guidelines (digital.go.jp)
- Noto Sans/Serif JP and Source Han (OFL), M PLUS, Zen fonts, BIZ UDPGothic; Morisawa and Fontworks for commercial type
- Kenya Hara (MUJI, *Designing Design*), Ikko Tanaka, Yusaku Kamekura (1964 Olympic posters), Tadanori Yokoo
- LINE's public design resources, Rakuten, MUJI, Uniqlo and Nintendo as public brand references
- Personal Information Protection Commission (ppc.go.jp) guidance and Consumer Affairs Agency notices
