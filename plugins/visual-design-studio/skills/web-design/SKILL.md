---
name: web-design
description: >-
  Designs and ships websites: landing pages, homepages, product, pricing, about and blog pages, conversion and ethical
  persuasion, responsive and fluid layouts, images, Core Web Vitals performance, SEO and structured data, stack and CMS
  choice (Astro, Next.js, WordPress, Webflow, Framer) and launch QA. Use when planning, designing, building, auditing or
  launching a website or landing page, improving conversion, speed or search visibility, or choosing a web stack.
license: MIT
metadata:
  version-timestamp: "2026-10-20 02:04:32 UTC"
  agent-attribution: "computer=vm; tool=Claude Code; version=2.1.304; timestamp=2026-10-20 02:04:32 UTC"
---

# Web design

An excellent website says what it offers and for whom within five seconds, proves it with specifics, makes the next step obvious, loads fast on a mid-range phone, works for everyone, and can be found. Its look comes from the chosen direction and brand tokens, never from the template every other site uses.

## Defaults

| Decision | Default | Change when |
| --- | --- | --- |
| Breakpoints | Mobile-first `min-width` at sm 640, md 768, lg 1024, xl 1280, 2xl 1536px (token contract) | Content breaks earlier: add a component-level container query, not a new global breakpoint |
| Containers | Page max `--container-xl` (1280px); text at `--measure-body` (66ch); side padding `--gutter` | Editorial or luxury: wider canvas with narrower text |
| Body text | 16-18px, line-height 1.5-1.65 (`--line-height-normal` to `--line-height-relaxed`) | Long-form articles: 18-21px |
| Fluid type | `clamp()` with rem + vw; max size no more than 2.5x min so 200% zoom still works | Fixed sizes for UI controls |
| Section rhythm | Vertical padding `clamp(var(--space-12), 2rem + 5vw, var(--space-24))` (48px at 320 to 96px at 1280) | Dense product pages: `--space-8` to `--space-16` |
| Hero | Headline of 6-12 words naming the outcome, one supporting sentence, one primary CTA, real product or proof visual | Brand campaigns: image-led hero with a short line |
| CTAs | One primary goal per page; verb + outcome labels ("Start free trial"); 44-48px tall | Content pages: soft secondary CTA (newsletter) only |
| Core Web Vitals (p75, field) | LCP 2.5 s or less, INP 200 ms or less, CLS 0.1 or less; design for LCP 2.0 s to keep margin | Never relax |
| Budgets (starting points) | JS 150 KB compressed on marketing pages; LCP image 200 KB or less; 2 font families, 4 font files or fewer | App-like pages: JS up to about 300 KB, split by route |
| Images | AVIF with WebP fallback in `picture`, `srcset` + `sizes`, explicit `width`/`height`, lazy below the fold, `fetchpriority="high"` on the LCP image | Logos and icons: SVG |
| SEO | Unique `title` (about 50-60 characters), meta description (about 120-160), one `h1`, JSON-LD for Organization and page type, canonical, XML sitemap | Noindex utility and thin pages |
| Accessibility | WCAG 2.2 AA; axe plus keyboard plus one screen reader before launch | Public sector and EU services: add an accessibility statement |
| Stack | Astro for marketing and content sites; Next.js for app-like sites; WordPress, Webflow or Framer when the client edits without developers | See [stack selection](references/stack-selection.md) |
| Consent | No non-essential cookies or tags before consent in the EU and UK; "Reject all" as prominent as "Accept all" | Cookieless, consent-exempt analytics where the jurisdiction allows |
| Social cards | Open Graph and Twitter card per page, image 1200x630 | |

## Workflow

Paths in commands are relative to this skill's directory; resolve them to absolute paths before running.

