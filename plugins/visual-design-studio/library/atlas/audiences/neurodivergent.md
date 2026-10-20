---
id: audience.neurodivergent
axis: audience
name: Neurodivergent Users
aliases: [neurodiversity, adhd, autism, autistic, dyslexia, dyscalculia, dyspraxia, cognitive accessibility, sensory sensitivity]
summary: Users with ADHD, autism, dyslexia and related differences; reduce sensory load and surprises, support memory and executive function, keep language literal, and let people tune the interface.
tags: [neurodivergent, adhd, autism, dyslexia, cognitive accessibility, sensory, executive function, calm, personalization]
pairs_with: [style.quiet-minimal, style.clinical-calm, style.civic-plain, style.scandinavian-nordic, style.flat-material, industry.digital-health-wellness, industry.education-edtech, archetype.caregiver, archetype.sage, channel.web-app]
avoid_with: [style.maximalist-eclectic, style.kinetic-experimental-type, style.y2k-cyber, style.grunge-punk-zine, style.vibrant-gradient-saas]
version_timestamp: 2026-10-20 02:08:35 UTC
---

# Neurodivergent Users

## Who and what they need

- **Not a single profile.** ADHD (attention, working memory, time perception, rejection sensitivity), autism (sensory processing, literal language, preference for predictability and routine), dyslexia (decoding and spelling), dyscalculia (number handling), dyspraxia (coordination), Tourette's, and combinations. Frequently cited estimates put neurodivergence at 15-20% of people; figures vary by definition (verify before quoting).
- **Shared needs:** predictability, control, low sensory noise, information that does not depend on memory or fast reading, and permission to work in their own way.
- **Strengths to design for:** deep focus when not interrupted, pattern recognition, careful attention to detail, creative problem solving. Good support for these users usually removes friction for everyone.
- **Context:** work tools, learning platforms, health and wellbeing apps, public services, shopping. Many users run browser extensions, custom styles or OS settings; do not fight them.
- **Guidance sources:** W3C COGA (Making Content Usable for People with Cognitive and Learning Disabilities), the British Dyslexia Association Style Guide, and WCAG 2.2 criteria 2.2.2, 3.2.6, 3.3.7 and 3.3.8.

## Design defaults

| Variable | Default for this audience | General default | Source or reasoning |
| --- | --- | --- | --- |
| Minimum body text | 16-18px; user can scale text and spacing without breaking layout | 16px | BDA Style Guide recommends 12-14pt sans serif (about 16-19px; verify); WCAG 1.4.4, 1.4.12 |
| Text spacing | Line-height 1.5-1.8, paragraph spacing 1.5-2x, letter-spacing +0.02 to +0.12em, word-spacing up to 0.16em | 1.5, 0 | WCAG 1.4.12 override values; BDA Style Guide (verify exact spacing figures) |
| Target size | 44-48px with 8px gaps (helps dyspraxia and tremor) | 44px | WCAG 2.5.5 |
| Contrast | 7-12:1 for body on off-white or tinted background, not pure #000 on #FFF; offer light, dark, cream and high-contrast themes | 4.5:1 | WCAG 1.4.6; BDA recommends non-white backgrounds; evidence on color overlays is mixed |
| Reading level | Literal, concrete, grade 6-8; no idioms, sarcasm or metaphors in instructions | Grade 8-10 | COGA content guidance; plainlanguage.gov |
| Line length | 45-65 characters, ragged-right, no justified text, no italics or underline for emphasis, no all caps | 60-75ch | BDA Style Guide; WCAG 1.4.8 |
| Motion | No autoplay, parallax or flashing; any animation under 5 seconds or pausable; in-app reduce-motion toggle beyond the OS setting; no sudden sound | 120-240ms | WCAG 2.2.2, 2.3.1, 1.4.2; sensory sensitivity |
| Information density | Low to medium; strong hierarchy, chunked content, progressive disclosure, one primary action per view, stable layout (CLS 0.1 or less) | Medium | COGA: limit distractions; Core Web Vitals (web.dev) |
| Session and attention | Save state continuously; "resume where you left off"; show steps, progress and estimated time ("about 3 minutes"); optional break and focus modes; steps of 5-7 minutes | Task-based | COGA: do not rely on memory; time perception support |
| Error tolerance | Very high: undo, draft recovery, fuzzy search and spelling suggestions, lenient input formats, no timed tests, no penalties for slowness | Standard | WCAG 3.3.7 (redundant entry), 3.3.8 (no memory tests), COGA |
| Predictability | Same patterns in the same places; announce changes before they happen; no surprise redirects or modals; confirm before leaving unsaved work | Consistent | WCAG 3.2.1-3.2.6; COGA |

## Interaction and content

