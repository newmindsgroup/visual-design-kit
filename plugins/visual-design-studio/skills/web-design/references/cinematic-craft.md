# Cinematic craft: taste rules for media-led pages

Version-Timestamp: 2026-11-05 18:10:00 UTC

Adapted from MotionSites claude-skill (MIT), see NOTICE.md.

These are the recurring decisions that separate gallery-grade cinematic pages from average output. They add to the kit's `typography`, `layout`, `color` and `motion` defaults; they do not replace them. Where a source value differs from a kit default, the kit default stands and the [conflicts table](#conflicts-with-kit-defaults) says when the cinematic value applies instead. Break any rule on purpose and say why in the spec.

## Composition

- **One idea per first screen.** Mark, nav, one headline, one sub, 1-2 CTAs and one media plane, plus at most one quiet strip (logos, stats or socials). Cards, stat grids and icon stacks go below the fold unless they are the concept.
- **The media carries the design; the UI stays quiet.** 3-5 nav links, sparse text, one material. Often the only graphic is the footage.
- **Anchor somewhere specific.** Choose one: centred stack (badge, H1, sub, CTA); bottom-anchored (headline bottom-left, a secondary element bottom-right, flex spacer above); left column, vertically centred; editorial four corners (labels in the corners around a big headline). Centred is the safe choice, not the best one.
- **Text and subject never collide.** The subject takes the centre or right third; the text takes the other side or the empty band. Move the media first (`object-position`, oversize 110-120 %, translate) before shrinking the text.
- **Depth comes from layering, not decoration:** a giant ghost word behind a cut-out subject, a cut-out in front of the headline, a foreground frame over video, a spotlight mask revealing a second aligned image.
- **Inset-frame variant:** the hero sits in 16-24 px padding inside a media container with a 24-40 px radius; calm and expensive.
- **Sheet transitions between sections:** the next section gets a 40-60 px top radius, `margin-top: -40px` to `-56px` and a higher `z-index`, alternating near-black and white.

## Typography additions

- **Pairing archetypes for cinematic pages:** (1) editorial serif display, often italic, with a neutral grotesk, or serif only on 1-3 accent words inside a sans headline, set in a muted tone rather than a brighter one; (2) a single grotesk at display weight 400-500 where size and space do the work; (3) heavy condensed display for mega words with a calm body face; (4) mono or dot-matrix as a micro-label system for indices (`01 / 05`), eyebrows and metadata.
- **Scale contrast does the work:** the H1 is 5-6x the body size.
- **Break headlines by hand** into 2-3 lines; prevent bad desktop wraps per line and let mobile flow (kit `text-wrap: balance` still applies).
- **Mega words** (one decorative word at 14 vw or more): line-height 0.75-0.88, weight 800-900 or 300 for numerals, clipped with `overflow-x: clip`.
- **Gradient text is rare and controlled:** a subtle vertical silver on display type, or nothing.
- **Wordmarks** are tight-tracked text with a superscript registered or trademark sign, or a small custom inline-SVG mark; never a generic icon beside a bold word.
- **Rendering:** `-webkit-font-smoothing: antialiased` on dark pages, `font-variant-numeric: tabular-nums` on changing numbers, `preconnect` to fonts.gstatic.com with `crossorigin`.
- **Micro-label formats:** `// Capabilities`, `[ 02 ] Section`, `01` followed by a 64 x 1.5 px rule, `/ SERVICE NAME` lists, an eyebrow led by a 32 px hairline or a 6 px dot, counts as superscripts on nav items. Keep them at 12 px or more and 4.5:1.

## Color additions

- **The page background equals the media's edge color:** black footage on black, white studio on off-white, a red backdrop on red. That is why strong heroes need no overlay and never flash.
- **Near-blacks and off-whites** read richer than pure values: dark `#050505`, `#0a0a0a`, `#0c0c0c`; light `#f0f0ee`, `#f7f5f0`, `#fcfcfc`. Put them in the brand's neutral ramp or as `--brand-stage`, and recheck contrast pairs.
- **Hierarchy over media comes from opacity, not new colors:** text at 100 / 80 / 60 % of the foreground; borders at 10-20 %.
- **Theme the selection color:** `rgba(255,255,255,.2)` on dark pages, or the accent at 30 % alpha.
- **Text over media uses text-shadow, not boxes:** body `0 2px 18px rgba(0,0,0,.42)`, display `0 16px 38px rgba(0,0,0,.32)`, nav `0 2px 16px rgba(0,0,0,.2)`. Never a flat 50 % black wash.
- **Ambient light, never "the visual":** `radial-gradient(ellipse at top, rgba(255,255,255,.03), transparent 70%)` behind dark sections.
- **Avoid by default:** purple or indigo gradients, glow orbs, blobs, radial gradients as the main visual, heavy drop shadows (soft only, for example `0 4px 14px rgba(0,0,0,.16)`).

