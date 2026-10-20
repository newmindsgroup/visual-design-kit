---
id: style.civic-plain
axis: style
name: Civic Plain / Public Service
aliases: [government design, gov.uk style, uswds, public sector design, plain language ui, service design, civic design, accessible-first]
summary: Task-first public-service design with plain language, large readable type, high contrast, strong focus states and proven patterns, as in the GOV.UK Design System and the US Web Design System.
tags: [civic, government, public-service, plain-language, accessible, forms, gov-uk, uswds, utilitarian, trust]
pairs_with: [industry.government-civic, industry.nonprofit-ngo, audience.low-literacy-plain-language, audience.older-adults, audience.disability-accessibility-first, audience.low-bandwidth-entry-devices, archetype.everyperson, channel.web-app, market.united-kingdom-ireland, market.united-states]
avoid_with: [archetype.outlaw, archetype.jester, tier.luxury, tier.ultra-luxury, industry.fashion-apparel, industry.luxury-goods]
version_timestamp: 2026-10-20 01:57:45 UTC
---

# Civic Plain / Public Service

## Essence

Make it work for everyone, first time, without help. Public services are used by people who cannot choose another provider and who often arrive under stress, on old phones, with limited literacy or assistive technology. The GOV.UK Design System (Government Digital Service, UK) and the US Web Design System (USWDS) turned this into a style: restrained, text-led, high-contrast, built from tested patterns, with content designed as carefully as pixels. The aesthetic is a by-product of removing everything that is not needed. It is also a model for any product whose job is to get people through a task.

## Visual signature

- White page, near-black text, one strong link blue, and a very small set of functional colors (green action, red error, yellow focus).
- Large body text (19px on GOV.UK desktop, 16px base on USWDS), left-aligned, short lines, plain headings in sentence case.
- Always-underlined links; buttons that look like buttons; thick, high-contrast input borders and a bold yellow or blue focus state.
- One question per page for complex forms, with back links, error summaries, "check your answers" and confirmation pages.
- Minimal imagery, no hero carousels, no decorative animation, and sparse iconography.
- A clear identity marker: a header bar with service name and a recognizable government banner or crown/seal (reserved for official use).

## Token recipe

| Token | Value |
| --- | --- |
| Display font | Public Sans (OFL; the USWDS default); GDS Transport on GOV.UK domains only (licensed use, Arial fallback elsewhere); commercial: Frutiger, Helvetica Neue |
| Body font | Public Sans (OFL) or Source Sans 3 (OFL); Merriweather (OFL) or Source Serif 4 (OFL) for long guidance text |
| Mono | Roboto Mono (OFL) for reference numbers and codes |
| Type scale ratio | Fixed steps rather than a ratio: 16, 19, 24, 27, 36, 48px (GOV.UK) or the USWDS scale; headings stay modest |
| Body size / line-height | 19px / 1.3-1.4 at tablet and up on GOV.UK-style services, 16-18px / 1.5 in USWDS-style services; measure 60-75ch (GOV.UK uses a 2/3 column) |
| Display letter-spacing | 0; no tight tracking; headings in bold or semibold at 27-48px |
| Caps / labels | Sentence case; use caps only for acronyms; caption text 16px |
| Weights | 400 body, 700 headings and button text; avoid 300 and 500-only hierarchies |
| Palette | Text #0B0C0C (oklch 0.15 0.002 0); Secondary text #484949 (oklch 0.40 0.001 0); Link blue #1D70B8 (oklch 0.53 0.136 250); Link hover #003078 (oklch 0.33 0.132 260); Visited #4C2C92 (oklch 0.40 0.158 292); Focus yellow #FFDD00 (oklch 0.90 0.186 98); Error red #D4351C (oklch 0.57 0.199 32); Success green #00703C (oklch 0.48 0.121 154); Background grey #F3F2F1 (oklch 0.96 0.002 0) |
| Palette (USWDS reference) | Primary #005EA2 (oklch 0.47 0.132 249); Primary dark #1A4480 (oklch 0.39 0.112 258); Ink #1B1B1B (oklch 0.22 0 0); Error dark #B50909 (oklch 0.49 0.196 29); verify against the current USWDS tokens |
| Accent proportion | Color under 10% of the page; blue only for links and actions; green only for the primary or start button; yellow only for focus |
| Radius | 0px on GOV.UK components; about 4px on USWDS; keep consistent |
| Borders | Inputs have 2px near-black borders; cards use 1px #B1B4B6 (decorative, 2.08:1 on white) or a 5px colored left rule for callouts and errors |
| Shadow / elevation | None; the primary button has a 2px darker bottom edge for pressability; no blurred shadows |
| Spacing density | 5px/8px-based scales (GOV.UK uses a 5px unit, USWDS 8px); question pages 20-30px between groups; targets at least 44px high |
| Grid | GOV.UK: container max 960px, two-thirds/one-third columns; USWDS: 12-column grid with a default container of about 1024px (verify) |
| Motion | None by default; 0-150ms state changes; expand/collapse without animation |

## Composition and layout

- Organize around tasks and questions, not departments. The start page says what the service does, who can use it, how long it takes and what to have ready, then a single "Start now" button.
- Use the proven patterns: question page, radios or checkboxes with hints, date input as three fields, address lookup, file upload, task list, summary list with Change links, check-your-answers, confirmation panel, error summary.
- Keep one primary action per page. The back link sits above the main content; the error summary is the first focusable thing in the main region.
- Put the service name and the beta/alpha phase banner in the header; keep the footer links to accessibility statement, cookies, privacy and contact.
- Make pages work without JavaScript, on slow connections and on small screens by default (progressive enhancement). Prefer server-rendered HTML.

