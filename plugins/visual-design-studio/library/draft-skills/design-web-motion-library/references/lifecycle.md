# Lifecycle and accessibility contract

Version-Timestamp: 2026-10-14 11:13:07 AST

DOM work begins after Vue onMounted. Pass the DOM element value to gsap.context, not the Vue ref object. Revert context/matchMedia on unmount and route swap. Collect event-created tweens too. Remove each registered listener with its original handler/options; cancel frames/timers; disconnect observers. Never kill every project's ScrollTrigger globally to clean one component.

The supplied useMotion helper combines OS reduced motion, local reduced preview, explicit playing, page visibility and route disposal. Operating-system preference cannot be overridden by Play. The component's own visibility observer adds offscreen suspension for loops. No component is persisted across Astro routes. Delayed graphics imports guard disposed generations and immediately dispose late results.

Initial content is visible in SSR output. Apply hidden/from states only after an explicit animation starts; revert on pause/reduced state. Native details remains usable without JS. Custom demo controls are disabled until mounted. Tabs preserve APG roles, linked IDs, selected state, roving tabindex and arrow/Home/End focus. Manual carousel has no auto-advance timer. Reordering has a keyboard-operable button and polite announcement. One sample passing these checks is not an accessibility certification.

Prefer normal document flow and bounded scrollers. Pinning cannot hide focused content or trap scroll; mobile may need a static/vertical alternative. Text splitting preserves a coherent accessible reading sequence and nested links. Do not flash/strobe or obscure factual results. Pause/stop/hide and interaction animation disablement are separate WCAG criteria; document the applicable target level rather than equate reduced motion with compliance.

Canvas/Three effects are decorative, opt-in, offscreen/hidden-paused and resolution-capped. Dispose geometry, material, textures where used, renderer and context; cancel the render loop before releasing resources. Context loss and initialization failure keep the static fixture visible. Replaying creates a fresh instance; no automatic network/write retry is implied.

Sources: [GSAP Vue context](https://gsap.com/docs/v3/GSAP/gsap.context()/), [Astro lifecycle](https://docs.astro.build/en/guides/view-transitions/), [W3C tabs](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/), [W3C carousel](https://www.w3.org/WAI/ARIA/apg/patterns/carousel/), [pause/stop/hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html).

Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-14 11:13:07 AST
