# Headless UI adoption

Version-Timestamp: 2026-10-14 13:57:29 AST

Use @headlessui/vue only for selected stateful Vue islands. The playground pins 1.7.23 with Vue peer ^3.2.0. Read [Vue Dialog](https://headlessui.com/v1/vue/dialog) and [Vue Transition](https://headlessui.com/v1/vue/transition); React v2 APIs are not the Vue API contract.

Headless UI owns keyboard semantics, focus and scroll locking. Tailwind owns visual tokens and transitions. Astro ClientRouter remains the route owner. Prefer native details/summary and selects when sufficient. Site navigation uses ordinary links within a labeled nav, not application menu semantics.

The original HeadlessOverlay.vue specimen demonstrates dialog and drawer variants. Gate portals until mounted, disable the trigger before hydration and provide meaningful static fallback links/text. Bind reduced and paused preferences inside the teleported tree, not only the island wrapper. Remove route listeners on unmount and close/dispose portals before page swap. Do not animate the same properties with GSAP and CSS.

Acceptance: initial focus, forward/backward focus trap, Escape, close and outside dismissal, focus return, closed/open axe checks, 320/390/desktop rendering, OS/local reduced motion, pause during transitions, no hydration warnings, navigation portal/inert/scroll-lock cleanup and no-JS fallback. Screen-reader and real-device checks remain project requirements. No inquiry form backend is included.

License: official Tailwind Labs package is MIT. Retain third-party license notices when redistributing package code. Exact dependency graph must be audited for each adopting project.
