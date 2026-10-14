---
name: design-web-astro
description: Build or maintain explicitly selected Astro websites with version-matched Tailwind styling, Vue islands, content and navigation decisions. Use after the website platform has been selected or for an explicit Astro evaluation.
---

# Astro website implementation

Version-Timestamp: 2026-10-14 14:03:25 AST

Read the project brief, DESIGN.md, tokens, package manifest/lockfile, runtime versions and accepted web-frontend inputs. Reuse existing audience/editor/host decisions; resolve material gaps before dependent work. Stack evaluation does not authorize migration or deployment.

Start with [the architecture and setup](references/architecture.md). For animation read [the engine comparison](references/research.md), then select `web-motion-library` and its exact technique. The [playground source](../../examples/astro-motion/README.md) provides original reusable specimens, not a mandatory website theme.

Use Astro for content and routing. Use the official Vue integration only for stateful islands; client:load for immediate controls, client:visible for deferred independent widgets. Prefer server-rendered content and explicit hydration over client:only for essential meaning. Keep one router owner. A Vue island does not turn the whole site into a Vue SPA.

Use Tailwind 4 through its Vite plugin when selected and supported. Keep statically detectable class strings or a static lookup map; do not build utility names from interpolated runtime values. Preserve the host project's tokens, package manager and layout conventions.

Consult installed-major docs, not only current latest docs. Verify adapter peers and Node constraints. Static output plus a compatible adapter can serve selected on-demand routes where required; do not copy legacy hybrid output or adapter subpaths. Choose CMS/editing and content freshness per project. Never expose server credentials through props, public variables or generated markup.

For component adoption, copy only the chosen original component and its explicit helper/style dependencies to project-owned paths, adapt imports, and test against project versions. Do not overwrite existing helpers or copy package node_modules/caches. The library lockfile pins the standalone example, not every adopting project.

Run project diagnostics, Vue typecheck, build and changed-path checks. Render desktop/mobile and relevant states. Record runtime evidence separately from a successful build. Use `web-motion-library` verification for motion; retain release authorization and project privacy boundaries.

Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-14 11:13:07 AST

For complex dialogs, navigation drawers or selection widgets read [Headless UI adoption](references/headless-ui.md). Keep this dependency selective.
