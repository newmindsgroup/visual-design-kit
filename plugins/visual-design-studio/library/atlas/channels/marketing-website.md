---
id: channel.marketing-website
axis: channel
name: Marketing Website
aliases: [website, landing page, brochure site, corporate site, company website, microsite, campaign site]
summary: Public websites that explain, persuade and convert; judged by clarity of message, speed, search visibility, accessibility and conversion rather than feature depth.
tags: [website, landing page, conversion, seo, responsive, performance, hero, cms, astro, core web vitals]
pairs_with: [style.corporate-modern, style.editorial-magazine, style.swiss-international, style.vibrant-gradient-saas, industry.saas-b2b, industry.creative-agencies-studios, audience.b2b-buying-committee, archetype.sage, archetype.creator, tier.mid-market]
avoid_with: [audience.low-bandwidth-entry-devices]
version_timestamp: 2026-10-20 02:01:01 UTC
---

# Marketing Website

## Formats and specs

Web specs below are stable standards; thresholds and browser support change slowly. Confirm Core Web Vitals at web.dev/articles/vitals and WCAG at w3.org/TR/WCAG22 before sign-off.

| Item | Spec | Notes |
| --- | --- | --- |
| Design widths | 390 (mobile), 768 (tablet), 1440 (desktop); test 320 and 1920 | Kit breakpoints: 640, 768, 1024, 1280, 1536 px |
| Content container | 1120-1280px max; text measure 60-75ch | Full-bleed backgrounds, contained content |
| Core Web Vitals (field, p75) | LCP 2.5s or less; INP 200ms or less; CLS 0.1 or less | "Poor" above 4s, 500ms, 0.25; judged on real-user data at the 75th percentile (web.dev) |
| Page weight (starting point) | 1-1.5 MB transferred for a landing page; 170 KB or less of compressed JavaScript | Set a performance budget in CI |
| Images | AVIF or WebP with JPEG fallback; hero 200 KB or less; `srcset` at 480, 768, 1080, 1600, 2400 widths; explicit `width` and `height` | LCP image: no lazy-load, `fetchpriority="high"` |
| Color space | sRGB for all assets; Display P3 optional via CSS `color()` with sRGB fallback | Tag exported images |
| Fonts | WOFF2, 1-2 families, 4 files or fewer, subset; `font-display: swap` (or `optional`) | Preload only the display face |
| Video | MP4 H.264 plus WebM or AV1; muted, `playsinline`, poster frame; ambient loops under 2-5 MB | Never autoplay audio |
| Link preview image | 1200x630 (1.91:1), JPG or PNG, under 5 MB | Absolute HTTPS URL; confirm with each platform's debugger |
| Icons | SVG favicon, 32px ICO, 180px apple-touch-icon, 192 and 512px maskable PWA icons | |
| Targets | 24x24 CSS px minimum (WCAG 2.2 AA), 44px recommended for touch | |
| Metadata | Title 50-60 chars; description 120-160 chars; one H1; canonical; JSON-LD where relevant | Search engines rewrite snippets |

## Structure and hierarchy

- **Page architecture:** home, product or service pages, proof (cases, customers), pricing or engage, about, resources, contact. Primary navigation of 5-7 items plus one persistent CTA; footer carries the long tail.
- **Landing page order (default):** hero with promise and single CTA; proof (logos, numbers) within the first 1.5 screens; problem and outcome; 3-5 benefits with evidence; how it works; case study; objections or FAQ; repeat CTA. Move pricing earlier for high-intent traffic.
- **Hero:** headline 6-12 words at 40-72px desktop (32-40px mobile); subhead 18-22px, under 25 words; one primary and at most one secondary action; real product or place imagery, not abstract gradients.
- **One job per page:** one primary conversion, repeated every 1-2 screens. Forms ask for the minimum (3-5 fields); explain why you ask for phone numbers.
- **Rhythm:** section spacing 96-128px desktop, 56-80px mobile; alternate density so scrolling has a pulse.

### Page-type defaults

