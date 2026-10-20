---
id: style.dark-tech-developer
axis: style
name: Dark Tech / Developer
aliases: [developer dark mode, dev tools aesthetic, terminal aesthetic, dark mode saas, hacker aesthetic, linear style, devtool dark]
summary: Near-black canvas, hairline borders, monospace accents and one signal color; built for people who live in terminals and editors, with code and real product output as the hero visual.
tags: [dark, developer, terminal, code, monospace, devtools, technical, minimal, keyboard]
pairs_with: [industry.developer-tools, industry.ai-products, industry.crypto-web3, industry.gaming-esports, audience.expert-power-users, archetype.magician, archetype.explorer, channel.web-app, channel.marketing-website]
avoid_with: [audience.older-adults, audience.children-under-13, industry.healthcare-provider, industry.government-civic, archetype.caregiver, tier.ultra-luxury]
version_timestamp: 2026-10-20 01:57:45 UTC
---

# Dark Tech / Developer

## Essence

Respect the reader's time and eyes. Developers spend hours in dark editors, so a dark, low-chrome interface with precise borders, monospace details and instant response reads as "made by people who use this". The product itself (code, logs, a command palette, a diff) is the illustration. Reference points: Vercel's Geist system, Linear, GitHub Primer dark, Raycast, Warp, Supabase, Zed.

## Visual signature

- Canvas near black but never pure `#000`; three surface steps separated by 1px borders rather than shadows.
- One signal color (mint, lime, electric blue or amber) for primary actions, active states and the logo mark; everything else is neutral.
- Monospace for labels, numbers, keyboard hints (`⌘K`), version tags and code; a neutral grotesque for prose.
- Real code, terminal output, API responses and diffs as the hero visual, syntax-highlighted with a restrained 4-color theme.
- Keyboard-first cues: visible shortcuts, command palette, focus rings that are always shown.
- Faint grid, dot or noise texture at 3-6% opacity behind the hero; a single soft glow behind the signal color at most once per screen.

## Token recipe

