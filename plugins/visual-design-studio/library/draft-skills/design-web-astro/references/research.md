# Motion engine research and selection

Version-Timestamp: 2026-10-14 11:13:07 AST

No library is universally best. Select by required control, navigation ownership, lifecycle, actual browser support, payload and license. The implemented example uses one coherent default stack; optional alternatives are researched, not installed automatically.

| Job | Starting choice | Why and limit |
| --- | --- | --- |
| Hover/focus, small feedback, color/transform | Tailwind CSS transitions/keyframes | No animation-engine dependency; motion-reduce/motion-safe are preference controls, not complete accessibility proof |
| Mount/unmount or keyed-list state | Vue Transition/TransitionGroup | Fits Vue state; preserve keys, focus and announcements |
| Independent simple browser animation | Web Animations API | Native control without another dependency; handle cancellation and target support |
| Route continuity | Astro ClientRouter | One navigation owner; native crossfade/shared-element capabilities can avoid a custom layer |
| Sequenced choreography, scrub, pin, SVG | GSAP/ScrollTrigger and selected plugins | Fine control and scoped cleanup; costs JS and needs purpose-specific tests |
| Springs/gestures inside Vue | Motion for Vue | Evaluate as an alternative to GSAP in the selected island; avoid overlapping controllers |
| Reactive scroll helpers | VueUse | Useful in existing Vue stacks; not needed for the reference's small native listener |
| Smooth scrolling | Lenis | Optional and measurable; not a default. Anchors, keyboard, nested scrollers, dialogs and router cleanup need checks |
| 3D/shaders | Three.js; evaluate TresJS if Vue scene composition is needed | Lazy experimental tier, bounded GPU/resolution and static/error fallback |
| Authored vector playback | Lottie | Approved export/asset route; pause and native source fidelity still need verification |

Scroll-triggered playback starts a time-based animation after a threshold. Scroll-driven progress maps position to state. Do not substitute one for the other. Native CSS scroll/view timelines can be excellent for supported targets; check current support and supply @supports/static alternatives rather than claim universal support.

Tailwind class generation is build-time. Use full class names in source/maps. Translate project motion tokens to duration/easing/custom properties; do not create arbitrary dynamic class strings. Vue scoped CSS and GSAP should have one owner for each property. Component-scoped gsap.context and matchMedia support reverting; delayed event callbacks also need registration/cleanup.

GSAP uses its Standard No Charge license, not MIT. The official terms cover commercial website/interface use and constrain certain competing visual animation builders. This library is coded specimens, replay/pause and implementation recipes; it is not a no-code timeline or animation-authoring product. Reassess that license if scope changes. Three.js, Vue, Astro and Tailwind are MIT; preserve dependency notices. Do not assume an example's images/fonts carry its source-code license.

Sources: [Tailwind motion](https://tailwindcss.com/docs/animation), [Tailwind state variants](https://tailwindcss.com/docs/hover-focus-and-other-states), [Vue Transition](https://vuejs.org/guide/built-ins/transition.html), [TransitionGroup](https://vuejs.org/guide/built-ins/transition-group.html), [GSAP context](https://gsap.com/docs/v3/GSAP/gsap.context()/), [GSAP matchMedia](https://gsap.com/docs/v3/GSAP/gsap.matchMedia()/), [ScrollTrigger](https://gsap.com/docs/v3/Plugins/ScrollTrigger/), [license](https://gsap.com/standard-license/), [Motion Vue](https://motion.dev/docs/vue), [VueUse scroll](https://vueuse.org/core/useScroll/), [Lenis](https://github.com/darkroomengineering/lenis), [Three.js](https://threejs.org/docs/), [native timelines](https://developer.mozilla.org/en-US/docs/Web/CSS/animation-timeline), [Lottie](https://github.com/airbnb/lottie-web).

Agent-Attribution: computer=NMG-MBP-M5.local; tool=Codex; version=codex-cli 0.160.0; timestamp=2026-10-14 11:13:07 AST
