# Writing rules for kit content

Version-Timestamp: 2026-10-20 01:42:00 UTC

The reader is Claude doing real design work for a client. Every sentence should change what it designs.

## 1. Strong defaults, documented overrides

Give the number, then say when to move off it.

- Good: "Body text 16-18px, line-height 1.5-1.6, measure 60-75ch. Go to 1.65+ for long-form reading; tighten to 1.4 for dense UI tables."
- Bad: "Choose a readable size appropriate to the context."

When a value is a convention rather than a rule, say so in four words ("a common starting point") and still give it. Ranges beat single values when practitioners genuinely vary.

## 2. Concrete over abstract

Name fonts, hex/OKLCH values, cubic-bezier curves, pixel and point sizes, grid columns, durations, word counts and real public references. Show a short example when a principle is subtle. Prefer tables for specs.

## 3. Direct voice

Imperative mood, active voice, short sentences. No preambles ("This section describes..."), no hedging chains, no repeated disclaimers. One verification note is fine where it is real: "Platform specs change; confirm against the current HIG before production."

Never use: "delve", "in the realm of", "in today's fast-paced world", "elevate", "seamless", "unleash", "game-changer", "thrilled to", "excited to share", "humbled to", "robust" (as filler).

## 4. Truthfulness

- Do not invent statistics, studies, laws, regulation details, platform limits or quotes. If unsure of a specific figure, give the well-established range or say "verify".
- Regulatory notes name the regime and what it typically affects in design (e.g., "COPPA (US): verifiable parental consent before collecting children's personal data; avoid persistent identifiers in analytics"), then: "Confirm requirements with counsel for the specific product and jurisdiction."
- Cite the owning source for standards (W3C WCAG 2.2, Apple HIG, Material Design 3, Core Web Vitals at web.dev) and date volatile specs ("as of 2026").
- Real brands may be named as public reference anchors for a style or category. Never reproduce their logos, artwork or proprietary copy in the repo.

## 5. Anti-generic stance

Name the generic AI look explicitly when relevant and give the specific alternative: default purple/indigo-to-pink gradients, Inter or system sans used for everything, centered hero plus three icon cards, emoji as icons, glassmorphism on everything, uniform 16px radius and drop shadow on every element, stock "diverse team high-fiving" imagery, lorem-like copy ("Unlock your potential"). A style or color is not banned; using it by default without a reason is the problem.

## 6. Length and structure

- Registered SKILL.md bodies: 60-160 lines. Route to references for depth.
- Reference files: 80-300 lines, one topic each, start with H1 then `Version-Timestamp:` line.
- Atlas entries: 70-160 lines following the exact schema.
- Use H2 for sections, tables for specs, bullets for lists of rules. No HTML in Markdown.

## 7. Accessibility is a default, not a section to skip

Every visual recommendation must survive WCAG 2.2 AA: text contrast 4.5:1 (3:1 for 24px+ regular or 18.66px+ bold), non-text UI contrast 3:1, target size at least 24x24 CSS px (44x44 recommended for touch), visible focus, reduced-motion alternative, no information by color alone.
