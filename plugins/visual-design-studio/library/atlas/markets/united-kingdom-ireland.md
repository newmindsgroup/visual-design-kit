---
id: market.united-kingdom-ireland
axis: market
name: United Kingdom and Ireland
aliases: [UK, Britain, Great Britain, GB, Ireland, Eire, en-GB, en-IE, British Isles, Wales, Scotland]
summary: English-language British and Irish markets with distinct spelling, GBP versus EUR, strong plain-language and accessibility traditions, UK GDPR/PECR and EU GDPR, and bilingual Welsh and Irish duties.
tags: [uk, ireland, britain, en-gb, gov.uk, uk gdpr, pecr, eircode, faster payments, open banking]
pairs_with: [industry.fintech-banking, industry.government-civic, industry.legal-professional-services, industry.hotels-travel, style.civic-plain, style.editorial-magazine, style.swiss-international, channel.marketing-website, channel.web-app, audience.older-adults]
avoid_with: []
version_timestamp: 2026-10-20 02:17:13 UTC
---

# United Kingdom and Ireland

## Language and script

- English (`en-GB`, `en-IE`) in Latin script. British spelling: colour, organisation (GOV.UK style prefers -ise; Oxford -ize also exists), centre, licence (noun) versus license (verb), cancelled, programme (but program for computing). Use `lang="en-GB"`.
- Wales: Welsh (Cymraeg) has official status; public bodies in Wales must meet the Welsh Language Standards, and many brands add Welsh. Welsh uses ŵ ŷ and the circumflex, grave, acute and diaeresis; fonts must support them. Welsh text expands about +15-25% and mutates initial letters (do not concatenate strings).
- Ireland: Irish (Gaeilge) is the first official language and English the second; Irish uses fadas (á é í ó ú) and traditionally dot-above consonants (ḃ ċ ḋ ḟ ġ ṁ ṗ ṡ ṫ) in older type. Dual-language public sector content is a legal duty (Official Languages Act), and brands in the Gaeltacht regions often add Irish. Scotland: Scottish Gaelic and Scots appear in public contexts (Gàidhlig uses grave accents).
- Tone: understated, polite, wry. British users distrust hard-sell superlatives; "brilliant", "cheers", "no worries" are natural for casual brands; do not overuse slang (innit, mate) or US idioms (awesome, y'all, "reach out").
- Vocabulary: lift (elevator), trousers, postcode, mobile, car park, bin, fortnight, "Ts and Cs", "post" (mail). Use "Sign in" and "Log in" consistently (GOV.UK prefers "Sign in").
- Plain English: the Government Digital Service (GDS) content design principles, reading age around 9 for public services. Avoid Latin abbreviations (e.g., i.e.) in public-facing copy.

## Typography and layout

- Fonts: Inter, IBM Plex Sans, Source Sans 3, Lato, Open Sans; for a British editorial feel, serifs such as Source Serif 4, Libre Baskerville, Newsreader; heritage voices use Johnston- or Gill Sans-like faces (Gill Sans is commercial; open alternatives include Jost). GOV.UK Frontend uses GDS Transport for gov.uk services and Arial elsewhere; its body type is 19px with 25px line-height (GOV.UK Design System type scale; verify the current frontend version).
- Body 16-19px, line-height 1.4-1.6, measure 66-75 characters (GOV.UK caps at about 2/3 of a page). Left-align text; avoid justified.
- Names routinely contain apostrophes (O'Brien), hyphens, fadas (Síle) and multi-word surnames; accept all of them and never strip diacritics. Use curly quotes in body copy but straight apostrophes inside data fields.
- Text expansion: not applicable from English; to Welsh and Irish +15-30%. For bilingual signage and websites, give equal prominence and keep language switch visible in the header.
- Layout: page-per-question forms ("one thing per page"), clear back links, summary lists with "Change" links, error summaries at the top; British retail pages are often dense with promotions but pre-checkout steps stay simple.
- Print: A4 (210 x 297 mm), not US Letter; envelope DL (110 x 220 mm); business card 85 x 55 mm; ISO paper sizes everywhere.

## Color and symbolism

- Red, white and blue (Union Jack) signals national identity; red pillar boxes, black cabs, green countryside and tartans are tourism clichés. Ireland uses green, white and orange tricolour; the shamrock and harp are national symbols. Orange and green carry political and sectarian associations in Northern Ireland; avoid these pairings in Northern Ireland-facing work unless intended.
- Poppies (red) around Remembrance (Nov 11) require care: wear them respectfully; do not use for promotion. Black ribbons and purple (Lent) also have mourning meanings.
- Navy and bottle green read as heritage and trust; pastel and sage palettes read as modern wellness; black and gold as premium.
- Weather-aware palettes: soft, muted greys-and-greens suit the regional light; bright sunny stock can feel foreign.
- Status colors need non-color cues (icons, text) per WCAG; GOV.UK uses red text plus a thick left border for errors.

## Imagery and representation

- The UK is diverse (in England and Wales, around 18% identify as Asian, Black, mixed or other ethnic groups per Census 2021; Ireland's population has grown more diverse, with large Polish, Indian, Brazilian, Romanian and Ukrainian communities; verify current figures). Represent a range of ages, regions, ethnicities, accents, abilities, class and religions.
- Regional identity: England, Scotland, Wales and Northern Ireland are distinct nations; "British" and "English" are not interchangeable, and Irish audiences dislike being grouped under "British Isles". Use "UK and Ireland". Do not use the Union Jack for Scotland-, Wales- or Ireland-specific work.
- Class and regional accents are politically sensitive; avoid caricature (cloth caps, posh countryside, Irish pub clichés, leprechauns, shamrock-and-Guinness defaults).
- Humour and irony can build brand but require tonal calibration; ASA and CAP codes police harm, offence, misleading claims, body image and gender stereotypes (Advertising Standards Authority rule on gender stereotypes since 2019).
- Photography: natural light, real homes, high streets and public transport (buses, trains, Tube) feel authentic; Irish imagery benefits from real places (not just cliffs and castles).

## Formats and conventions

| Item | Convention | Example |
| --- | --- | --- |
| Date | DD/MM/YYYY; long: 20 October 2026 (no comma, no ordinal) | 20/10/2026 |
| Time | 24-hour in transport and formal; 12-hour in speech; "am/pm" lowercase | 15:30 or 3.30pm |
| Number | Comma thousands, point decimal | 1,234,567.89 |
| Currency | £ in UK (GBP), € in Ireland (EUR); Northern Ireland uses sterling | £1,234.56 / €1,234.56 |
| Address | House number and street, town, (county), postcode | 10 Downing Street, London SW1A 2AA |
| Postcode | UK alphanumeric (5-7 characters, outward + inward); Ireland Eircode (7 characters, routing key + unique ID) | SW1A 1AA / D02 AF30 |
| Phone | UK +44 7xxx xxxxxx (mobile), 020 xxxx xxxx (London); Ireland +353 8x xxx xxxx | 07700 900123 |
| Name | Titles Mr, Mrs, Miss, Ms, Mx, Dr, Prof; no mandatory middle name | Seán Ó Briain |

- Postcode lookup: UK uses Royal Mail's Postcode Address File (PAF); Ireland uses Eircode/An Post. Allow manual address entry always.
- Units: metric for most things; miles for roads, pints for beer and milk, stones and pounds for body weight in everyday speech; keep unit toggles in health and fitness products.
- Week starts Monday; bank holidays (UK) vary by nation; Ireland has its own public holidays. Prices include VAT (20% UK, 23% Ireland standard; verify).

## Platforms, devices and payments

- iOS leads UK smartphone usage (roughly 50-55%, StatCounter; verify) and is stronger in Ireland among premium users. Wi-Fi and 4G/5G are widely available; rural broadband is patchier.
- Payments: debit cards dominate; contactless is the default (limit £100 in the UK since 2021), Apple Pay and Google Pay widely accepted; PayPal common online. **Faster Payments** and Open Banking "pay by bank" (Plaid, TrueLayer, Yapily) are growing; Direct Debit (Bacs) for recurring bills with the Direct Debit Guarantee; Klarna, Clearpay and PayPal Pay in 3 for BNPL (FCA regulation of BNPL started 15 July 2026; verify).
- Ireland: Revolut and AIB/Bank of Ireland, Apple Pay, Google Pay, SEPA transfers; Laser cards are gone. Cheques are rare in both.
- Identity: GOV.UK One Login (UK government), NHS login, Open Banking-based ID; Ireland's MyGovID for state services (verify current status).
- Retail ecosystems: Amazon UK, Tesco, Sainsbury's, John Lewis, ASOS, Argos, Boots; Ireland: Dunnes, SuperValu, Penneys/Primark, Brown Thomas.
- Messaging: WhatsApp dominant; SMS and email for transactional; strong newsletter and podcast culture; LinkedIn is key for B2B.

## Regulatory and compliance notes

- **Privacy (UK):** UK GDPR and Data Protection Act 2018 plus PECR for cookies and marketing. The Data (Use and Access) Act 2025 amended PECR: cookie provisions in force since 5 February 2026 add consent exemptions (statistical analytics, security, functionality, with clear information and an easy opt-out) while advertising cookies still need consent, and fines rise to the greater of £17.5m or 4% of turnover (verify against ICO guidance). Provide equal-prominence "Reject all" and "Accept all", granular choices, easy withdrawal.
- **Privacy (Ireland):** EU GDPR enforced by the Data Protection Commission, plus the ePrivacy Regulations 2011 for cookies and e-marketing.
- **Children:** ICO Age Appropriate Design Code (Children's Code) and the Online Safety Act 2023 (Ofcom age assurance for harmful content since mid-2025; verify); Ireland's Online Safety Code and Coimisiún na Meán for video platforms.
- **Accessibility:** Equality Act 2010 requires reasonable adjustments for services; public sector bodies follow the 2018 accessibility regulations (WCAG 2.1 AA, moving toward 2.2) and publish accessibility statements; Ireland follows the EU Web Accessibility Directive and the European Accessibility Act (applying to products and services from 28 June 2025). UK businesses selling into the EU must meet the EAA.
- **Consumer and finance:** Consumer Rights Act 2015, the Digital Markets, Competition and Consumers Act 2024 (CMA fines for fake reviews and drip pricing since April 2025; subscription rules expected later, reportedly spring 2027; verify), FCA Consumer Duty and financial promotions rules, ASA/CAP advertising codes, and the Consumer Contracts Regulations (14-day cancellation).
- Confirm requirements with counsel for the specific product and jurisdiction.

## Localization pitfalls

- US spelling and dates (month first) read as foreign; mm/dd/yyyy leads to booking errors.
- Quoting prices without VAT to consumers; prices must show VAT-inclusive totals.
- Treating Northern Ireland as Ireland (currency, law and politics differ) or the UK as England.
- A single "Postcode" field that rejects Eircodes or short UK postcodes; forcing a county field.
- Using "Ireland" imagery based on leprechauns, or "UK" imagery of only London; regional publics respond poorly.
- Cookie banners that hide "Reject"; ICO and CNIL-style enforcement make this costly.
- Ignoring Welsh duties for Welsh public-sector customers.
- Forgetting bank holiday and school-term calendars in campaign timing; Easter and Christmas shutdowns are long.

## Reference anchors

- GOV.UK Design System (design-system.service.gov.uk) and GDS content design principles
- Government Digital Service posts on accessibility and plain English; Plain English Campaign
- ICO guidance on cookies and the Children's Code; Data Protection Commission (Ireland)
- ASA and CAP Code (asa.org.uk); FCA Consumer Duty guidance
- Monzo, Starling, Revolut and Wise for UK-Irish fintech tone; BBC GEL and Nation Cymru style guides as public references
- Edward Johnston, Eric Gill and Margaret Calvert (road sign typography) for British type history