## Surfaces and components

- **One material, reused everywhere:** define one glass or frosted class and apply it to the nav, chips, cards and secondary buttons. No extra border classes on glass; the material provides the edge. Recipes: [surfaces and buttons](../../../library/knowledge/web-techniques/surfaces-and-buttons.md).
- **Buttons:** primary solid and inverse (white on dark, black on light), weight 500; secondary glass, ghost or a text link with an icon. An arrow in a contrasting circle inside the pill nudges 2 px or rotates -45 degrees on hover. Tech and metal styles use a crisp 6-7 px radius instead of pills.
- **Credibility micro-components:** an announcement badge with an inner chip; three overlapping avatars plus one line of verified social proof; 2-4 stats (big number, small muted label); a logo strip at 40-50 % opacity with an edge fade (with permission); an email pill (input plus round submit).
- **Grain:** an SVG fractal-noise layer at 0.04-0.15 opacity, `pointer-events: none`, on top. It unifies video and UI and removes gradient banding. Keep it at 0.04-0.08 over text.
- **Media cards:** 16:9, radius 24 px, media zoom 1.05 over 700 ms on hover and focus, a bottom scrim only where text sits.

## Motion additions

- **Order:** nav, eyebrow, H1, sub, CTA, secondary strip. The nav enters from above, content from below, secondary items sideways; logos and fine print only fade.
- **Base move:** opacity 0 to 1 plus translateY 20-30 px, optionally blur 10 px to 0 or scale 0.96 to 1. Release transforms after the entrance (`animation: none` or an `.is-in` class) so hover transforms still work.
- **Headline treatments, one per page:** per-word blur-in (60-100 ms stagger; add a word gap because negative tracking eats spaces), masked line rise from 110 % inside `overflow: hidden`, per-character slide (30 ms stagger), typewriter (35 ms per character) or scramble.
- **Media entrance:** video fades in from 0 over about 500 ms on `loadeddata`, and may settle from scale 1.06 to 1 over 1.8 s. Never a CSS transition on the `<video>` element itself.
- **What is not animated, which is where the restraint shows:** backgrounds and decorative layers, infinite pulsing or floating blobs, shimmer on headlines. The media is the ambient motion.
- **Lerp factors:** 0.1 cursor spotlight; 0.12 pointer parallax and scroll-scrubbed video; 0.14 pinned scroll stages.
- **Ambient loops stay slow:** orbits 30-60 s, marquees 20-40 s (about 40-60 px/s). Each needs the pause control (WCAG 2.2.2).
- **Spring overshoot** `cubic-bezier(.34,1.56,.64,1)` only for small confirmations (a check, a pop), never for layout.

## Copy

- **Headline:** 3-9 words over 2-3 lines for image-led heroes: a two-beat statement, a contrast pair or a three-word staccato. Emphasize with italic serif or a muted tone, never bold. Specific, not salesy.
- **Sub:** 1-2 sentences, 15-30 words: a concrete benefit plus texture, in a muted tone.
- **Nav:** 3-5 links of 1-2 words; specific labels (Studio, Work, Journal, Inquire) beat defaults. Repeat the primary CTA label in the nav.
- **CTA:** 2-3 words, verb first. Primary direct (Start, Book, Get); secondary softer (Watch the film, See how).
- **Microcopy adds brand texture:** coordinates, a live local time, "Available for projects" with a dot, index numbers. All of it true.

## Failure modes to design against

| Failure | Guard |
| --- | --- |
| White flash | `html,body{background:...}` as the first CSS rule; media starts at opacity 0 and fades in on `loadeddata`; check with `render_review.mjs --early 350` |
| Visible loop seam | rAF fade loop, boomerang, crossfade, or loopable footage ([recipes](../../../library/knowledge/web-techniques/video-and-media.md)) |
| Text unreadable over video | Footage with an empty zone; a bottom fade to the stage color; glass behind small UI; a soft text-shadow; check the busiest frame |
| Mobile 100vh clipping | `height: 100vh; height: 100dvh`; safe-area insets |
| Layout shift | Fixed-height lines for typed or rotating text; reserved media aspect ratios |
| Scrubbed-video jitter | Seek only when `!video.seeking`; lerp the target; short GOP encodes |
| Competing animations | Cancel the previous rAF; an animation lock of 650-1000 ms |
| Blank page if scripts fail | Rest state visible; hide only through `animation-fill-mode: both` or a `.js` class |
| Desktop-only interactions on touch | Disable hover and scrub effects under 1024 px or on `(hover: none)`; give an autonomous or static alternative |
| Horizontal scroll | `overflow-x: clip` on the root; vw-sized mega type with `nowrap` and clipping |
| Menu leaves the page scrollable | Lock body scroll while open; close on link, Esc and resize; `inert` on the closed menu |

