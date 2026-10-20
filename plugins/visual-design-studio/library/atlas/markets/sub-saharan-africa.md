---
id: market.sub-saharan-africa
axis: market
name: Sub-Saharan Africa
aliases: [Africa, Nigeria, Kenya, South Africa, Ghana, Ethiopia, Anglophone Africa, Francophone Africa, M-Pesa market]
summary: Young, mobile-money-led, multilingual region with low-end Android, costly data and USSD reach; Nigeria, Kenya, South Africa and Ghana lead digital adoption, with fast-growing data laws.
tags: [africa, sub-saharan africa, nigeria, kenya, south africa, ghana, m-pesa, mobile money, ussd, low bandwidth]
pairs_with: [industry.fintech-banking, industry.ecommerce-dtc, industry.marketplaces-platforms, industry.education-edtech, industry.nonprofit-ngo, industry.healthcare-provider, style.playful-bubbly, style.flat-material, channel.native-app, audience.low-bandwidth-entry-devices]
avoid_with: []
version_timestamp: __TS__
---

# Sub-Saharan Africa

## Language and script

- About 45 countries and 1,000+ languages. English is official or widely used in Nigeria, Ghana, Kenya, Uganda, Zambia, Zimbabwe, South Africa and others; French across West and Central Africa (Senegal, Côte d'Ivoire, Cameroon, DR Congo); Portuguese in Angola and Mozambique. Major African languages: Swahili (East Africa), Hausa, Yoruba, Igbo and Nigerian Pidgin (Nigeria), Amharic (Ethiopia), Zulu, Xhosa, Afrikaans and eight other official languages in South Africa, Twi, Wolof, Fula, Somali. Arabic script appears in the Sahel and Horn.
- Plan locales by country and market goal, e.g. `en-NG`, `en-KE`, `sw-KE`, `en-ZA`, `zu-ZA`, `af-ZA`, `fr-SN`, `am-ET`, `ha-NG`, `yo-NG`. English UI reaches urban, educated users; Swahili, Hausa, Pidgin, Yoruba and Zulu raise reach, trust and comprehension in finance, health and education. Code-switching is normal (Sheng in Kenya, Pidgin and "Naija" English in Nigeria).
- **Latin extensions:** Yoruba uses ẹ ọ ṣ with tone marks and combining dots; Hausa uses ɓ ɗ ƙ ƴ; Igbo uses ị ọ ụ ṅ; Ewe/Akan use ɛ ɔ ɖ ƒ ŋ; Fula and Wolof use ŋ ñ ɓ ɗ. Fonts must cover Latin Extended-A/B and Additional (Noto Sans, Inter, Open Sans, Noto Serif do; many display fonts do not). Never strip diacritics from names or search terms. **Ethiopic (Ge'ez/Fidel)** is an abugida used for Amharic and Tigrinya: Noto Sans Ethiopic, Abyssinica SIL (OFL); line-height 1.5-1.7. Other scripts: N'Ko, Tifinagh, Adlam (Noto families).
- Plain, concrete language works: short sentences, familiar words, icons paired with text. Reading level 6th grade or below for mass-market finance and health. Voice, audio and video explainers help where literacy varies.
- Text expansion from English: French +15-25%, Swahili +20-30%, Hausa/Yoruba/Zulu +20-40%, Amharic similar to English in width. Heuristics; test with real copy.
- Honorifics matter: titles such as Chief, Dr., Engr., Alhaji/Alhaja, Hajia, Pastor, Sir/Ma are used in Nigeria and Ghana; Bwana/Mama in East Africa; do not strip them.

## Typography and layout

| Item | Default | Override when |
| --- | --- | --- |
| UI fonts | Noto Sans (broad African Latin and Ethiopic coverage), Inter, Open Sans, Roboto, Source Sans 3 | Brand fonts must be tested on Yoruba, Hausa, Igbo, Twi characters |
| Display | Poppins, Nunito Sans, Montserrat, DM Sans, Space Grotesk | Check ɓ ɗ ƙ ẹ ọ ṣ glyphs |
| Font loading | System font first; subset to needed scripts; WOFF2; no render-blocking font files | Brand display only for headings |
| Body size | 16px minimum; 14px secondary; larger for older users and sunlight use | 18px for health and finance |
| Line-height | 1.5-1.6 | Ethiopic 1.6-1.7 |
| Contrast | 7:1 where possible: glare on low-brightness, low-quality screens | Large text 4.5:1 |
| Touch targets | 48px for fat-finger and cracked screens | Minimum 44px |

- Design for 360 x 640 CSS px (and smaller, down to 320 px); one-column layouts; large tap targets; short forms; progressive disclosure.
- Performance budgets are decisive: target initial transfers under 150-200 KB on key flows, total app size under about 10-30 MB (Android Go), lazy-load images (WebP/AVIF), cache aggressively, support offline drafts and resumable uploads. Provide a "lite" mode, image-quality toggle and data-usage indicators. Avoid autoplaying video and heavy JavaScript frameworks for core flows.
- **USSD and SMS:** feature-phone users interact via USSD (`*123#`) menus; keep menus to 3-4 levels, 160-182 characters per screen, numbered options, and a "0 back" convention. Mirror critical app flows in USSD or WhatsApp where reach demands it.
- Power and connectivity: load-shedding in South Africa and unreliable grids elsewhere mean sessions drop. Save state frequently, show retry states, and avoid draining batteries (dark mode helps OLED).
- Sunlight readability: avoid low-contrast greys and thin weights.

## Color and symbolism

- Do not default to "earth tones and safari" for African markets; urban African brands use bright, high-contrast palettes. Pan-African colors (red, gold, green, black) appear in many flags (Ghana, Ethiopia, Senegal, Cameroon, Mali); use with sensitivity and avoid appropriating national flags for products.
- Color meanings vary by culture and community; examples include Ghanaian kente and Adinkra (each pattern and color has meaning), Yoruba adire indigo, Maasai shuka red (Kenya/Tanzania; Maasai cultural IP concerns), Zulu beadwork color codes. Confirm meaning with local reviewers before borrowing cultural motifs. Funeral and wedding colors differ by country and ethnicity; avoid generalizing.
- Telecom and fintech brands use bold colors (Safaricom green, MTN yellow, Airtel red, Vodacom red, Orange orange); avoid color-and-shape conflicts with them in mobile money.
- Ankara/wax-print patterns, Afrobeats and Amapiano visual culture inspire youthful brands; commission local designers rather than copying prints.
- Ensure contrast and non-color cues; many users have cracked or low-brightness screens.

## Imagery and representation

- Avoid "poverty porn", savior narratives and generic "Africa" imagery (sunsets, acacia trees, wildlife) in commercial and nonprofit work. Show contemporary, diverse life: startup founders, tailors, nurses, farmers using phones, students, commuters (matatus, danfo, tro-tro), markets, mobile-money agents, creative scenes in Lagos, Nairobi, Accra, Kigali, Johannesburg and Cape Town.
- Photograph with local photographers; get consent, especially for children; credit creators. Avoid stock photos that mis-code countries (e.g., Maasai imagery for Nigeria).
- Represent faith respectfully: Christianity, Islam and traditional religions all matter; Sunday church and Friday prayer rhythms affect timing. Ramadan matters in the Sahel, Horn and East African coast.
- Colorism: skin-lightening products are heavily marketed in some markets and criticized; show a full range of skin tones.
- LGBTQ+ expression is criminalized or restricted in many countries (for example Nigeria and Uganda); consult local counsel on legal exposure and staff safety before featuring it.
- Urban/rural, informal economy and youth are central: gig riders, entrepreneurs, side hustles; portray ambition and competence rather than need.
- Maps and borders: use client- and country-specific approved maps; disputed areas (Western Sahara, Abyei, Somaliland) are sensitive.

## Formats and conventions

| Item | Convention | Example |
| --- | --- | --- |
| Date | DD/MM/YYYY (South Africa also YYYY-MM-DD officially); Ethiopia has its own calendar (13 months, ~7-8 years behind Gregorian) | 20/10/2026 |
| Time | 12-hour in speech and consumer apps, 24-hour in transport; Ethiopian clock counts from sunrise (offset 6 hours) | 15:30 |
| Number | Comma thousands, period decimal (Nigeria, Kenya, Ghana); South Africa's standard uses space and comma but common practice mixes | ₦1,234.56; R 1 234,56 |
| Currency | NGN ₦, KES KSh, GHS GH₵, ZAR R, UGX USh (no decimals), TZS TSh, ETB Br, XOF/XAF CFA francs (two zones, no decimals) | KSh 1,234 |
| Address | Often informal: landmark, area, LGA/county, city, state; postal codes rare in Nigeria; P.O. Box in Kenya; Ghana's digital address (GhanaPostGPS); South Africa suburb + 4-digit code | Provide pin drop and landmark |
| Phone | +234 80X, +254 7XX/1XX, +27 8X, +233 2X/5X; mobile numbers are primary identity | +254 712 345 678 |
| Name | Varied: Yoruba/Igbo/Akan day names (Kofi, Ama); Ethiopian given name + father's name (no family name); mononyms exist | Single "Full name" field |
| ID | Nigeria NIN/BVN, Kenya National ID/KRA PIN, Ghana Card, South Africa ID (13 digits) | Collect minimally |

- Prices: show local currency; many consumers think in daily and weekly amounts; show total cost including delivery and mobile-money fees.
- Weekend and holidays: Friday prayers (Muslim-majority areas), Sunday church; public holidays are many and sometimes announced late; Eid and Christmas peaks.
- Mobile money agents act as cash-in/cash-out points; design for agent flows (show agent code, float, receipts).

## Platforms, devices and payments

- Android dominates (roughly 80-90% of smartphones; verify with StatCounter). Handset mix is local: Transsion brands (Tecno, Infinix, itel) hold about a quarter of Africa-wide use and over half in Nigeria; Samsung leads many markets (e.g., over half in South Africa); Apple is a minority (IntelPoint/StatCounter 2025; verify). Many devices have 2-4 GB RAM, small storage, cracked screens and shared use. Feature phones remain significant (KaiOS, basic handsets). Opera Mini and data-saving browsers are popular.
- Data is costly relative to income; bundles are small and daily; WhatsApp, Facebook and sometimes zero-rated apps carry commerce. WhatsApp is the main business channel (catalogs, orders, support); Facebook (Marketplace), TikTok, Instagram, YouTube and X (Nigeria) follow.
- **Mobile money:** **M-Pesa** (Safaricom/Vodacom; Kenya, Tanzania, DR Congo, Mozambique, Ethiopia) with Lipa na M-Pesa (Till/Paybill) and STK push prompts; MTN MoMo (Ghana, Uganda, Rwanda, Côte d'Ivoire, Cameroon), Airtel Money, Orange Money, Wave (Senegal, Côte d'Ivoire, Mali), Telebirr (Ethiopia), EcoCash (Zimbabwe). Use the STK push or USSD prompt flows: user enters amount, gets a PIN prompt on the phone; show a clear "check your phone" state, timeout, and retry.
- Nigeria: bank transfer with dynamic virtual accounts, USSD banking, Paystack, Flutterwave, Moniepoint, OPay, PalmPay, Verve/Mastercard cards, NQR codes; South Africa: card, instant EFT (Ozow), PayShap, Capitec Pay, SnapScan/Zapper QR, Yoco, buy-now-pay-later (Payflex, Mobicred); card payments with 3-D Secure OTP remain central in SA. Cash on delivery and pay-at-pickup remain common in Nigeria and Kenya.
- Delivery: informal addresses, riders (boda-boda, dispatch riders), pickup points and lockers; show rider contact and call/WhatsApp.
- E-commerce and apps: Jumia, Takealot, Konga, Glovo, Bolt, Uber, Safaricom, Showmax; super-app ambitions (MTN, M-Pesa); verify local players per country.

## Regulatory and compliance notes

- **South Africa:** POPIA (effective July 1, 2021; Information Regulator) requires purpose limitation, consent or other lawful basis, direct-marketing opt-in (with exceptions for existing customers), security and breach notification. ECTA and the Consumer Protection Act require supplier details on websites, clear pricing, and a 7-day cooling-off for most online sales (verify exceptions).
- **Nigeria:** Nigeria Data Protection Act 2023 and the NDPC's General Application and Implementation Directive (GAID, effective September 2025): lawful basis, notice and consent, data protection officers and annual compliance audit returns for data controllers/processors "of major importance" (verify tiers and fees); CBN tiered KYC (BVN/NIN) for fintech; FCCPC for consumer protection; ARCON ad vetting.
- **Kenya:** Data Protection Act 2019 (ODPC): register as controller or processor (with turnover/employee-based exemptions), consent, data subject rights; digital lenders are licensed by the Central Bank; Computer Misuse and Cybercrimes Act. **Ghana:** Data Protection Act 2012 with Data Protection Commission registration. **Rwanda, Uganda, Tanzania, Senegal, Ethiopia and others** have data laws or proclamations (verify). The African Union Malabo Convention encourages harmonization.
- **Telecom/SIM:** mandatory SIM registration with ID in many countries; mobile-money KYC tiers cap balances and transfers; design onboarding with tiered limits.
- **Accessibility:** few explicit web mandates; Kenya's Persons with Disabilities Act and South Africa's equality laws apply; target WCAG 2.2 AA and include screen-reader and low-literacy support.
- **Taxes and fees:** VAT (e.g., South Africa 15%, Kenya 16%, Nigeria 7.5%, Ghana 15% plus levies; verify) and mobile-money transaction fees; show them.
- Confirm requirements with counsel for the specific product and jurisdiction.

## Localization pitfalls

- Treating Africa as one market; payment rails, regulators, languages and device mixes differ by country.
- Heavy pages, large app bundles, autoplay video and fonts that do not render Yoruba, Hausa, Igbo or Ethiopic.
- Card-only checkout; no mobile money, USSD, transfer or cash options; no clear "check your phone" state during STK push.
- Requiring addresses with postal codes or surnames; stripping diacritics from names.
- Relying on email for identity; mobile number plus OTP is primary, but SMS delivery can be delayed, so provide resend and voice OTP.
- Stock imagery that stereotypes, mixes countries or ignores local fashion and settings; using sacred patterns as decoration.
- Ignoring load-shedding and connectivity drops; sessions that lose state.
- Scheduling around Friday prayers, Sunday services, Ramadan or election periods without care; not accounting for sudden policy changes.

## Reference anchors

- Google Fonts and Noto script coverage (Latin Extended, Ethiopic, N'Ko, Adlam); SIL International fonts (Abyssinica SIL, Charis SIL, Andika) for African orthographies
- Safaricom M-Pesa developer documentation (Daraja) and brand guidelines; MTN MoMo, Wave, Flutterwave and Paystack docs
- GSMA *State of the Industry Report on Mobile Money* and *Mobile Economy Sub-Saharan Africa* (verify current editions)
- Nigeria NDPC, South Africa Information Regulator, Kenya ODPC and Ghana DPC guidance
- African design communities such as Design Indaba (Cape Town) and local studios and photographers credited by name
- Google "Next Billion Users" research and Android Go guidelines for low-end devices
