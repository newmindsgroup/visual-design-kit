---
id: market.canada
axis: market
name: Canada
aliases: [Canadian market, en-CA, fr-CA, Quebec, Canadian French, bilingual Canada]
summary: Officially bilingual (English and French) North American market where Quebec French law, Canadian spelling, Interac payments and accessibility statutes shape design.
tags: [canada, quebec, bilingual, french canadian, interac, bill 96, law 25, aoda, canadian english]
pairs_with: [industry.fintech-banking, industry.government-civic, industry.ecommerce-dtc, industry.healthcare-provider, industry.energy-climate, style.civic-plain, style.corporate-modern, channel.marketing-website, channel.web-app]
avoid_with: []
version_timestamp: 2026-10-20 02:17:13 UTC
---

# Canada

## Language and script

- English (en-CA) and French (fr-CA) are the official languages federally; Quebec's sole official language is French. Roughly three quarters of Canadians report English as a first official language and about a fifth French (Statistics Canada census; verify). Other common mother tongues: Mandarin, Cantonese, Punjabi, Spanish, Tagalog, Arabic. Indigenous languages (Cree, Inuktitut, Ojibwe and others) matter for public-sector and community work; syllabics need Noto Sans Canadian Aboriginal.
- Canadian English mixes British and American conventions: colour, centre, favourite (British) but -ize endings (organize) and "tire", "curb" (American). Use `lang="en-CA"`. Do not ship en-US copy to Canada unchanged.
- fr-CA differs from France French: vocabulary (courriel for email, fin de semaine, magasiner), no "tu" in formal commerce (use "vous"), no ligature oversights (keep oe/ae: cœur, œuvre), accents retained on capitals (ÉTÉ). Punctuation: a no-break space before : ; ! ? and inside « guillemets » is the traditional rule; Quebec's Office québécois de la langue française (OQLF) publishes the reference vocabulary (Grand dictionnaire terminologique).
- French is not a translation afterthought: write fr-CA natively or transcreate; France-French copy reads as foreign in Quebec.
- Reading level target: grade 6-8 for general public; the Government of Canada Content Style Guide favors plain language.

## Typography and layout

- Latin script with full Latin Extended-A diacritics (é è ê ë à â î ï ô û ù ü ç œ). Check fonts for oe ligature and uppercase accents. Safe families: Inter, IBM Plex Sans, Source Sans 3, Noto Sans, Lato; Canada.ca uses Lato and Noto Sans.
- Body 16px, line-height 1.5; French needs headroom for accented capitals, so keep display line-height at least 1.15.
- Text expansion: English to French +15-30%; plan buttons for +35%. Never size buttons to English labels; allow two lines in tabs and filters.
- Language toggle: a persistent "Français" / "English" link in the header (Canada.ca pattern), always labeled in the target language, preserving the current page when a twin exists.
- Hyphenation: set `hyphens: auto` with the right `lang`; avoid breaking before a trailing punctuation mark with the no-break space rule.
- Print: US Letter (8.5 x 11 in) is the Canadian standard, not A4; envelopes #10.
- Signage and packaging: bilingual layouts give English and French equal prominence (Consumer Packaging and Labelling Act), usually 1:1 text size or mirrored panels.

## Color and symbolism

- Red and white (flag) signal national identity; the maple leaf is a federal and consumer icon. Government of Canada identifiers (flag signature, "Canada" wordmark) are protected for official use; do not imitate them for commercial brands.
- Quebec has its own symbols (fleur-de-lis, blue and white flag); do not treat Quebec as a "French version of Canada" in imagery or tone.
- Winter palettes (snow white, icy blue, evergreen) fit seasonal retail; cold-climate realism (boots, layers) beats generic sun-and-beach stock.
- Poppies and red appear around Remembrance Day (Nov 11); orange signals the National Day for Truth and Reconciliation (Sept 30; "Every Child Matters"); use these only with understanding, never as decoration.
- Green for go, red for error is standard; same accessibility rules as elsewhere (no color-only status).

## Imagery and representation

- Canada is highly multicultural; about a quarter of people are immigrants (verify latest census). Show South Asian, Chinese, Filipino, Black, Indigenous, francophone and newcomer faces in everyday roles.
- Indigenous representation: commission Indigenous artists and photographers, credit them, and avoid pan-Indigenous motifs (totem poles, headdresses, "tribal" patterns) as decoration. Engage the specific Nations when content concerns them. Land acknowledgments should be sincere and tied to action, not boilerplate.
- Landscape clichés (moose, mountains, canoes, Mounties, hockey) are widely used and read as tourism; use sparingly in tech and finance.
- Show both official languages in imagery with text (storefronts, signs) in bilingual regions; in Quebec show French-only signage.
- Seasonal accuracy: winter lasts months in most regions; show it without making the whole country look rural.

## Formats and conventions

