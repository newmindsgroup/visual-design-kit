---
id: market.middle-east-north-africa-arabic
axis: market
name: Middle East and North Africa (Arabic)
aliases: [MENA, Arab world, GCC, Gulf, Saudi Arabia, UAE, Egypt, Levant, Maghreb, Arabic RTL, ar-SA, ar-AE, ar-EG]
summary: Right-to-left Arabic-script markets from the Gulf to the Maghreb, mobile-first and young, with strong religious and family norms, mada and cash-on-delivery payments, and fast-evolving data laws.
tags: [arabic, rtl, mena, gcc, saudi arabia, uae, egypt, ramadan, mada, right-to-left]
pairs_with: [industry.ecommerce-dtc, industry.fintech-banking, industry.real-estate-proptech, industry.luxury-goods, industry.hotels-travel, industry.government-civic, style.classic-luxury-serif, style.art-deco, channel.native-app, channel.social-media]
avoid_with: []
version_timestamp: 2026-10-20 02:17:13 UTC
---

# Middle East and North Africa (Arabic)

## Language and script

- Arabic script, written right to left (RTL), cursive: each letter has up to four forms (isolated, initial, medial, final) and joins to its neighbors. No capitals, no italics. Written Modern Standard Arabic (MSA, fusha) is shared; speech and marketing use dialects (Gulf/Khaleeji, Egyptian, Levantine, Maghrebi/Darija). Use MSA for UI and legal copy, and a light dialect touch only in social and campaign copy written by native speakers.
- Maghreb markets (Morocco, Algeria, Tunisia) use French widely in business and retail, Amazigh/Tifinagh appears in Morocco and Algeria, and Kurdish in Iraq. Gulf markets have large expatriate populations (South Asian, Filipino, Western), so English is a working language there; offer English and Arabic with a persistent language switch.
- Diacritics (tashkeel) are normally omitted; use them only for children, learners or ambiguous words. Punctuation: Arabic comma ، (U+060C), semicolon ؛, question mark ؟; guillemets «».
- **Digits:** Western digits (0-9) and Arabic-Indic digits (٠-٩) both occur. CLDR defaults differ by country (the Maghreb typically uses Western digits; Egypt, Saudi Arabia and Iraq often use Arabic-Indic; verify with `Intl.NumberFormat('ar-XX')`). Never mix both in one screen; offer a user preference.
- Text expansion: English to Arabic runs about +20-25% in characters, but Arabic glyphs are narrower, so line length changes less than height; plan for taller lines. Test with real copy.
- Formality: formal address and honorifics (السيد, السيدة) in banking, government and B2B; warm, respectful greetings in consumer apps (أهلاً وسهلاً). Gender is grammatical in verbs and pronouns; use neutral or plural phrasing where the user's gender is unknown.
- Religion: Islamic greetings and the Hijri calendar are normal; do not use Qur'anic verses or the word Allah as decoration, in logos or on disposable items.

## Typography and layout

| Item | Default | Override when |
| --- | --- | --- |
| UI fonts | IBM Plex Sans Arabic, Noto Sans Arabic, Cairo, Tajawal, Almarai, Readex Pro, Rubik (OFL) | Brand voice: Noto Kufi Arabic or Reem Kufi for geometric display; Noto Naskh Arabic or Amiri for editorial |
| Commercial | Frutiger Arabic, DIN Next Arabic (Nadine Chahine), 29LT Zarid (Pascal Zoghbi) | Large brand programs |
| Body size | 16-18px; scale Arabic +10-15% over adjacent Latin (smaller x-height) | Dense tables: 14px minimum |
| Line-height | 1.6-1.8 body; 1.3-1.4 display (marks above and below) | Tight display: never below 1.2 |
| Letter-spacing | 0 always; tracking breaks joins | Never apply `letter-spacing` or `text-transform` |
| Weights | 400/500/700; avoid ultra-thin; avoid synthesized bold | Variable fonts preferred |

- Pair Arabic and Latin deliberately: match x-height optically, align baselines, and keep the same weight; Plex Sans Arabic with Plex Sans Latin and Noto Sans Arabic with Inter are workable pairs.
- Justification uses kashida (tatweel) elongation; browsers support `text-justify: inter-character`, but avoid justification in UI. Use `lang="ar"` and `dir="rtl"` on `html`.
- **RTL mirroring: mirror** layout order, navigation, back/forward chevrons and arrows, progress bars, sliders, list indents, toggle direction, swipe/drag gestures, carousels, step trackers, "send" and "reply" glyphs, and text alignment. **Do not mirror:** numerals, phone numbers, Latin words and code (use `<bdi>` or `dir="ltr"`), media playback controls, clocks, photos, logos and brand marks, charts' value axes (mirror category order, not numeric magnitude; test), and icons depicting real objects (phones, keys). Use CSS logical properties (`margin-inline-start`, `padding-inline`, `inset-inline-end`, `text-align: start`).
- Use Material and Apple HIG RTL guidance; test with pseudolocalization and real Arabic copy because screenshots from LTR templates hide bugs (broken joins, reversed parentheses, bidi punctuation).
- Tables and forms follow reading direction: labels sit at the right of inputs and first columns start at the right. Leading icons inside inputs sit on the right, trailing icons on the left.

