# Intake and qualifying questions

Version-Timestamp: 2026-10-20 02:05:00 UTC

Intake turns a loose request into the variables that decide the design. Fill the table silently from the brief, ask only about unknowns that would change the answer, and state assumptions for the rest.

## The variable checklist

| Variable | What to capture | Atlas axis | Why it changes the design |
| --- | --- | --- | --- |
| Objective | The business result: awareness, sign-ups, sales, trust, retention, fundraising, recruitment | - | Sets the scoring weights and the primary CTA |
| Deliverable | Logo, identity, website, app screens, campaign, packaging, deck, motion, design system | channel | Sets format, fidelity and the discipline skills to load |
| Channel and formats | Where it will live: web, iOS/Android, social, print, retail, OOH, email, video | channel | Hard specs, safe areas, performance budgets |
| Industry and category | What the business does and who it competes with | industry | Trust signals, conventions, clichés, regulation |
| Market and language | Countries, regions, languages, scripts, reading direction | market | Fonts, layout direction, formats, color meaning, payments, law |
| Audience | Primary user and buyer; age, expertise, accessibility needs, context of use | audience | Text size, density, reading level, interaction model |
| Brand personality | Archetype (primary + secondary), 3-5 personality words, what it must never feel like | archetype | Type classification, shape language, motion, voice |
| Price position | Value, mid-market, premium, luxury, ultra-luxury | tier | Whitespace, density, imagery, material and pace |
| Existing brand | Guidelines, logo, colors, type, voice, approved assets, what is locked vs open | - | Defines the exploration range |
| Competitors and references | 3-12 competitors; references the client likes and dislikes | - | Category map, white space, anti-references |
| Constraints | Accessibility level, regulation, budget, timeline, tech stack, CMS, team skills | - | Removes infeasible directions early |
| Success metric | How the client will judge it: KPI, launch date, stakeholder approval | - | Tie-breaker and post-launch evaluation |

Label each row **given**, **inferred** (say from what) or **unknown**.

## Which unknowns to ask about

Ask when two plausible answers would produce materially different work. Typical high-value questions:

1. **Audience and context**, when the brief names only a product. "Who is the primary user: (a) first-time consumers, (b) professionals using it daily, (c) buyers evaluating vendors? I recommend (b) because..."
2. **Ambition level**, when the category has strong conventions. "Should this (a) fit the category and win on craft, (b) borrow from an adjacent category, or (c) break category norms? I recommend (b)..."
3. **Brand locks**, when an existing brand is mentioned. "Which elements are fixed: logo, colors, typefaces, voice?"
4. **Market and language**, when the business could operate in several regions or languages.
5. **Price position**, when the offer could plausibly sit at two tiers.
6. **Channel priority**, when the deliverable spans channels. "Which matters most at launch: website, app store, social, retail?"

Rules:

- 2-4 questions. Each has 2-3 concrete options and your recommendation first, with a one-line reason.
- Never ask what the brief or the conversation already answers.
- Skip questions entirely for mechanical tasks and small revisions.
- If the person wants speed ("just go"), proceed on stated assumptions and offer the questions as levers in the presentation.

## Default assumptions when unanswered

| Unknown | Assume | And say |
| --- | --- | --- |
| Accessibility target | WCAG 2.2 AA | "Raise to AAA for public sector or health contexts if required" |
| Market | The language of the brief; that country's formats | "Tell me if other markets or languages are in scope" |
| Audience age | Adults 25-54, mixed expertise | "Older or younger audiences change text size and density" |
| Tier | Mid-market | "Premium or value positioning changes the whole visual pace" |
| Stack (web) | Astro for marketing sites, Next.js + React for apps | "Tell me if you have a CMS or platform already" |
| Brand assets | None exist | "Share any logo, colors or guidelines and I will work within them" |

## Brief template (write this back before diverging)

```markdown
**Objective:** ...
**Deliverable and channel:** ...
**Audience:** ... (atlas: audience.<id> if applicable)
**Industry / market:** industry.<id> / market.<id>
**Personality:** archetype.<primary> + archetype.<secondary>; feels: a, b, c; never: x, y
**Price position:** tier.<id>
**Locks:** ...
**Constraints:** WCAG 2.2 AA; ...
**Competitors:** ...
**Success looks like:** ...
**Assumptions I made:** ...
```

Confirm the brief in one short message only when the stakes are high (identity, flagship launch). Otherwise proceed and show it alongside the directions.
