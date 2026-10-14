# Headless UI fit for Motion Atlas

Version-Timestamp: 2026-10-14 11:39:17 AST

Recommendation: use Headless UI selectively as the behavior layer for complex Vue controls. Keep Astro routing/content, Tailwind visual tokens, and the existing motion engines. This is researched guidance, not an implemented or runtime-validated integration.

## Roles

| Layer | Responsibility |
| --- | --- |
| Astro | Pages, server-rendered content, navigation and hydration boundaries |
| Vue | Stateful interactive islands |
| Headless UI | Component state semantics, keyboard behavior and focus management |
| Tailwind | Brand styling, responsive states and simple transitions |
| Motion Atlas | Purposeful reveals, scroll scenes, SVG and optional graphics |

## Priority candidates

1. Dialog: project inquiry modal, case-study lightbox and mobile navigation drawer. Test focus trapping, Escape, outside click, focus return, scroll lock and portal removal on Astro navigation.
2. Popover: small navigation or contextual panels. Use appropriate navigation semantics; an application Menu is not the default for website navigation.
3. Combobox/Listbox: searchable service selection or content filters when native select no longer meets requirements. Keep labels, errors and form submission accessible.
4. Tabs and Disclosure: useful for complex controlled widgets; retain native details/summary for simple FAQs and existing lightweight patterns unless replacement has a clear benefit.

## Motion ownership

Use the Vue TransitionRoot/TransitionChild APIs from the Vue documentation for coordinated enter/leave states. Tailwind can style opacity and transform. Keep reduced-motion classes and the kit's local preference. Do not let GSAP and CSS transitions animate the same property. Headless UI does not supply scroll storytelling, particle effects, shaders or the brand design.

Keep one Vue island around a trigger and its controlled content. Hydrate immediate navigation controls with client:load; essential links/content must still have a useful server-rendered path. Test portal lifecycle and scroll lock after Astro ClientRouter swaps and back navigation. Do not assume framework peer compatibility proves Astro SSR compatibility.

## Version and adoption boundaries

Registry inspection on 14 October 2026: @headlessui/vue 1.7.23, Vue peer ^3.2.0, MIT license. The website's React landing page shows v2.1 while Vue documentation shows v1.7. Use Vue documentation and the pinned package API; do not copy React-only newer APIs or assume feature parity. Tailwind 4 can style components through static classes and slot state; do not automatically add the legacy Headless UI Tailwind plugin without checking Tailwind-major compatibility.

No package was added, no existing component was replaced, and no new live specimen was claimed in this assessment. First integration should be a branded dialog specimen with keyboard, reduced-motion, no-JS fallback and navigation cleanup checks, followed by desktop/mobile and assistive-technology review. Vet exact dependency graph before runtime installation and preserve MIT attribution when distributing third-party code.

## Primary evidence

- [Headless UI](https://headlessui.com/)
- [Official repository and license](https://github.com/tailwindlabs/headlessui)
- [Vue Dialog](https://headlessui.com/v1/vue/dialog)
- [Vue Menu](https://headlessui.com/v1/vue/menu)
- [Vue Transition](https://headlessui.com/v1/vue/transition)

Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-14 11:39:17 AST

Version-Timestamp: 2026-10-14 14:06:36 AST

Implementation update: original dialog and drawer specimens added to local candidate 0.4.1. See plugins/visual-design-studio/library/HEADLESS-UI-EVIDENCE.md for current acceptance. The earlier assessment above predates implementation.
