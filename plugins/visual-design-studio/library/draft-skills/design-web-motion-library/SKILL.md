---
name: design-web-motion-library
description: Select, adapt and verify original website motion components and effect recipes, especially for Astro, Tailwind and Vue. Covers everyday interface patterns and optional experimental scroll, pointer, canvas and WebGL effects.
---

# Website motion library

Version-Timestamp: 2026-10-14 11:13:07 AST

Use `motion` for movement purpose/choreography and `web-frontend` for semantic implementation. Reuse those accepted inputs. This entry owns technique selection, component adoption and runtime evidence; it does not authorize a new visual direction or production release.

Read [lifecycle and accessibility](references/lifecycle.md), then the selected entries in [the canonical technique catalog](../../examples/astro-motion/src/lib/catalog.mjs). The [playground guide](../../examples/astro-motion/README.md) describes launch and reusable file dependencies. For stack choices read [engine research](../design-web-astro/references/research.md). For visual reference discovery read [creative sources](references/creative-sources.md). Read [verification](references/verification.md) before completion.

The catalog has two tiers and an independent status. Everyday prioritizes feedback and orientation; experimental adds expressive effects only when justified. Implemented means original example code exists, not approved for all projects. Researched means a recipe/source exists, not a runnable component. Do not market a recipe as implemented or infer smoothness from a successful build.

Choose the smallest engine for the intended effect. Preserve the project's visual tokens, audience, reading order, normal pointer and native controls. Tailwind supplies style; Vue supplies island state; one animation controller owns each animated property; Astro owns route navigation. Do not add GSAP, Motion, Lenis and custom routing as one default stack.

Adopt only selected source and explicit helper/style dependencies into the project. Essential content starts visible, and controls requiring hydration start disabled. Show loading/error/static states for optional imports. Scope selectors, frames, timers, listeners and observers; tear them down on Vue unmount and Astro swap. System reduced motion wins over local preview and Play. Pause long-running optional effects; stop offscreen/hidden loops and clean graphics resources.

For typing, SVG morph, shader distortion, video scrubbing or heavy pinning, use the researched recipe as a bounded prototype contract first. Keep approved identity/data exact, source assets licensed and an equivalent static explanation. Test route/back/rapid repeat, keyboard/touch, preference changes, loading/error, resize and real target devices before adoption. Update evidence for the exact project version only.

Record effect IDs, engine/version, purpose, initial/end/interrupt states, static/reduced fallback, measured costs, checked browsers and known gaps in the existing motion specification/design-work record. A new motion package does not change active client pins or grant spending, publication or API access.

Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-14 11:13:07 AST
