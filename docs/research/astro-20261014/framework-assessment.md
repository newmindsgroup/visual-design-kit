# Astro for the next website build

Version-Timestamp: 2026-10-14 10:29:10 AST

Status: researched from official sources; replacement skill installed locally and packaged as a portable team plugin. No website pilot, package installation, deployment, or MCP setup performed. Original community skill archived before replacement.

## Recommendation

Include Astro in the shortlist for the next content-led website. Start with one updated `astro` skill and selectively loaded references. Do not create a large family of overlapping skills before a real pilot shows where specialization helps.

Astro focuses on marketing, publishing, documentation, portfolios, and other content-rich sites. It combines HTML-first pages with selective interactivity. This makes it a credible candidate for agency websites with strong content and a limited number of interactive features. Performance is a design opportunity, not a guaranteed result. [Why Astro](https://docs.astro.build/en/concepts/why-astro/), [islands architecture](https://docs.astro.build/en/concepts/islands/).

For a product dominated by shared browser state and account workflows, compare an app framework against the actual requirements. For clients needing familiar visual page editing, compare WordPress/Elementor against Astro plus a CMS, including handoff and maintenance effort. Astro can support dynamic work, but choosing it does not supply an editor or simplify every business workflow.

## Rendering and hosting

Static pages are a sensible starting candidate where rebuild latency is acceptable. Add request-time rendering where freshness or request-specific behavior requires it. Current Astro supports per-route rendering choices with an appropriate adapter. The old `hybrid` output option was removed in Astro 5. A wholly static site does not require a server adapter. [Rendering guide](https://docs.astro.build/en/guides/on-demand-rendering/), [migration guide](https://docs.astro.build/en/guides/upgrade-to/v5/).

Vercel is a candidate if it matches the project workflow. Cloudflare, Netlify, and Node are alternatives, selected by runtime and operational requirements. Verify host-specific feature behavior rather than assuming local preview proves deployment compatibility. [Deployment overview](https://docs.astro.build/en/guides/deploy/), [Vercel adapter](https://docs.astro.build/en/guides/integrations-guide/vercel/).

## Content and client handoff

Astro supports schema-based collections and Markdown/MDX, with loaders connecting content sources. The editor decision should come first: Git content, a headless CMS, or an existing WordPress backend. Decide draft preview, publishing roles, content freshness, localization, cost, and maintenance ownership before choosing a CMS. Current collections use loader-based configuration and APIs that differ from older tutorials. [Collections](https://docs.astro.build/en/guides/content-collections/).

Headless WordPress is supported as a content-source approach. It is not an automatic conversion of existing visual-builder layouts or plugin behavior. A migration needs explicit treatment of URLs, forms, SEO, shortcodes, previews, and editorial workflows. [WordPress guide](https://docs.astro.build/en/guides/cms/wordpress/).

## AI-assisted development

Astro provides an official remote documentation MCP at `https://mcp.docs.astro.build/mcp`, backed by kapa.ai. It can help agents retrieve current APIs. Direct documentation remains a valid fallback. Connecting it requires a separate configuration and trust decision; generic technical queries should avoid confidential project data. The docs also describe version-dependent agent background-server behavior. The skill therefore requires installed-version checks and owned-process tracking instead of hardcoded assumptions. [AI guide](https://docs.astro.build/en/guides/build-with-ai/).

## Integration shortlist

| Capability | Candidate | Reason to include |
| --- | --- | --- |
| Public sitemap | @astrojs/sitemap | Public route discovery with explicit exclusions |
| Rich authoring | @astrojs/mdx | Components inside content when actually needed |
| Interactive widgets | @astrojs/react | Reuse React with selective hydration |
| Documentation site | Starlight | Specialized documentation UX |
| On-demand routes | Host-specific adapter | Runtime behavior matched to hosting |
| Utility styling | Tailwind 4 via Vite | Optional, preserve project style choice |

The directory is a discovery tool with both official and community entries. Package popularity is not a trust verdict. Review package identity, maintenance, compatibility, license, and data flows before use. [Integrations](https://astro.build/integrations/).

The directory still lists the legacy Astro Tailwind integration, while current styling guidance uses the Tailwind Vite plugin for Tailwind 4. Astro >=5.2 supports installing it through `astro add tailwind`. This illustrates why the skill must consult package-specific, version-matched docs. [Styling guide](https://docs.astro.build/en/guides/styling/).

## Existing skill audit and proposed structure

The installed `the authoring machine local Astro skill` declares community authorship and predates current guidance. It contains legacy collection configuration, `post.slug`, `post.render()`, `output: 'hybrid'`, an old Vercel import, and overbroad claims about private variables never reaching clients. Its examples also do not establish production form reliability. It was inspected as source material, not executed or trusted as a client-work dependency.

The replacement has one short entrypoint and four references: architecture, content/editing, integration/AI decisions, and observable verification. It reuses existing design and engineering gates. Later specialist skills should be added only after repeated evidence, for example a WordPress migration workflow or a reusable CMS connector with real tests.

## First pilot and acceptance

Use a bounded local or private pilot with a home page, reusable service page, article collection, and one form connected to a mock or authorized test destination. Match the selected design system. Verify mobile/desktop rendering, keyboard behavior, drafts excluded from production routes/feed/sitemap, diagnostics/build, form failure and duplicate handling, and measured JS/image performance. If a CMS is chosen, verify an editor can preview and publish an update and measure delivery latency. If request-time routes are used, verify the actual host runtime in an authorized preview deployment.

Three open decisions: client editing workflow, first site's interaction requirements, and hosting/maintenance ownership. First move: choose the pilot site and editor workflow. No CMS, hosting provider, or production migration has been selected by this research.

## Validation and provenance

Skill validation and independent review results are recorded in `validation.txt` and review JSON files in this packet. Those checks concern the research and skill documents; no website runtime performance or delivery is claimed.

Routing: model-governor classified public research as subscription Terra Medium, Standard. Current Codex runtime retained for live-tool orchestration; no model switch claimed. Primary skill: system skill-creator. Independent review: claude-opus-delegator via bounded helper, public-only evidence. Review provenance is recorded in returned JSON. Missing review capacity leaves review pending.

Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-14 10:29:10 AST

## Selected scope and delivery

User confirmed client marketing/content websites, CMS selected per project, and both a local Codex skill and reusable team plugin. Local entrypoint: `the authoring machine local Astro skill`. Portable source: [portable skill source](../../../extras/astro-website-studio/skills/astro/SKILL.md). Package: `astro-website-studio-0.1.0.zip`. The package is ready for team installation; it has not been uploaded or shared. Use one delivery path per receiving environment to avoid loading duplicate skills.

Publication note: this is the dated initial assessment. The portable source is included in this repository; no ZIP is required. The integrated Design Kit implementation is documented in HEADLESS-UI-041.md.
