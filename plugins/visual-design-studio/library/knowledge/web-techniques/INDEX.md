# Web technique recipes: index

Version-Timestamp: 2026-11-05 18:10:00 UTC

Adapted from MotionSites claude-skill (MIT), see NOTICE.md.

58 working recipes in 7 files for cinematic landing pages and heroes: what each is for, the parameter values that make it look finished, a single-file implementation, a React variant where it differs, and reduced-motion and touch behavior. The kit added the token wiring, the focus and pause baseline below, pinned library versions and a "Kit addition" note wherever a recipe needed more for WCAG 2.2 AA. Use them from the [cinematic landing workflow](../../../skills/web-design/references/cinematic-landing.md); motion values still follow the `motion` skill unless a recipe says why it differs.

## Choose one signature

Pick **one signature technique per page**: the single idea the page will be remembered for (a real 3D object, a scrubbed film, a giant word behind a cut-out, a pinned cinematic stage). Then add **2-4 quiet supporting techniques**: one entrance, one material, one type move and one reveal for the sections below. Never stack five effects in one viewport; if two techniques compete for the same attention (spotlight, magnet and parallax), cut one. Allow at most **one heavy** technique per page and let the media or the signature carry the motion.

Typical sets:

- **Cinematic video hero:** background video layer + edge-blend scrim + liquid glass + blur-rise + serif accent.
- **Product object:** 3D model hero + floating pill nav + blur-rise + count-up stats.
- **Editorial portfolio:** giant display type + split-text entrance + magnetic hover + scroll-linked word reveal + stacking cards.

## Kit baseline

Every recipe assumes the kit's token contract. Link the project's built `tokens.css` (from `design-system` or `../../tokens/dist/tokens.css` for the reference brands); a single-file page inlines it in the first `<style>` instead (the reference build is about 29 KB uncompressed, a one-brand build less). Dark pages set `<html data-theme="dark">` so the semantic colors, including `--color-focus-ring`, switch to their dark values.

Paste this once, after the tokens. The first rule removes the white flash; the recipes' own `--brand-ease-*` blocks add their curves.

```css
html,body{background:var(--color-bg-canvas);color:var(--color-fg-default)}   /* first rule: no white flash */
*,*::before,*::after{box-sizing:border-box}
:where(a,button,input,select,textarea,summary,[tabindex]):focus-visible{outline:2px solid var(--color-focus-ring);outline-offset:3px}
.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
```

When the page background must equal a video's edge color that the tokens do not hold, set it as a page value (`--brand-stage: #050505`) and use it in that first rule. Never redefine a contract name.

## Motion pause control

WCAG 2.2 success criterion 2.2.2 requires a way to pause, stop or hide anything that moves, blinks or auto-updates for more than 5 seconds alongside other content. Background video loops, marquees, orbit rings, shader backdrops, rotating words and auto-advancing carousels all qualify, whatever the visitor's reduced-motion setting. One page-level control covers them:

```html
<button class="motion-toggle" type="button" aria-pressed="false">
  <svg aria-hidden="true" width="16" height="16" viewBox="0 0 16 16"><path class="i-pause" d="M4 3h3v10H4zM9 3h3v10H9z"/><path class="i-play" d="M4 3l9 5-9 5z"/></svg>
  Pause background motion
</button>
```

```css
.motion-toggle{position:fixed;right:16px;bottom:max(16px,env(safe-area-inset-bottom));z-index:var(--z-sticky);
  display:inline-flex;align-items:center;gap:8px;min-height:var(--size-target-comfortable);padding:0 16px;border-radius:var(--radius-full);
  border:var(--border-width-thin) solid var(--color-border-strong);background:var(--color-bg-surface);color:var(--color-fg-default);
  font:var(--font-weight-medium) var(--font-size-sm)/1 var(--font-family-body);cursor:pointer}
.motion-toggle svg{fill:currentColor}
.motion-toggle .i-play,.motion-toggle[aria-pressed="true"] .i-pause{display:none}
.motion-toggle[aria-pressed="true"] .i-play{display:inline}
html.motion-paused *,html.motion-paused *::before,html.motion-paused *::after{animation-play-state:paused!important}
```

