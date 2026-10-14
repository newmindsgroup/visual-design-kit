# Motion Atlas

Version-Timestamp: 2026-10-14 14:03:25 AST

An original coded playground and component library for Astro, Tailwind and Vue, with everyday and experimental tiers. There are 42 catalog techniques: 22 working studies and 20 researched recipes. The latter are labeled Recipe in the UI and do not claim implemented runtime behavior. Source policy is in [DESIGN.md](DESIGN.md); technique data is in [catalog.mjs](src/lib/catalog.mjs). [Research](../../draft-skills/design-web-astro/references/research.md) and [motion lifecycle](../../draft-skills/design-web-motion-library/references/lifecycle.md) accompany the code.

## Run in a separate working directory

Copy this example folder to a new project-owned folder outside the installed plugin. Do not install dependencies into the package. From that copy, with Node >=22.12.0 and npm 11:

```sh
npm ci --ignore-scripts
npm test
npm run check
npm run check:vue
npm run build
ASTRO_PREVIEW_BACKGROUND=0 npm run preview -- --port 17731
```

The reference install/build passed with lifecycle scripts disabled on the authoring Mac. Other platforms may require reviewed native build-tool setup. The source lockfile does not prove all OS combinations. Disable Astro telemetry if your environment requires it. The preview is local and noindex; deployment is not part of the example.

## Reuse selected components

The fourteen effect Vue files support nineteen local specimens; the twentieth study uses Astro page navigation. Do not copy the entire app merely to add one effect. Preserve the selected file's dependency paths or adapt them deliberately: effect files import src/lib/useMotion.ts and, where used, src/lib/runtime.mjs. GSAP components need GSAP; ScrollScene also needs ScrollTrigger. WebGLScene loads src/lib/webgl.mjs and Three.js only after Play. Shared fixture styles are in src/styles/global.css; translate them to the adopting project's tokens. The original specimens contain generic synthetic text/shapes and no client imagery.

All components accept reduced and playing props, with variant where declared in the catalog. The playground remounts a selected component for Replay. OS reduced motion takes precedence. Props are demonstration controls, not a no-code timeline or animation-building interface. Replace fixture text/markup with project-owned content while preserving semantics, helper imports and lifecycle cleanup.

## QA

Six runtime-policy/disposal tests use the Node test runner. The optional browser harness requires Playwright and axe-core from a separately vetted QA environment. See [verification](../../draft-skills/design-web-motion-library/references/verification.md). Actual check results and limitations are recorded in [kit evidence](../../MOTION-ATLAS-EVIDENCE.md).

## Sources and licensing

Original code/documentation follow the kit's MIT license. Dependencies retain their own terms: GSAP Standard No Charge, Three.js/Vue/Astro/Tailwind MIT, optional axe-core MPL-2.0. No third-party assets or creative demo code were copied. The Codrops and other external references are inspiration/read-only sources, not bundled dependencies. Verify asset licenses and compatibility if adopting a referenced resource.

Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-14 11:13:07 AST

This standalone playground assumes deployment at the root URL. Adapt root-relative navigation and assets before adopting a project with a non-root Astro base path.

Headless UI: branded dialog and mobile navigation drawer share HeadlessOverlay.vue. No form delivery is implemented. Optional tests/headless-ui.mjs checks keyboard/focus, dismissal, animation, reduced motion, axe and route cleanup.

Version-Timestamp: 2026-10-14 15:15:59 AST

Known native Safari finding: plain Tab under the authoring browser keyboard preference left the dialog. Option+Tab/Option+Shift+Tab wrapped. Safari drawer and screen-reader acceptance remain incomplete. Do not treat the Chromium suites as cross-browser certification. tests/headless-ui.mjs requires AXE_SCRIPT and verified Playwright/Chromium; its CDP listener-count checks are Chromium-specific. Dependencies are installed by the receiving developer and are not bundled.
