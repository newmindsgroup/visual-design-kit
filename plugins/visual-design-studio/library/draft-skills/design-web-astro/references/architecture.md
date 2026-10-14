# Architecture and setup

Version-Timestamp: 2026-10-14 11:13:07 AST

The reference example pins Astro 7.3.8, @astrojs/vue 7.0.3 (peers Astro ^7 and Vue ^3.5.24), Vue 3.5.44, Tailwind/@tailwindcss/vite 4.3.3, GSAP 3.15.0 and Three.js 0.186.1. Registry identities and peers were inspected on 14 October 2026. Example runtime: Node 24.15.0, npm 11.12.1. Astro requires Node >=22.12.0. These are example pins, not an instruction to upgrade other projects.

Prefer native Astro components for layouts, copy and static cards. Vue owns an island's reactive state and native Transition/TransitionGroup behavior. Tailwind defines tokens, layout and simple state transitions. GSAP may own imperative properties in a selected component after onMounted. Three.js is a separately lazy-loaded experimental renderer. Never let Vue/CSS/GSAP simultaneously control the same property.

Fresh selected setup can use npm create astro@latest, followed by astro add vue and astro add tailwind for compatible versions. For an existing project, inspect before mutating. The example provides an explicit astro.config.mjs using the Vue integration and Tailwind Vite plugin. Read current installation docs before reusing a command or configuration.

Astro ClientRouter owns route changes. Component cleanup runs on Vue unmount and astro:before-swap. The specimens intentionally do not use transition:persist. Persisted components need an explicit reuse/reset contract and cannot rely solely on unmount. Test back navigation and scroll restoration. Refresh scroll measurements after geometry changes, not in an unbounded loop.

Sources: [Vue integration](https://docs.astro.build/en/guides/integrations-guide/vue/), [styling](https://docs.astro.build/en/guides/styling/), [Astro transitions](https://docs.astro.build/en/guides/view-transitions/), [Vue SSR](https://vuejs.org/guide/scaling-up/ssr.html).

Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-14 11:13:07 AST