| Token | Value |
| --- | --- |
| Display font | Geist (OFL); Hubot Sans (OFL, GitHub's technical variable-width sans); commercial: Söhne, GT America |
| Body font | Geist (OFL); commercial: Söhne Text |
| Mono (code, labels) | Geist Mono (OFL); JetBrains Mono (OFL); commercial: Berkeley Mono, Söhne Mono |
| Type scale ratio | 1.200 for product UI, 1.250 for marketing; product body is 13-14px, marketing body 16px |
| Body size / line-height | UI 14px / 1.4; docs and marketing 16px / 1.6; code 13-14px / 1.6; measure 60-68ch |
| Display letter-spacing | -0.03em to -0.04em at 48px+; line-height 1.0-1.1; mono labels +0.02em |
| Caps / labels | 11-12px mono, uppercase, +0.06em, regular weight, muted color |
| Weights | 400 body, 500 UI and buttons, 600 display; dark backgrounds make type look heavier, so avoid 700 |
| Palette | Canvas #0A0B0E (oklch 0.15 0.007 271); Surface #12141A (oklch 0.19 0.013 271); Raised #1A1D25 (oklch 0.23 0.016 269); Border #2A2E38 (oklch 0.30 0.019 268); Text #E7E9EE (oklch 0.93 0.007 269); Muted #9AA1AE (oklch 0.71 0.021 263); Signal mint #3DDC97 (oklch 0.80 0.164 160); Syntax blue #7AA2F7 (oklch 0.72 0.132 264) |
| Status colors | Amber #F5B83D (oklch 0.82 0.15 81) for warnings; coral #FF6B6B (oklch 0.71 0.181 23) for errors; always pair with an icon or label |
| Accent proportion | Signal color under 5% of pixels: primary button, active nav marker, cursor, one chart series |
| Radius | 4-6px controls, 8px cards and menus, 0 for terminal panes; avoid pills except tags |
| Borders | 1px #2A2E38 for dividers; interactive controls use #6B7586 (oklch 0.56 0.029 261) for 3:1 or better |
| Shadow / elevation | Prefer borders plus `inset 0 1px 0 rgb(255 255 255 / 0.04)`; menus `0 12px 32px rgb(0 0 0 / 0.5)`; glow only `0 0 24px rgb(61 220 151 / 0.25)` on the single hero accent |
| Spacing density | 4px base; product rows 32-36px high, 8-12px padding; marketing sections 96-128px |
| Grid | Marketing 12 columns max 1200px with visible 1px column rules optional; docs 240px nav + 720px content + 200px table of contents |
| Motion | 100-160ms, cubic-bezier(0.2, 0, 0, 1); command palette scales 0.98 to 1 with opacity; typing and cursor effects only where they show real output |

## Composition and layout

- Left-align the hero: headline across 6-7 columns, a one-line value statement, a copy-able install command or "Get started" button, and the live product panel at right or below.
- Make code the layout unit: tabbed code blocks, split diff views, terminal frames at consistent 8px radius with a title bar of three neutral dots (no traffic-light colors).
- Docs-grade information architecture: persistent left nav, in-page table of contents, search (`/` or `⌘K`), version selector, copy buttons on every code block.
- Use dense lists and tables for pricing, changelogs and benchmarks; link every claim to a doc, repo or benchmark methodology.
- Provide a light theme. A meaningful share of developers prefer light mode, and docs are read in bright rooms and print; build tokens for both from the start.

## Imagery and iconography

- Product screenshots, terminal recordings and architecture diagrams drawn in the system palette. No stock photography; team photos only on about or careers pages.
- Icons: 1.5px outline on a 16px or 20px grid, square-ish joins, monochrome; use brand logos of integrations in grayscale until hover.
- Diagrams: boxes with 1px borders, monospace labels, one highlighted path in the signal color.
- OG images and social cards: a real code snippet or changelog line at 72-96px, not abstract orbs.

## Motion

Fast and informational. Hover states change border-color and background in 100ms; menus open in 120ms with a 4px offset; toasts slide 8px. Animate real behavior: a log streaming, a build progressing, a diff applying. Avoid parallax, scroll-jacking and looping hero animations that do not correspond to the product. Respect `prefers-reduced-motion` by rendering the final frame of any terminal animation.

## Fits and risks

- **Fits:** developer tools, APIs, infrastructure and observability, AI tooling, security products, crypto and web3 infrastructure, gaming launchers and esports tooling. Strong with `audience.expert-power-users` who value density, shortcuts and honest documentation.
- **Risks:** it has become the default look for AI startups, so it signals "technical" but no longer signals "different". Dark UI also hides low contrast problems: gray-on-black text that looks fine on a calibrated studio display fails on a laptop outdoors.
- **Wrong for:** older adults, children, healthcare, government and caregiving brands, where warmth, large type and light backgrounds are expected.
- **Why these pair:** `industry.developer-tools`, `industry.ai-products` and `industry.crypto-web3` buyers read dark, code-forward UI as credible; `industry.gaming-esports` already works in dark, neon-accent environments; `archetype.magician` and `archetype.explorer` suit frontier and power themes; `channel.web-app` and `channel.marketing-website` can share one token set for product, docs and landing pages.
- **Why these clash:** `audience.older-adults` and `audience.children-under-13` need larger type, light backgrounds and warmth; `industry.healthcare-provider` and `industry.government-civic` depend on plain, high-contrast, light interfaces; `archetype.caregiver` contradicts the cool technical tone; `tier.ultra-luxury` reads as software, not craft.

## Do and don't

- Do set body copy to #E7E9EE or a slightly softer step instead of pure white; pure white on near-black halates and tires eyes.
- Do show real output: a genuine response body, an actual latency number, a changelog with dates.
- Do keep one signal color and let layout and spacing do the rest.
- Don't use neon green on black as a "hacker" costume unless the brand is literally about terminals.
- Don't put text on glowing gradient orbs; contrast changes under the text across the glow.
- Don't fake a terminal that types `npm install` in every hero; show something only this product can do.

## Clichés and AI tells

- Lazy version: black background, Inter or Space Grotesk, a purple-to-blue radial glow behind a centered headline, glass cards with 1px white-10% borders, an animated "typing" tagline, and a fake terminal.
- Fix: choose the signal color from the brand (mint, amber or a saturated blue) and name it; left-align the layout; replace the glow with a real product panel; set headings in Geist or Hubot Sans with tight tracking; show actual logs, diffs and benchmarks; add a light theme and a docs-quality reading mode.

## Accessibility notes

- Text #E7E9EE is 16.20:1 on canvas; muted #9AA1AE is 7.09:1 on surface and 6.49:1 on raised, so it is safe for secondary text. Muted text can drop to #8A92A0 (5.87:1 on surface, 5.38:1 on raised) but no lower for body-size copy.
- Signal mint #3DDC97 is 11.14:1 on canvas and 9.53:1 on raised; dark text #0A0B0E on a mint button is also 11.14:1.
- Hairline borders #2A2E38 are 1.45:1 on canvas: fine as decoration, not as the only edge of an input or button. Use #6B7586 (4.23:1 on canvas, 3.96:1 on surface) for control outlines.
- Syntax blue is 7.31:1, coral 6.63:1 and amber 10.35:1 on surface; keep error text to coral or lighter and never rely on red versus green alone in diffs (add +/- glyphs).
- Provide visible focus rings (2px mint, 2px offset), keyboard operability for every control, and a `prefers-contrast: more` step that raises borders to #6B7586.

## Reference anchors

- Vercel Geist (typeface and design system) and Vercel marketing site
- Linear (app and marketing) for restrained dark UI craft
- GitHub Primer dark themes and the Mona Sans / Hubot Sans typefaces
- Raycast, Warp and Zed for keyboard-first product design
- Stripe Docs and Tailwind CSS docs for documentation layout
- JetBrains Mono and Berkeley Mono type specimens