## Conflicts with kit defaults

The kit default applies unless the "Cinematic value applies when" column is true and the spec says so.

| Topic | Source value | Kit default (stands) | Cinematic value applies when |
| --- | --- | --- | --- |
| Display weight | 400-500, never bold | Headings 700 (`typography`) | The approved direction's style entry calls for light display (luxury, editorial, quiet minimal); never below 300 |
| Display tracking | -0.02 to -0.05em; mega -0.04 to -0.08em | -0.03 to -0.04em at 64 px+ (`typography`) | Mega words at 14 vw or more may go to -0.08em, checked by eye for touching glyphs |
| Fluid display size | 14-28 vw for mega type | `clamp()` with a rem term, max at most 2.5x min (`typography`, WCAG 1.4.4) | The word is decorative and duplicated in real text (`aria-hidden="true"` on the giant word) |
| Body size | 14-18 px | 16-18 px (`typography`, `web-design`) | Never for body; 14 px only for secondary copy |
| Labels and micro-labels | 10-13 px at 40-60 % opacity | 12 px minimum UI text; 4.5:1 contrast (`typography`, `color`) | Never below 12 px; 40 % opacity only on decoration that carries no information |
| Hierarchy opacity | 100 / 80 / 60 / 40 | 4.5:1 for every text role (`color`) | 40 % only for decoration; 60 % white on near-black passes, recompute on any other ground |
| Entrance timing | 0.6-1.1 s per element, steps 0.1-0.2 s, done by about 1.5 s | Stagger 20-50 ms, last item within 300 ms; editorial moments up to about 1.2 s total (`motion`) | A one-time hero entrance on a marketing page: elements 0.6-0.9 s, steps 80-150 ms, whole sequence done by 1.2 s, input never blocked |
| Entrance easing | `cubic-bezier(.22,1,.36,1)` or `(.16,1,.3,1)` | `--ease-decelerate` or `--ease-emphasized-decelerate` (`motion`) | The direction's motion personality is slow and luxurious; declare it as `--brand-ease-expo`, never redefine a contract token |
| State-change easing | `cubic-bezier(.4,0,.2,1)` | `--ease-standard` `cubic-bezier(0.2, 0, 0, 1)` | Never; the recipes were rewired to the kit token |
| Scroll reveals | Every section, 0.6-0.9 s, 0.1 s stagger | Reveal only meaningful content, once; 320-480 ms with 20-50 ms stagger (`motion`) | Editorial pages: up to 650 ms with a 120 ms stagger, as in the kit's Astro `Reveal.vue` |
| Button size | Pills 10-12 x 20-32 px at 14 px (about 34-38 px tall) | CTAs 44-48 px tall (`web-design`); 44 px touch targets (`layout`) | Never for primary CTAs; nav links may be 30-32 px tall on desktop-only layouts (still above the 24 px minimum) |
| Side margins | 20-24 px mobile, 48-64 px desktop | 16 px phones, 32-80 px desktop (`layout`) | Full-bleed cinematic heroes may use 20-24 px on phones when the copy block has no card |
| Section padding | 128-176 px vertical | 80-160 px desktop (`layout`) | Luxury tier pacing may reach 176 px on 1440 px+ viewports |
| Hero headline length | 3-9 words | 6-12 words naming the outcome (`web-design` page architecture) | Image-led brand, campaign and launch heroes (the kit's own override for brand campaigns) |
| Hero video loading | `autoplay`, `preload="auto"` everywhere | No autoplaying hero video on mobile data unless it is the product; `preload="metadata"`, poster, pause control (`web-design` performance) | Desktop and fast connections; on phones play the lighter encode only when the video is the product, otherwise show the poster |
| Background video size | 5-8 MB | LCP image 200 KB; JS 150 KB (`web-design` budgets) | The poster carries LCP at 200 KB or less; the clip loads after first paint (see [media for the web](../../imagery/references/media-for-web.md)) |
