# Content and editing

Version-Timestamp: 2026-10-14 10:29:10 AST

Choose the editing workflow before building templates. Git-managed Markdown/MDX suits technical maintainers; a CMS may suit client editors. Compare CMS options by editor usability, preview and publishing needs, roles, localization, ongoing cost, portability, and operational ownership. Do not select a CMS merely because a loader exists.

Current collection guidance uses src/content.config.ts, defineCollection, loaders such as glob/file, entry IDs, and the render function from astro:content. Verify exact schema and import APIs against the installed major. Define required fields, URL rules, ordering, localization, image metadata, and draft status. Filter drafts consistently from route generation, listings, search, feeds, and sitemaps. Protect preview access; noindex alone is not access control.

For CMS content, choose build-time fetching or request-time fetching based on freshness requirements. Record webhook/rebuild or cache-invalidation ownership and failure behavior. Verify retries, upstream errors, missing entries, and invalid schemas. Avoid exposing CMS credentials through generated HTML, props, public environment variables, URLs, or logs.

Headless WordPress retains a WordPress editing backend while Astro supplies the frontend. It does not automatically reproduce Elementor/WPBakery layouts or plugin behavior. Before migration, inventory forms, search, redirects, SEO metadata, structured data, media, previews, memberships, commerce, and any shortcodes. Preserve source URLs and assets; map redirects and replacement behavior explicitly.

Sources: [collections](https://docs.astro.build/en/guides/content-collections/), [CMS overview](https://docs.astro.build/en/guides/cms/), [headless WordPress](https://docs.astro.build/en/guides/cms/wordpress/).


## Preview and freshness choices

| Path | Requirements | Failure or privacy concern |
| --- | --- | --- |
| Build-time content and isolated preview build | Rebuild trigger and protected preview hosting | Stale content after failed rebuild; drafts must stay isolated |
| Request-time authenticated preview route | Compatible server adapter, CMS draft access, authorization and private cache policy | Prevent preview responses or draft data from entering public caches |
| Live collections where installed version supports them | Version-matched loader contract and request-time runtime | Validate errors, schema and cache behavior; do not assume build-time loaders work unchanged |

Latest docs describe live collections; older releases may require experimental flags or lack the API. Check the installed major's release and reference documentation before adoption. Do not assume feature availability or stability from a historical example.

Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-14 10:32:00 AST
