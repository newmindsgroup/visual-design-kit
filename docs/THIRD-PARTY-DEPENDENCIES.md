# Third-party dependencies and sources
Version-Timestamp: 2026-10-14 15:15:59 AST

Repository original material uses the root LICENSE. The Astro playground has its own package manifest and exact npm lockfile; third-party runtime source, node_modules and compiled bundles are excluded from this source distribution. Installing dependencies retrieves separately licensed packages. Preserve their notices when redistributing a compiled project.

Runtime packages include Astro, the Astro Vue integration, Vue, Tailwind and Headless UI (MIT); GSAP has its own standard license and must not be represented as MIT; Three.js uses MIT. Verify each resolved package license for receiving projects. Optional axe-core QA uses MPL-2.0 and Playwright uses Apache-2.0; neither is vendored here. AXE_SCRIPT points at the user's verified separate QA installation.

Creative references and researched recipes link to attributed sources. Their original code, demo media and brand assets are not licensed by this repository. The playground specimens are original generic geometry/text; do not copy third-party assets simply because a source is listed.

## 0.5.0 additions

Version-Timestamp: 2026-10-20 03:55:00 UTC

**React reference system** (`plugins/visual-design-studio/library/examples/react-system/`): exact pins and an npm lockfile; `node_modules` and build output are excluded from the repository and the payload. License fields read from the installed packages on 2026-10-20:

- Runtime: React and React DOM 19.3.0 and ten `@radix-ui/react-*` primitives (MIT).
- Build and type checking: Vite 8.3.2, `@vitejs/plugin-react` 6.1.2, Tailwind CSS and `@tailwindcss/vite` 4.3.3, `@types/react` and `@types/react-dom` 19.3.0 (MIT); TypeScript 7.0.2 (Apache-2.0).
- Transitive, build-time only: lightningcss and its platform binaries (MPL-2.0, file-level copyleft; used as a build tool, not modified or vendored), source-map-js (BSD-3-Clause), graceful-fs and picocolors (ISC), tslib (0BSD).
- QA only, not vendored: Playwright (Apache-2.0) and axe-core (MPL-2.0), installed separately by CI or the user.

**Fonts:** all bundled example fonts are SIL OFL 1.1 with their license files beside them; see [NOTICE](../NOTICE.md) for the list.

**Python helpers** (`atlas.py`, `tokens.py`, `color_tools.py`, `type_scale.py`, `score_directions.py`, `tools/validate_plugin.py`): standard library only.

**Claude Code CLI** is installed in CI at a pinned version only to run `claude plugin validate`; it is not distributed.
