# Stack selection

Version-Timestamp: 2026-10-20 02:04:32 UTC

Choose the stack from three questions: who edits the site after launch, how interactive and personalized it is, and who maintains it. The best-looking design fails if the client cannot update it or if it ships a megabyte of JavaScript to show a brochure. Products, features and pricing below change often; verify current plans before recommending one to a client.

## Decision matrix

| Site profile | Default | Why | Watch for |
| --- | --- | --- | --- |
| Marketing, brochure, portfolio, content or campaign site maintained by developers or a studio | **Astro** | Static-first output with zero JavaScript by default, islands for the interactive parts, content collections with typed schemas, Markdown and MDX, built-in image optimization; works with Vue, React, Svelte or plain HTML | Highly personalized or app-like pages push toward Next.js |
| Documentation | **Astro Starlight** | Search, navigation, i18n and accessible defaults out of the box | Custom app features |
| App-like site: authentication, dashboards, personalization, heavy interactivity, custom commerce logic | **Next.js** (App Router) | React Server Components keep much of the work on the server; mature routing, data fetching, middleware, image and font tooling | Client components quietly growing the bundle; hosting features that tie you to one provider |
| App-like alternatives | React Router v7 (the Remix line), SvelteKit, Nuxt | Team skills and preferences | Ecosystem size for needed integrations |
| Client edits often, no developers on retainer, broad plugin needs | **WordPress** (block themes with `theme.json`) | Familiar editor, huge ecosystem, many hosts and freelancers | Plugin sprawl, security updates, performance depends on theme discipline |
| Design-led team that wants visual building and hosting in one tool | **Webflow** | Visual layout with a CMS, interactions and managed hosting | Plan limits on CMS items, locales and seats; code export is limited |
| Fast, animated marketing pages owned by designers | **Framer** | Very fast iteration, strong motion, CMS for blogs and simple collections | Complex logic, large content models, deep integrations |
| Online store | **Shopify** (themes, or Hydrogen for headless); WooCommerce on WordPress; Medusa for custom headless | Payments, tax, inventory and checkout solved | Theme performance, app sprawl, checkout customization limits |
| Content-heavy site edited daily by marketers, built by developers | **Astro or Next.js with a headless CMS** | Editors get a CMS; developers keep performance and design control | Preview and visual editing setup; CMS cost at scale |

**Separate marketing site and app?** When the marketing team ships weekly and the product team ships on its own cadence, build the marketing site in Astro (or a no-code tool) and the app in Next.js, and share the kit tokens (`library/tokens/dist/tokens.css` and `tailwind.css`) so both look like one brand.

## Astro in this kit

- Deep process and decisions: [Astro build skill](../../../library/draft-skills/design-web-astro/SKILL.md), including its architecture, Headless UI and research references.
- Working example: [Astro motion example](../../../library/examples/astro-motion/) with Astro, Vue islands, Tailwind 4, GSAP and Headless UI components, including reduced-motion handling and tests. Copy it to a project folder before installing; never install into the plugin.
- Hydration directives: `client:visible` for below-the-fold widgets, `client:idle` for non-urgent ones, `client:load` only for what must work immediately (menu toggles should be plain HTML and CSS or a tiny script).
- Output: static by default; add an adapter (Node, Vercel, Netlify, Cloudflare) only for routes that need a server.
- Motion components and recipes: [web motion library](../../../library/draft-skills/design-web-motion-library/SKILL.md).

## Next.js notes

- Keep marketing routes static (generated at build or cached with revalidation); use server components by default and mark client components deliberately.
- Use `next/image` and `next/font` for image and font optimization.
- Watch the client bundle per route with the build output and a bundle analyzer; budgets are in [performance](performance.md).
- Middleware for locale routing and auth redirects; avoid heavy work there.
- Hosting: Vercel is the reference platform; self-hosting on Node or containers and other platforms' adapters work but may lack some features. Check which features the chosen host supports.

## Self-edit platforms: protect the design

- Mirror the token names as the tool's variables or global styles (colors, type scale, spacing, radius), so editors pick from the system instead of inventing values.
- Build page sections as locked components or patterns with editable content slots; restrict free-form styling.
- Write an editor guide: image sizes and ratios, headline lengths, alt text, how to add a page.
- WordPress: map tokens into `theme.json` presets; limit plugins to a reviewed list; managed hosting with automatic updates and backups.
- Webflow and Framer: confirm plan limits (CMS items, locales, form submissions, bandwidth) against the content plan before committing.

## Headless CMS selection criteria

