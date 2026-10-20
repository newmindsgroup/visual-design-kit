---
id: audience.disability-accessibility-first
axis: audience
name: Disability and Accessibility-First
aliases: [accessibility, a11y, inclusive design, wcag, blind users, low vision, deaf, motor impairment, assistive technology]
summary: Products where people with vision, hearing, motor or cognitive disabilities are core users; treat WCAG 2.2 AA as the floor, build in keyboard, screen-reader and zoom support, and test with real users.
tags: [accessibility, wcag, a11y, screen reader, keyboard, low vision, inclusive, assistive technology, ada]
pairs_with: [style.civic-plain, style.clinical-calm, style.swiss-international, style.flat-material, industry.government-civic, industry.healthcare-provider, industry.education-edtech, channel.web-app, channel.marketing-website, archetype.caregiver]
avoid_with: [style.glass-spatial, style.soft-ui-neumorphic, style.kinetic-experimental-type, style.y2k-cyber]
version_timestamp: 2026-10-20 02:08:35 UTC
---

# Disability and Accessibility-First

## Who and what they need

- **Permanent, temporary and situational.** Microsoft's Inclusive Design toolkit frames it as a spectrum: one arm (permanent), an arm injury (temporary), a baby in the other arm (situational). Designing for the permanent case helps everyone.
- **Groups:** blind and low-vision (screen readers, magnifiers, high contrast, large text), deaf and hard of hearing (captions, transcripts, visual alerts, sign language), motor and dexterity (keyboard, switch, voice control, head or eye tracking, tremor), cognitive and learning (plain language, predictability, memory support), speech, seizure and vestibular (motion), and color-vision deficiency.
- **Needs:** every function reachable by keyboard and touch alone, meaningful structure and names for assistive technology, content that adapts to the user's size, spacing, color and motion settings, enough time, and clear recovery from errors.
- **Reality check:** assistive-technology users are experts in their tools. They want your product to expose correct semantics, not a special version.

## Design defaults

Defaults go beyond the WCAG 2.2 AA floor where the audience depends on it. Success criteria numbers refer to W3C WCAG 2.2 (Recommendation, October 2023).

| Variable | Default for this audience | General default | Source or reasoning |
| --- | --- | --- | --- |
| Minimum body text | 16-18px in rem; layout works at 200% zoom and 400% reflow at 320 CSS px; text-spacing overrides cause no clipping | 16px | SC 1.4.4, 1.4.10, 1.4.12 (line-height 1.5, paragraph 2x, letter 0.12em, word 0.16em) |
| Target size | 44x44px default; 24x24px with spacing is the hard floor; 48dp on Android | 44px | SC 2.5.5 (AAA) and 2.5.8 (AA); Apple HIG; Material |
| Contrast | 7:1 for body, 4.5:1 for large text, 3:1 for UI components, states and focus; support dark, high-contrast and forced-colors | 4.5:1 | SC 1.4.3, 1.4.6, 1.4.11 |
| Focus | Visible on every control, 2px+ thick, 3:1 against adjacent colors, never hidden by sticky headers | Browser default | SC 2.4.7, 2.4.11 (AA), 2.4.13 (AAA) |
| Reading level | Lower secondary level or a plain-language alternative; grade 6-8 target | Grade 8-10 | SC 3.1.5 (AAA); plainlanguage.gov |
| Line length | 45-75 characters, never above 80; left-aligned | 60-75ch | SC 1.4.8 (AAA) |
| Motion | Honor prefers-reduced-motion; nothing flashes more than 3 times per second; auto-moving content over 5 seconds can be paused | 120-240ms | SC 2.3.1, 2.2.2, 2.3.3 |
| Information density | Low to medium; real headings, landmarks and consistent navigation; multiple ways to find pages | Medium | SC 1.3.1, 2.4.5, 2.4.6, 3.2.3, 3.2.6 |
| Session and timing | No time limits, or user can turn off, adjust (10x) or extend; warn before data-loss timeouts | Standard | SC 2.2.1, 2.2.6 |
| Error tolerance | Identify, describe and suggest fixes; reversible, checked or confirmed for legal, financial and data submissions; no redundant entry | Inline validation | SC 3.3.1-3.3.4, 3.3.7, 3.3.8 |
| Input modes | Keyboard for everything, no traps, drag has an alternative, visible label equals accessible name | Mouse and touch | SC 2.1.1, 2.1.2, 2.5.2, 2.5.3, 2.5.7 |

## Interaction and content

