---
id: market.india-south-asia
axis: market
name: India and South Asia
aliases: [India, Bharat, Hindi, Indic scripts, Devanagari, Bangladesh, Pakistan, Sri Lanka, Nepal, UPI market, vernacular]
summary: Android-first, multilingual and multi-script region where UPI, WhatsApp and vernacular interfaces drive adoption, with Indic-script typesetting, lakh/crore numbers and new DPDP privacy rules.
tags: [india, south asia, hindi, devanagari, indic, upi, vernacular, rtl urdu, dpdp, bangladesh]
pairs_with: [industry.fintech-banking, industry.ecommerce-dtc, industry.education-edtech, industry.media-entertainment-streaming, industry.food-beverage-cpg, style.maximalist-eclectic, style.vibrant-gradient-saas, style.playful-bubbly, channel.native-app, audience.low-bandwidth-entry-devices]
avoid_with: []
version_timestamp: __TS__
---

# India and South Asia

## Language and script

- India has 22 scheduled languages and many scripts: Devanagari (Hindi, Marathi, Nepali), Bengali-Assamese, Gurmukhi (Punjabi), Gujarati, Odia, Tamil, Telugu, Kannada, Malayalam, and Perso-Arabic Nastaliq for Urdu (also Pakistan; right to left). Sinhala (Sri Lanka) and Latin (English, plus romanized "Hinglish") complete the set. Hindi is the largest first language, but English remains the link language in business, banking and premium e-commerce.
- Digital adoption growth is largely vernacular: offer language choice at first launch, remember it, and let users switch quickly. Voice input and search in Indic languages are important. Mix English terms where users actually say them (OTP, UPI, bill) instead of forcing literal translation.
- Indian English follows British spelling (colour, organisation) with local vocabulary (lakh, crore, "prepone", "do the needful"); avoid regional idioms in global copy.
- Regional neighbors: Bangladesh (Bangla, BDT ৳), Pakistan (Urdu and English, PKR ₨), Sri Lanka (Sinhala, Tamil, English, LKR), Nepal (Nepali, NPR ₨). Treat each as its own market; Tamil is shared by India and Sri Lanka but dialects differ.
- Translation expansion from English: Hindi +20-30%, Marathi +20-30%, Bengali +20-30%, Tamil and Malayalam +30-50% (long agglutinative words, wide glyphs), Urdu +20-30% with taller lines. Heuristics; test with real copy.
- Honorifics and tone: respectful second person (आप, நீங்கள்) for finance, health and elders; friendly (तुम) for youth brands. Use gender-neutral phrasing when possible; verbs inflect for gender in Hindi.
- Locale codes: `hi-IN`, `bn-IN`, `bn-BD`, `ta-IN`, `te-IN`, `kn-IN`, `ml-IN`, `mr-IN`, `gu-IN`, `pa-IN`, `ur-PK`, `en-IN`.

## Typography and layout

| Script | Fonts (OFL, Google Fonts) | Line-height | Notes |
| --- | --- | --- | --- |
| Devanagari | Noto Sans/Serif Devanagari, Mukta, Hind, Poppins (Latin + Devanagari), Baloo 2, Tiro Devanagari | 1.6-1.8 | Headline bar (shirorekha) joins letters; matras above and below need space |
| Bengali | Noto Sans Bengali, Hind Siliguri, Baloo Da 2 | 1.6-1.8 | Complex conjuncts; test rendering |
| Tamil | Noto Sans Tamil, Hind Madurai | 1.6-1.8 | Wide glyphs; long words |
| Telugu / Kannada | Noto Sans Telugu, Noto Sans Kannada, Mandali, Hind Guntur | 1.6-1.8 | Stacked consonants |
| Malayalam | Noto Sans Malayalam, Manjari | 1.7-1.9 | Very wide, intricate conjuncts |
| Gujarati / Gurmukhi | Noto Sans Gujarati, Hind Vadodara, Noto Sans Gurmukhi | 1.6-1.8 | |
| Urdu (Nastaliq) | Noto Nastaliq Urdu | 1.9-2.2 | Diagonal baseline needs tall lines; Noto Naskh Arabic is more UI-friendly |

- Multi-script families such as Anek (OFL) and Noto Sans pair Latin with Indic scripts; commercial options include Kohinoor (Indian Type Foundry). Pair Latin and Indic at matching optical size: Indic needs about +10% font size to match Latin x-height.
- Rules: no letter-spacing (it breaks conjunct and headline-bar continuity), no italics or uppercase, avoid synthetic bold, no justified text without a language-aware hyphenation engine, and never truncate mid-grapheme (use `Intl.Segmenter`). Subset fonts carefully with `unicode-range`; do not strip conjunct glyphs. Ensure the OS or browser shaper (HarfBuzz) is available on older Android versions by embedding webfonts.
- Body size 16-18px (mobile 16px minimum), headings with 1.3-1.4 line-height in Indic scripts, never tighter than 1.25.
- Layouts are mobile-first at 360x640 to 412x915; dense cards, bottom navigation, sticky action bars, language switch in the top bar. Urdu pages use RTL; mirror layouts as described for Arabic and Hebrew markets.
- Performance budgets: a common target is a first load under 150-200 KB on 3G-like profiles; apps under 20-30 MB for entry devices (Android Go). Use WebP/AVIF, system font fallback and skeleton screens.

