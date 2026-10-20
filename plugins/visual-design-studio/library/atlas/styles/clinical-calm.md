---
id: style.clinical-calm
axis: style
name: Clinical Calm
aliases: [healthcare ui, medical clean, calm health design, patient-friendly design, clinical clarity, care ui, wellbeing clean]
summary: Reassuring healthcare clarity with soft teal-blue, warm neutrals, plain language, large targets and low-stimulation layouts that lower anxiety and prevent errors without feeling sterile.
tags: [healthcare, clinical, calm, clarity, patient, medical, reassuring, accessible, teal, plain-language]
pairs_with: [industry.healthcare-provider, industry.digital-health-wellness, industry.pharma-biotech, industry.insurance, audience.older-adults, audience.disability-accessibility-first, archetype.caregiver, archetype.sage, channel.web-app, channel.native-app]
avoid_with: [archetype.outlaw, archetype.jester, industry.gaming-esports, tier.ultra-luxury]
version_timestamp: 2026-10-20 01:57:45 UTC
---

# Clinical Calm

## Essence

Lower the user's heart rate while raising their confidence. People meet healthcare interfaces when they are worried, tired, in pain or caring for someone else, so the design must be quiet, exact and humane. Clarity means plain words, one task at a time, unambiguous numbers and obvious next steps. Calm does not mean cold: warm neutrals, humanist type, real photography and a trace of color keep it from reading as a sterile hospital corridor. It is the visual language of NHS.UK, patient portals, digital therapeutics and good telehealth.

## Visual signature

- Very light canvas (cool white to pale teal-gray), white surfaces, one muted teal-blue primary, and quiet tints for grouping.
- Large, clear sans-serif body text (17-19px), short lines, generous line spacing, sentence-case headings.
- Single-column flows with one question or action per screen for intake and instructions; summary cards for status.
- Soft radii (8-12px), thin borders, very light shadows; no gradients, no glass, no heavy decoration.
- Status shown with icon, word and color together; critical alerts are rare, unmistakable and never decorative.
- Human, diverse, consented photography and gentle spot illustration; occasional sage or peach warmth.

## Token recipe

| Token | Value |
| --- | --- |
| Display font | Figtree (OFL); Source Serif 4 (OFL) for reassuring long-form headings in educational content; commercial: Frutiger (the NHS brand font), Sofia Pro, Avenir Next |
| Body font | Figtree (OFL) or Atkinson Hyperlegible Next (OFL) for maximum character distinction; commercial: Frutiger, Avenir Next |
| Mono / numerals | Figtree with `tabular-nums` for vitals and lab values; DM Mono (OFL) for IDs |
| Type scale ratio | 1.250 (major third); headings 24/30/38px, body 17-19px |
| Body size / line-height | 17-19px / 1.6; measure 55-65ch; form labels 16-18px, never below 14px for any health information |
| Display letter-spacing | 0 to -0.01em; avoid tight tracking for readability |
| Caps / labels | Avoid all caps for clinical terms; if used for tags, 12-13px weight 600, +0.04em |
| Weights | 400 body, 500-600 headings and labels; avoid 300 |
| Palette | Canvas #F7FAFB (oklch 0.98 0.003 220); Surface #FFFFFF (oklch 1 0 0); Primary teal #0F6C7A (oklch 0.49 0.081 211); Primary tint #E3F2F4 (oklch 0.95 0.016 206); Ink #1B2B34 (oklch 0.28 0.027 234); Muted #51636E (oklch 0.49 0.028 235); Control border #6F8591 (oklch 0.60 0.031 232); Hairline #D6E0E4 (oklch 0.90 0.012 224) |
| Status colors | Success #25694B (oklch 0.47 0.085 161); Warning text #8A5300 (oklch 0.49 0.109 67); Critical #B3261E (oklch 0.50 0.178 29); each with icon and word |
| Warmth accent | Sage #7FA99B (oklch 0.70 0.05 172) for illustration and backgrounds behind dark text, never as text |
| Accent proportion | Primary teal 5-10% (buttons, links, active nav); tints and sage for grouping; critical red under 2% and only for true urgency |
| Radius | 8px inputs and buttons, 12px cards and sheets; avoid pills for primary buttons so they read as controls |
| Borders | 1px hairline #D6E0E4 for cards (decorative); inputs and checkboxes use #6F8591 (3:1) with 2px on focus |
| Shadow / elevation | `0 1px 2px rgb(27 43 52 / 0.06)` resting; `0 8px 24px rgb(27 43 52 / 0.10)` for dialogs; no colored glows |
| Spacing density | Comfortable: 8px base, 24-32px between groups, 16px form field gap; targets 48px minimum |
| Grid | Single column up to 640px content width for flows; 12 columns for dashboards with 1120px max; stack on mobile |
| Motion | 150-250ms, cubic-bezier(0.2, 0, 0, 1); fades and short slides; breathing guides 4-6s per cycle only inside wellness features |

## Composition and layout