1. **Brief and discovery.** Goal and KPI per site and per page, audiences and their top tasks, traffic sources, competitors, existing analytics and Search Console data. For a redesign, audit content, SEO, Core Web Vitals field data and accessibility first.
2. **Direction.** If the look is not set, run the `design-director` skill. Query the atlas: `python3 ../../library/scripts/atlas.py query "<industry, market, audience, tier> marketing website"` and read the `channel.marketing-website` entry.
3. **Structure.** Sitemap, page types and content model with `ux-design` [information architecture](../ux-design/references/information-architecture.md); messaging hierarchy per page.
4. **Page architecture.** Wireframe each page type section by section with real copy using [page architecture](references/page-architecture.md) and [conversion](references/conversion.md).
5. **Visual design.** Apply the direction's tokens; design at 375px and 1440px, then specify behavior at every breakpoint with [responsive and fluid](references/responsive-and-fluid.md). Components and states come from `ui-design`.
6. **Choose the stack and CMS** with [stack selection](references/stack-selection.md), including hosting, consent and analytics.
7. **Build** semantic HTML on the kit tokens (`../../library/tokens/dist/tokens.css`), the image pipeline, fluid type, and performance budgets per [performance](references/performance.md); SEO per [SEO](references/seo.md).
8. **Render and inspect.** Screenshot every page type at 375, 768, 1280 and 1440px in light and dark; review with the `design-critique` skill; run Lighthouse on mobile and axe on every template; fix before showing anyone.
9. **Launch** with the [launch checklist](references/launch-checklist.md); recheck field Core Web Vitals and Search Console after 28 days.

## Decisions that change the answer

- **Site type.** Single-goal landing page: minimal navigation, one CTA repeated. Corporate multi-page: audience routing from the homepage. Content or editorial: reading comfort, search, related content. Commerce: product detail and checkout patterns from `ui-design` [flows](../ui-design/references/flows.md). Docs: search, versioning, code samples.
- **Traffic source.** Paid traffic: message match between ad and page. Organic: depth of content and internal linking. Direct and returning: fast paths to sign-in and top tasks.
- **Industry and market.** Atlas entries set trust signals, regulation and conventions. Market changes language and `hreflang`, legal pages (an Impressum in Germany and Austria), consent rules, payment methods and type support for the script.
- **Audience.** `audience.low-bandwidth-entry-devices`: halve the budgets and test on a low-end Android device. `audience.older-adults`: 18px+ body, high contrast, no hover-only content. `audience.b2b-buying-committee`: pages for each role, pricing transparency, security and procurement content.
- **Price tier.** Luxury: slower pacing, larger imagery, fewer words, but the same LCP budget. Value: price and proof up front, dense comparison.
- **Who edits after launch.** Developers only: Astro or Next.js with Markdown or a headless CMS. Marketers daily: a visual CMS or a no-code builder with locked design tokens.

## Common failures

- The generic AI site: centered headline over a purple gradient blob, three icon cards, a logo strip and "Unlock your potential". Fix: a specific value proposition, real product proof, the direction's layout logic and copy with numbers.
- A perfect Lighthouse score with poor field INP from tag managers and chat widgets. Fix: judge by CrUX or RUM at p75; facade or defer third parties.
- Lazy-loading the hero image. Fix: eager load, `fetchpriority="high"`, preload if discovered late.
- Autoplaying hero video with no pause control. Fix: poster image, muted, a visible pause button (WCAG 2.2.2), no autoplay under reduced motion.
- Cookie banners that hide "Reject", cover the CTA or trap focus. Fix: equal-weight buttons, bottom placement that does not obscure focus.
- Eight "Learn more" buttons. Fix: one primary CTA per section with a specific label; descriptive links.
- Staging `noindex` shipped to production, or no redirect map after a migration. Fix: the launch checklist.
- Pure `vw` font sizes that do not scale with zoom. Fix: `clamp()` with a rem component.
- Fake countdown timers and "Only 2 left" when untrue. Fix: the dark-pattern rules in [conversion](references/conversion.md).

## References

