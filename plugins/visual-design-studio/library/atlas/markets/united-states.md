---
id: market.united-states
axis: market
name: United States
aliases: [US, USA, America, American market, en-US, US English]
summary: Large, diverse English-first market with Spanish as a major second language; shaped by card and wallet payments, a patchwork of state privacy laws, and ADA accessibility litigation.
tags: [united states, usa, american, en-us, us english, ccpa, ada, apple pay, venmo, state privacy]
pairs_with: [industry.fintech-banking, industry.saas-b2b, industry.ecommerce-dtc, industry.healthcare-provider, style.corporate-modern, style.vintage-heritage-americana, channel.web-app, channel.ecommerce-store, audience.older-adults]
avoid_with: []
version_timestamp: 2026-10-20 02:17:13 UTC
---

# United States

## Language and script

- Primary locale `en-US`: Latin script, American spelling (color, center, license, canceled), serial comma common, sentence-level plain language. Write at a 6th-8th grade reading level for consumer products; the US federal Plain Writing Act (2010) sets that tone for government content (plainlanguage.gov).
- Spanish is the largest second language (roughly 40 million people speak it at home per Census ACS). Next most common: Chinese, Tagalog, Vietnamese, Arabic, French, Korean (ACS; verify the current ranking). Offer Spanish first when localizing; see `market.us-hispanic-puerto-rico-caribbean` for bilingual patterns.
- Title Case versus sentence case: Apple HIG and Material both favor sentence case for UI labels; marketing headlines vary. Pick one rule per product and apply it everywhere.
- Inclusive language: singular "they" is accepted in most style guides (AP, Chicago, Microsoft, Google). Avoid sports idioms ("touch base", "home run", "out of left field") in products with international users; they do not translate.
- Name the file `lang="en-US"` in HTML so spell-check and hyphenation use the right dictionary.

## Typography and layout

| Item | Default | Override when |
| --- | --- | --- |
| UI font | System stack (SF Pro, Roboto, Segoe UI Variable) or Inter / IBM Plex Sans for brand | Brand needs personality: pair with a display serif such as Fraunces or a grotesk such as Schibsted Grotesk |
| Body size | 16px web, 17pt iOS body, 16sp Android | 18px+ for older adults or long-form reading |
| Line-height | 1.5 body, 1.2-1.3 headings | 1.65 for long articles |
| Measure | 60-75 characters | 45-55 for mobile columns |
| Text expansion | English is the source; budget +30% for most translations | Short labels and buttons need +40-50% |

- Print and PDF: US Letter (8.5 x 11 in), not A4; business card 3.5 x 2 in; envelope #10; slides 16:9. Margins 0.5-1 in. Offer both Letter and A4 downloads when the product ships abroad.
- Layout expectations: logo top-left, primary navigation top, "Sign in" and cart top-right, sticky header on mobile, footer with legal links ("Privacy Policy", "Terms", "Accessibility", plus the California opt-out link where required).
- Density is tolerated: marketplaces and SaaS dashboards commonly run dense. Long-scroll landing pages are normal; keep one primary call to action per viewport.
- Units: imperial (in, ft, lb, oz, fl oz, miles, degrees F). Show metric as a secondary unit for products sold abroad.

## Color and symbolism

- Red, white and blue read as patriotic; in news and political contexts red and blue also signal party (red Republican, blue Democratic since about 2000). Avoid a dominant red-plus-blue pair for nonprofits, civic tools or news products unless the political reading is intended.
- Green: money, "go", growth, and environmental claims. Stock tickers use green for up and red for down (reversed in China, Japan and Korea).
- Red: error, danger, sale. Yellow: caution. Pink and red: Valentine's. Orange and black: Halloween. Red and green: Christmas. Pastels: Easter and spring. Retail calendars (Black Friday, back to school) drive seasonal palette swaps.
- Black means luxury or formality in retail and mourning at funerals; white means weddings and cleanliness. Meanings vary by subculture and religion, so confirm with the audience.
- About 8% of men and 0.5% of women have red-green color vision deficiency (commonly cited estimates); never encode status by red versus green alone.

## Imagery and representation

- No single group is a majority of every region. Census estimates put non-Hispanic white around 58%, Hispanic around 19-20%, Black around 14%, Asian around 6% (verify the latest release). Show real range in age, body type, ability, family structure and region.
- Regional spread matters: avoid coastal-city-only imagery for national reach; include small-town, suburban, Southern and Midwestern settings when the audience is national.
- People with disabilities should appear in ordinary roles (work, family, leisure), not only in accessibility contexts.
- Candid photography with visible emotion and direct eye contact converts well in consumer categories. Avoid the stock "diverse team high-fiving around a laptop" shot and flat Corporate Memphis people illustrations, now widely read as generic.
- Flag use: the US Flag Code (4 U.S.C. 8) is advisory but discourages flag imagery in advertising and on disposable items. Use stars-and-stripes motifs with care and never alter the flag.
- Cultural calendar to plan around: Black History Month (Feb), Pride (Jun), Juneteenth (Jun 19), Independence Day (Jul 4), Hispanic Heritage Month (Sep 15-Oct 15), Thanksgiving, winter holidays. Use "holiday season" rather than assuming Christmas.

## Formats and conventions

