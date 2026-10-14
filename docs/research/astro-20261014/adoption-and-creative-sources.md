# Who uses Astro, and creative sources to study

Version-Timestamp: 2026-10-14 10:48:41 AST

## Finding and scope

Current evidence supports Astro use on the checked pages of 12 AI, branding and marketing agency/consultancy sites, plus Bejamas as an adjacent web engineering agency. Thirteen public properties across twelve recognizable brands also showed current Astro-specific HTML signals. This is a curated sample, not a complete market census.

Public pages were fetched on 14 October 2026 with curl using ordinary TLS verification. Strong signals mean an Astro generator meta tag, data-astro-cid scoped attributes, or an astro-island element. An /_astro asset path alone was not accepted as a strong signal. These markers support an inference of Astro-generated output on the fetched page; they do not prove all routes, backend systems, authorship, accessibility, performance or corporate-wide use. Published first-party case studies and official showcase listings corroborate several entries. Other rows rely on live HTML markers for Astro evidence; their homepage links establish the business category. Raw requests, redirects, statuses and marker results are in live-checks.json, additional-checks.json and corrected-checks.json.

## AI and automation agencies/consultancies

| Organization | Focus | Evidence on its own website |
| --- | --- | --- |
| [Flow Digital](https://flow.digital/) | AI and workflow automation agency | Astro + Sanity migration documented by Lucky Media. [Source](https://www.luckymedia.dev/case-studies/automation-agency-escapes-webflow-lock-in-and-improves-performance). Current HTML signal: yes. |
| [Wanessa Labs](https://wanessalabs.com/) | AI consultancy | Own-site case study names Astro, Tailwind, three.js and Cloudflare Pages. [Source](https://wanessalabs.com/projects/wanessalabs-website/). Current HTML signal: yes. |
| [Ansell AI](https://ansell.ai/) | Fractional AI consultancy for agencies | Code23 documents its Astro launch site. [Source](https://code23.com/work/ansell-ai/). Current HTML signal: yes. |

## Branding and creative agencies

| Organization | Focus | Evidence on its own website |
| --- | --- | --- |
| [Embark](https://embarkagency.com.au/) | Brand strategy and design agency | Own-site article describes Astro + WordPress + Vercel. [Source](https://embarkagency.com.au/insights/what-building-our-award-winning-website-taught-us). Current HTML signal: yes. |
| [Bodkin](https://www.bodkin.studio/) | Brand identity, web and digital product design | Own-site article describes moving from Next.js to Astro with Markdown and no CMS. [Source](https://www.bodkin.studio/blog/why-we-rebuilt-the-bodkin-website). Current HTML signal: yes. |
| [Axxellance](https://axxellance.com/) | Brand and digital design studio | Own-site case study explicitly identifies an Astro build. [Source](https://axxellance.com/case-study/axxellance). Current HTML signal: yes. |
| [DesignMe](https://www.designme.agency/) | Brand, product and web design for tech/AI businesses | Homepage offers Astro and Next.js; current homepage HTML contains Astro-scoped attributes. [Source](https://www.designme.agency/). Current HTML signal: yes. |
| [Juice](https://www.juice.agency/) | Branding, web and marketing agency | Homepage identifies services; live generator tag explicitly names Astro. [Source](https://www.juice.agency/). Current HTML signal: yes. |
| [LOLO](https://loloagency.com/) | Brand design and strategy agency | Homepage identifies services; live generator tag explicitly names Astro. [Source](https://loloagency.com/). Current HTML signal: yes. |

## Marketing agencies

| Organization | Focus | Evidence on its own website |
| --- | --- | --- |
| [ClickForest](https://www.clickforest.com/en) | Performance marketing, SEO, commerce and AI automation | About page establishes agency services; current HTML contains Astro-scoped attributes. [Source](https://www.clickforest.com/en/about-us). Current HTML signal: yes. |
| [Rollin](https://www.agenciarollin.com/en) | Mixed AI, digital marketing and website agency | Astro development page explicitly says the agency own site uses Astro. [Source](https://www.agenciarollin.com/en/desenvolvimento-astro). Current HTML signal: yes. |
| [Hypefluency](https://hypefluency.com/) | Influencer and digital marketing agency | Homepage establishes services; live generator tag explicitly names Astro. [Source](https://hypefluency.com/). Current HTML signal: yes. |

## Adjacent web agency

| Organization | Focus | Evidence on its own website |
| --- | --- | --- |
| [Bejamas](https://bejamas.com/) | Website engineering and migration agency | Current generator names Astro; also an official partner. Do not classify all its clients as Astro users. [Source](https://astro.build/agencies/). Current HTML signal: yes. |

## Major-brand properties with current Astro signals

All thirteen properties below appear in the [official Astro showcase](https://astro.build/showcase/) and showed strong Astro signals in the current fetch. The named scope is deliberately narrower than claiming the entire company uses Astro. A single marker meets the minimum signal threshold; multiple markers provide stronger corroboration.

| Brand | Exact property | Current signal |
| --- | --- | --- |
| IKEA | [IKEA global gateway](https://www.ikea.com/) | data_astro_cid, astro_island |
| Porsche | [Dominican Republic regional site](https://www.porsche.com/latin-america-es/_dominican-republic_/?cs_redirect=1) | astro_generator, data_astro_cid, astro_island |
| Michelin | [Group corporate website](https://www.michelin.com/) | astro_island |
| Cloudflare | [Corporate/marketing homepage](https://www.cloudflare.com/) | astro_generator, data_astro_cid, astro_island |
| Netlify | [Corporate/marketing homepage](https://www.netlify.com/) | astro_generator, data_astro_cid, astro_island |
| Proton | [Public marketing homepage](https://proton.me/) | astro_island |
| Ricola | [Canadian English site](https://www.ricola.com/en-ca/) | astro_island |
| Jamie Oliver | [Official homepage](https://www.jamieoliver.com/) | astro_generator |
| Microsoft | [Fluent 2 design-system site](https://fluent2.microsoft.design/) | data_astro_cid, astro_island |
| Google Firebase | [Firebase blog](https://firebase.blog/) | data_astro_cid |
| Google Firebase | [Firebase Studio landing site](https://firebase.studio/) | astro_generator, data_astro_cid, astro_island |
| Visa | [Product design-system site](https://design.visa.com/) | astro_generator, data_astro_cid, astro_island |
| The Guardian | [Engineering publication](https://theguardian.engineering/) | data_astro_cid, astro_island |

Microsoft Fluent 2 also has an [October 2023 case study](https://astro.build/case-studies/microsoft/). Firebase blog has an [August 2023 case study](https://astro.build/case-studies/firebase/). Those historical articles are corroborated by current HTML checks here.

Porsche redirected to its Dominican Republic regional page. IKEA evidence concerns the global gateway, not all localized stores or checkout. Ricola evidence concerns en-ca. Visa, Microsoft and The Guardian examples are specific design/documentation/editorial properties, not their main corporate or consumer websites.

## Listed but current direct confirmation unavailable

Unilever and NordVPN appear in Astro current showcase, but both returned HTTP 403 to the direct check. Keep them as officially listed examples, with current implementation unconfirmed in this research. Dodonut is also listed, but dodonut.com now redirects to Bejamas. Count Bejamas as the current destination, not Dodonut as a separate current agency site. Lusion has a secondary directory listing and Astro-like asset paths, but lacked the stronger markers used for this list; it remains a creative lead rather than a confirmed main-list entry.

## Creative sources and how to use them

| Source | What to study | Reuse/status |
| --- | --- | --- |
| [Astro Showcase](https://astro.build/showcase/) | Production-site discovery across brands, agencies and personal sites. | Inspiration directory; listings are not proof of every route or current stack. |
| [Agency Gallery, Astro filter](https://agencygallery.com/stack/astro) | Agency positioning, service pages, portfolios and visual direction. | Secondary directory; verify live sites before describing them as current Astro users. |
| [Astro September 2026 roundup](https://astro.build/blog/whats-new-september-2026/) | Cosmic Canvas and Weird Wide Web sections surface creative Astro work. | Framework-published references; useful for fresh discovery. |
| [Codrops Creative Hub](https://tympanus.net/codrops/hub/) | Filter by Astro, GSAP, typography, transitions and WebGL. | Mixed-framework collection; not every creative demo is an Astro example. |
| [Atelier North tutorial](https://tympanus.net/codrops/2026/10/09/architecture-studio-astro-gsap/) | Minimal architecture-studio layout with GSAP pixel transitions and image reveals. | Fictional studio demo with source code, not an agency adoption example. |
| [Interlude](https://tympanus.net/codrops/2026/10/07/interlude-astro-page-transitions/) | 21 custom transitions using Astro ClientRouter and GSAP, including optional WebGL. | Starter, not a maintained package. Use native Astro transitions when sufficient. |
| [Astro WebGL gallery tutorial](https://tympanus.net/codrops/2026/02/02/building-a-scroll-revealed-webgl-gallery-with-gsap-three-js-astro-and-barba-js/) | Scroll-triggered shader reveals and multi-page portfolio transitions. | Advanced Astro + Three.js + GSAP + Barba demo. Keep one navigation owner; review lifecycle cleanup. |
| [Isle Thorne Collective](https://tympanus.net/codrops/2026/10/07/isle-thorne-collective-astro-template/) | Editorial product catalogue, reusable content collections and understated page transitions. | Publisher states MIT; checkout/newsletter are demos, with no production payments/accounts/stock. |
| [CodeTV landing-page challenge](https://codetv.dev/series/web-dev-challenge/s3/e5-best-landing-page-gsap) | Different creative approaches from animation specialists, with demo and source links. | Learning reference; starter source is https://github.com/webflow-examples/astro-gsap. Video not reviewed end to end. |

Code links: [Interlude](https://github.com/codrops/interlude/), [Isle Thorne Collective](https://github.com/codrops/isle-thorne-collective), [Atelier North](https://github.com/codrops/atelier-north), [WebGL gallery](https://github.com/J0SUKE/gsap-threejs-codrops), [Webflow Astro + GSAP starter](https://github.com/webflow-examples/astro-gsap). Source availability is not blanket clearance for bundled images, fonts, videos or dependencies. Check the selected repository license and asset rights before adoption. No third-party code was installed or executed. No browser screenshots or motion QA were performed; creative descriptions come from author documentation and site content.

## Suggested first references for our pilot

Start with Bodkin for content-led agency positioning and its Markdown workflow, Embark for the headless WordPress editing model, and Flow Digital for Astro plus Sanity. For a creative implementation experiment, use the Atelier North tutorial with one small reveal, or native Astro transitions before adding Interlude. The actual design choice still needs desktop/mobile rendering, reduced-motion and keyboard checks, plus a measured JavaScript budget. These are recommendations to evaluate, not validated design directions or benchmark results.

## Acceptance and next action

Checked: agency role against public descriptions, own-site scope, current page HTTP status and markers, brand property scope, published source links, demo-versus-production labels and report punctuation. Independent document review is recorded separately. Not checked: every route, browser rendering, performance, business outcomes, full video coverage, repository compatibility or security of reusable code. No emails, forms, account mutations, installations, sharing or browser tabs were involved.

First move: choose three reference sites and one motion pattern for a bounded pilot. Keep client content local and adapt the pattern to the approved project DESIGN.md.

Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-14 10:48:41 AST
