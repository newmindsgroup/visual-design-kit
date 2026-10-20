---
id: style.kinetic-experimental-type
axis: style
name: Kinetic / Experimental Typography
aliases: [kinetic type, experimental typography, variable font motion, type-as-image, expressive typography, moving type, typographic motion]
summary: Letterforms as the main image and behavior, using variable-font axes, scale extremes and motion that respond to scroll, pointer or sound, with a readable resting state and disciplined limits.
tags: [kinetic, typography, experimental, variable-fonts, motion, type-as-image, expressive, scroll, animation, poster]
pairs_with: [industry.creative-agencies-studios, industry.events-conferences, industry.media-entertainment-streaming, industry.fashion-apparel, archetype.magician, archetype.creator, archetype.outlaw, channel.video-motion, channel.marketing-website, channel.ooh-signage]
avoid_with: [audience.older-adults, audience.disability-accessibility-first, audience.neurodivergent, audience.low-bandwidth-entry-devices, industry.healthcare-provider, industry.government-civic]
version_timestamp: 2026-10-20 01:57:45 UTC
---

# Kinetic / Experimental Typography

## Essence

Make the letters do the work of the image. Type becomes shape, rhythm and behavior: a headline stretches as you scroll, a word's weight swells with the music, a poster's letters orbit a grid. The lineage includes Saul Bass and Kyle Cooper's title sequences, Swiss and Dutch experimental posters, and, since OpenType variable fonts (2016), continuous control over weight, width and slant in the browser. The style is memorable and cheap in assets, but it only works when the text can still be read, paused and skipped.

## Visual signature

- Giant type (20-60vw wide), cropped by the viewport, aligned to a strong axis or rotating along a path.
- Variable fonts animated across width, weight, slant, optical size or custom axes.
- Extreme scale contrast between display type and tiny functional text; few other elements.
- Grid-based or deliberately broken layouts where words are the only graphics, with plain backgrounds and one electric accent.
- Type interacting with pointer, scroll position, audio or time: stretch, squash, scatter, assemble.
- A quiet counterpoint: set body copy in a neutral, static text face at normal size.

## Token recipe

| Token | Value |
| --- | --- |
| Display font | Anybody (OFL, wdth 50-150, wght 100-900); Mona Sans (OFL, wdth 75-125, wght 200-900); Recursive (OFL, axes MONO, CASL, wght 300-1000, slnt); Fraunces (OFL, axes opsz, wght, SOFT, WONK); commercial: ABC Diatype Variable, GT Flexa, Obviously Variable |
| Body font | Mona Sans or Roboto Flex (OFL) at fixed axes; static text faces such as Newsreader (OFL) for reading copy |
| Mono (data, captions) | Recursive Mono (MONO 1) or Space Mono (OFL) |
| Type scale ratio | Extreme: 1.618 or larger between body and display; body 16-18px, display `clamp(4rem, 14vw, 22rem)` |
| Body size / line-height | 16-18px / 1.5; measure 55-65ch; display line-height 0.8-0.95 |
| Display letter-spacing | -0.04em to -0.06em on dense widths; animate tracking +/-0.02em for breathing effects |
| Caps / labels | 11-13px mono uppercase, +0.06em; labels pin to corners and grid edges |
| Weights | Interpolate 100-900 where the family allows; at rest use a legible default (wght 600-800) |
| Palette | Ink #0A0A0A (oklch 0.14 0 0); Paper #EDEDE7 (oklch 0.94 0.008 107); Dim ink #55554F (oklch 0.45 0.01 107); Signal blue #2B2BFF (oklch 0.49 0.29 269); Acid #E4FF1A (oklch 0.95 0.216 117); Hot red #D91E3F (oklch 0.57 0.215 20) |
| Accent proportion | Black and paper 85-95%; one accent (blue on paper, or acid on ink) 5-12%; never combine all three accents |
| Radius | 0; UI controls 0-4px; pills only for toggles |
| Borders | 1-2px ink rules for grid scaffolding and hairline frames; underlines under links |
| Shadow / elevation | None; avoid blur and glow; depth from scale, overlap and mix-blend-mode difference used sparingly |
| Spacing density | Extreme contrast: 8px base; margins 16-32px; empty space between hero words; dense captions |
| Grid | Strict 12 or 16 columns with visible tick marks or fine rules; type deliberately overflows or snaps to the grid |
| Motion | 600-2000ms hero sequences with cubic-bezier(0.16, 1, 0.3, 1); scroll-scrubbed linear mapping; per-word stagger 30-80ms (per-letter only for 1-2 words); idle loops 4-8s |

## Composition and layout

- Decide the resting state first: a static poster that already works. Motion is the second layer.
- Define a motion grammar of 3-4 verbs (stretch, squash, orbit, scatter) and assign each a meaning (stretch = loading, squash = error, orbit = idle). Reuse them across pages.
- Use one kinetic hero per screen. Surround it with calm layout, plain body text and clear navigation.
- Tie motion to input: scroll progress maps linearly to width or weight; pointer position maps to slant; audio amplitude maps to weight. Map one input to one property to keep behavior legible.
- For sites, keep the document semantic: a real `<h1>` with the full text; visual effects applied to spans with `aria-hidden` and the complete label on the parent, so screen readers do not read letter by letter.
- Provide a visible way to pause or stop any motion longer than 5 seconds that begins automatically.

## Imagery and iconography

