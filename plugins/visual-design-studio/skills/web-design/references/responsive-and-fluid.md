# Responsive and fluid design

Version-Timestamp: 2026-10-20 02:04:32 UTC

Design content order on a phone first, compose for wide screens second, and let fluid type and space handle the widths in between. Breakpoints are where the layout changes; fluid values are how everything scales between them. Layout grids themselves are covered by the `layout` skill.

## Breakpoints (token contract)

| Name | Min width | In `rem` for media queries | Typical layout change |
| --- | --- | --- | --- |
| base | 0 | | Single column, stacked sections, menu button |
| sm | 640px | 40rem | Two-up cards, side-by-side form pairs |
| md | 768px | 48rem | Two-column layouts, tablet navigation |
| lg | 1024px | 64rem | Full desktop navigation, sidebars, 3-4 column grids |
| xl | 1280px | 80rem | Max content width (`--container-xl`), wider gutters |
| 2xl | 1536px | 96rem | Extra whitespace or a wider editorial canvas; never stretch text past its measure |

Breakpoints live in the token JSON and the Tailwind build because CSS variables cannot drive media queries. Write `min-width` queries in `rem` or `em` so they respond to user font-size settings:

```css
.feature-grid { display: grid; gap: var(--space-6); grid-template-columns: 1fr; }
@media (min-width: 48rem) { .feature-grid { grid-template-columns: repeat(2, 1fr); } }
@media (min-width: 64rem) { .feature-grid { grid-template-columns: repeat(3, 1fr); } }
```

Rules:

- Mobile-first: base styles for the smallest screen, `min-width` overrides upward.
- Add a breakpoint only where the content breaks; use a container query when only one component breaks.
- Containers: `--container-sm` 640, `--container-md` 768, `--container-lg` 1024, `--container-xl` 1280px, centered with `--gutter` (clamp(1rem, 4vw, 2rem)) side padding.
- Text never exceeds `--measure-wide` (75ch), whatever the viewport.

## Fluid type with clamp()

Formula for a size that grows linearly from `min` at viewport `vmin` to `max` at `vmax`:

```text
slope     = (max - min) / (vmax - vmin)
intercept = min - slope * vmin
font-size: clamp(min, intercept + slope * 100vw, max)
```

Worked values from 320px to 1280px, mapped to the kit's size tokens:

| Role | Min | Max | CSS |
| --- | --- | --- | --- |
| Body | 16px (`--font-size-md`) | 18px | `clamp(1rem, 0.9583rem + 0.2083vw, 1.125rem)` |
| H3 | 20px (`--font-size-lg`) | 30px (`--font-size-2xl`) | `clamp(1.25rem, 1.0417rem + 1.0417vw, 1.875rem)` |
| H2 | 30px (`--font-size-2xl`) | 48px (`--font-size-4xl`) | `clamp(1.875rem, 1.5rem + 1.875vw, 3rem)` |
| H1 / display | 36px (`--font-size-3xl`) | 60px (`--font-size-5xl`) | `clamp(2.25rem, 1.75rem + 2.5vw, 3.75rem)` |

Rules:

- Always include a `rem` term. Pure `vw` sizes ignore browser zoom and text-size settings and can fail WCAG 1.4.4 (Resize Text).
- Keep `max` no more than 2.5 times `min`; with that ratio, text still reaches 200% when zoomed (Maxwell Barvian's analysis, Smashing Magazine, 2023).
- Tighten line height as size grows: body 1.5-1.65, headings `--line-height-snug` (1.25), display `--line-height-tight` (1.1).
- Tools such as Utopia (utopia.fyi) generate full fluid type and space scales from two ratios.

## Fluid space

```css
:root {
  --section-space: clamp(var(--space-12), 2rem + 5vw, var(--space-24)); /* 48px at 320 to 96px at 1280 */
  --stack-space:   clamp(var(--space-4), 0.6667rem + 1.6667vw, var(--space-8)); /* 16px to 32px */
}
section { padding-block: var(--section-space); }
```

Use fluid space for section padding, hero spacing and large gaps; keep component-internal spacing on fixed tokens so controls stay consistent.

## Container queries

Use container queries for components that appear in containers of different widths (cards in a sidebar and in a main grid), media queries for page-level layout.

```css
.card-list { container-type: inline-size; container-name: cards; }
.card { display: grid; gap: var(--space-3); }
@container cards (min-width: 28rem) {
  .card { grid-template-columns: 10rem 1fr; }
}
.card__title { font-size: clamp(1.125rem, 0.9rem + 2cqi, 1.5rem); }
```

- Size container queries and `cq*` units have been supported in all major evergreen browsers since 2023.
- Style queries (`@container style(...)`) have partial support; check caniuse.com before relying on them.
- A container cannot query its own size; wrap the component.

## Responsive images

**Resolution switching with `srcset` and `sizes`:**

```html
<img
  src="/img/team-1280.jpg"
  srcset="/img/team-640.jpg 640w, /img/team-960.jpg 960w, /img/team-1280.jpg 1280w,
          /img/team-1920.jpg 1920w, /img/team-2560.jpg 2560w"
  sizes="(min-width: 80rem) 1280px, (min-width: 48rem) 90vw, 100vw"
  width="1920" height="1080"
  alt="The studio team reviewing printed proofs at a long table"
  loading="lazy" decoding="async">
```

- `sizes` must describe the rendered CSS width at each breakpoint; a wrong `sizes` downloads images that are too large.
- Generate widths up to about 2x the largest rendered width; 5-6 steps between 320 and 2560px is usually enough.
- Always set `width` and `height` (the intrinsic ratio) so the browser reserves space and avoids layout shift.

**Formats with `picture`:**

```html
<picture>
  <source type="image/avif" srcset="/img/hero-960.avif 960w, /img/hero-1600.avif 1600w, /img/hero-2400.avif 2400w" sizes="100vw">
  <source type="image/webp" srcset="/img/hero-960.webp 960w, /img/hero-1600.webp 1600w, /img/hero-2400.webp 2400w" sizes="100vw">
  <img src="/img/hero-1600.jpg" srcset="/img/hero-960.jpg 960w, /img/hero-1600.jpg 1600w, /img/hero-2400.jpg 2400w"
       sizes="100vw" width="2400" height="1350" alt="" fetchpriority="high">
</picture>
```

| Format | Use | Starting quality (check visually) |
| --- | --- | --- |
| AVIF | First choice for photos and complex images; supported in all major browsers since early 2024 | About 50-65 |
| WebP | Fallback for older browsers; also good for transparency | About 75-82 |
| JPEG (mozjpeg) | Final fallback | About 75-85 |
| PNG | Screenshots with sharp text when lossless is needed | Lossless, optimized |
| SVG | Logos, icons, simple illustrations | Optimized with SVGO; `title` or `aria-label` when meaningful |

**Art direction** (a different crop per layout):

```html
<picture>
  <source media="(min-width: 48rem)" srcset="/img/hero-wide-1280.avif 1280w, /img/hero-wide-1920.avif 1920w"
          sizes="100vw" type="image/avif" width="1920" height="800">
  <source srcset="/img/hero-tall-640.avif 640w, /img/hero-tall-960.avif 960w"
          sizes="100vw" type="image/avif" width="960" height="1200">
  <img src="/img/hero-wide-1280.jpg" width="1920" height="800" alt="Ceramic cups drying on a wooden rack">
</picture>
```

Use art direction when the subject would be lost in a narrow crop; otherwise one image with `object-position` is simpler. `width` and `height` on each `source` keep the reserved space correct per crop.

**Loading:** the LCP image is never lazy; give it `fetchpriority="high"`. Images below the first viewport get `loading="lazy"`. Background images in CSS cannot use `srcset` well and are discovered late; use `img` for meaningful and LCP images. More in [performance](performance.md).

## aspect-ratio and object-fit

```css
.media { aspect-ratio: 16 / 9; width: 100%; object-fit: cover; }
.avatar { aspect-ratio: 1; border-radius: var(--radius-full); }
iframe.video { aspect-ratio: 16 / 9; width: 100%; height: auto; }
```

Set a consistent ratio per card grid (16:9, 4:3, 3:2 or 1:1) so rows align and nothing shifts when images load.

## Viewport, input and preference queries

- Full-height heroes: `min-height: 100svh` (small viewport height) avoids jumps when mobile browser toolbars show and hide; `100dvh` changes while scrolling and can cause shifts.
- Notches and rounded corners: `viewport-fit=cover` in the viewport meta plus `padding: env(safe-area-inset-top) ...` on fixed bars.
- Hover effects only where hover exists: `@media (hover: hover) and (pointer: fine)`.
- Respect `prefers-reduced-motion`, `prefers-color-scheme` and `prefers-contrast`; the kit tokens already switch durations and themes.
- Reflow: everything works at 320 CSS px wide without horizontal scrolling (WCAG 1.4.10), except content that needs two dimensions (data tables, maps), which scrolls inside its own region.

## Right-to-left and logical properties

Use logical properties (`margin-inline-start`, `padding-block`, `inset-inline-end`, `text-align: start`) so layouts mirror correctly with `dir="rtl"`. Mirror directional icons (arrows, back chevrons) but not logos, media controls or clocks.

## Test widths

Check at 320, 360, 375, 390, 414 or 430 (phones), 768 and 820-834 (tablets), 1024, 1280, 1440, 1536 and 1920px, plus 200% zoom. Device popularity shifts; confirm the top widths in the site's analytics. Screenshot each page type at 375, 768, 1280 and 1440px for review with the `design-critique` skill.

## Responsive transformations checklist

- Navigation: see `ui-design` [navigation](../../ui-design/references/navigation.md).
- Tables: scroll region with sticky first column, or cards under 640px.
- Multi-column text: one column under 768px.
- Side-by-side media and text: stack with media first only if the media carries the message; otherwise text first.
- Long forms: full-width fields on phones, natural widths on desktop.
- Hidden content: never remove content on mobile that mobile users need; collapse it instead.
