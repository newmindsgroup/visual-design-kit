# Web motion implementation

Version-Timestamp: 2026-10-20 01:59:37 UTC

Use the smallest engine that does the job, drive it from the token contract, keep essential content visible if scripts never run, and let one controller own each animated property. Browser support notes are as of late 2026; confirm on MDN or caniuse for the target browsers.

## Choose the engine

| Need | Use |
| --- | --- |
| Hover, press, focus and state changes | CSS transitions on tokens |
| Entrance from `display: none`, popovers, `<dialog>` | CSS transitions with `@starting-style` and `transition-behavior: allow-discrete` |
| Loops, skeletons, spinners | CSS `@keyframes` |
| Script-controlled, cancellable, awaitable animation | Web Animations API (WAAPI) |
| Moving between two DOM states or two pages | View Transitions API |
| Scroll-linked progress (reading bar, scrubbed scene) | CSS scroll-driven animations, with a fallback |
| Complex timelines, SVG morph, text splitting, cross-browser pinning | GSAP |
| React enter/exit, layout and shared-element animation, gestures, springs | Motion (formerly Framer Motion) |
| Designer-authored illustration or interactive character | Lottie or Rive (see [Lottie and Rive](lottie-and-rive.md)) |

Do not stack GSAP, Motion, a smooth-scroll library and a custom router as a default kit. Each adds weight and another owner of the same properties.

## CSS transitions

```css
.button {
  transition:
    background-color var(--duration-fast) var(--ease-standard),
    transform var(--duration-fast) var(--ease-standard);
}
@media (hover: hover) {
  .button:hover { background-color: var(--color-accent-hover); }
}
.button:active { transform: scale(0.97); }
```

- Name each property. Never write `transition: all`; it animates layout properties by accident and fights other animations.
- Put hover effects inside `@media (hover: hover)` so touch devices do not get sticky hover states.

Entrance and exit for a popover, with a faster exit (`@starting-style` is Baseline 2024; the `overlay` property is Chromium-only, so verify):

```css
.menu[popover] {
  opacity: 0;
  transform: translateY(-4px) scale(0.98);
  transition: opacity var(--duration-fast) var(--ease-accelerate),
              transform var(--duration-fast) var(--ease-accelerate),
              overlay var(--duration-fast) allow-discrete,
              display var(--duration-fast) allow-discrete;
}
.menu[popover]:popover-open {
  opacity: 1;
  transform: none;
  transition-duration: var(--duration-moderate);
  transition-timing-function: var(--ease-emphasized-decelerate);
}
@starting-style {
  .menu[popover]:popover-open { opacity: 0; transform: translateY(-4px) scale(0.98); }
}
```

Animating to `height: auto`: use `interpolate-size: allow-keywords` (Chromium 129+) as an enhancement, with the widely supported grid fallback, which transitions `grid-template-rows` from `0fr` to `1fr` on a wrapper whose child has `overflow: hidden`.

## CSS keyframes

```css
.skeleton {
  background: linear-gradient(90deg, var(--color-bg-sunken) 0%, var(--color-bg-surface) 50%, var(--color-bg-sunken) 100%);
  background-size: 200% 100%;
  animation: shimmer 1.6s linear infinite;
}
@keyframes shimmer { from { background-position: 100% 0; } to { background-position: -100% 0; } }
@media (prefers-reduced-motion: reduce) { .skeleton { animation: none; } }
```

`background-position` repaints on every frame. That is acceptable for a few skeleton blocks; for large areas, move a pseudo-element with `transform` instead.

## Web Animations API

```js
const ms = (name) => parseFloat(getComputedStyle(document.documentElement).getPropertyValue(name)) || 0;

const anim = panel.animate(
  [{ opacity: 0, transform: 'translateY(8px)' }, { opacity: 1, transform: 'none' }],
  { duration: ms('--duration-moderate'), easing: 'cubic-bezier(0, 0, 0, 1)', fill: 'both' }
);
await anim.finished;
anim.commitStyles();
anim.cancel();
```

Reading durations from the tokens means the reduced-motion override (0.01ms) applies to script animations as well. `anim.reverse()` handles interrupted toggles; `element.getAnimations()` finds and cancels running animations before you start new ones.

## View Transitions API

Same-document transitions are Baseline as of October 2025 (Chrome 111, Safari 18, Firefox 144). Cross-document transitions (`@view-transition`) work in Chrome 126+ and Safari 18.2+; Firefox support is partial. Verify before relying on them.

```js
export function transition(update) {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!document.startViewTransition || reduce) { update(); return; }
  document.startViewTransition(update);
}
```

