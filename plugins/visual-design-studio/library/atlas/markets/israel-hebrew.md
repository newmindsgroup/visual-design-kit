---
id: market.israel-hebrew
axis: market
name: Israel (Hebrew)
aliases: [Israel, Hebrew, he-IL, RTL Hebrew, Israeli market, Start-up Nation]
summary: Hebrew right-to-left market with a tech-savvy, direct, mobile-first audience, Hebrew-Arabic-Russian-English multilingualism, installment-heavy payments and Shabbat and holiday rhythms.
tags: [israel, hebrew, rtl, he-il, shabbat, bit, installments, ils, amendment 13]
pairs_with: [industry.saas-b2b, industry.fintech-banking, industry.developer-tools, industry.ecommerce-dtc, industry.healthcare-provider, industry.events-conferences, style.dark-tech-developer, style.corporate-modern, channel.web-app, channel.native-app]
avoid_with: []
version_timestamp: 2026-10-20 02:17:13 UTC
---

# Israel (Hebrew)

## Language and script

- Hebrew (`he-IL`) is written right to left in the square script (Ktav Ashurit); 22 letters, five final forms (ך ם ן ף ץ), no capitals, no true italics. Vowel marks (niqqud) are used in children's books, poetry, liturgy and for learners; everyday text is unvocalized. Cursive Hebrew is used in handwriting and playful or children's branding.
- Arabic has special status in law and is used by Arab citizens (roughly a fifth of the population; verify), and Russian, Amharic and English are widely spoken. Public-sector and national brands offer Hebrew and Arabic; startups and B2B often offer English too. Treat Arabic as an RTL peer, not an afterthought; see `market.middle-east-north-africa-arabic` for Arabic typography.
- **Grammatical gender in UI:** Hebrew verbs and adjectives inflect for gender. Avoid slash forms (לחץ/י, בחר/י) in polished copy; use the plural imperative (לחצו, בחרו), the infinitive (ללחוץ) or noun phrases. Decide a house rule and apply it everywhere.
- Punctuation: Hebrew uses gershayim ״ (U+05F4) in acronyms (צה״ל) and geresh ׳ (U+05F3) for abbreviations; avoid straight quotes inside acronyms. Maqaf (־) is the Hebrew hyphen. Parentheses and brackets mirror in RTL text.
- Tone: informal, direct and fast; Israelis dislike marketing fluff and long onboarding. Humor and irony are common; avoid overly formal translations ("בבקשה" in every line). Use first names; "you" is unmarked in plural forms.
- Text expansion: Hebrew runs about 15-25% shorter than English in characters because vowels are omitted, but mixed English terms (brand names, code) increase bidi complexity; plan for slightly more height for diacritics when niqqud is used. Test with real copy.
- Calendars: Gregorian for business; the Hebrew calendar (lunisolar) sets holidays and school years (Rosh Hashana, Yom Kippur, Sukkot, Pesach, Shavuot, Hanukkah, Purim). Show Hebrew dates only where relevant (events, religious products).

## Typography and layout

| Item | Default | Override when |
| --- | --- | --- |
| UI fonts (OFL) | Heebo, Assistant, Rubik, Noto Sans Hebrew, IBM Plex Sans Hebrew, Open Sans Hebrew | Geometric/rounded brands: Varela Round, Rubik |
| Display | Secular One, Suez One, Alef, Karantina (display), Heebo Black | Brand needs more personality |
| Serif | Frank Ruhl Libre, David Libre, Miriam Libre, Noto Serif Hebrew | Editorial, legal, cultural |
| Commercial | Fedra Hebrew, Narkis Tam, platform system fonts (Arial Hebrew, Segoe UI) | Large programs |
| Body size | 16-18px; Hebrew appears slightly smaller than Latin at the same size | Dense data: 14px minimum |
| Line-height | 1.5-1.65 (Hebrew has fewer tall ascenders than Arabic) | Niqqud: 1.8+ |
| Weights | 400, 500, 700; avoid very light weights at small sizes (ד/ר, ו/ן, ב/כ look alike) | Headlines may go 800-900 |
| Italics | Do not slant Hebrew; use bold, color or underline for emphasis | Latin words may italicize |

