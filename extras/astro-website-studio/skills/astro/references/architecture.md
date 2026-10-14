# Fit and rendering

Version-Timestamp: 2026-10-14 10:29:10 AST

Astro is a candidate for marketing sites, portfolios, publications, documentation, and content-led commerce. For a dashboard with pervasive shared client state, evaluate an app framework against real requirements. Astro can support dynamic applications; avoid making framework selection a rigid category rule.

Decide page by page:

| Requirement | Candidate design | Operational question |
| --- | --- | --- |
| Public content with acceptable rebuild latency | Prerendered pages | Who triggers rebuilds, and what happens on failure? |
| Isolated browser interaction | Client island or small script | When must it hydrate, and what works without JS? |
| Request-specific or frequently changing data | On-demand route with adapter | Which runtime, cache policy, and failure behavior? |
| Delayed personalized fragment | Server island, if supported | Does it need request-time infrastructure and a fallback? |

In current docs, static output is the default. With an adapter, routes can opt into on-demand rendering using prerender = false. Server output reverses the default; routes can opt into prerendering. The hybrid output option was removed in Astro 5. Verify version-specific behavior before editing configuration.

Islands reduce unnecessary hydration but do not guarantee a fast website. Images, fonts, external scripts, and application code still need measurement. Server islands and client islands solve different problems.

Sources: [Why Astro](https://docs.astro.build/en/concepts/why-astro/), [islands](https://docs.astro.build/en/concepts/islands/), [rendering](https://docs.astro.build/en/guides/on-demand-rendering/), [Astro 5 migration](https://docs.astro.build/en/guides/upgrade-to/v5/).


## Version inspection

Use the package manager's dependency inspection (for example npm ls astro with npm projects) to establish resolved versions, then compare the lockfile and package manifest. Check Node engine constraints and the adapter's peerDependencies for those exact releases. Resolve disagreements before changing code. If dependencies are absent, record declared versions as declarations, not installed evidence.

Astro 4 legacy patterns and Astro 5+ patterns differ. The modern collection APIs described in [content.md](content.md), plus the rendering changes in this reference, are a starting map, not proof that every later major is interchangeable. Read the major upgrade guide and tagged package docs for the installed release; verify schema imports, experimental flags, image handling, and server runtime changes independently.

Use Astro's asset facilities where appropriate for optimized images; verify supported remote sources and avoid passing untrusted remote URLs to image processing. Choose navigation transitions only when the brief benefits and check the installed API name (modern docs use ClientRouter rather than older ViewTransitions examples). Do not add navigation animation by default.

Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-14 10:32:00 AST

For later majors, start with the [upgrade guide](https://docs.astro.build/en/upgrade-astro/) and select the relevant major migration guide.

Navigation source: [view transitions](https://docs.astro.build/en/guides/view-transitions/).