```js
(() => {
  const btn = document.querySelector('.motion-toggle');
  if (!btn) return;
  const root = document.documentElement;
  const set = (paused) => {
    root.classList.toggle('motion-paused', paused);
    btn.setAttribute('aria-pressed', String(paused));
    document.querySelectorAll('video[autoplay], video[data-ambient]').forEach((v) => (paused ? v.pause() : v.play().catch(() => {})));
    dispatchEvent(new CustomEvent('motionpause', { detail: { paused } }));   // rAF loops, timers and canvases listen for this
  };
  btn.addEventListener('click', () => set(btn.getAttribute('aria-pressed') !== 'true'));
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) set(true);
})();
```

The label stays the same and `aria-pressed` carries the state, which is how a toggle button is announced. Recipes driven by `requestAnimationFrame`, `setInterval` or a canvas check `root.classList.contains('motion-paused')` or listen for `motionpause`; their "Kit addition" notes say where. Scroll-scrubbed and pointer-driven effects are user-driven and do not need it.

## Libraries and licenses

Versions were checked with `npm view <package>@<version> version` on 2026-11-05, and the CDN file paths against each package's published tarball. Pin exactly these, or newer versions you have tested; never an unpinned or major-only URL.

| Library | Pinned | Used by | License | Notes |
| --- | --- | --- | --- | --- |
| three | 0.170.0 | [3D model hero](3d-and-webgl.md), shader backdrop | MIT | `three/addons/` and the Draco decoder load from the same pinned package (`examples/jsm/libs/draco/gltf/`). 0.187.0 was current on the check date; the recipe was written against 0.170.0. |
| Draco decoder (inside three) | 0.170.0 path | GLB files compressed with Draco | Apache-2.0 | Loaded only for Draco-compressed models. |
| hls.js | 1.5.20 | [Video layer](video-and-media.md) for `.m3u8` sources | Apache-2.0 | Safari plays HLS natively; 1.7.4 was current on the check date. |
| gsap (+ ScrollTrigger) | 3.15.0 | GSAP variants in [scroll](scroll.md) and [layout](layout-and-ui.md) | GSAP Standard "No Charge" License | Same version the kit's Astro example pins. Since GSAP 3.13 every plugin is free, including commercial use, but the license is not OSI open source and restricts tools that compete with Webflow's animation builder; see `motion`'s [web implementation](../../../skills/motion/references/web-implementation.md#gsap) before shipping a product that lets end users build animations. |
| motion (formerly framer-motion) | 14.4.0 | "Framer Motion variant" snippets | MIT | Import from `motion/react`; 14.4.0 exports `useScroll`, `useSpring`, `useTransform`, `useInView`, `AnimatePresence` and `useReducedMotion`. The package releases weekly; pin it in `package.json`. |

Google Fonts named in recipes (Inter, Instrument Serif and others) are OFL; follow the [asset licenses](../ASSETS-LICENSES.md) record when you bundle them. Every recipe works without a library unless it says otherwise.

## Rules for using a recipe

- Keep the reduced-motion and touch branches when you adapt a recipe; they are part of it.
- Replace sample colors with tokens or `--brand-` page values and check every text and control pair: the contract guarantees token pairs, not your overrides.
- Numbers in sample markup ("[verified count]", a count-up target) are placeholders. Ship only figures the client can verify.
- `VIDEO_URL.mp4`, `poster.jpg` and `model.glb` are placeholders. Media comes from the client, from a recorded generation, or the page is type and motion led: see [media for the web](../../../skills/imagery/references/media-for-web.md). Never invent URLs.
- Render and check with `design-critique`'s `render_review.mjs --early 350` (first paint, video readiness, broken media, failed requests) at 390 and 1440 px, with and without `--reduced-motion`.

## Techniques