- Set `lang="he"` and `dir="rtl"`; use CSS logical properties and `unicode-bidi: isolate` or `<bdi>` for mixed-direction fragments.
- **Mirror in RTL:** layout, navigation, back/next arrows, progress, carousels, tabs, form alignment, list bullets, swipe gestures, chart category order. **Do not mirror:** numbers and phone numbers, Latin brand names and code, media controls, clocks, photographs, logos; real-world icons stay as they are.
- Hebrew letterforms are square and compact; avoid ultra-condensed and ultra-thin fonts. When matching Latin and Hebrew in one lockup, align cap height to Hebrew letter height and keep weights equal.
- Tracking: normal Hebrew text uses 0 letter-spacing; slightly positive spacing (+0.01-0.03em) is acceptable for small labels.
- Layout: Israeli sites are often dense and promotion-heavy in retail; tech and B2B favor sleek, product-led layouts in English-influenced styles. WhatsApp contact links and phone numbers appear prominently.
- Print: A4; Hebrew books bind on the right; page numbers and tables run RTL.

## Color and symbolism

- Blue and white (the flag, tallit stripes, Star of David) are national colors and appear widely in civic and holiday marketing; use them with care in commercial work, especially near Independence Day (Yom HaAtzmaut) and memorial days (Yom HaShoah, Yom HaZikaron), when promotional tone is inappropriate.
- Political and religious contexts attach to colors and symbols (flag, menorah, olive branch, ribbons of various colors); since October 2023 symbols tied to the war and hostages are emotionally charged. Avoid appropriating them for brand tone; follow the lead of respected local brands and sectors.
- Mediterranean palettes (sea blue, stone, olive, citrus) fit tourism and food; high-contrast neon and dark mode are common in tech.
- Black and white are neutral. Red also evokes the "Red Alert" (Tzeva Adom) rocket-siren system, so avoid alarm-style red screens and sounds in non-urgent contexts.

## Imagery and representation

- Israeli society is diverse: Jewish Israelis from Ashkenazi, Mizrahi, Sephardi, Ethiopian, Russian-speaking and other backgrounds, secular, traditional (masorti), religious Zionist and Haredi (ultra-Orthodox) communities, and Arab citizens (Muslim, Christian, Druze, Bedouin). Show this range; avoid defaulting to one group.
- Haredi audiences expect modest dress and often no images of women in publications; if you target this community, work with community-specific agencies, use separate creative, and expect filtered-internet ("kosher phone") contexts. Do not assume the same imagery works for secular audiences.
- Avoid stereotypes about Israelis (soldiers everywhere, desert, tech bros, Jerusalem stone only) and about Arabs and Haredim. Mandatory military service means many young adults have served; reservist (miluim) benefits appear in campaigns, which should be genuine.
- Maps and place names are politically sensitive (Jerusalem, the West Bank, Gaza, the Golan). Use the client's reviewed, market-specific map set and terminology; when serving multiple markets (see MENA), expect different legal and reputational constraints.
- Respect Shabbat and Jewish holidays in imagery (candles, challah, family tables) only when authentic; avoid showing work or commerce on Yom Kippur.
- Product categories: alcohol, pork and shellfish content depends on the audience; kosher certification matters in food and hospitality.

## Formats and conventions

| Item | Convention | Example |
| --- | --- | --- |
| Date | DD/MM/YYYY (also D.M.YYYY); long form with Hebrew month names | 20/10/2026 |
| Week | Sunday-Thursday workweek; Friday half-day or off; Saturday is Shabbat | Calendars start Sunday |
| Time | 24-hour | 15:30 |
| Number | Comma thousands, point decimal; Western digits | 1,234.56 |
| Currency | New shekel (ILS), ₪ displayed to the left of the amount in RTL (number then symbol in logical order) | ‏1,234.56 ₪ |
| Address | Street, house number, apartment, city, 7-digit postal code | הרצל 10, תל אביב, 6578201 |
| Phone | +972 5X XXX XXXX (mobile 05X); landlines 02, 03, 04, 08, 09 | 050-123-4567 |
| ID | 9-digit Teudat Zehut with check digit | Validate; mask when displayed |
| Name | Given + family name; Arabic and Russian names are common | Accept non-Hebrew scripts |

- Shabbat (Friday sunset to Saturday night) affects delivery, push notifications and public transport; Jewish holidays close most businesses. Show estimated delivery on business days (Sunday-Friday). Offer a Shabbat-aware scheduling option where relevant.
- VAT: 18% from January 2025 (verify); prices shown to consumers include VAT.
- Installments ("תשלומים") of 3-12 or more are expected at checkout; show the installment amount and whether interest applies.