- **Front-load.** Put the answer or the next action first; use short paragraphs, descriptive headings and numbered steps. Offer a one-line summary above long content.
- **One instruction, one step.** Avoid double negatives and compound instructions; give examples; define abbreviations; name buttons with verbs.
- **Support memory and executive function:** checklists, templates, sensible defaults, saved preferences, autofill, recognition over recall, no codes to remember or retype, reminders that users opt into and tune.
- **Personalize without sign-up gates:** themes, density, font choice, reduced motion, hide-decoration and quiet modes; persist them across devices (COGA personalization objective).
- **Multiple modalities:** text plus diagram plus short captioned video or audio; speech-to-text input; read-aloud.
- **Sensory control:** muted by default, volume and haptics optional, no auto-playing video, no full-screen flashes, notification batching that the user controls.
- **Social and communication:** clear, literal tone; give agendas before meetings; offer text or asynchronous alternatives to live video; avoid ambiguous read-status pressure.
- **Avoid pressure patterns:** countdown timers, "only 3 left", streak loss, urgent red badges, onboarding tours that cannot be skipped, chat widgets that pop open.

## Visual tone

- **Calm, quiet, unambiguous.** Warm paper #FAF7F0 (oklch 0.98 0.010 87) with ink #22252A (oklch 0.26 0.010 261) is 14.37:1; secondary #4A5560 (oklch 0.44 0.023 248) 7.11:1; accent teal #2B6F77 (oklch 0.50 0.068 206) 5.39:1 on paper and 5.76:1 with white text; alert orange #9A3412 (oklch 0.47 0.143 37) 6.83:1. A highlight band #FDF6B2 (oklch 0.96 0.086 103) under ink is 13.91:1 for key sentences.
- **Type:** Atkinson Hyperlegible, Lexend, Noto Sans, Source Sans 3 (all OFL); choose faces with distinct I, l, 1, O, 0 and avoid condensed, light, script and decorative faces. Special dyslexia fonts (OpenDyslexic, Dyslexie) show mixed evidence; offer them as user options, never as the only default.
- **Pattern and imagery:** avoid tight stripes, moire and busy textures, which trigger visual stress (pattern glare research by Arnold Wilkins); use plain backgrounds behind text.
- **Icons:** literal and labeled; avoid abstract or culturally specific metaphors.
- **Symbols:** the puzzle-piece motif is disliked by many autistic people; consult community voices before using any representation.

## Pitfalls

- A dyslexia font and a pastel overlay presented as the whole solution.
- Infantilizing visuals or tone, or removing options "for your own good".
- Cookie banners, newsletters, chat widgets and tours that interrupt at random moments.
- Dense dashboards with ten competing animated or colored elements.
- Time-boxed tasks, countdowns and CAPTCHAs that punish slow processing.
- Layout shifts, auto-updating content and moving buttons that break orientation.
- Ambiguous language: "Click the usual place", "We'll be in touch soon", idioms.
- Storing or inferring neurotype (for example an ADHD tag) from behavior; it is sensitive health data in many regimes. Let users set preferences without disclosing a diagnosis.

## Regulatory and compliance notes

- **Accessibility law applies:** ADA and Section 508 in the US, the European Accessibility Act (from 28 June 2025) and EN 301 549 in the EU, the Equality Act 2010 (reasonable adjustments) in the UK. WCAG 2.2 added criteria with cognitive impact (3.3.7 Redundant Entry, 3.3.8 Accessible Authentication, 3.2.6 Consistent Help); COGA is guidance, not normative, but is increasingly cited in procurement.
- **Employment tools:** ADA Title I and equivalent laws require reasonable accommodation, so workplace software that blocks adjustments creates risk for employers.
- **Data protection:** health and disability information is special-category data under GDPR Article 9 and sensitive under many US state laws; avoid collecting or inferring neurodivergence for targeting or personalization.
- **Health claims:** apps claiming to treat ADHD or autism may fall under FDA software-as-medical-device rules or EU MDR; marketing claims need substantiation (verify with regulatory counsel).

Confirm requirements with counsel for the specific product and jurisdiction.

## Reference anchors

- W3C, *Making Content Usable for People with Cognitive and Learning Disabilities* (COGA Working Group Note)
- British Dyslexia Association, *Dyslexia Style Guide* (verify current edition)
- WCAG 2.2 success criteria 1.4.12, 2.2.2, 3.2.6, 3.3.7, 3.3.8
- GOV.UK accessibility guidance on cognitive and neurodiverse users; the National Autistic Society and Autistica guidance on sensory-friendly design
- Braille Institute, Atkinson Hyperlegible; Lexend (Bonnie Shaver-Troup, Thomas Jockin)
- Arnold Wilkins, research on visual stress and pattern glare