| Item | Convention | Example |
| --- | --- | --- |
| Date | Official standard is ISO YYYY-MM-DD; DD/MM/YYYY and MM/DD/YYYY both circulate | 2026-10-20; use spelled-out months in marketing |
| Time | 12-hour in English with a.m./p.m.; 24-hour in French (21 h 30) | 3:30 p.m. / 15 h 30 |
| Number en-CA | Comma thousands, period decimal | 1,234,567.89 |
| Number fr-CA | Space (no-break) thousands, comma decimal | 1 234 567,89 |
| Currency | CAD; en: $1,234.56; fr: 1 234,56 $ (symbol after) | 24,99 $ |
| Address | Number and street, unit, city, province (2 letters), postal code A1A 1A1 | 123 Rue Sainte-Catherine O, Montréal, QC H3B 1A7 |
| Phone | 10 digits | (514) 555-0147 or +1 514 555 0147 |
| Units | Metric (km, kg, °C); some imperial in everyday use (pounds, feet and inches, cooking) | |

- Province dropdown: 10 provinces and 3 territories; postal code letters never include D, F, I, O, Q, U; accept lowercase and optional space.
- Taxes: GST 5% federal; PST/HST by province; Quebec QST. Display tax-exclusive prices (retail norm) and itemize at checkout. Prices in CAD, not USD, for Canadian audiences.

## Platforms, devices and payments

- Smartphones: iOS roughly 55-60% of traffic and Android 40-45% (StatCounter; verify). Strong 4G/5G in cities; remote and northern communities have limited bandwidth, so keep pages light.
- Interac Debit is the default domestic debit network; Interac e-Transfer is the dominant P2P and bill-pay method (email or mobile number, Autodeposit); confirm with the processor how Interac Debit is offered online. Visa, Mastercard and Amex dominate credit; tap (contactless) limits are higher than in many markets.
- Wallets: Apple Pay, Google Pay, PayPal; BNPL: Affirm, Klarna, Afterpay, Sezzle. Cash on delivery is rare. Open banking (consumer-driven banking) is rolling out under federal law; verify the current framework status.
- Social: Facebook, Instagram, YouTube, TikTok, LinkedIn; WhatsApp is common in immigrant communities; Quebec has distinct media habits (e.g., Radio-Canada, TVA) and its own influencer scene.
- Federal digital identity and Quebec's own identity systems differ; do not assume a single national login.

## Regulatory and compliance notes

- **Privacy:** PIPEDA governs private-sector commercial activity federally (meaningful consent, accountability, breach reporting); Alberta and British Columbia have substantially similar laws. Quebec's Law 25 (phased in 2022-2024) adds strong consent (opt-in for tracking and profiling, high-privacy defaults, clear and simple consent requests, privacy impact assessments, a designated privacy officer, rules on automated decisions and cross-border transfers). Penalties are significant; design consent screens that are specific and layered, with tracking off by default for Quebec users.
- **Language:** Quebec's Charter of the French Language as amended by Bill 96: French must be available and markedly prominent in commercial websites, ads, contracts and product information aimed at Quebec; the main provisions took effect in stages, with the commercial and signage rules fully in force from June 1, 2025 (verify). English can accompany French but not overshadow it. Trademark exceptions apply with conditions.
- **Accessibility:** Accessible Canada Act (federally regulated sectors) and the Ontario AODA (websites of organizations with 50+ employees and the public sector must meet WCAG 2.0 AA; WCAG 2.2 AA is the safer target). Manitoba, Nova Scotia and British Columbia have their own accessibility statutes.
- **Messaging:** CASL (Canada's anti-spam law) requires consent (express or implied), identification and a working unsubscribe for commercial electronic messages, with large penalties.
- **Consumer rules:** provincial consumer protection acts regulate online contracts, cancellation and auto-renewals; Quebec's Consumer Protection Act is among the strictest.
- Confirm requirements with counsel for the specific product and jurisdiction.

## Localization pitfalls

- Shipping an English site with a machine-translated French tab: fails Bill 96 expectations and loses Quebec trust.
- Using France-French phrasing, tutoiement or euro-style formats (1 234,56 EUR) for Quebec users.
- Showing USD or US spelling; cross-border price shock (CAD versus USD) erodes trust.
- Treating postal codes like US ZIP codes: wrong validation rejects "H3B 1A7" with a space.
- Province-agnostic tax or shipping logic; HST/QST and territory surcharges differ.
- Using Indigenous art or language as decoration without permission.
- Assuming a French-speaking user is in Quebec: francophones live in New Brunswick, Ontario and Manitoba too.

## Reference anchors

- Canada.ca Design System (design.canada.ca) and the Government of Canada Content Style Guide
- Office québécois de la langue française (oqlf.gouv.qc.ca), Grand dictionnaire terminologique
- Interac Corp. brand and checkout guidance
- Office of the Privacy Commissioner of Canada (priv.gc.ca) and Quebec's Commission d'accès à l'information
- Accessibility Standards Canada and the AODA portal (ontario.ca/page/accessibility-laws)
- Statistics Canada census language data