## Color and symbolism

- Green has strong Islamic and national associations (it is the field color of Saudi Arabia's flag); white signifies peace and purity; black signals mourning in many places but also luxury (abaya, formalwear); gold signals wealth and celebration; deep blue, turquoise and sand/earth tones evoke the region's landscape and heritage architecture.
- Ramadan and Eid campaigns use deep purple, midnight blue, emerald and gold with lanterns (fanous), crescents and geometric patterns; National Day campaigns (Saudi National Day Sept 23, UAE National Day Dec 2) use flag colors. Do not reproduce flags containing the Shahada (Saudi Arabia) on products, packaging or items likely to be discarded or stepped on.
- Colors have meaning that varies by country, class and community. Confirm with local reviewers before committing a palette. Red signals danger in UI; check cultural readings in political contexts (party colors).
- Gulf luxury and real-estate branding often uses gold, deep green or navy and dark palettes; whatever the style, meet WCAG contrast in both scripts, as Arabic strokes thin at small sizes.

## Imagery and representation

- Modesty norms: use covered shoulders and knees in imagery for mainstream audiences, avoid alcohol, pork and revealing dress in general ads (alcohol and nightlife are restricted or banned in several countries), and avoid public displays of intimacy. Standards differ across the Gulf, Levant and Maghreb; the UAE and Lebanon are more permissive than Saudi Arabia or Kuwait, though Saudi norms have been changing.
- Show real diversity within the region: women at work (hijab-wearing and not), families, youth, entrepreneurs, expatriates, and different nationalities. Representation of women in leadership aligns with national visions (Saudi Vision 2030, UAE) but should not stereotype. Avoid casting that equates "Arab" with desert, camels and oil; Gulf cities like Riyadh and Dubai are highly modern.
- Gestures and etiquette: use the right hand for giving and eating, avoid showing soles of feet, and be careful with thumbs-up and pointing gestures.
- Calligraphy and geometric patterns (arabesque, mashrabiya) are cultural heritage; use them with respect and with native-speaking calligraphers. The most damaging error is broken, reversed or disconnected Arabic in ads and packaging; always have a native speaker proof the final art.
- Maps and borders are legally sensitive (Western Sahara, Palestine/Israel, Golan, Gulf names). Use maps approved by the client's legal team per market; some countries restrict specific depictions.
- Avoid depicting religious figures, mosques interiors in commercial contexts without permission, or using prayer imagery to sell goods.

## Formats and conventions

| Item | Convention | Example |
| --- | --- | --- |
| Date | Gregorian for commerce, Hijri alongside for religious and some government use (Saudi); DD/MM/YYYY | ٢٠/١٠/٢٠٢٦ or 20/10/2026; 1448 AH |
| Weekend | Fri-Sat in Saudi Arabia, Qatar, Kuwait, Egypt; Sat-Sun in the UAE (since 2022, with a short Friday), Morocco | Make it configurable |
| Time | 12-hour with ص/م or 24-hour; prayer times (Fajr, Dhuhr, Asr, Maghrib, Isha) in religion-aware apps | ٣:٣٠ م |
| Number | Arabic-Indic or Western digits; decimal ٫ and thousands ٬ with Arabic digits | ١٬٢٣٤٫٥٠ |
| Currency | SAR (ر.س), AED (د.إ), EGP (ج.م), MAD (د.م.), QAR (ر.ق); KWD, BHD, OMR, JOD, TND use 3 decimals | 150.000 د.ك |
| Phone | +966 5X XXX XXXX (Saudi), +971 5X XXX XXXX (UAE), +20 1X XXXX XXXX (Egypt); keep numbers LTR | +971 50 123 4567 |
| Address | Saudi National Address (building number, street, district, city, postal code, short address); UAE uses emirate, area, building, PO Box or Makani (Dubai); many addresses use landmarks | Provide map pin and landmark fields |
| Name | Given + father's + grandfather's + family name; "Al-/Bin/Bint" particles; transliteration varies (Mohammed/Muhammad) | Accept Arabic and Latin names; match ID spelling |

- Ramadan changes working hours, shopping rhythm (night peaks after iftar) and push-notification timing. Friday midday prayer: avoid scheduling launches, webinars or deliveries about 11:30-13:30.
- VAT: Saudi Arabia 15%, UAE 5%, Egypt 14% (verify current rates). Prices include VAT for consumers in the Gulf.
- Digital IDs: UAE Pass, Nafath (Saudi), Emirates ID; plan login and KYC flows around them.

## Platforms, devices and payments

- Mobile-first, very young populations. iOS share is high in the Gulf (roughly 40-60%; verify), while Android dominates in Egypt, Morocco, Algeria and Iraq (75-90%). Data is affordable in the Gulf and costly in lower-income markets, so keep pages light.
- Social: WhatsApp is universal; Snapchat is huge in Saudi Arabia; TikTok, Instagram, YouTube and X are central; Facebook dominates in Egypt and the Maghreb; Telegram is common in Egypt, Iraq and Algeria.
- Commerce: Noon, Amazon (.ae, .sa, .eg), Namshi, Jumia (Egypt, Morocco), Shein, Talabat, HungerStation, Jahez, Mrsool and Careem for delivery and rides. Events: Ramadan, Eid, White Friday (the regional Black Friday), Back to School.
- Payments: cards with Apple Pay; **mada** is the Saudi debit network and must be supported for Saudi shoppers; STC Pay and urpay wallets; Sadad bill payment; **Tabby** and **Tamara** BNPL in Saudi Arabia and the UAE; KNET (Kuwait), Benefit (Bahrain), NAPS (Qatar), Thawani (Oman); **Fawry** kiosks and online (Egypt), InstaPay, Meeza cards, Vodafone Cash; CliQ (Jordan); cash-on-delivery remains significant, especially in Egypt and Saudi Arabia. Provide COD with an explicit fee line and confirmation by SMS/WhatsApp. 3-D Secure with SMS OTP is standard; local currency display builds trust.
- Gulf governments have strong digital-service ecosystems (Absher, Tawakkalna, UAE Pass); align login and document flows with them when working with public-sector or regulated clients.

## Regulatory and compliance notes

- **Data protection:** Saudi Arabia's PDPL (in force September 2023, fully enforceable since September 14, 2024; SDAIA) requires clear notice, consent, rights handling and limits on cross-border transfer; UAE Federal Decree-Law 45/2021 (PDPL), with DIFC and ADGM having their own regimes; Egypt Law 151/2020 (executive regulations and authority still maturing; verify); Qatar Law 13/2016; Bahrain Law 30/2018; Morocco Law 09-08 (CNDP); Tunisia and Algeria have national laws; Jordan enacted a PDP law in 2023. Provide privacy notices in Arabic.
- **Consumer and e-commerce:** UAE Consumer Protection Law (Federal Law 15/2020) and e-commerce rules; Saudi E-commerce Law and Maroof registry for online merchants; product information in Arabic; return and warranty rights; clear total price.
- **Content and advertising:** strict public-morality, religion, privacy and cybercrime laws (for example UAE Federal Decree-Law 34/2021); influencer licensing in Saudi Arabia (Mawthooq) and the UAE (advertiser permits; verify current rules); restrictions on alcohol, gambling, pork, dating and some health and cosmetic claims. Review all campaigns with local counsel.
- **Accessibility:** Saudi Digital Government Authority standards, UAE disability rights law and TDRA guidance; Egypt Law 10/2018; target WCAG 2.2 AA and test with Arabic screen readers (VoiceOver, TalkBack, NVDA).
- **Data residency:** some sectors (government, health, financial) require local hosting or approvals; verify per country.
- Confirm requirements with counsel for the specific product and jurisdiction.

## Localization pitfalls

- Mirroring a Latin UI by flipping a screenshot: broken joins, reversed parentheses, wrong icon directions and swapped numbers.
- Applying `letter-spacing`, uppercase transforms or truncating with CSS ellipsis mid-word; using low-quality fallback fonts that disconnect letters.
- Using Eastern digits in some fields and Western in others; failing to isolate phone numbers and Latin names with `dir="ltr"`.
- Designing in MSA only, or in a single dialect, for a pan-Arab audience; machine translation without review.
- Treating "Arab" as one culture: Gulf, Levant, Egypt and Maghreb differ in taste, language, law and payment rails.
- Launches during Ramadan without rhythm changes, or on Friday prayer time.
- Missing mada, COD, BNPL or local ID options; collecting data without Arabic notices.
- Ignoring a Hijri date or the fact that months shift each year.

## Reference anchors

- W3C Arabic Layout Requirements (alreq) and Unicode Bidirectional Algorithm (UAX #9)
- Material Design and Apple HIG right-to-left guidance; IBM Plex Sans Arabic and Noto Arabic font families (OFL)
- Huda Smitshuijzen AbiFarès, *Arabic Typography: A Comprehensive Sourcebook*; type designers Nadine Chahine and Pascal Zoghbi
- Saudi Digital Government Authority and UAE government digital design resources
- Careem, Noon, STC Pay and Tabby as public product references
- SDAIA (sdaia.gov.sa) PDPL guidance; UAE Data Office