- [Page architecture](references/page-architecture.md): landing page anatomy, section patterns, homepage, product, pricing, about, blog, CTA design.
- [Conversion](references/conversion.md): value proposition, social proof, friction, ethical persuasion, dark-pattern rules (FTC, EU DSA, UCPD, UK DMCC).
- [Responsive and fluid](references/responsive-and-fluid.md): breakpoints, fluid type and space, container queries, responsive images, AVIF/WebP, art direction, aspect ratio.
- [Performance](references/performance.md): Core Web Vitals thresholds, budgets, image, font and third-party strategy, lab versus field data.
- [SEO](references/seo.md): semantic HTML, titles, meta descriptions, headings, JSON-LD, sitemaps, canonicals, hreflang, Open Graph.
- [Stack selection](references/stack-selection.md): Astro, Next.js, WordPress, Webflow, Framer, headless CMS criteria, hosting, consent and privacy.
- [Launch checklist](references/launch-checklist.md): browsers, accessibility, performance, SEO, analytics, legal pages, redirects, 404, favicons, OG images, security headers.
- Atlas: `python3 ../../library/scripts/atlas.py query "boutique hotel website in Japan, luxury"`; `show channel.marketing-website` for channel specs.
- Working code: [Astro motion example](../../library/examples/astro-motion/README.md) (Astro, Vue, Tailwind 4, GSAP, Headless UI) and the [Astro build skill](../../library/draft-skills/design-web-astro/SKILL.md).
- Deep process for client projects, by lifecycle stage ([website workflow](../../library/WEBSITE-WORKFLOW.md)):
  - **Discover and plan:** [discovery](../../library/draft-skills/design-web-discovery/SKILL.md), [audit](../../library/draft-skills/design-web-audit/SKILL.md), [migration](../../library/draft-skills/design-web-migration/SKILL.md), [content strategy](../../library/draft-skills/design-web-content-strategy/SKILL.md).
  - **Structure:** [information architecture](../../library/draft-skills/design-web-information-architecture/SKILL.md), [page architecture](../../library/draft-skills/design-web-page-architecture/SKILL.md), [page templates](../../library/draft-skills/design-web-page-templates/SKILL.md), [site search](../../library/draft-skills/design-web-search/SKILL.md).
  - **Design:** [art direction](../../library/draft-skills/design-web-art-direction/SKILL.md), [responsive](../../library/draft-skills/design-web-responsive/SKILL.md), [media](../../library/draft-skills/design-web-media/SKILL.md), [system assembly](../../library/draft-skills/design-web-system-assembly/SKILL.md), [conversion](../../library/draft-skills/design-web-conversion/SKILL.md), [forms](../../library/draft-skills/design-web-forms/SKILL.md), [copy fit](../../library/draft-skills/design-web-copy-fit/SKILL.md), [storytelling](../../library/draft-skills/design-web-storytelling/SKILL.md), [visual review](../../library/draft-skills/design-web-visual-review/SKILL.md).
  - **Build:** [frontend](../../library/draft-skills/design-web-frontend/SKILL.md), [Astro](../../library/draft-skills/design-web-astro/SKILL.md), [motion library](../../library/draft-skills/design-web-motion-library/SKILL.md), [CMS](../../library/draft-skills/design-web-cms/SKILL.md), [platform adapters](../../library/draft-skills/design-web-platform-adapters/SKILL.md), [integrations](../../library/draft-skills/design-web-integrations/SKILL.md), [privacy and consent](../../library/draft-skills/design-web-privacy/SKILL.md).
  - **Verify:** [fidelity](../../library/draft-skills/design-web-fidelity/SKILL.md), [accessibility](../../library/draft-skills/design-web-accessibility/SKILL.md), [performance](../../library/draft-skills/design-web-performance/SKILL.md), [SEO](../../library/draft-skills/design-web-seo/SKILL.md), [browser QA](../../library/draft-skills/design-web-browser-qa/SKILL.md), [analytics](../../library/draft-skills/design-web-analytics/SKILL.md).
  - **Launch and run:** [release](../../library/draft-skills/design-web-release/SKILL.md), [maintenance](../../library/draft-skills/design-web-maintenance/SKILL.md).
  - **Site types, when relevant:** [commerce](../../library/draft-skills/design-web-commerce/SKILL.md), [accounts](../../library/draft-skills/design-web-accounts/SKILL.md), [localization](../../library/draft-skills/design-web-localization/SKILL.md), [directories and marketplaces](../../library/draft-skills/design-web-directory/SKILL.md), [editorial](../../library/draft-skills/design-web-editorial/SKILL.md), [booking](../../library/draft-skills/design-web-booking/SKILL.md).
- Related skills: `design-director` (direction), `ux-design` (research, IA, content), `ui-design` (components, forms, flows), `typography`, `color`, `layout`, `imagery`, `motion`, `design-critique`.

Catalog IDs covered: web-discovery, web-audit, web-migration, web-content-strategy, web-information-architecture, web-page-architecture, web-page-templates, web-search, web-art-direction, web-responsive, web-media, web-system-assembly, web-conversion, web-forms, web-copy-fit, web-storytelling, web-visual-review, web-frontend, web-astro, web-motion-library, web-cms, web-platform-adapters, web-integrations, web-privacy, web-fidelity, web-accessibility, web-performance, web-seo, web-browser-qa, web-analytics, web-release, web-maintenance, web-commerce, web-accounts, web-localization, web-directory, web-editorial, web-booking