| Criterion | Questions to answer |
| --- | --- |
| Editor experience | Is there live preview or visual editing? Do editors compose pages from sections, or fill structured fields? |
| Content modeling | References, nested components, validation, custom rich-text blocks, reusable snippets |
| Localization | Field-level or document-level translation, fallback locales, translation workflow integrations |
| Workflow and roles | Drafts, scheduled publishing, approvals, granular roles, audit log, SSO |
| Media | Asset library, image CDN with transformations, focal points, alt text fields |
| Developer experience | REST or GraphQL, generated TypeScript types, webhooks to trigger rebuilds, preview APIs, rate limits |
| Hosting model | SaaS or self-hosted open source; data residency (EU hosting); backups; export format and lock-in |
| Cost at scale | Seats, records, locales, API calls and bandwidth at the expected volume in year two |
| Longevity | Company or community health, release cadence, migration path |

Common options by fit: **Sanity** (schema in code, real-time collaboration, visual editing), **Contentful** (enterprise workflows and governance), **Storyblok** (visual editor with component blocks), **Prismic** (slice-based page building for marketers), **Payload** (open source, TypeScript, self-hosted, close to Next.js), **Strapi** and **Directus** (open source, self-hosted), **DatoCMS** and **Hygraph** (hosted, GraphQL-first). Git-based editors (**Keystatic**, **Decap CMS**, **TinaCMS**) keep content in the repository and suit small teams and developer-run sites.

Model content as types with fields (Article: title, slug, summary, body, author reference, topics, hero image with alt, SEO title, SEO description, OG image), not as pages of free-form blocks, unless marketers truly need to compose landing pages.

## Hosting criteria

- Global CDN, automatic HTTPS, HTTP/2 or HTTP/3, Brotli.
- Preview deployments per branch or pull request for client review.
- Serverless or edge functions for forms and APIs, with logs.
- Image optimization at the edge, or a build-time pipeline.
- Instant rollback to a previous deployment.
- Pricing at expected traffic: bandwidth, function invocations, build minutes, seats.
- Region and data residency for regulated clients; DDoS protection and a web application firewall.

Typical choices: Vercel, Netlify and Cloudflare (Pages and Workers) for static and hybrid sites; container hosts (Fly.io, Render, Railway, or a cloud provider) for custom servers; managed WordPress hosts for WordPress.

## Consent and privacy

These shape design; confirm requirements with counsel for the specific product and jurisdiction.

- **EU and UK:** the ePrivacy Directive (Article 5(3)) and the UK's PECR require consent before setting non-essential cookies or similar storage, with consent to the GDPR standard: freely given, specific, informed, unambiguous, and as easy to withdraw as to give. Regulators expect a first-layer "Reject all" as prominent as "Accept all". The UK's Data (Use and Access) Act 2025 added narrow exceptions, including analytics used only to compile aggregate statistics that improve the site, provided visitors are told and can object easily; advertising cookies still need consent. Check the ICO's current storage and access technologies guidance.
- **United States:** state privacy laws (California's CCPA/CPRA and a growing list of others) require privacy notices, an opt-out of sale, sharing and targeted advertising (a "Do Not Sell or Share My Personal Information" link where applicable), and honoring Global Privacy Control browser signals in states that require it.
- **Google tags:** Google requires Consent Mode v2 signals for ads measurement and personalization with EEA and UK users (since March 2024), and a Google-certified consent platform for publishers serving Google ads there.
- **Consent platforms:** Cookiebot, OneTrust, Usercentrics and Didomi are common commercial options; open-source libraries (such as Klaro or orestbida's CookieConsent) suit small sites. Whatever the tool, block tags until consent, log consent, and keep a footer link to reopen settings.
- **Analytics:** GA4 is free but needs consent in the EU and UK. Privacy-focused tools (Plausible, Fathom, Simple Analytics, Matomo configured without cookies) collect less data; some EU regulators (such as France's CNIL) exempt properly configured audience measurement from consent, but rules differ by country.
- **Privacy by design:** self-host fonts (a Munich court ruled in 2022 that embedding Google Fonts from Google's servers transmitted visitors' IP addresses without a legal basis); load YouTube and map embeds behind a click-to-load facade; collect only the form fields you need; set retention periods.
- **Pages to publish:** privacy policy, cookie policy, terms, and an accessibility statement where required (EU public sector; services under the European Accessibility Act). The [launch checklist](launch-checklist.md) lists the rest.

## Recording the decision

Write a short stack decision record: the profile of the site, the options considered, the choice and why, who edits and how, hosting and cost estimate for year one and two, consent and analytics approach, and what would trigger a change. The deep process for client projects is in the [CMS](../../../library/draft-skills/design-web-cms/SKILL.md), [platform adapters](../../../library/draft-skills/design-web-platform-adapters/SKILL.md) and [privacy](../../../library/draft-skills/design-web-privacy/SKILL.md) drafts.
