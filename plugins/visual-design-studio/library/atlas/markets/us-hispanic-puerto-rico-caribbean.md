---
id: market.us-hispanic-puerto-rico-caribbean
axis: market
name: US Hispanic, Puerto Rico and the Caribbean
aliases: [US Hispanic, Latino market, Hispanic marketing, Puerto Rico, boricua, Caribbean, Spanglish, bilingual EN/ES]
summary: Bilingual English/Spanish design for US Hispanic and Latino audiences, Puerto Rico (a US territory with Spanish dominant) and Caribbean markets; varied origins, Spanish variants and payments.
tags: [hispanic, latino, puerto rico, caribbean, bilingual, spanish, spanglish, ath movil, zelle, remittances]
pairs_with: [industry.fintech-banking, industry.food-beverage-cpg, industry.healthcare-provider, industry.media-entertainment-streaming, industry.ecommerce-dtc, style.playful-bubbly, style.illustrative-narrative, channel.social-media, channel.native-app, archetype.caregiver]
avoid_with: []
version_timestamp: 2026-10-20 02:17:13 UTC
---

# US Hispanic, Puerto Rico and the Caribbean

## Language and script

- Latin script; Spanish needs ¿ ¡, ñ, and accents on every vowel including capitals (ACCIÓN, not ACCION). Roughly one in five US residents identifies as Hispanic or Latino (about 65-68 million, Census Bureau estimates; verify). This is not one culture: Mexican American, Puerto Rican, Cuban American, Dominican, Salvadoran, Colombian and many others differ in food, music, vocabulary, history and politics.
- Language use is a spectrum: Spanish-dominant, bilingual, and English-dominant U.S.-born users who relate to Spanish emotionally. Offer a persistent EN | ES toggle, remember the choice, and never auto-switch by guessing from name or ZIP code.
- Terminology: "Hispanic" and "Latino/Latina" are both widely used; preferences vary by region and person (Pew Research surveys show many prefer their national origin, e.g., Puerto Rican). "Latinx" is used by a small minority of the people it describes; prefer "Latino/a" or neutral rewording (la comunidad, las personas) unless the audience asks otherwise.
- Puerto Rico: Spanish and English are both official, Spanish dominates daily life, and English use is common in professional and online contexts. Puerto Rican Spanish features include dropped or aspirated final consonants (spoken), "china" for orange, "guagua" for bus, "zafacón" for trash can, "chavos" for money, and "boricua" as an identity term. Use regional words sparingly, and only after review by native writers from the island; a neutral international Spanish baseline is safer for UI.
- Other variants: Mexican (computadora, celular, camión for bus), Caribbean Cuban/Dominican (carro, guagua), Spain (ordenador, móvil, vosotros, which US audiences do not use). Use "ustedes" for plural you. Use "tú" for consumer apps and youth; "usted" for banking, healthcare, older adults and first contact.
- Spanglish and code-switching are natural in social, music and youth contexts; use in headlines only when the brand voice is truly bilingual, never as a gimmick. Translate meaning, not words (transcreate slogans); avoid machine-only translation.
- Other Caribbean languages: Haitian Creole (Kreyòl), Jamaican Patois (rarely written in UI), French in the Antilles, Dutch and Papiamento in ABC islands, English in Jamaica, Trinidad and the Bahamas.

## Typography and layout

- Spanish expands +20-30% over English; design bilingual buttons and tabs for +35%. Long words and two-line labels need space.
- Sentence case: Spanish capitalizes only the first word of headlines and proper nouns; months and days are lowercase (15 de octubre de 2026). Avoid all-caps body copy; if caps are needed, keep accents.
- Fonts need Latin Extended-A and accented capitals: Inter, Nunito Sans, Poppins, Montserrat, Lato, Noto Sans. Display options with Latin warmth: Fraunces, DM Serif Display, Baloo 2 for playful. Check ¿ ¡ glyph height and ñ tilde collisions with tight line-height (keep display at 1.15+).
- Bilingual layouts: toggle (best for apps, avoids doubling content), parallel columns (print, signage; Spanish second only if English is truly the lead), or stacked (packaging, flyers, where space is tight). Give both languages equal weight and size when audiences are mixed; do not set Spanish smaller.
- Hyphenation: enable with `lang="es"`; Spanish breaks at syllables.
- Layout can be warm and lively, but legibility rules still apply; avoid dense sales-flyer clutter in digital.