## Platforms, devices and payments

- Smartphone usage is among the highest in the world; iPhone and Android are roughly balanced to iOS-leaning (about half each; verify). 5G is available in cities. Israelis expect fast, polished apps and instant support.
- Messaging and social: WhatsApp dominates (family and business groups), Facebook groups and Marketplace, Instagram, TikTok, Telegram; LinkedIn matters for tech. WhatsApp Business catalogs and click-to-chat links are common for local commerce.
- Payments: credit cards (Isracard, Cal, Max) with Apple Pay and Google Pay; **Bit** (Bank Hapoalim's P2P and checkout app) and **PayBox** for P2P and groups; bank transfers; PayPal is less central. Show card installment options and tokenized saved cards; offer Bit at checkout for mobile conversion.
- Local platforms: Wolt, 10bis, Yad2 (classifieds), Super-Pharm, Shufersal, KSP, Zap price comparison, Gett and Moovit (transit).
- Identity and government: gov.il accounts and digital ID; the government design system follows RTL and accessibility rules.
- Government and municipal services rely on SMS OTP and ID number plus phone.

## Regulatory and compliance notes

- **Privacy:** Protection of Privacy Law 1981, significantly amended (Amendment 13) with effect from August 14, 2025: broader definition of personal information, tighter notice and consent, a data protection officer requirement for certain organizations, reduced database registration and stronger Privacy Protection Authority fines. The EU recognizes Israel as adequate for GDPR transfers (verify current status).
- **Spam law:** the Communications Law's Section 30A requires prior opt-in consent for commercial messages (with limited exceptions for existing customers), the word "פרסומת" (advertisement) at the start, and an easy opt-out; fines apply (verify details with counsel).
- **Accessibility:** the Equal Rights for Persons with Disabilities Law 1998 and the 2013 service accessibility regulations require accessible websites and apps, based on Israeli Standard 5568 (aligned with WCAG 2.0 AA, with debate on newer versions; confirm the applicable version). An accessibility statement (הצהרת נגישות) with a named contact is expected. Private lawsuits for inaccessible sites are common; target WCAG 2.2 AA.
- **Consumer law:** the Consumer Protection Law 1981 and distance-sale regulations (cancellation within 14 days, with limited fees; verify), clear total price and Hebrew-language product information and labels.
- **Financial services:** Bank of Israel and Capital Markets regulators require standardized disclosures; open banking (Financial Information Service Law 2021) is rolling out.
- **Sensitive content:** hate speech, incitement and defamation laws; trademark and "Made in Israel" rules; war-related content may carry special restrictions.
- Confirm requirements with counsel for the specific product and jurisdiction.

## Localization pitfalls

- Mirroring problems: numbers reversed, parentheses flipped wrongly, punctuation jumping to the wrong end (use `dir` and Unicode marks), mixed English terms breaking line order.
- Using slash gender forms or masculine-only copy; translating "you" without a gender policy.
- Putting a Latin-style date (MM/DD) or thinking the week starts Monday; scheduling deliveries on Shabbat.
- Unsubstantiated tone: heavy hype or flowery formal Hebrew; Israelis prefer plain, quick copy.
- Hebrew fonts that lack a bold weight, giving faux-bold; narrow fonts that confuse similar letters.
- Using flags, military or war imagery for promotion; running upbeat campaigns on memorial days.
- Skipping installments and Bit; omitting Arabic for services that serve Arab citizens.
- Forgetting an accessibility statement and a visible contact for accessibility.

## Reference anchors

- W3C Internationalization: Hebrew layout requirements and the Unicode Bidirectional Algorithm (UAX #9)
- Fonts: Heebo, Assistant, Rubik, Frank Ruhl Libre, IBM Plex Sans Hebrew (OFL); Ben Nathan, Henri Friedlaender (Hadassah Hebrew), Zvi Narkiss (Narkis), Ada Yardeni (Hebrew type history)
- Israel Standards Institute SI 5568 and the Israeli Commission for Equal Rights of Persons with Disabilities (gov.il)
- Israel's Privacy Protection Authority guidance on Amendment 13 (gov.il)
- Bit, PayBox, Wolt, Monday.com, Wix and Gett as public product references
- Israel's government design system and digital-services guidance (gov.il)
