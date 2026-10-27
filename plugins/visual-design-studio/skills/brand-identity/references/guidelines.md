# Brand guidelines and brand portal

Version-Timestamp: 2026-10-27 12:00:00 UTC

Guidelines exist so that someone who was not in the room can make on-brand work tomorrow. That means files and templates first, rules second, and explanations short. A rule without a downloadable asset or a template is a rule people will break.

## Formats

| Format | When | Size |
| --- | --- | --- |
| Quick reference | Everyone; partners and agencies on day one | 1-2 pages: logo do/don't, colors, fonts, contacts, download link |
| Brand book (PDF or web) | Core identity reference | 20-80 pages for most brands; 100+ only for large multi-brand systems |
| Digital brand portal | Organizations with many users, regions or partners | A website with search, downloads, templates and versioning |
| Channel playbooks | Teams that produce one channel at volume | Social, retail, packaging, signage, presentations: 10-30 pages each |
| AI handoff | Teams using generators or agents | One Markdown file plus token JSON with locked values and prompts |

## Structure and must-have contents

| Section | Must include |
| --- | --- |
| 1. Start here | Purpose of the guide, how to use it, version and date, owner and contact, where to download assets |
| 2. Brand foundation | Purpose, positioning, personality ("X, not Y"), archetype; one or two pages |
| 3. Verbal identity | Voice principles with do/don't lines, tone by context, vocabulary and banned words, naming conventions, mechanics (capitalization, numbers, dates, punctuation) |
| 4. Logo | Every version and lockup, clear space with the measuring element shown, minimum sizes in px and mm, color versions, approved backgrounds, placement per format, co-branding rules, 8-12 misuse examples drawn (stretched, recolored, rotated, outlined, effects, rearranged, crowded, low-contrast background, on a busy photo, tagline at illegible size) |
| 5. Color | HEX and RGB from the DTCG tokens (the source of truth); CMYK coated and uncoated, Pantone C and U, RAL or NCS labeled as nearest matches until verified against a press proof, the physical guide or the sign maker's swatch; proportions; tints; approved text pairs with computed contrast ratios; dark-mode values; colors never to combine |
| 6. Typography | Families and weights, where to license and download, web and app embedding rights, fallbacks for Office and email, hierarchy and scale, settings (tracking, line height, case), non-Latin scripts |
| 7. Graphic elements | Device, patterns and textures with scale, crop and color rules |
| 8. Imagery | Photography principles with 6-12 do and don't examples, illustration style, iconography grid and stroke, AI imagery policy and labeling |
| 9. Layout | Grids and margins per main format, logo position, typographic hierarchy examples |
| 10. Motion and sound | Logo animation, easing and durations, transitions, sonic logo, reduced-motion behavior |
| 11. Applications | Real examples: stationery, email signature, website, app, social templates, presentations, signage, packaging, merchandise |
| 12. Accessibility | Contrast requirements, minimum text sizes, color-blind-safe pairs, alt text and captions policy |
| 13. Assets and files | Download library, file naming convention, which file for which use, font and image licenses |
| 14. Governance | Approval process, who to ask, how to request new assets, changelog |

Must-haves that are most often missing: minimum sizes in both px and mm, computed contrast ratios, Office and email fallback fonts, a reversed logo on photography example, co-branding rules, and the changelog.

## Writing the rules

- **Rule, reason, example.** "Use the symbol alone only under 48px wide, because the wordmark fills in below that. Example: app icon, favicon, social avatar."
- **Imperatives, not wishes.** "Set headlines in Display Bold" beats "headlines should ideally be bold".
- **Show do and don't side by side** at the same size, with the don't clearly marked by a label, not only a red cross (do not rely on color alone).
- **Numbers over adjectives.** Clear space = 1x cap height; minimum 20mm; tracking −1% at 48pt and above.
- **Separate status:** approved, provisional, deprecated. Never mix them on one page without labels.
- **Source of truth:** link to the token file, the asset library and the templates. Never paste values that can drift; generate the color and type pages from tokens where possible.

## Digital brand portal

Information architecture:

1. Home: quick reference, latest updates, search.
2. Brand foundation.
3. Identity: logo, color, type, graphic elements, imagery, motion, sound.
4. Voice.
5. Templates: grouped by channel (social, deck, documents, email, print, signage).
6. Downloads: logo packs, fonts (where licensed for distribution), photography library, icons.
7. Channel playbooks.
8. Requests and contacts: forms for new templates, approvals and questions.
9. Changelog.

Features to require from a platform (dedicated tools such as Frontify, Bynder, Brandfolder or Corebook, a design-system docs tool such as zeroheight, or a custom static site):

- Search across rules and assets; deep links to each rule.
- Role-based downloads (internal, agency, press, partner) and expiring links for licensed photography.
- Download the right file for the use: "I need a logo for PowerPoint" returns a PNG; "for a sign shop" returns PDF or EPS.
- Editable templates (Figma, Canva, PowerPoint, Google Slides, Keynote, InDesign) that lock logo, colors and fonts.
- Versioning with dates, and a public changelog.
- Usage analytics to see which assets and pages people use.

Each portal page: one-sentence rule, visual example, download buttons, do/don't, related pages, last updated date and owner.

## AI handoff file

For teams that brief generators or agents, ship one concise file next to the tokens:

```markdown
# <Brand> AI handoff (v1.2, 2026-10-20)
Locked: logo files (never generate or redraw), name spelling "Ledgerly", colors (see tokens.json)
Type: Display = <family> 700; Text = <family> 400/600; fallback Arial
Color roles: ink #1F2430, paper #F4EFE6, accent #0B5C66 (white text on accent: 7.67:1)
Imagery: candid, natural window light, warm grade; real clinic staff; no stock handshakes
AI imagery: allowed for backgrounds and illustration; never for product shots, staff or testimonials; label per policy
Voice: plain, specific, calm; never "revolutionary", "seamless"
Do not: gradients on the logo, emoji as icons, centered body text
```

Keep values identical to the token source; regenerate the file when tokens change.

## Templates to ship with the guidelines

- Social: feed (1080x1350), story/reel cover (1080x1920), carousel (1080x1350), link preview (1200x630).
- Presentation master: 16:9 with title, section, statement, chart, image and closing layouts.
- Documents: letterhead, report cover, one-pager, invoice, proposal.
- Email: signature and newsletter shell.
- Print: business card, A4 or Letter flyer, poster.
- Digital: favicon set, app icon set, Open Graph image template.

Test every template by giving it to someone outside the project and asking them to make one piece without help. Fix whatever they get wrong.

## Governance and versioning

- Version numbers: major for identity changes, minor for new sections or templates, patch for corrections (v2.3.1).
- Every page shows its last updated date and owner.
- Review cadence: quarterly for templates and channel specs, annually for the whole guide.
- Deprecated assets stay downloadable in an archive folder with a deprecation date, so old work can be traced.

## Common failures

- A 120-page PDF nobody opens → quick reference plus portal plus templates.
- Rules without files → every rule links to the asset that satisfies it.
- Color values that differ between pages → generate them from tokens.
- No fallback fonts → teams substitute random fonts in Office and email.
- Misuse page with only color-coded crosses → text labels for accessibility.
- Guide frozen at launch → changelog, owner, review cadence.

For client approvals, source precedence and rendered editions, use the deep process skill [brand guidelines](../../../library/draft-skills/design-brand-guidelines/SKILL.md) and [identity delivery](../../../library/draft-skills/design-identity-delivery/SKILL.md).