## Color and symbolism

- Warm, saturated palettes are a common reference in the category (coral, marigold, teal, magenta), but they are not required; do not default every Hispanic-facing brand to red-yellow-orange or to "fiesta" colors. Match the product category and sub-audience.
- Flags and national colors carry strong identity: Puerto Rican flag (red, white, blue with a white star), Dominican, Cuban, Colombian, Mexican. Puerto Rican flag shades and the black-and-white variant carry political meaning around the status debate and protest; avoid casual recoloring or decoration with flags.
- Religious color: purple (Lent, Holy Week), white and gold (weddings, Catholic ceremonies), and Day of the Dead (Mexican, mostly Mexican American) marigold orange. Use only when the audience and occasion fit; never as generic "Latin" decoration.
- Flower and candle symbolism around mourning and remembrance differs by country and community; ask a local reviewer before using it.
- Always meet WCAG contrast; warm yellows and oranges fail 4.5:1 on white as text.

## Imagery and representation

- Show range: skin tones from light to dark, Afro-Latino and Indigenous Latino people, mixed families, multigenerational households, young professionals, students and older adults. Latino audiences are diverse in income and education; avoid cartoonish stereotypes (sombreros, mustaches, maracas, tropical-beach-for-everyone, domestic-worker roles only, gang-or-crime tropes, "spicy" food puns).
- Reflect real life: U.S.-born bilingual youth, small-business owners, healthcare workers, tech people, parents managing two languages. Family and community matter, but do not reduce Latino identity to family-only.
- Puerto Rico imagery: avoid showing only hotel beaches or only disaster. Include urban San Juan, mountain towns, local businesses, and everyday life; the island has endured hurricanes (Maria 2017) and recurring outages, so resilience stories should be told with respect and not used as marketing drama.
- Use local casting and locations; hire Latino photographers, illustrators and writers.
- Music, food and sports references vary by origin (reggaeton and salsa for Caribbean audiences, regional Mexican for Mexican Americans, baseball for Caribbean, soccer broadly). Do not assume.

## Formats and conventions

| Item | Convention | Example |
| --- | --- | --- |
| Date | Spell out the month to avoid DD/MM versus MM/DD ambiguity; both circulate | 20 de octubre de 2026 |
| Time | 12-hour with a. m./p. m. or 24-hour in formal text | 3:30 p. m. |
| Number | US: 1,234.56; most of Latin America and Spain use a comma decimal | US Hispanic audience: follow the US |
| Currency | USD in US and Puerto Rico; DOP (RD$) Dominican; JMD, TTD, BBD elsewhere | $1,234.56 |
| Address (PR) | Urbanización, street, number, city, PR, ZIP 006xx-009xx | Urb. Villa Carolina, Calle 12 #234, Carolina, PR 00985 |
| Phone | PR area codes 787, 939; US format | (787) 555-0123 |
| Name | Two surnames: given name + paternal + maternal | María Rivera Santiago |

- Name fields: allow two last names, particles (de la, del) and accented characters; do not force a middle initial. Sort by first surname.
- Address fields: support "Urb.", "Cond.", "Res.", "Bo." and highway addresses (Carr. 2 Km 15.3); Puerto Rico ZIP codes begin 006-009.
- IVU (Impuesto sobre Ventas y Uso), Puerto Rico's sales tax, is generally cited as 11.5% (10.5% state + 1% municipal; verify with Hacienda); show a tax line at checkout.