- Type is the imagery. If images appear, make them sparse, high-contrast and grain-treated, often cropped by letter shapes (`background-clip: text` or SVG masks).
- Icons are minimal glyphs in the display family or simple 1.5-2px marks; arrows and plus/minus symbols as typographic characters.
- 3D and generative extensions: extruded letters with three.js, text-on-path in SVG, particle type in WebGL; keep a 2D fallback and test on low-end phones.
- For video and social, export from After Effects, Rive, Lottie or Remotion at 30 or 60fps; reuse the same grammar as the web.

## Motion

The motion is the content, so budget it. Hero sequences run 600-2000ms with an expo-out feel (cubic-bezier(0.16, 1, 0.3, 1)); scroll-scrubbed type maps 0-100% scroll to the axis range linearly; stagger words 30-80ms and avoid per-letter stagger beyond a headline or two. Animating `font-variation-settings` forces layout and repaint, so limit it to a few large elements, animate transforms where possible, and test on a mid-range Android phone. Use CSS scroll-driven animations (`animation-timeline`) where supported or GSAP ScrollTrigger as a fallback; verify browser support. Under `prefers-reduced-motion`, show the final composition, remove scroll-scrubbing and keep only opacity changes.

## Fits and risks

- **Fits:** creative studios and portfolios, festivals and conferences, film, music and fashion launches, art institutions, product reveal microsites, title sequences and social video. Matches `archetype.magician` and `archetype.creator`.
- **Risks:** legibility, accessibility (vestibular and cognitive load), performance, SEO and screen-reader behavior when text is split into spans. Experiments can overpower the message, and similar scroll-reveal headlines are now everywhere, which erodes distinctiveness.
- **Wrong for:** older adults, neurodivergent audiences prone to overload, accessibility-first products, low-bandwidth contexts, healthcare and government. For those contexts keep type static and use motion only for state change.
- **Why these pair:** `industry.creative-agencies-studios`, `industry.events-conferences`, `industry.media-entertainment-streaming` and `industry.fashion-apparel` reward expressive launches; `archetype.outlaw` fits rule-breaking; `channel.video-motion`, `channel.marketing-website` and `channel.ooh-signage` are natural stages for motion type.
- **Why these clash:** `audience.older-adults`, `audience.disability-accessibility-first` and `audience.neurodivergent` are most harmed by motion, scale extremes and unpredictability; `audience.low-bandwidth-entry-devices` cannot afford the runtime; `industry.healthcare-provider` and `industry.government-civic` require stable, plain reading.

## Do and don't

- Do check each frame of an animation for a readable moment; a word should rest long enough to read (a common starting point is 0.3-0.5s per short word, longer for unfamiliar words; test with real readers).
- Do build with variable fonts and CSS custom properties (`--wght`, `--wdth`) so motion is data-driven and tokens remain consistent.
- Do give users control: pause, skip, reduce motion, and a plain-text alternative.
- Don't split every heading into letters and fade each one in; that is a default library effect, not a concept.
- Don't hijack scrolling or trap focus in a pinned section without keyboard and screen-reader paths.
- Don't animate body text or form labels.

## Clichés and AI tells

- Lazy version: every heading uses a SplitText stagger with blur-in, a giant "WE CREATE DIGITAL EXPERIENCES" marquee, a cursor-follower circle, a WebGL gradient blob, scroll-jacked sections and a black background with white Inter at 12vw.
- Fix: invent one typographic behavior tied to the brand (a font whose width tracks live data, a headline that reflows to the music, a word that breaks along a real map), keep it to the hero, set the rest in calm type, and write copy that says something specific so the motion has a reason.

## Accessibility notes

- Ink #0A0A0A on paper #EDEDE7 is 16.85:1; Dim ink #55554F on paper is 6.38:1; signal blue #2B2BFF on paper is 6.18:1 and white on it is 7.26:1; acid #E4FF1A on ink is 17.55:1 and acid on blue is 6.44:1.
- Hot red #D91E3F on paper is 4.25:1 (large text only); white on it is 4.99:1; the brighter #FF2E4D is 3.11:1 on paper and 5.42:1 on ink. Mid gray #6E6E68 on paper is 4.37:1 and fails for body copy.
- WCAG 2.2.2 (Pause, Stop, Hide) requires a mechanism for automatic motion longer than 5 seconds; 2.3.3 (AAA) asks for a way to disable motion animation; 2.3.1 limits flashing to 3 per second.
- Large-scale movement and parallax can trigger vestibular symptoms; keep scroll-scrubbed type to a small area or offer a static mode. Honor `prefers-reduced-motion` and persist a manual toggle.
- Splitting text: keep the full string in one accessible element, mark animated fragments `aria-hidden="true"`, and make sure the text remains selectable and searchable.

## Reference anchors

- Saul Bass and Kyle Cooper title sequences (*Se7en*, 1995) as foundations of kinetic type in film
- Variable fonts (OpenType 1.8) and the v-fonts.com specimen library; CSS Fonts Level 4 `font-variation-settings`
- Google Fonts axis registry and the families Anybody, Recursive, Fraunces, Mona Sans
- Paula Scher's Public Theater typography and Wim Crouwel's experimental posters as static ancestors
- GSAP (ScrollTrigger, SplitText) and CSS scroll-driven animations for implementation
- WCAG 2.2: 2.2.2 Pause, Stop, Hide; 2.3.1 Three Flashes; 2.3.3 Animation from Interactions
