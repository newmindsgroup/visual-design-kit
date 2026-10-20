---
id: market.southeast-asia
axis: market
name: Southeast Asia
aliases: [SEA, ASEAN, Indonesia, Thailand, Vietnam, Philippines, Malaysia, Singapore, Cambodia, Myanmar, Laos]
summary: Mobile-first, young, multilingual region (Latin, Thai, Khmer, Lao, Burmese scripts) where super apps, QR wallets, cash on delivery and messaging commerce shape design; laws differ by country.
tags: [southeast asia, asean, indonesia, thailand, vietnam, philippines, malaysia, singapore, super app, thai]
pairs_with: [industry.ecommerce-dtc, industry.fintech-banking, industry.marketplaces-platforms, industry.food-beverage-cpg, industry.gaming-esports, industry.hotels-travel, style.playful-bubbly, style.vibrant-gradient-saas, channel.native-app, audience.low-bandwidth-entry-devices]
avoid_with: []
version_timestamp: 2026-10-20 02:17:13 UTC
---

# Southeast Asia

## Language and script

- Do not treat the region as one market. Languages and scripts: Indonesian and Malay (Latin), Filipino/Tagalog and English (Latin), Vietnamese (Latin with tone marks), Thai (Thai script), Khmer (Cambodia), Lao, Burmese (Myanmar script), Mandarin, Tamil and English in Singapore and Malaysia. Religion, law and consumer habits differ: Muslim-majority Indonesia, Malaysia and Brunei; Buddhist Thailand, Cambodia, Laos and Myanmar; Catholic Philippines; mixed Vietnam and Singapore.
- Honorifics and register: Indonesian "Bapak/Ibu" and friendly "Kak" in commerce, "Anda" for neutral formal; Thai polite particles ครับ/ค่ะ are gendered, so UI often uses neutral phrasing; Vietnamese pronouns are relational, with "bạn" as a neutral UI default; Filipino uses "po/opo" for respect and Taglish is natural in social and marketing.
- Expansion from English (planning heuristics, verify with real copy): Indonesian/Malay +20-35%, Filipino +25-40%, Vietnamese +15-25%, Thai +10-30% in width, Khmer and Burmese +20-50%.
- **Thai:** no spaces between words; browsers segment with dictionaries when `lang="th"` is set; use `Intl.Segmenter` for truncation and wrap, and insert U+200B only where dynamic strings break badly. Thai uses the Buddhist Era (2026 CE = 2569 BE); government and formal documents use BE, commerce often Gregorian.
- **Vietnamese:** stacked diacritics (ế, ệ, ữ) need tall line-height and fonts that support the full Vietnamese set; normalize text to NFC so search and equality work.
- **Burmese:** legacy Zawgyi encoding conflicts with Unicode (Myanmar moved to Unicode around 2019); detect and convert. **Khmer, Lao, Burmese** need complex-script shaping: embed webfonts and test on low-end Android.
- Singapore English is British-based; Singlish is colloquial and fits social tone only.

## Typography and layout

| Script | Fonts (OFL) | Line-height | Notes |
| --- | --- | --- | --- |
| Thai | Noto Sans Thai, IBM Plex Sans Thai, Sarabun, Prompt, Kanit, Mitr, Bai Jamjuree, Noto Serif Thai | 1.6-1.8 | Tone marks stack above vowels; add 1-2px over Latin size; loopless faces are the modern default |
| Vietnamese | Be Vietnam Pro, Inter, Roboto, Noto Sans, Lexend, Montserrat | 1.5-1.7 | Check Ế Ệ Ỗ stacking; uppercase needs headroom |
| Khmer | Noto Sans Khmer, Battambang, Hanuman, Kantumruy Pro | 1.7-1.9 | Subscript consonants; tall line-height |
| Lao | Noto Sans Lao, Noto Sans Lao Looped | 1.6-1.8 | |
| Burmese | Noto Sans Myanmar, Padauk | 1.7-1.9 | Unicode only |
| Latin (ID, MY, PH) | Inter, Plus Jakarta Sans (designed in Indonesia), Poppins, Nunito Sans, DM Sans | 1.5-1.6 | Rounded friendly sans are popular |

- Do not apply letter-spacing, uppercase or italics to Thai, Khmer, Lao or Burmese. Avoid truncating mid-cluster. Body 16px mobile; Thai and Khmer at 17-18px read more comfortably.
- Layouts: mobile-first at 360-412px, dense feeds and cards, bottom tabs, sticky "Buy now" and chat buttons, banners with flash sales and vouchers. Marketplace-style pages (Shopee, Lazada, Tokopedia) set expectations: coupons, star ratings, sold counts, free-shipping badges, countdown timers. Premium and Singapore finance brands use cleaner layouts.
- Performance: entry-level Android and prepaid data; target pages under about 1-2 MB and apps under about 30-50 MB where reach matters; lazy-load images; support light and data-saver modes; offline-friendly flows.
- Video and chat first: short video, live commerce and WhatsApp/LINE/Zalo links often replace long forms. Voice messages are common in Indonesia and Thailand.
- Print: A4 in most countries; the Philippines commonly uses Letter and Legal bond paper.