```css
.product-card img { view-transition-name: var(--vt-name); } /* unique per page, e.g. style="--vt-name: product-42" */
::view-transition-group(*) {
  animation-duration: var(--duration-slower);
  animation-timing-function: var(--ease-standard);
}
@view-transition { navigation: auto; } /* cross-document, same-origin; put it on both pages */
@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(*), ::view-transition-old(*), ::view-transition-new(*) { animation: none !important; }
}
```

- Every `view-transition-name` must be unique on the page at snapshot time. Use `view-transition-class` to style groups of them.
- Use transition types (`startViewTransition({ update, types: ['forward'] })` with `:active-view-transition-type(forward)`) for direction-aware page motion; check support first.
- Move focus to the new view's heading after the update; the transition does not do it for you.
- Astro: the `<ClientRouter />` component wraps this API, and the [Astro motion example](../../../library/examples/astro-motion/README.md) uses Astro page navigation for its page-transition study.

## Scroll-driven animations

Supported in Chromium 115+ and Safari 26+; Firefox stable still had it behind a flag in mid-2026. Gate it with `@supports` and make content visible by default.

```css
@supports (animation-timeline: view()) {
  @media (prefers-reduced-motion: no-preference) {
    .reveal {
      animation: reveal linear both;
      animation-timeline: view();
      animation-range: entry 10% cover 30%;
    }
  }
}
@keyframes reveal { from { opacity: 0; transform: translateY(24px); } }

.reading-progress {
  transform-origin: 0 50%;
  animation: grow linear both;
  animation-timeline: scroll(root block);
}
@keyframes grow { from { transform: scaleX(0); } to { transform: scaleX(1); } }
```

- Use `linear` timing for scrubbed timelines, because the scroll is the easing; put any easing inside the keyframes.
- Scroll-triggered playback (cross a threshold, then play a timed animation) is a different thing. Use IntersectionObserver to add a class, or GSAP ScrollTrigger.
- Never hijack scroll speed, and keep parallax speed differences within 10-20%.

## GSAP

License (verified October 2026): since GSAP 3.13 (April 2025), GSAP and every formerly paid plugin (SplitText, MorphSVG, DrawSVG, ScrollSmoother, Inertia and the rest) are free, including for commercial use, under Webflow's GSAP Standard "No Charge" License ([gsap.com/standard-license](https://gsap.com/standard-license/)). It is not an OSI open-source license: it prohibits use in tools that compete with Webflow's visual animation builder without written permission, and Webflow can change the terms. Re-check the license before shipping a product that lets end users build animations. Install from `gsap` on npm; `gsap-trial` is deprecated. The kit's Astro example pins `gsap` 3.15.0.

```js
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { CustomEase } from 'gsap/CustomEase';
gsap.registerPlugin(ScrollTrigger, CustomEase);
CustomEase.create('standard', '0.2,0,0,1');

const mm = gsap.matchMedia();
mm.add({ motion: '(prefers-reduced-motion: no-preference)', reduce: '(prefers-reduced-motion: reduce)' }, (ctx) => {
  const { motion } = ctx.conditions;
  gsap.from('.feature', {
    opacity: 0,
    y: motion ? 24 : 0,
    duration: motion ? 0.48 : 0.15,
    ease: 'standard',
    stagger: motion ? 0.04 : 0,
    scrollTrigger: { trigger: '.features', start: 'top 80%', once: true },
  });
});
```

`gsap.from()` leaves content visible if the script never runs. Clean up with `gsap.context()` and `ctx.revert()`, or the `useGSAP()` hook from `@gsap/react`, and remember that `mm` reverts its own animations when the media query changes.

## Motion (formerly Framer Motion)

Framer Motion became the independent Motion library in late 2024. Install `motion`; import from `motion/react` for React or from `motion` for the vanilla `animate()`, `scroll()` and `inView()` functions. The core library is MIT; Motion+ is a separate paid add-on. Verify the current terms at motion.dev.

```jsx
import { AnimatePresence, MotionConfig, motion } from 'motion/react';

const enter = { duration: 0.32, ease: [0.05, 0.7, 0.1, 1] };
const exit = { duration: 0.2, ease: [0.3, 0, 0.8, 0.15] };

<MotionConfig reducedMotion="user">
  <AnimatePresence>
    {open && (
      <motion.div key="dialog" role="dialog" aria-modal="true" aria-labelledby="dlg-title"
        initial={{ opacity: 0, scale: 0.96 }}
        animate={{ opacity: 1, scale: 1, transition: enter }}
        exit={{ opacity: 0, scale: 0.98, transition: exit }} />
    )}
  </AnimatePresence>
</MotionConfig>
```

- `reducedMotion="user"` turns off transform and layout animations for reduced-motion users while keeping opacity and color.
- `layout` animates size and position changes with transforms (FLIP); `layoutId` gives a shared-element transition between components.
- Springs: `transition={{ type: 'spring', visualDuration: 0.3, bounce: 0.15 }}`.
- Motion animates, it does not manage focus. Use an accessible dialog primitive (native `<dialog>`, Headless UI, Radix) for semantics and focus.