| Technique | File | Use it when | Cost |
| --- | --- | --- | --- |
| Cinematic background video layer (autoplay, HLS, settle-in) | [video-and-media.md](video-and-media.md) | Footage carries the mood; the default foundation of a video hero | medium |
| Seam-free video loop with rAF opacity fades | [video-and-media.md](video-and-media.md) | A looping clip shows a hard cut or mismatched first and last frame | light |
| Background-video framing and art direction | [video-and-media.md](video-and-media.md) | The clip's subject collides with the copy or crops badly on phones | light |
| Edge-blend scrims and text protection | [video-and-media.md](video-and-media.md) | Copy needs contrast over footage, or the hero must melt into the next section | light |
| Progressive bottom blur | [video-and-media.md](video-and-media.md) | Bottom-anchored titles over footage whose colors must stay untouched | medium |
| Cursor-scrubbed video (delta, split dual) | [video-and-media.md](video-and-media.md) | A turntable or head-turn clip should feel like a live 3D object (desktop) | medium |
| Scroll-scrubbed video with canvas frame cache | [video-and-media.md](video-and-media.md) | Scrolling should drive a transformation clip behind sparse copy | heavy |
| Boomerang (ping-pong) video loop | [video-and-media.md](video-and-media.md) | A non-looping clip (push-in, bloom, smoke) must loop; pre-render it | light |
| Crossfading multi-video scene switcher | [video-and-media.md](video-and-media.md) | Visitors pick an atmosphere or location from 3-5 moods | heavy |
| Liquid-glass surface | [surfaces-and-buttons.md](surfaces-and-buttons.md) | UI floats over moving footage: nav, chips, cards, secondary CTAs | light |
| Frosted glass UI kit (chips, badge, numbered panel, contact card) | [surfaces-and-buttons.md](surfaces-and-buttons.md) | Text must sit on glass over video and stay legible | light |
| Premium button finishes (liquid metal, halo, jewel) | [surfaces-and-buttons.md](surfaces-and-buttons.md) | The CTA itself should feel machined or glow on a dark hero | light |
| Text-roll button with rotating arrow chip | [surfaces-and-buttons.md](surfaces-and-buttons.md) | A studio or agency CTA needs a tactile hover | light |
| Sliding-fill buttons (+ hard offset shadow) | [surfaces-and-buttons.md](surfaces-and-buttons.md) | Editorial or playful pages want a color-wipe hover | light |
| Animated gradient border ring | [surfaces-and-buttons.md](surfaces-and-buttons.md) | One CTA must pull the eye without changing the layout | light |
| Media card hover (icon-to-label pill, zoom, veil) | [surfaces-and-buttons.md](surfaces-and-buttons.md) | Case-study and work grids | light |
| Texture overlays (grain, noise type, halftone, dot grid) | [surfaces-and-buttons.md](surfaces-and-buttons.md) | Flat color, gradients or video banding look too digital | light |
| Staggered blur-rise load choreography | [type-and-text-motion.md](type-and-text-motion.md) | Every hero entrance (the default) | light |
| Fail-safe entrance system with a motion vocabulary | [type-and-text-motion.md](type-and-text-motion.md) | Rich single-file choreography that must never leave a blank page | light |
| Word-by-word blur-in headline | [type-and-text-motion.md](type-and-text-motion.md) | A big italic-serif headline over video should "exhale" in | light |
| Split-text entrances (masked lines and words, char cascade) | [type-and-text-motion.md](type-and-text-motion.md) | Giant display words or stacked statements rising out of a slot | light |
| Serif-italic accent words | [type-and-text-motion.md](type-and-text-motion.md) | Almost any headline with a natural key phrase | light |
| Gradient-clipped text (metallic, shine sweep) | [type-and-text-motion.md](type-and-text-motion.md) | Name-as-hero metal type, or one "magic" word in a headline | light |
| Scramble and decode text | [type-and-text-motion.md](type-and-text-motion.md) | AI, tech or sci-fi brands with monospace type | light |
| Typewriter with zero-reflow caret and depth-of-field lead-in | [type-and-text-motion.md](type-and-text-motion.md) | An assistant or persona voice, or a typed contact headline | light |
| Rotating word slot | [type-and-text-motion.md](type-and-text-motion.md) | One word in a sentence should cycle (roles, verbs, places) | light |
| Scroll-linked word and character opacity reveal | [type-and-text-motion.md](type-and-text-motion.md) | A manifesto or About paragraph read at scroll pace | medium |
| Giant display type as image (ghost word, wordmark, watermark, scattered) | [type-and-text-motion.md](type-and-text-motion.md) | A word should be architecture: behind a cut-out, edge to edge, or as a backdrop | light |
| Geometric SVG wordmark assembly | [type-and-text-motion.md](type-and-text-motion.md) | An institution or studio header with a constructed mark | light |
| Count-up stats and counter preloader | [type-and-text-motion.md](type-and-text-motion.md) | Verified proof numbers, or a portfolio intro loader | light |
| Depth carousel with role slots and color crossfade | [depth-and-interaction.md](depth-and-interaction.md) | 3-6 products or characters, each with its own color | medium |
| Magnetic hover | [depth-and-interaction.md](depth-and-interaction.md) | A hero subject or primary CTA should feel weighted and alive | light |
| Pointer parallax depth layers | [depth-and-interaction.md](depth-and-interaction.md) | A layered still (cut-outs over a backdrop) needs depth | light |
| Cursor-following spotlight reveal mask | [depth-and-interaction.md](depth-and-interaction.md) | Two aligned images where the hidden one is decoration (x-ray, night, render) | medium |
| Cursor image trail | [depth-and-interaction.md](depth-and-interaction.md) | A closing CTA block should spray portfolio thumbnails | medium |
| Exclusion-blend overlay UI and custom cursor | [depth-and-interaction.md](depth-and-interaction.md) | Fixed UI must stay legible as the page goes video, black, white | light |
| Orbit rings with counter-rotating avatars | [depth-and-interaction.md](depth-and-interaction.md) | A community, talent network or integrations visual | medium |
| Sand-dissolve image transition and auto-cycling index | [depth-and-interaction.md](depth-and-interaction.md) | Cycling collection or chapter images with an archival feel | heavy |
| Viewport-triggered staggered reveal (+ corner decor) | [scroll.md](scroll.md) | Every section below the hero | light |
| Sticky cinematic stage with CSS-variable choreography | [scroll.md](scroll.md) | Layered photography tells a story across one long pinned scroll | heavy |
| Panel slide-over, viewport-scaled scattered gallery, blend outro | [scroll.md](scroll.md) | Fashion or archive pages with many tall images | medium |
| Pinned heading with counter-drifting parallax columns | [scroll.md](scroll.md) | A gallery "playground" orbiting a pinned title | medium |
| Sticky stacking cards that scale down | [scroll.md](scroll.md) | 3-5 case studies or process steps | medium |
| Scroll-linked opposing marquee rows | [scroll.md](scroll.md) | A wall of work right after a portfolio hero | medium |
| 3D tilted text crawl (spring-smoothed) | [scroll.md](scroll.md) | A manifesto paragraph over video should feel like a film opening | medium |
| Hero composition patterns | [layout-and-ui.md](layout-and-ui.md) | Deciding where copy sits over a full-bleed visual | light |
| Viewport-locked single-frame hero | [layout-and-ui.md](layout-and-ui.md) | A poster hero that must look identical on every screen size | light |
| Floating pill navigation | [layout-and-ui.md](layout-and-ui.md) | The nav for most cinematic heroes (glass, frosted, white, dock, editorial) | light |
| Expanding glass capsule menu | [layout-and-ui.md](layout-and-ui.md) | Minimal heroes where a full link row would be noise | light |
| Mobile menu (burger morph, overlay, drawer, bottom sheet) | [layout-and-ui.md](layout-and-ui.md) | Every page with navigation, below 768-1024 px | light |
| Overlapping avatar trust cluster | [layout-and-ui.md](layout-and-ui.md) | Compact, verified social proof above a SaaS or AI headline | light |
| Selectable chip group with spring check | [layout-and-ui.md](layout-and-ui.md) | Contact, enquiry or onboarding forms that should feel conversational | light |
| In-page product UI mockup | [layout-and-ui.md](layout-and-ui.md) | SaaS, dev tools or dashboards, instead of a screenshot | light |
| Desktop grid to mobile scroll-snap rail | [layout-and-ui.md](layout-and-ui.md) | 3-4 large cards (pricing, plans, features) | light |
| Infinite marquee (logos, images, giant text) | [layout-and-ui.md](layout-and-ui.md) | A logo strip, image strip or giant text band | light |
| Infinite looping card slider | [layout-and-ui.md](layout-and-ui.md) | Locations, testimonials or case studies in a carousel | light |
| Real 3D model hero (Three.js + GLB) | [3d-and-webgl.md](3d-and-webgl.md) | The object is the story and you have (or can generate) a GLB | heavy |
| Animated shader backdrop (swirl, chroma blob, fluted glass) | [3d-and-webgl.md](3d-and-webgl.md) | A light agency hero with a living, refractive background | heavy |

**Cost** is the runtime weight on a mid-range phone: light means CSS or a little JavaScript; medium means per-frame work, filters or extra media; heavy means WebGL, large frame caches, several videos or SVG filters on bitmaps. A heavy signature still has to meet the `web-design` budgets (LCP 2.5 s or less at p75, INP 200 ms or less, CLS 0.1 or less); give it a poster or still that paints first.