| Page | Job | Defaults |
| --- | --- | --- |
| Home | Orient and route | Hero promise, 2-3 audience paths, proof, one featured story; 5-7 sections |
| Product or service | Explain and convince | Outcome headline, 3-5 sections, real product visuals, comparison or specs, CTA repeated |
| Pricing | Remove doubt | 2-4 plans with one recommended, monthly/annual toggle, comparison table below, FAQ, "contact us" for enterprise, tax and currency stated |
| Case study | Prove it | Result number in the headline, challenge-approach-outcome, named quote with photo, 400-800 words |
| Article | Educate | 65-75ch measure, 18-20px body, line-height 1.6-1.7, byline and date, related links, contents list for long pieces |
| Contact or demo | Capture intent | 3-5 fields, response-time promise, alternative contact route, confirmation state |
| 404 and errors | Recover | Plain explanation, search, top links, brand voice kept light |

## Craft defaults

- Body 16-18px, line-height 1.5-1.6; headings use a 1.25-1.333 scale; fluid sizes with `clamp()` between 360 and 1440 widths.
- Buttons 44-56px high, label 16px+ medium weight, visible hover, focus (2px ring, 3:1 against adjacent colors) and pressed states.
- Motion: 160-320ms with `cubic-bezier(0.2, 0, 0, 1)`; scroll-triggered reveals only on non-critical content; honor `prefers-reduced-motion`. Avoid auto-advancing carousels and parallax that hijacks scroll.
- Navigation: sticky header 56-72px; mobile menu opens as a full-height panel with 44px targets; skip link; mega menus only above 20 destinations.
- Make the first screen specific. Replace default "centered hero plus three icon cards" with a product view, a proof number or an editorial layout built from the brand's `style.*` choice.
- Write real copy before final layout; test headlines at 320px width.

## Production and handoff

- Stack: static or hybrid frameworks (Astro for content-led marketing sites; Next.js when the site shares app code) with a headless CMS (Sanity, Contentful, Storyblok, Payload) or Markdown. The `web-design` skill covers page patterns, conversion, SEO, accessibility and stack choice in depth.
- Hand off Figma with tokens exported as CSS variables (see the kit's `--color-*`, `--space-*` names), real breakpoints, states, and a content model (fields, character limits).
- Specify analytics events (CTA click, form start, form submit) and consent behavior before launch.
- Privacy and law: cookie consent for non-essential tracking (GDPR and ePrivacy in the EU and UK, CCPA/CPRA opt-out in California); accessibility statements and the European Accessibility Act (applying to many consumer services in the EU since June 2025). Confirm requirements with counsel for the jurisdiction.
- Internationalize early: allow 30-40% text expansion, `hreflang`, locale-aware dates, currency and fonts for the script.

## QA checklist

- [ ] Field or lab data meets LCP 2.5s, INP 200ms, CLS 0.1 on a mid-range Android over 4G.
- [ ] WCAG 2.2 AA: contrast 4.5:1 text and 3:1 UI, keyboard path, visible focus, alt text, headings in order, reduced motion.
- [ ] Layouts verified at 320, 390, 768, 1024, 1440, 1920 and with 200% zoom and large text.
- [ ] One H1, unique titles and descriptions, canonical tags, sitemap, social images render in debuggers.
- [ ] All forms validate with clear errors, succeed, and send analytics events.
- [ ] 404, empty search, form failure and offline states designed.
- [ ] No lorem ipsum, placeholder logos or broken links; legal pages linked in footer.
- [ ] Screenshots reviewed for the generic AI look (indigo-pink gradients, uniform 16px card radius, Inter everywhere).

## Reference anchors

- web.dev Core Web Vitals documentation (web.dev/articles/vitals) and W3C WCAG 2.2
- Steve Krug, *Don't Make Me Think* (3rd ed., 2014); Ethan Marcotte, *Responsive Web Design* (2011)
- Nielsen Norman Group research on homepage and landing-page usability
- GOV.UK Design System and service manual for clarity-first content design
- Stripe, Linear, Apple and Vercel marketing sites as craft benchmarks for product storytelling and motion