## Performance rules

- Animate `transform` and `opacity`; browsers can run these on the compositor without layout or paint. `filter` and `clip-path` are often accelerated but cost more, so test them. Avoid animating `width`, `height`, `top`, `left`, `margin`, `padding`, `font-size` and `box-shadow`.
- For a shadow lift, fade in a pseudo-element that already carries the larger shadow, rather than animating `box-shadow`.
- Frame budget: 16.7ms per frame at 60Hz and 8.3ms at 120Hz. The browser needs part of each frame, so keep script, style and layout work near 10ms at 60Hz (web.dev RAIL guidance).
- Set `will-change: transform` just before an animation and remove it afterwards. A global `will-change` wastes memory and creates layer explosions.
- Avoid layout thrash: read all geometry (`getBoundingClientRect`) first, then write. Animate layout changes with FLIP (First, Last, Invert, Play).
- Prefer IntersectionObserver and scroll timelines over scroll listeners; make any scroll listener `passive`.
- Core Web Vitals: keep INP at 200ms or less; break up long tasks (over 50ms) so animation never blocks input. CLS ignores transform-based movement, but animating `top`, `height` or `margin` can register as layout shift.
- Pause loops, canvas and WebGL offscreen (IntersectionObserver) and in hidden tabs (`visibilitychange`).
- Measure on a mid-range Android phone or with 4x CPU throttling in Chrome DevTools: use the Performance panel, then Rendering, then Paint flashing and Frame rendering stats.

## Reduced-motion patterns

- The token build sets every `--duration-*` except `--duration-instant` to `0.01ms` under `prefers-reduced-motion: reduce`, so token-driven transitions become instant automatically.
- Replace motion rather than deleting all feedback. Because tokens are zeroed there, write the gentle alternative with a literal value:

```css
@media (prefers-reduced-motion: reduce) {
  .sheet { transform: none !important; transition: opacity 150ms linear; }
}
```

- Keep: opacity and color state feedback, focus indicators, progress indicators (static or slow), and motion that is essential to the content (a video the user started).
- Remove: parallax, zooms, large slides, spins, bounces, scroll-jacking and auto-playing loops.
- In script: `const rm = matchMedia('(prefers-reduced-motion: reduce)'); rm.addEventListener('change', update);`.
- Where motion is a large part of the product, add an in-app "Reduce motion" setting that defaults to the OS preference.
- Autoplay video only when muted, show a pause control, and show the poster frame under reduced motion.

## Working examples in this kit

- [Website motion library](../../../library/MOTION-LIBRARY.md): the coded collection and its coverage; [motion and asset recipes](../../../library/MOTION-RECIPES.md): media inserts, Lottie, grading and transitions.
- [Astro motion playground](../../../library/examples/astro-motion/README.md) and its shared helper [useMotion.ts](../../../library/examples/astro-motion/src/lib/useMotion.ts), which handles reduced motion, hidden tabs and teardown.
- [HeadlessOverlay.vue](../../../library/examples/astro-motion/src/components/effects/HeadlessOverlay.vue): dialog and drawer, 200ms ease-out in and 150ms ease-in out (enter and exit asymmetry).
- [ButtonFeedback.vue](../../../library/examples/astro-motion/src/components/effects/ButtonFeedback.vue): press and hover feedback in Tailwind.
- [ListMotion.vue](../../../library/examples/astro-motion/src/components/effects/ListMotion.vue): keyed reorder with an `aria-live` announcement.
- [Reveal.vue](../../../library/examples/astro-motion/src/components/effects/Reveal.vue): GSAP reveal at 650ms with a 120ms stagger. That suits editorial pages; tighten it to `--duration-slower` with a 30-40ms stagger for product UI.
- [TextReveal.vue](../../../library/examples/astro-motion/src/components/effects/TextReveal.vue), [MaskReveal.vue](../../../library/examples/astro-motion/src/components/effects/MaskReveal.vue) and [SvgDraw.vue](../../../library/examples/astro-motion/src/components/effects/SvgDraw.vue): word, mask and path reveals.
- [ScrollScene.vue](../../../library/examples/astro-motion/src/components/effects/ScrollScene.vue) and [ReadingProgress.vue](../../../library/examples/astro-motion/src/components/effects/ReadingProgress.vue): scroll-linked scenes and progress.
- [PointerCard.vue](../../../library/examples/astro-motion/src/components/effects/PointerCard.vue): tilt, magnetic and spotlight effects, gated to fine pointers.
- Adoption and QA: [lifecycle](../../../library/draft-skills/design-web-motion-library/references/lifecycle.md) and [verification](../../../library/draft-skills/design-web-motion-library/references/verification.md).
- Token specimen: [motion-specimen.html](motion-specimen.html).