## Color and symbolism

- Colors vary by community. Chinese communities (Singapore, Malaysia, Indonesia, Thailand, Vietnam) treat red and gold as auspicious at Lunar New Year; Malay Muslim communities use green, white and gold at Hari Raya; Tamil and Hindu communities use orange, gold and red at Deepavali; Thai tradition assigns colors to days of the week (yellow for Monday, associated with the monarchy). Number 4 is avoided by Chinese communities; 9 is auspicious in Thailand.
- National colors carry pride: Indonesia red-white, Thailand red-white-blue, Vietnam red with a yellow star, Philippines blue-red-white with yellow sun, Malaysia red-white-blue-yellow. Use flags carefully and never on disposable items.
- Mourning colors differ: Thai mourning dress is black (and white), Chinese funerals use white and black, and Muslim communities favor white shrouds with modest dark dress. Confirm with local reviewers rather than assuming.
- Bright, saturated and warm palettes work for consumer and super-app brands (Grab green, Shopee orange, Tokopedia green, GoTo green, Tiki blue), but each tier has its own cues; cool blues and navy for finance.
- Multi-ethnic markets need inclusive seasonal color systems: rotate festival palettes across communities rather than centering one.

## Imagery and representation

- Respect for royalty and religion is legally and socially critical: Thailand's lèse-majesté law (Section 112) and strong royal reverence apply to images, edits and humor; Malaysia and Brunei have strict royal and religious sensitivities. Do not use the monarchy, Buddha images or religious texts as decoration, logos, tattoos, footwear or fashion motifs (Buddha imagery is sensitive in Thailand, Myanmar, Cambodia and Laos).
- Body language: the head is sacred and feet are low in Buddhist cultures; avoid pointing feet or touching heads. In Muslim-majority countries use modest dress, avoid pork and alcohol imagery in general ads, and use halal context for food; hijab-wearing and non-hijab women both appear.
- Show the regional range: urban professionals, gig drivers, small shopkeepers (warung, sari-sari store), farmers, students, families and Indigenous communities (Orang Asli, Dayak, Igorot, hill tribes) with dignity.
- Avoid tropes: only rice paddies, conical hats, floating markets, beaches and "exotic" tourism. Avoid skin-lightening aspirations common in cosmetics ads; show wide skin tones.
- Sensitive maps and names: South China Sea (West Philippine Sea in the Philippines, Biển Đông in Vietnam), Myanmar, and border areas. Use neutral labels or client-approved terms per market.
- Representation of LGBTQ+ people, religion and politics is legally restricted in some countries (Malaysia, Indonesia, Brunei); consult counsel.
- Local celebrities, football, badminton, e-sports (Mobile Legends, Free Fire), K-pop and local music drive social proof.

## Formats and conventions

| Item | Convention | Example |
| --- | --- | --- |
| Date | DD/MM/YYYY; Philippines often MM/DD/YYYY; Thailand BE option | 20/10/2026 or 20 ตุลาคม 2569 |
| Time | 24-hour in Indonesia, Thailand (15.30 น.), Vietnam; 12-hour in Malaysia, Singapore, Philippines; Indonesia has WIB, WITA, WIT zones (UTC+7/+8/+9) | 15:30 |
| Number | Indonesia and Vietnam: 1.234.567,89; others: 1,234,567.89 | Rp 1.234.567 |
| Currency | IDR Rp, THB ฿, VND ₫ (after the number), MYR RM, SGD S$, PHP ₱, KHR ៛ (USD widely used in Cambodia) | 1.234.567 ₫ |
| Address | Indonesia: Jl., No., RT/RW, kelurahan, kecamatan, city, province, 5-digit code; Philippines: unit, street, barangay, city, province, 4-digit ZIP; Singapore: Blk, street, #unit, 6-digit postal code; Vietnam: house number, street, ward, province/city (district level abolished in 2025; verify) | Jl. Sudirman No. 10, RT 03/RW 05, Jakarta 12190 |
| Phone | +62 8XX, +66 8X/9X, +84 9X, +63 9XX, +65 8XXX XXXX, +60 1X | +62 812 3456 7890 |
| Name | Indonesia: mononyms common; Vietnam: family name first; Thailand: given + family plus nickname; Malaysia: bin/binti, a/l, a/p; Philippines: given + mother's maiden name + surname | Single "Full name" field |
| ID | NRIC (SG), MyKad (MY), KTP/NIK 16 digits (ID), Thai 13-digit ID, CCCD (VN) | Collect only when lawful |

- Addresses are often informal; support landmarks, map pins and delivery notes.
- Festival and shopping calendar: double days (9.9, 10.10, 11.11, 12.12) and payday sales, Ramadan and Lebaran/Hari Raya, Tet, Songkran, Lunar New Year, Christmas in the Philippines (a very long season from September), Sinulog and similar regional festivals.

## Platforms, devices and payments