| Item | Convention | Example |
| --- | --- | --- |
| Date | Month/Day/Year; spell out in long form | 10/20/2026 or October 20, 2026 |
| Time | 12-hour with AM/PM; 24-hour for aviation, military, healthcare | 3:30 PM |
| Week start | Sunday in calendars (CLDR en-US) | |
| Time zones | ET, CT, MT, PT with daylight saving (second Sunday of March to first Sunday of November); Arizona and Hawaii skip DST | 9:00 AM PT |
| Number | Comma thousands, period decimal | 1,234,567.89 |
| Currency | Symbol before amount, two decimals; negatives as -$12.50 (consumer) or ($12.50) (accounting) | $1,234.56 |
| Pricing | Shown before sales tax; tax added at checkout and varies by state and locality | $24.99 + tax |
| Address | Street number first, then unit, city, 2-letter state, ZIP or ZIP+4 | 350 5th Ave, Apt 4B, New York, NY 10118 |
| Phone | 10 digits with area code | (415) 555-0132 or +1 415 555 0132 |
| Name | First, middle, last; suffixes (Jr., III) | Use one "Full name" field when possible |

- ZIP lookup should auto-fill city and state. Include DC and the territories in state lists. Do not require a Social Security number unless a law demands it; mask input and display only the last four digits.
- Restaurant and service checkouts show tip presets (commonly 18, 20, 25%) on payment screens.

## Platforms, devices and payments

- Mobile OS: iOS holds roughly 55-60% of US mobile traffic and Android 40-45% (StatCounter; verify). Premium device mix and 5G coverage are strong, but rural broadband gaps persist. Design iOS-first for consumer apps, then verify Android parity.
- Browsers: Chrome leads desktop; Safari is strong on mobile, so test WebKit behavior (viewport units, input zoom, date inputs).
- Cards dominate: Visa, Mastercard, American Express (15 digits, 4-digit CID), Discover. Wallets: Apple Pay, Google Pay, PayPal, Shop Pay. P2P: Venmo, Zelle, Cash App. BNPL: Affirm, Klarna, Afterpay. ACH bank transfer via Plaid-style linking for B2B and subscriptions. HSA/FSA and EBT cards matter in health and grocery.
- Apple requires Sign in with Apple when an iOS app offers third-party social login (App Store Review Guidelines; verify current wording).
- Channels: SMS and email remain primary for transactional and marketing messages; WhatsApp is niche outside immigrant communities; TikTok, Instagram, YouTube, Facebook, Reddit and LinkedIn (B2B) drive social.

## Regulatory and compliance notes

- **Accessibility (ADA):** Title III has no codified web standard, but courts and the DOJ treat many commercial sites and apps as public accommodations; thousands of web accessibility suits are filed yearly, and California's Unruh Act adds statutory damages. Target WCAG 2.2 AA. Title II (state and local governments): the 2024 DOJ rule requires WCAG 2.1 AA; an April 2026 interim final rule moved deadlines to April 26, 2027 (population 50,000+) and April 26, 2028 (others). Federal procurement follows Section 508.
- **Privacy:** There is no comprehensive federal law; about 20 states have one (California CCPA/CPRA, Virginia, Colorado, Connecticut, Texas and others; counts vary by tracker). Typical design impact: notice at collection, a visible "Do Not Sell or Share My Personal Information" link, opt-out preference signals such as Global Privacy Control honored in several states, and opt-in for sensitive data in many states. Washington's My Health My Data Act adds consent for consumer health data.
- **Children:** COPPA (under 13) requires verifiable parental consent; the amended FTC rule's compliance date was April 22, 2026. Avoid persistent identifiers for child-directed audiences.
- **Marketing and dark patterns:** FTC Act Section 5 (deceptive design), ROSCA and state auto-renewal laws (clear terms, express consent, easy cancellation; the FTC's 2024 click-to-cancel rule was vacated in 2025 but these laws remain), CAN-SPAM (working unsubscribe, physical address), TCPA (prior express written consent for marketing texts), FTC fake-review rule and Endorsement Guides (#ad disclosures), and all-in price display for live-event tickets and short-term lodging.
- **Sector rules:** HIPAA (health), GLBA (financial privacy notices), state insurance and lending disclosures.
- Confirm requirements with counsel for the specific product and jurisdiction.

## Localization pitfalls

- Using MM/DD/YYYY or "ZIP code" and a required state field in a global form locks out other countries; localize address and date inputs by country.
- Quoting prices without tax confuses VAT markets; the reverse (tax-inclusive prices) can read as inflated in the US.
- Assuming every user has a credit card, a Social Security number or a US phone number excludes immigrants, students and visitors.
- Treating "American" as one culture: regional, racial, generational and political differences are large; test with the real audience segment.
- Over-polishing legal copy: stacked cookie banners and wall-of-text terms are ignored; use layered notices.
- Forgetting Alaska, Hawaii and territories in shipping and tax logic.

## Reference anchors

- U.S. Web Design System (designsystem.gov) and plainlanguage.gov for civic patterns and plain language
- Apple Human Interface Guidelines and Material Design 3 for platform conventions
- Mailchimp Content Style Guide (styleguide.mailchimp.com) for American product voice
- W3C WCAG 2.2 and Section508.gov for accessibility baselines
- Pew Research Center and U.S. Census Bureau for audience data
- Baymard Institute checkout research for US ecommerce patterns