## Imagery and iconography

- Content comes first; use imagery only to explain or to help people recognize something (a document, a sign, a form). Include text alternatives.
- Icons: few and functional: arrow, tick, warning, external link; labeled with text. No icon-only buttons.
- Diagrams and process maps: simple, high-contrast, with equivalent text lists.
- Charts: tables first, a chart only if it adds meaning; label directly; avoid color-only distinctions.
- Official marks (crown, seal, flag banner) are reserved for authorised government services; do not use them to imply endorsement.

## Motion

Almost none. Loading and progress are explained in text ("We're checking your details, this can take up to 30 seconds"). Accordions and details elements open without animation or with under 150ms. Never auto-advance, auto-play or time out silently; if a session will expire, warn at least 2 minutes before and allow extension. No carousels. The reduced-motion implementation is the default implementation.

## Fits and risks

- **Fits:** government and civic services (`industry.government-civic`), benefits, tax, licensing, immigration and voting; nonprofits delivering services; utilities and insurers' claims journeys; any product for `audience.low-literacy-plain-language`, `audience.older-adults` and `audience.disability-accessibility-first`. Cultural anchors are the UK and US (`market.united-kingdom-ireland`, `market.united-states`); other countries run comparable systems (Canada, Australia, Singapore, Germany, Netherlands).
- **Risks:** it can look austere or "official" in a way that feels cold for consumer brands. Private companies copying the visual skin without the research and content discipline get the aesthetic but not the outcomes. Copying government branding can mislead users.
- **Wrong for:** luxury, fashion, entertainment and brands whose job is to seduce; use the underlying principles (plain language, contrast, focus, error handling) inside a different visual style.
- **Why these pair:** `industry.nonprofit-ngo` often delivers services; `audience.low-bandwidth-entry-devices` benefits from server-rendered, light pages; `archetype.everyperson` suits unpretentious, universal design; `channel.web-app` is where transactional forms live.
- **Why these clash:** `archetype.outlaw` and `archetype.jester` need attitude; `tier.luxury`, `tier.ultra-luxury`, `industry.luxury-goods` and `industry.fashion-apparel` sell desire and ornament.

## Do and don't

- Do write in plain English or the local plain language: short sentences, active voice, the word the user uses, one idea per paragraph, reading age around 9 as a target.
- Do test with assistive technologies and with people who have low confidence online, not only with developers.
- Do show the user what happens next after every submit, with a reference number and a time frame.
- Don't hide labels in placeholders, disable submit buttons to show validation, or split one question across steps.
- Don't use "click here", vague link text or icon-only controls.
- Don't customize components until you have confirmed the standard version fails users; adopt updates from the design system.

## Clichés and AI tells

- Lazy version: a "modernized" government site with a gradient hero, a three-card service grid, a hamburger menu hiding the top tasks, Roboto 14px gray text, rounded 16px buttons, placeholder labels, and a decorative flag. Or a pastiche "gov.uk" skin on a private product with no accessibility statement.
- Fix: begin with a task inventory, use the established components, keep body text at 19px (or 16-18px USWDS), enlarge targets to 44px, put real, tested content first, and run an accessibility audit with keyboard, screen reader and zoom before launch.

## Accessibility notes

- Contrast (computed): text #0B0C0C on white 19.59:1; secondary #484949 on white 9.03:1 and on #F3F2F1 8.08:1; link blue #1D70B8 on white 5.17:1 and on #F3F2F1 4.62:1; hover #003078 12.40:1; visited #4C2C92 10.08:1; error red #D4351C 4.86:1; green #00703C 6.21:1 (white on green the same).
- Focus: yellow #FFDD00 with black text is 14.55:1, but yellow alone on white is 1.35:1, which is why GOV.UK pairs the yellow with a thick black underline or border. Never rely on the yellow fill alone.
- USWDS reference values: primary #005EA2 on white 6.72:1, primary dark #1A4480 9.62:1, ink #1B1B1B 17.22:1, gray #71767A 4.59:1; its focus blue #2491FF is only 3.20:1 on white, so it needs a thick outline. USWDS grades colors so a grade difference of 40+ meets 3:1, 50+ meets 4.5:1 and 70+ meets 7:1 (verify in the current docs).
- Meets or exceeds WCAG 2.2 AA; public bodies often have legal duties (UK Public Sector Bodies Accessibility Regulations, US Section 508, ADA Title II rules for state and local governments; confirm current dates and versions). Provide an accessibility statement.
- Target 44px, inputs with visible labels, hints and specific error messages, error summaries linking to fields, no reliance on color, and 200% zoom and 400% reflow without loss.

## Reference anchors

- GOV.UK Design System (design-system.service.gov.uk) and GOV.UK Frontend; GDS service manual and content design guidance
- US Web Design System (designsystem.digital.gov) and Public Sans typeface
- 18F and US Digital Service plain-language and accessibility playbooks; the Plain Writing Act of 2010
- Jock Kinneir and Margaret Calvert's Transport alphabet, the origin of GDS Transport
- Canada.ca Design System, Australian Government Design System and NHS.UK frontend as sibling systems
- Caroline Jarrett, *Forms that Work*; Sarah Richards, *Content Design*