- Android is roughly 65-90% of mobile traffic in most markets; Singapore is closer to iOS parity (StatCounter; verify). Low- and mid-range devices, prepaid data and variable networks are the norm outside Singapore.
- Super apps and marketplaces: Grab, GoTo (Gojek and Tokopedia), Shopee, Lazada, TikTok Shop, Tiki, Traveloka, Foodpanda. Messaging: WhatsApp (ID, MY, SG), LINE (Thailand), Zalo (Vietnam), Facebook Messenger (Philippines), Telegram, Viber. Social: Facebook (dominant in PH, VN, MM), TikTok, Instagram, YouTube.
- Payments (verify per country): Indonesia: QRIS (national QR), GoPay, OVO, DANA, ShopeePay, LinkAja, bank virtual accounts (VA), Indomaret/Alfamart cash, cash on delivery, paylater; Thailand: PromptPay (ID or phone-based QR), TrueMoney, Rabbit LINE Pay, ShopeePay, 7-Eleven payment; Vietnam: MoMo, ZaloPay, VNPay, VietQR (NAPAS), bank transfer, COD; Philippines: GCash, Maya, QR Ph, 7-Eleven (CLiQQ), Cebuana, COD, bank transfers (InstaPay/PESONet); Malaysia: DuitNow QR, FPX online banking, Touch 'n Go eWallet, Boost, GrabPay; Singapore: PayNow, SGQR, DBS PayLah!, cards, Apple Pay, GrabPay; Cambodia: Bakong QR, ABA Pay. Cash on delivery remains high in Indonesia, Vietnam and the Philippines; virtual-account payment needs a copyable number, bank list and expiry timer.
- ASEAN cross-border QR linkages let users pay with their home wallet in several countries; useful for tourism flows.
- Installments and BNPL: SPayLater, GoPayLater, Kredivo, Atome, Akulaku, Home Credit.
- Regional gotcha: Indonesia's 2023 ban on direct social-commerce transactions led TikTok Shop to partner with Tokopedia; platform rules change quickly.

## Regulatory and compliance notes

- **Singapore PDPA:** consent and purpose limitation, mandatory breach notification, Do Not Call Registry for marketing, penalties up to the higher of S$1 million or 10% of annual turnover for serious breaches (verify). **Thailand PDPA** (in force June 1, 2022): GDPR-like consent in clear Thai, representative for foreign controllers. **Indonesia PDP Law** (No. 27 of 2022, transition ended October 2024; implementing rules pending, verify) plus PSE registration for private electronic system operators. **Vietnam PDP Law** (91/2025/QH15, effective January 1, 2026; the earlier Decree 13/2023 status is being clarified, verify) and Cybersecurity Law localization duties. **Malaysia PDPA** (amended 2024: data protection officer, breach notification, portability; phased). **Philippines Data Privacy Act 2012** (NPC registration, 72-hour breach notice).
- **Consumer and e-commerce:** Singapore CPFTA, Philippines Internet Transactions Act (2023), Thai and Indonesian consumer protection laws; clear total prices, return policies, local-language terms. Indonesian halal certification is mandatory for many food, drink and cosmetics categories and requires the halal label.
- **Content and speech:** Thailand lèse-majesté; Singapore POFMA and online safety rules; Malaysia and Indonesia religion and decency rules; Vietnam content rules; Myanmar restrictions. Advertising codes cover alcohol, gambling, health and children.
- **Accessibility:** Singapore government WCAG 2.1 AA requirements and the Enabling Masterplan; disability laws exist in Malaysia, Thailand and the Philippines but private enforcement is limited. Target WCAG 2.2 AA.
- **Children:** age protections are expanding; check each country's rules for under-13 or under-16 data.
- Confirm requirements with counsel for the specific product and jurisdiction.

## Localization pitfalls

- Mixing markets: Indonesian copy for Malaysia, Singapore pricing for Indonesia, Taglish for formal Filipino finance.
- Missing e-wallet, QRIS/PromptPay/QR Ph, virtual-account and COD options; card-only checkout.
- Fonts without Thai, Khmer or Vietnamese diacritics; line-heights that clip stacked marks; letter-spacing on Thai.
- Heavy pages and apps for entry-level devices; ignoring data costs and spotty networks.
- Using royal, Buddha or religious imagery casually; pork or alcohol visuals in Muslim-majority markets.
- Western address forms (state and ZIP) and rigid name fields; mandatory national ID fields.
- Launching during Ramadan, Tet or Songkran without adjusting timing; ignoring local public holidays.
- Using wrong dates (BE versus CE), time zones across Indonesia, or Western-only celebrity casting.

## Reference anchors

- W3C Southeast Asian layout requirements (Thai, Khmer, Burmese) and Unicode script charts; Google Fonts script guides for Thai and Vietnamese
- Grab, GoTo, Shopee and Traveloka as public product and design references; Plus Jakarta Sans (Tokotype) and Be Vietnam Pro
- Bank Indonesia QRIS, Bank of Thailand PromptPay, NAPAS VietQR, BSP QR Ph, MAS PayNow documentation
- PDPC Singapore (pdpc.gov.sg), Thailand PDPC, Indonesia Kominfo/Komdigi, Vietnam MPS and Philippines NPC publications
- Google, Temasek and Bain *e-Conomy SEA* reports for market context (verify current edition)
- Singapore Government Design System (designsystem.tech.gov.sg)