## Color and symbolism

- Color meanings vary by religion, region and community. Red is auspicious and bridal (weddings, sindoor), yellow and marigold orange are festive and sacred, white signals purity and, in some Hindu contexts, mourning, green is associated with nature and Islam, black is considered inauspicious in some rituals but is fashionable elsewhere, blue is linked to Krishna and to the Ambedkarite movement. Do not assert one universal meaning.
- Saffron and green carry strong religious and political associations (Hindu and Muslim symbolism, national flag colors). Avoid pairing them in civic, news or nonprofit work without intent.
- Festival palettes: Diwali (gold, red, orange, diya warmth), Holi (bright powders), Eid (green, white, gold), Navratri (nine colors by day), Pongal, Onam (white and gold), Christmas in Kerala, Goa and the northeast. Retail seasons: Diwali, Big Billion Days and Great Indian Festival, IPL cricket season, weddings (roughly Nov-Feb).
- Vibrant, high-saturation palettes are widely used; they still need contrast. Pastel-on-white minimalism often fails 4.5:1 and washes out on low-brightness screens.
- National symbols (tricolour, Ashoka Chakra, Gandhi's image) are regulated for commercial use under Indian emblem laws; avoid them in brand marks.

## Imagery and representation

- Diversity is the baseline: religions (Hindu, Muslim, Christian, Sikh, Buddhist, Jain and others), regions, castes, languages, rural and urban life, skin tones, body types and abilities. Avoid defaulting to the northern, upper-caste, light-skinned urban norm. Skin-lightening aspiration has drawn criticism and regulator action (ASCI guidelines); show a range of skin tones with dignity.
- Avoid clichés: snake charmers, slums-as-scenery, "Bollywood dance" for every brand, call-center jokes, Taj Mahal as stand-in for India, curry and spice stereotypes. Show contemporary life: metros, trains, small shops (kirana), startup offices, farms, schools, family gatherings, cricket.
- Religious imagery: do not print deities or religious symbols on footwear, doormats or trivial products, or use sacred syllables (Om) lightly. Cow imagery and beef, alcohol and pork content need caution in advertising.
- Family-centered narratives (joint families, weddings) resonate but do not reduce women to caregiving; urban working women and entrepreneurs are common. Safety is a visible theme for women in mobility and delivery products.
- Maps: depicting India's borders incorrectly (Jammu and Kashmir, Arunachal Pradesh) causes legal and public backlash; use official Survey of India boundaries (verify with counsel).
- Honor local creators: regional illustrators, photographers and directors; folk art (Madhubani, Warli, Pattachitra, Kalamkari) is living craft; commission or credit artisans rather than tracing patterns.

## Formats and conventions

| Item | Convention | Example |
| --- | --- | --- |
| Date | DD/MM/YYYY; financial year April-March (FY 2026-27) | 20/10/2026 |
| Time zone | IST UTC+5:30 single zone; Nepal UTC+5:45, Bangladesh UTC+6, Pakistan UTC+5 | |
| Number | Lakh/crore grouping: last three digits, then pairs; Western digits are standard in UI, native digits (०१२, ০১২) optional | 12,34,567.89 (en-IN) |
| Currency | ₹ (U+20B9) INR; abbreviations lakh (L) and crore (Cr); shorten large amounts | ₹12.3 lakh, ₹4.5 Cr |
| Address | Flat/house, building, street, landmark, locality, city, state, 6-digit PIN | Flat 4B, Rose Apts, MG Road, near Metro, Bengaluru, Karnataka 560001 |
| Phone | +91 and 10-digit mobile starting 6-9; OTP login is default | +91 98765 43210 |
| Name | No fixed first/last order; initials before names in South India; mononyms; Sikh Singh/Kaur | Use one "Full name" field |
| IDs | Aadhaar (12 digits; restricted use), PAN (AAAAA9999A), GSTIN (15 chars), DL, voter ID | Mask; collect only when lawful |

- Landmarks and map pins matter because many addresses are informal; support autocomplete and geolocation.
- Mobile number plus OTP replaces email as the primary identity; add WhatsApp OTP, email as backup.
- Weekdays and months localize; festivals follow lunar calendars (Vikram Samvat, Saka, Hijri, Tamil), so link to dated lists.
- Use 24-hour time in transport and 12-hour in consumer apps. Weekend days differ (for example Friday-Saturday in Bangladesh, Saturday in Nepal); make them configurable.

## Platforms, devices and payments

- Android is about 95% of Indian smartphones (StatCounter; verify), mostly Xiaomi/Redmi, Samsung, Vivo, Oppo, realme and others, with 2-6 GB RAM and 64-128 GB storage in the mass segment; KaiOS JioPhone for feature-phone upgraders. Shared family devices exist; avoid assuming one user per device. 4G is widespread and 5G is expanding; data is cheap but network quality varies.
- Messaging and social: WhatsApp is universal (including business catalogs and payments links), YouTube, Instagram, Facebook, ShareChat/Moj, Telegram. Video-first formats and vernacular voice are strong.
- **UPI** (NPCI's Unified Payments Interface) is the dominant digital payment rail: PhonePe, Google Pay, Paytm, BHIM, CRED and bank apps; UPI QR codes at nearly every merchant; UPI ID (VPA) like name@bank; intent flow opens the user's UPI app and the PIN is entered there, not in your page. UPI AutoPay supports recurring payments; UPI Lite handles small amounts. Offer "Pay with UPI" first, then cards (RuPay, Visa, Mastercard), net banking, wallets, EMI/BNPL and cash on delivery (still significant).
- RBI rules: card-on-file tokenization (merchants cannot store card numbers), e-mandates for recurring card payments with additional authentication above thresholds, and digital lending guidelines (key fact statement, APR disclosure). Verify the current thresholds.
- Neighbors: Bangladesh (bKash, Nagad, Rocket), Pakistan (JazzCash, Easypaisa, Raast), Sri Lanka (LankaQR, cards), Nepal (eSewa, Khalti, Fonepay).
- Public digital infrastructure: Aadhaar eKYC, DigiLocker, Account Aggregator, ONDC (open commerce network), Digital Public Goods; plan integrations with consent screens.
- Marketplaces: Flipkart, Amazon India, Myntra, Meesho, Nykaa, Blinkit, Zepto, Swiggy, Zomato, BigBasket; offline-to-online (kirana, Jio/Reliance Retail) is influential.

## Regulatory and compliance notes

- **Privacy (DPDP Act 2023):** the Digital Personal Data Protection Act 2023 and Rules (notified November 2025) are being phased in; core obligations (consent notice, purpose limitation, rights handling, breach reporting) apply after an 18-month period (reported as about May 2027; verify). Notices must be clear, itemized and available in English or any of the 22 Eighth Schedule languages; consent must be free, specific, informed and withdrawable as easily as given; consent managers are planned; verifiable parental consent applies for under-18s, with bans on tracking, behavioral monitoring and targeted ads to children. Until then, the IT Act 2000 and SPDI Rules 2011 apply.
- **Consumer and e-commerce:** Consumer Protection Act 2019 and Consumer Protection (E-Commerce) Rules 2020 (seller details, country of origin, price inclusive of taxes, grievance officer, clear refund terms). The 2023 CCPA Guidelines on Dark Patterns list 13 patterns (false urgency, basket sneaking, confirm shaming, forced action, subscription trap, interface interference, bait and switch, drip pricing, disguised ads, nagging, trick questions, SaaS billing, rogue malware); design checkout, subscriptions and nudges accordingly.
- **Advertising:** ASCI codes (influencer disclosures like #ad, health and fairness claims) and sector rules (RBI, SEBI, IRDAI for finance and insurance).
- **Accessibility:** Rights of Persons with Disabilities Act 2016 and GIGW 3.0 for government sites (WCAG-based); the Supreme Court has required accessible digital KYC (2025; verify). Target WCAG 2.2 AA with Indic screen reader testing (TalkBack, NVDA with Indic voices).
- **Neighbors:** Sri Lanka's Personal Data Protection Act (2022, phased), Nepal's Privacy Act 2018; Pakistan and Bangladesh have cybercrime laws with developing or draft data protection frameworks; verify current status.
- Confirm requirements with counsel for the specific product and jurisdiction.

## Localization pitfalls

- Using Latin-first fonts that lack Indic glyphs, falling back to a mismatched default, or rendering broken conjuncts on older Android.
- Applying letter-spacing, uppercase or italics to Indic text; truncating mid-syllable; tight line-height clipping matras.
- Western number grouping (1,234,567) in lakh/crore contexts; ₹ missing in fonts; confusing "Rs." and "INR".
- Email-only signup, no OTP, no UPI; credit-card-only checkout.
- Overweight pages and large app bundles for entry-level devices; requiring uploads of Aadhaar or PAN without need.
- Translating literally rather than using the colloquial hybrid language people use; ignoring dialects and honorifics.
- Using religious, caste or regional cues carelessly in names, imagery or color; stereotyped casting.
- Calendar and festival errors: dates shift each year (lunar), and regional festivals matter (Pongal, Onam, Durga Puja).

## Reference anchors

- Unicode, Google Fonts Noto/Hind/Mukta/Baloo families (OFL), Ek Type (Anek, Mukta) and Indian Type Foundry (Kohinoor); Google Fonts Indic language guidance
- NPCI UPI Product Guidelines and brand assets (npci.org.in); Digital India and India Stack
- GIGW 3.0 (guidelines.india.gov.in) and the Government of India design resources
- National Institute of Design (NID) and IDC School of Design, IIT Bombay; Satyajit Ray's typefaces and graphic design as a historical reference
- Google "Next Billion Users" research and Google Design's guidance on emerging markets
- CCPA India Dark Patterns Guidelines (consumeraffairs.nic.in) and MeitY DPDP documents
