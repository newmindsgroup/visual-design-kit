# Landing and hero build spec template

Version-Timestamp: 2026-11-05 18:10:00 UTC

Adapted from MotionSites claude-skill (MIT), see NOTICE.md.

Quality is decided here, before any code. A good spec reads like a precise brief from a senior designer to a developer: every visible element has real values, every asset a real path, every motion a delay, duration and easing. Aim for 600-1,200 words for a hero and 1,200-2,500 for a multi-section page; the stylescapes you studied set the density. Used by step 4 of the [cinematic landing workflow](cinematic-landing.md) and, unchanged, as the body of a [builder prompt](builder-prompts.md).

## Precision rules

- **No adjective stands alone.** "Cinematic", "premium" and "glassy" are followed by the values that produce them: blur px, alpha, gradient stops, durations.
- **Every visible element gets a full style line:** size at each breakpoint (3-5 tiers or `clamp()` with a rem term), weight, line-height, tracking, color token with opacity, max-width and margins.
- **Color:** contract tokens (`--color-fg-default`, `--color-accent-default`) or `--brand-` page values with hex, never a bare "dark grey". Opacity steps for hierarchy over media are 100 / 80 / 60; 40 % is for decoration only, because it falls under 4.5:1 for text.
- **Motion:** per element, the trigger, delay, duration, easing token and from-to values, plus the reduced-motion state. Write stagger formulas out (`delay = 0.3 + i * 0.12s`).
- **Media:** exact path, element and attributes, fit, focal point (`object-position`, oversize, offsets), playback mode, poster, and one sentence on what the footage shows, where its subject sits and where the empty zone for copy is.
- **Logic:** algorithms in steps, with constants (lerp factor, locks in ms, thresholds) and cleanup.
- **Absolute positions and grids are explicit** (`top: 18%; left: 6vw`; `grid-template-columns: 26% 1fr 48%`).
- **Verbatim blocks** for anything that must be exact: classes, keyframes, SVG paths, the font `<link>`.

## Consistency pass (before building)

- Every asset has a real path, or is declared as a stand-in the client will replace.
- No element has conflicting classes or values.
- Every "do not" agrees with the asset list and layout.
- Every font named is loaded, and only the weights used.
- The page background equals the hero media's edge color.
- Every color pair used for text or controls is a contract pair or has a computed ratio next to it.
- Every moving element has a reduced-motion state, and anything moving longer than 5 s sits under a pause control.

## Template

Fill every `{{ }}`. Write "none" rather than leaving a block blank; delete blocks that do not apply.

````markdown
# {{Brand}}: {{one-line concept}}

## 0. Brief
Build {{a single full-viewport hero | an N-section landing page: Hero, ...}} for **{{Brand}}**, {{what it is, for whom}}.
Direction: {{approved direction name}}; atlas: {{style.*, industry.*, tier.*, channel.marketing-website}}.
Mood: {{three words}}.
Signature idea (the ONE thing this page is remembered for): {{...}}; recipe: {{web-techniques file and number, or "original"}}.
Fidelity: build exactly as specified; add no sections, cards, badges, gradients or decorations not listed here.

## 1. Stack and files
{{single index.html, inline CSS/JS, tokens.css inlined, CDN libraries pinned (gsap@3.15.0) | Astro + tokens.css | React + Vite + motion@14.4.0}}; icons: {{inline SVG | lucide 1.61.0: ArrowUpRight, Menu, X}}.

## 2. Fonts
| Role | Family | Weights and style | Used on | Token |
|---|---|---|---|---|
| Display | {{...}} | {{...}} | {{H1, accent words, big numbers}} | `--font-family-display` |
| Body and UI | {{...}} | {{400/500}} | {{nav, body, buttons}} | `--font-family-body` |
| Labels (optional) | {{mono or body}} | {{...}} | {{eyebrows, indices, metadata}} | `--font-family-mono` |
Load: `{{exact Google Fonts URL with display=swap, or self-hosted woff2 paths}}`. Fallback stack: `{{...}}`. License: {{OFL 1.1 | ...}}.

## 3. Color
```css
/* after tokens.css; <html data-theme="{{light|dark}}" data-brand="{{brand}}"> */
:root{
  --brand-stage: {{hex}};   /* equals the hero media's edge color; only if no token matches */
}
html,body{background:var(--brand-stage, var(--color-bg-canvas));color:var(--color-fg-default)}   /* first rule */
```
Accent `--color-accent-default` only on: {{at most 3 element types: CTA fill, a dot, a glyph}}.
Text over media: {{fg 100 headline / 80 nav / 60 body}}; checked pairs: {{pair: ratio}}.

## 4. Global utilities (verbatim)
{{kit baseline (focus ring, sr-only), material class (glass), grain, keyframes, motion pause control, reduced-motion block}}