- **Semantics first.** Use native HTML controls (button, a, input, select), landmarks, one h1, ordered headings, and lists and tables for real lists and tables. The first rule of ARIA: no ARIA beats bad ARIA. Follow the WAI-ARIA Authoring Practices for custom widgets.
- **Names, roles, values** on every control (SC 4.1.2); status messages announced without moving focus (SC 4.1.3). Icon buttons have accessible names; visible labels match them.
- **Keyboard:** logical focus order, skip link, focus moved into and returned from dialogs, Escape closes, no single-character shortcuts without remap or disable (SC 2.1.4).
- **Media:** captions and transcripts for audio and video, audio description for visual-only information (SC 1.2.5), no autoplay with sound, controls for all media.
- **Alternatives:** informative images get specific alt text; decorative images get empty alt; charts get a data table or text summary; PDFs are tagged.
- **Platforms:** iOS Dynamic Type through the largest accessibility sizes, VoiceOver and Voice Control, Reduce Motion; Android font scale to 200%, TalkBack, Switch Access, 48dp targets; do not lock orientation (SC 1.3.4).
- **Process:** annotate focus order and landmarks in design files; test with keyboard only, NVDA or JAWS on Windows, VoiceOver on macOS and iOS, TalkBack, 200-400% zoom, forced colors and voice control; automated tools (axe, Lighthouse) catch only a minority to about half of issues, so pair them with manual tests and with disabled participants.
- **Governance:** publish an accessibility statement and feedback route; procurement buyers will ask for an Accessibility Conformance Report (ITI VPAT template).

## Visual tone

- **Accessible does not mean plain.** Constraints sharpen design; Swiss, civic and editorial systems all meet AA.
- **Palette example:** ink #1A1A1A on white is 17.40:1; link blue #0042A6 (oklch 0.41 0.172 260) is 9.01:1; visited purple #6A1B9A (oklch 0.42 0.190 308) 9.39:1; danger #8F0000 (oklch 0.41 0.168 29) 9.69:1. Focus ring 3px #005FCC (oklch 0.51 0.185 258), 5.98:1 on white, with a 2px offset; add a second white or dark ring so it holds on any background. Yellow #FFDD00 (the GOV.UK focus color) is 12.92:1 with ink but 1.35:1 on white, so never use it alone on light backgrounds.
- **Type:** Atkinson Hyperlegible (OFL), Public Sans, Source Sans 3, Noto Sans; weights 400 and up; underline links in body copy.
- **State:** convey with shape, text and icon plus color; errors carry an icon and a sentence.
- **Dark and high-contrast themes** are designed, not inverted; test the forced-colors mode for borders and icons.

## Pitfalls

- Accessibility overlays and widgets that promise automatic compliance; they do not fix the underlying code and have drawn criticism from practitioners (see overlayfactsheet.com) and enforcement attention (FTC action against an overlay vendor in January 2025; verify).
- Color-only status, placeholder-as-label, custom controls without keyboard support, removed focus outlines, hover-only reveals, drag-only interactions.
- Mismatch between visible label and accessible name, breaking voice control.
- Fixed-height containers that clip at 200% text, carousels that autoplay, sticky headers that hide focused elements.
- Treating accessibility as final QA instead of design input; a separate "accessible version" that drifts out of date.
- Testing only with automated tools, or only with blind users; disability is not one experience.
- Untagged PDFs, inaccessible CAPTCHAs and timeouts without warning.

## Regulatory and compliance notes

- **US:** ADA Title III covers places of public accommodation; there is no codified web standard but courts and settlements point to WCAG 2.1/2.2 AA, and litigation volume is high. The DOJ ADA Title II web rule (2024) requires WCAG 2.1 AA for state and local government web content and apps, with compliance starting April 2026 for larger entities and April 2027 for smaller ones (sources differ on exact days; verify in the Federal Register). Section 508 (Revised 508 Standards, WCAG 2.0 AA by reference) governs federal ICT and procurement; Section 504; CVAA for communications.
- **EU:** European Accessibility Act (Directive 2019/882) applies from 28 June 2025 to consumer e-commerce, banking services, e-books, electronic communications, passenger transport ticketing and audiovisual services, with a microenterprise exemption for services; EN 301 549 is the harmonized standard (verify current version). Web Accessibility Directive covers public-sector sites and apps.
- **UK:** Equality Act 2010; Public Sector Bodies Accessibility Regulations 2018 (WCAG 2.2 AA is GOV.UK practice).
- **Elsewhere:** Accessible Canada Act and AODA (Ontario), Australia's Disability Discrimination Act, Japan JIS X 8341-3, India RPwD Act. WCAG 3.0 (including APCA contrast) is a working draft and not yet a conformance target.

Confirm requirements with counsel for the specific product and jurisdiction.

## Reference anchors

- W3C WAI, WCAG 2.2 and *Understanding WCAG*; WAI-ARIA Authoring Practices Guide
- W3C COGA, *Making Content Usable for People with Cognitive and Learning Disabilities*
- Microsoft Inclusive Design toolkit (permanent, temporary, situational)
- GOV.UK Design System and accessibility manual
- Apple Human Interface Guidelines: Accessibility; Material Design accessibility guidance; Android accessibility developer docs
- Deque axe, WebAIM Million annual accessibility analysis of home pages (verify latest edition)
- Atkinson Hyperlegible, Braille Institute
