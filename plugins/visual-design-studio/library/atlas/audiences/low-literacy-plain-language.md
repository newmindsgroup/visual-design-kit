---
id: audience.low-literacy-plain-language
axis: audience
name: Low Literacy / Plain Language
aliases: [low literacy, plain language, plain english, easy read, health literacy, esl, limited english proficiency, functional literacy]
summary: People who read slowly, in a second language or under stress; write at grade 5-6, show one step at a time, pair icons with words and never make comprehension a hurdle to a service.
tags: [plain language, low literacy, readability, health literacy, easy read, icons, forms, government]
pairs_with: [style.civic-plain, style.flat-material, style.illustrative-narrative, industry.government-civic, industry.nonprofit-ngo, industry.healthcare-provider, industry.fintech-banking, archetype.everyperson, archetype.caregiver, market.india-south-asia]
avoid_with: [style.kinetic-experimental-type, style.soft-ui-neumorphic, style.glass-spatial, style.art-nouveau-ornamental]
version_timestamp: 2026-10-20 02:08:35 UTC
---

# Low Literacy / Plain Language

## Who and what they need

- **Larger than most teams assume.** In the 2023 PIAAC survey (NCES), about 28% of US adults aged 16-65 scored at Level 1 or below in literacy, up from 19% in 2017. Add English-language learners, people with dyslexia or low vision, and anyone reading under stress (a diagnosis, an eviction notice, a benefits deadline). Everyone reads worse when frightened or tired.
- **Capable adults.** Low literacy is not low intelligence. People compensate with memory, context, asking family, phone calls and visual cues. Respect shows in tone, not in oversimplified content.
- **Needs:** words they know, one thing at a time, examples, pictures that explain action, numbers in concrete terms ("$12 a month"), forgiving input, and a person to ask.
- **Numeracy often travels with literacy.** Avoid percentages, fractions, APR and charts without a plain-number translation.
- **Context:** government forms, healthcare instructions, banking, insurance, utilities, job applications, fintech for the underbanked, community services, mobile-only access.

## Design defaults

| Variable | Default for this audience | General default | Source or reasoning |
| --- | --- | --- | --- |
| Reading level | Target grade 5-6, ceiling grade 8; average sentence 12-15 words, ceiling 20; paragraph 3 sentences | Grade 8-10 | plainlanguage.gov; ISO 24495-1:2023; WCAG 2.2 SC 3.1.5 (lower secondary level or supplement) |
| Minimum body text | 18px (16px floor), regular weight or heavier, sentence case, no all caps | 16px | Readability research on lower-literacy users (NN/g); WCAG 1.4.4 |
| Line length | 45-60 characters, line-height 1.5-1.6, left-aligned, no justification | 60-75ch | WCAG 2.2 SC 1.4.8; reduces tracking errors |
| Target size | 48px with 8px+ gaps; buttons with verbs and often an icon | 44px | WCAG 2.5.5; Material 48dp |
| Contrast | 7:1 body, 4.5:1 minimum; status always icon plus word plus color | 4.5:1 | WCAG 1.4.6, 1.4.1 |
| Information density | Low; one question or decision per screen; 3-5 options; chunks of 3-5 bullets | Medium | COGA: limit interruptions and choices; GOV.UK "one thing per page" |
| Motion | Minimal; 200ms feedback; animation only to demonstrate a step and always pausable | 120-240ms | WCAG 2.2 SC 2.2.2; COGA on distractions |
| Session length | Save-and-return, no timeouts that lose work, "you are 60% done"; expect interruptions | Standard | COGA: processes must not rely on memory |
| Error tolerance | High: accept spaces, dashes and case variants; say what happened and how to fix it in one sentence; never show codes alone | Inline validation | WCAG SC 3.3.1, 3.3.3; GOV.UK error message patterns |
| Numbers and dates | "20 October 2026", "$12 a month", "1 in 4"; avoid percentages and unexplained units | Locale format | Numeracy research; plain-language guidance |
| Media | Text always present; add read-aloud audio, captioned video and pictograms as supplements, not replacements | Optional | COGA; WCAG 1.2 series |

## Interaction and content

- **Write like this:**
  - Before: "Remit payment of the outstanding balance prior to the delinquency date to avoid penalties." (Flesch-Kincaid about grade 11)
  - After: "Pay by 15 November. If you pay late, we add a $25 fee." (Flesch-Kincaid below grade 3)