- Design flows around "one thing per page" for intake, consent, medication instructions and results. Show progress ("Step 2 of 5") and let users go back without losing data.
- Put the next action first: appointment time, prescription ready, results available. Keep secondary information collapsible.
- Group by task, not by hospital department. Use plain headings: "Your appointments", "Your medicines", "Message your care team".
- Present numbers with context: value, unit, reference range and a plain sentence. A range bar with a marker plus text ("Within the expected range") beats a red/green dot alone.
- Make the escape routes visible: phone number, emergency instructions ("If this is an emergency, call 911/999/112"), and a human contact option on every high-stakes page.
- Keep navigation shallow (4-5 destinations) and consistent; use text labels with icons.

## Imagery and iconography

- Photography: real staff and patients with documented consent, natural light, eye-level framing, varied ages, bodies and abilities. Avoid stock doctors with crossed arms, stethoscopes as props and ominous close-ups of needles.
- Illustration: soft shapes in teal, sage and warm neutrals; people drawn with dignity and variation; avoid cartoon organs unless teaching anatomy.
- Icons: 2px rounded outline icons at 24px with text labels; medical symbols used correctly (a cross for pharmacy only where locally conventional).
- Data visualization: calm, labeled charts with sentences ("Blood pressure over 30 days") and thresholds shown as bands plus text.

## Motion

Reassuring, not performative. Transitions are 150-250ms fades and 8px slides; loading uses a plain progress indicator with a text status ("Checking your results"); no spinners that run indefinitely without explanation. Avoid confetti, shake animations and flashing alerts. For breathing or relaxation exercises, use a smooth 4-6 second expand/contract circle with a text cue and a stop button. Reduced motion replaces animation with static state changes and text.

## Fits and risks

- **Fits:** hospitals and clinics, patient portals, telehealth, health insurers and benefits, pharmacy, digital health and therapy apps, pharma patient-support sites, caregiving tools. Strongest for `audience.older-adults` and `audience.disability-accessibility-first`, and for `archetype.caregiver` and `archetype.sage`.
- **Risks:** blandness. The sea of identical pale blue and white makes providers indistinguishable. Over-softening can hide urgency; over-medicalizing can feel cold. Health content carries legal and safety obligations: HIPAA (US) governs protected health information, the EU MDR and FDA rules apply to software that acts as a medical device, and accessibility law applies broadly. Confirm requirements with counsel and clinical safety officers.
- **Wrong for:** playful or rebellious brands (`archetype.outlaw`, `archetype.jester`), gaming and nightlife, ultra-luxury wellness that sells exclusivity over clarity.

## Do and don't

- Do test comprehension with representative patients, including low health literacy, and aim for plain-language reading grade 6-8.
- Do spell out units and abbreviations ("micrograms", not "mcg" on its own where confusion with mg is possible), and format dates unambiguously ("14 March 2026").
- Do make destructive and irreversible actions require a clear confirmation that restates the consequence.
- Don't use red for anything but real danger or errors; don't fill dashboards with alert colors.
- Don't show sensitive health information in notifications, email subject lines or lock-screen previews.
- Don't use a heartbeat line, DNA helix or cross as decoration in every section.

## Clichés and AI tells

- Lazy version: pale blue gradient, white cards with 16px radius and shadows, Inter, a stock doctor smiling with a tablet, a heartbeat line divider, glossy 3D pill or DNA icons, and "Your health, simplified".
- Fix: choose a distinctive but calm hue (deep teal, sage, or warm coral as secondary), warm the neutrals slightly, set text in Figtree or Atkinson Hyperlegible Next at 17-19px, photograph the actual service, rewrite headlines as concrete tasks ("Book a blood test in 2 minutes"), and show real next steps, hours and phone numbers.

## Accessibility notes

- Ink #1B2B34 on canvas #F7FAFB is 13.89:1 and muted #51636E is 5.96:1. Primary teal #0F6C7A is 5.81:1 on canvas and 5.30:1 on its tint #E3F2F4; white on teal is 6.09:1.
- Status: success #25694B is 6.56:1 on white and 6.26:1 on canvas, warning text #8A5300 is 6.33:1 and critical #B3261E is 6.54:1 on white. The lighter success #2E7D5B passes on white (5.00:1) but leaves little headroom on tinted surfaces, so prefer #25694B.
- Hairlines #D6E0E4 are 1.28:1 on canvas (decorative). Inputs and checkboxes use #6F8591 at 3.68:1 on canvas; sage #7FA99B is 2.49:1 and is decoration only.
- Target 48px, spacing between targets 8px or more, forms with visible labels (never placeholder-only), error summaries at the top plus inline messages, no time limits without an extension option (WCAG 2.2.1 Timing Adjustable).
- Support 200% text zoom and 400% reflow, screen readers, voice control and switch access; avoid CAPTCHAs without alternatives; provide captions and transcripts for video.

## Reference anchors

- NHS digital service manual and NHS.UK frontend (service-manual.nhs.uk); Frutiger as the NHS brand font with Arial fallback
- GOV.UK Design System patterns for forms, error summaries and question pages
- Apple Human Interface Guidelines for health and fitness apps
- Atkinson Hyperlegible Next (Braille Institute) for character distinction
- Health literacy guidance from the CDC Clear Communication Index and the Plain Language Action and Information Network
- WCAG 2.2 and the Section 508 standards