## 5. Assets
| Slot | Type | Path | Element and attributes | Fit and focal point | Behavior | Fallback and poster | Rights |
|---|---|---|---|---|---|---|---|
| hero-bg | {{MP4 + WebM loop}} | `{{path}}` | `<video muted loop playsinline preload="metadata" poster="..." aria-hidden="true">` | `object-fit:cover; object-position:{{...}}` | {{autoplay on desktop and fast connections; fade in on loadeddata}} | {{poster.webp, 200 KB or less}} | {{client-owned / generated (record) / licensed}} |
Art direction: {{what the media shows, where the subject sits, where the empty zone is, dominant colors, motion speed}}.
Overlay policy: {{none | bottom fade to the stage color | edge vignette}}.

## 6. Layers and root
Root: {{position, height 100vh then 100dvh, overflow-x: clip}}.
z-ladder: media 0, fades 1, content 10, nav `--z-sticky`, menu `--z-overlay`, grain 100 (pointer-events none).
Skeleton: {{e.g. flex column: nav / flex-1 stage with content pinned bottom-left / bottom strip}}.

## 7. Navigation
Container: {{...}}. Left: {{wordmark}}. Centre: {{3-5 links, style}}. Right: {{CTA, style, height 44 px or more on touch}}.
Mobile: {{burger to full-screen menu, timing, stagger; closes on link, Esc and resize; focus returns to the burger}}.

## 8. Hero content (reading order)
| Element | Copy | Tag | Font | Size (base / md / lg) | Wt | Leading | Tracking | Color | Box and spacing | Motion (reduced) |
|---|---|---|---|---|---|---|---|---|---|---|
| Eyebrow | {{8 words or fewer}} | span | ... | ... | ... | ... | ... | ... | ... | ... |
| H1 | {{line breaks marked /}} | h1 | display | {{clamp(...)}} | ... | {{0.95-1.05}} | {{-0.03 to -0.04em}} | ... | ... | ... |
| Sub | {{15-30 words}} | p | body | ... | ... | 1.5-1.6 | ... | ... | {{max-width 28-42rem}} | ... |
| Primary CTA | {{verb + object}} | a | body | ... | ... | ... | ... | ... | {{44-48 px tall}} | ... |
| Secondary | {{softer action}} | a | ... | ... | ... | ... | ... | ... | ... | ... |

## 9. Sections (repeat per section)
### {{Name}}
Job: {{from page architecture}}. Background {{...}}; padding {{...}}; container {{...}}. Eyebrow, heading, body (each with full style lines). Grid {{...}}. Card {{radius, padding, material, inner layout}}. Media {{...}}. Reveal {{in-view once, threshold, duration, reduced state}}.

## 10. Motion table
Entrance easing `--ease-emphasized-decelerate` (or `--brand-ease-expo` when the direction's motion personality says so).
| Element | Trigger | Delay | Duration | From to | Reduced motion |
|---|---|---|---|---|---|
The entrance completes by {{1.2 s or less}}. Hovers: {{token durations}}. Not animated: {{backgrounds, decorative layers, video element transitions}}.
Pause control covers: {{every loop longer than 5 s}}.

## 11. Interaction and state
State, handlers, constants, algorithm in steps, cleanup, keyboard path, touch fallback.

## 12. Responsive
| Element | below 640 | 768 and up | 1024 and up | 1440 |
|---|---|---|---|---|
Use 100dvh and safe-area insets; no horizontal scroll at 375 or 390 px; add a short-viewport rule (max-height 720px) when the hero is dense.

## 13. Performance
LCP element: {{poster | H1}}; preload: {{...}}; JS weight: {{KB compressed}}; video sizes: {{desktop and mobile MB}}; fonts: {{files}}.

## 14. Constraints and acceptance
Do not: {{...}}.
Must: {{...}}.
Acceptance (first viewport at 1440 and 390): {{one paragraph describing exactly what is visible and where}}.
````

## Add-on modules

Append the ones that match the brief.

- **Video hero:** loop mode (native, rAF fade, crossfade, pointer scrub, scroll scrub, boomerang); focal point and oversize; overlay policy; poster; mobile behavior (in-flow block, lighter encode, or poster only on Save-Data); pause control placement.
- **Cut-out or 3D showcase:** per-role transform table (centre, left, right, back: position, height %, scale, blur, opacity, z); one shared transition with an animation lock; preloading; ghost mega-word behind the subject; for real 3D: camera, framing, lights, interaction model, keyboard rotation, loading state and PNG fallback.
- **Editorial or mega type:** display size in `clamp()`; line-height 0.75-0.9 for single decorative words; tracking; overflow clipping; which words sit in front of or behind the media; a micro-label system at 12 px or more.
- **SaaS:** product mockup anatomy (window chrome, columns, realistic but fictional rows); logo strip only with permission; pricing material and toggle.
- **Portfolio:** the name as a display element; work grid spans; hover reveals with focus equivalents; availability microcopy; marquee speed and pause.
- **Scroll story:** sticky stage height; segment ranges; per-frame variables; smoothstep and lerp helpers; choreography by scroll range; the reduced-motion mapping.
- **Regulated content:** mandatory lines placed in the first viewport per the atlas industry entry (for example ISI and fair balance on prescription drug pages) before any motion is designed.