## Platforms, devices and payments

- Mobile-first: Hispanic users over-index on smartphone-only internet use compared with other US adults (Pew Research; verify the latest release). Design for smaller screens, prepaid plans and data-saving modes.
- Messaging: WhatsApp is widely used in Latino communities and the Caribbean diaspora; Facebook, Instagram, YouTube, TikTok; SMS remains a reliable channel with consent.
- Payments in the US: Zelle (bank P2P, strong for family), Cash App, Venmo, PayPal, Apple Pay, debit cards; cash is still common and some users are unbanked or underbanked, so reload-at-store or cash-based options (e.g., at retailers) may be valuable. Remittances: Remitly, Western Union, Xoom, MoneyGram.
- Puerto Rico: ATH Móvil (Evertec) is the dominant mobile P2P and merchant wallet, with a deep local merchant base; ATH debit network; Banco Popular, FirstBank, Oriental, Santander. Cards, Apple Pay and Google Pay also work.
- Dominican Republic and other Caribbean markets: local acquirers and cash on delivery vary by country (e.g., Azul in the Dominican Republic); verify per country. Cuba has restricted access to US payment services because of sanctions.
- Connectivity: hurricane season (June-November) and grid outages mean offline-friendly forms, quick re-authentication and saved drafts are valuable.

## Regulatory and compliance notes

- **US federal law applies in Puerto Rico**: ADA, COPPA, CAN-SPAM, TCPA, FTC Act, HIPAA, GLBA and federal civil rights laws. Puerto Rico also has local consumer protection (DACO, Departamento de Asuntos del Consumidor) and its own statutes; verify whether any comprehensive local privacy law has been enacted.
- **Spanish-language consumer protection:** disclosures, terms and ads must be accurate and not misleading in the language used. Some US states require translations of certain contracts negotiated in Spanish (for example, California Civil Code 1632); the FTC and CFPB have acted on deceptive Spanish-language marketing and sales.
- **Privacy:** state laws (CCPA/CPRA, Texas, Florida's more limited law and others) apply by user residence. Sensitive data (immigration status, health) deserves explicit care: avoid collecting immigration status, explain data use in plain Spanish, and be careful with location data.
- **Accessibility:** ADA and Section 508 apply; provide Spanish screen-reader labels (`lang="es"` on Spanish segments).
- **Caribbean:** data protection laws vary (for example, Jamaica's Data Protection Act and the Dominican Republic's Law 172-13); language and consumer rules differ by country; French territories follow EU rules (GDPR).
- Confirm requirements with counsel for the specific product and jurisdiction.

## Localization pitfalls

- Treating "Hispanic" as one audience; segment by origin, language preference, generation and region.
- Using Mexican slang for a Puerto Rican or Dominican audience, or Spain's vosotros and ordenador.
- Literal translation of English slogans; puns rarely survive, and some words carry local vulgar meanings (for example, "coger" in parts of Latin America).
- Missing accents on capitals; breaking ¿ ¡ in dynamic strings; fonts lacking ñ.
- Assuming a Spanish speaker has low English proficiency, or that a Spanish name means Spanish-language preference.
- Auto-detecting language from IP or name; always provide a visible switch.
- Collecting ZIP codes without supporting Puerto Rico urbanización addresses; rejecting PR phone numbers.
- Using flags, hurricane imagery or political symbols casually in Puerto Rico campaigns.

## Reference anchors

- Pew Research Center, Hispanic Trends (pewresearch.org/race-and-ethnicity)
- U.S. Census Bureau, Hispanic Origin data
- Real Academia Española (rae.es) and Fundéu for correct Spanish usage; *Diccionario de americanismos* (ASALE)
- Evertec and ATH Móvil merchant materials
- Univision and Telemundo brand and audience research as public references for Spanish-language media
- Selig Center / Nielsen reports on Hispanic consumer markets (verify current editions)