- **Rules from plainlanguage.gov:** address the reader as "you"; use active voice; choose common words ("use" not "utilize"); put the most important point first; one idea per sentence; short sections with descriptive headings; define a hard term once, next to where it appears.
- **Buttons and links** say what happens: "Check my claim", "Send the money". Never "Click here" or "Submit".
- **Forms:** one question per page for long journeys; labels above fields; hints visible (not in placeholders); lenient formats; show-password toggle; allow paste; prefer radio buttons to dropdowns for fewer than 7 options; show a review page.
- **Icons help only with labels.** Use familiar pictograms (ISO 7001 style) beside words and test comprehension; icon-only controls fail more often than text.
- **Multichannel:** phone line, SMS, in-person help, community partners, translated versions written in plain language in each language (machine translation of complex source text compounds errors).
- **Respect:** no baby talk, cartoon overload or all-caps shouting; tell people what happens next and how long it takes.

## Visual tone

- **Calm, uncluttered, high-contrast.** Primary blue #0F4C81 (oklch 0.41 0.106 250) with white text is 8.86:1; danger #B3261E (oklch 0.50 0.178 29) 6.54:1 on white; success #146C2E (oklch 0.47 0.125 148) 6.53:1 on white. A callout on #FFF4CC (oklch 0.97 0.053 94) holds ink #1A1A1A at 15.80:1 and amber text #8A5A00 (oklch 0.51 0.108 73) at 5.38:1.
- **Type:** Atkinson Hyperlegible, Public Sans, Noto Sans (wide script support) or Source Sans 3. Lexend was designed to ease reading fluency, but independent evidence is limited; treat it as a pleasant option, not a proven fix.
- **Layout:** single column, generous white space between chunks, strong headings, numbered steps with large numerals, one primary button per screen.
- **Imagery:** photographs or illustrations that show the action ("insert the card here") rather than mood; include people of varied age, skin tone and dress.

## Pitfalls

- Equating a good readability score with comprehension; run a read-back or teach-back test with real readers.
- Dumbing down content so it loses the facts people need; shorten words and sentences, not information.
- Legal text, acronyms and error codes ("Error 403") surfaced to users.
- Placeholder-only labels, dropdowns for dates, strict phone formats and CAPTCHAs.
- Icon-only navigation, or icons that rely on cultural metaphors (floppy disk, hamburger).
- Walls of text before the action; important deadlines hidden in the last paragraph.
- Treating the plain-language version as a separate "easy" page that gets out of date.

## Regulatory and compliance notes

- **US:** Plain Writing Act of 2010 requires federal agencies to use plain language; federal guidelines at plainlanguage.gov. Title VI and Executive Order 13166 require meaningful access for people with limited English proficiency in federally assisted programs. Disclosure rules (for example Truth in Lending) require clear and conspicuous presentation.
- **EU:** GDPR Article 12 requires information in "concise, transparent, intelligible and easily accessible form, using clear and plain language"; the Unfair Contract Terms Directive (Article 5) requires terms drafted in plain, intelligible language.
- **UK:** FCA Consumer Duty (from July 2023) includes a consumer understanding outcome for financial services communications; GOV.UK content design standards for public services.
- **Accessibility:** WCAG 2.2 SC 3.1.5 (Reading Level, AAA) and the W3C COGA guidance are the web references; the EAA and ADA cover accessibility more broadly.
- **ISO 24495-1:2023** sets plain-language principles (relevant, findable, understandable, usable) and is increasingly cited in procurement.

Confirm requirements with counsel for the specific product and jurisdiction.

## Reference anchors

- plainlanguage.gov, *Federal Plain Language Guidelines*; ISO 24495-1:2023 *Plain language*
- W3C, *Making Content Usable for People with Cognitive and Learning Disabilities* (COGA)
- NCES, *Program for the International Assessment of Adult Competencies (PIAAC) 2023* results
- GOV.UK Design System and content design guidance (question pages, error messages, check-answers pattern)
- CDC Clear Communication Index; AHRQ Health Literacy Universal Precautions Toolkit
- Nielsen Norman Group research on lower-literacy users (Nielsen, 2005 and later)
