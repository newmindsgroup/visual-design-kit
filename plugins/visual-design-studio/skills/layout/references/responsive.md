# Responsive layout

Version-Timestamp: 2026-10-20 02:07:10 UTC

Responsive design recomposes content for each width; it does not scale a desktop layout down. Design small first, widen until the content breaks, and add a breakpoint there.

## Content-out breakpoints

1. Start at 360px (and check 320px, the WCAG 2.2 SC 1.4.10 Reflow width).
2. Widen the viewport slowly. Note where the layout fails: lines pass 75ch, images get oversized, navigation wraps, cards stretch too wide, whitespace goes dead.
3. Add a breakpoint at that width and recompose. Use the token breakpoints (sm 640, md 768, lg 1024, xl 1280, 2xl 1536px) when they are close enough; do not add breakpoints for device names.
4. Prefer container queries for components (cards, media objects, toolbars) so they adapt to the slot they sit in.
5. Write media queries in em so they respond to the user's font size: `@media (min-width: 40em)` is 640px at the default size.

Test widths: 320, 360, 390, 430, 768, 834, 1024, 1280, 1440, 1536 and 1920px, plus a couple of awkward in-betweens (700, 1100px).

## Recomposition patterns

| Pattern | What changes | Use for |
| --- | --- | --- |
| Mostly fluid | Columns stretch, then stack at small widths | Simple marketing pages |
| Column drop | Columns stack one by one as width shrinks | Sidebar plus content plus aside |
| Layout shifter | Different arrangement per breakpoint | Rich homepages, editorial |
| Tiny tweaks | Type size and spacing only | Single-column articles |
| Off canvas | Secondary panels slide in from the edge | Navigation, filters, settings |
| Priority+ navigation | Most important items visible, the rest under "More" | Wide navigation sets |
| Reveal and disclose | Secondary content behind accordions or "Show more" | Specs, FAQs, long filters |
| Table to cards, or scroll with a sticky first column | Data tables on phones | Comparison and data views |
| Sidebar to bottom sheet | Filters and details on phones | Search, maps, commerce |
| Grid to carousel (or the reverse) | Horizontal scroll with visible overflow on phones | Product rails, but keep a grid view for browsing |

The first five patterns come from Luke Wroblewski's "Multi-Device Layout Patterns" (2012).

## Source order and reading order

- DOM order is the reading and keyboard order. Visual reordering with `order`, `flex-direction: row-reverse` or grid placement must not contradict it (WCAG 2.2 SC 1.3.2 Meaningful Sequence and 2.4.3 Focus Order).
- Decide the phone order first ("image above or below the headline?"); usually headline first, then image, unless the image is the content (product, map, chart).
- Never hide essential content on phones. Move it, disclose it, or shorten it with the same meaning.

## Fluid space

Let spacing, gutters and headings grow continuously between breakpoints.

```css
:root {
  --section-space: clamp(var(--space-12), 7vw + 1rem, calc(var(--space-20) * 2));   /* 48px to 160px */
  --stack-space: clamp(var(--space-4), 2vw + 0.5rem, var(--space-8));             /* 16px to 32px */
}
.section { padding-block: var(--section-space); padding-inline: var(--gutter); }
```

- `--gutter` already scales from 16px to 32px.
- Inside components sized by container queries, use container units (`cqi`) for type or space that should follow the container.
- Fluid type rules (rem term, max at most 2.5x min) are in the `typography` skill's defaults reference.

## Aspect ratios and cropping

```css
.media { aspect-ratio: 16 / 9; inline-size: 100%; object-fit: cover; object-position: 50% 35%; }
```

| Ratio | Use |
| --- | --- |
| 21:9 | Cinematic heroes, wide banners |
| 16:9 | Video, desktop heroes, slides |
| 3:2 | Photography, editorial images |
| 4:3 | Product shots, presentations from older templates |
| 1:1 | Avatars, product tiles, social |
| 4:5 | Social portrait, mobile heroes |
| 2:3 | Posters, book covers, portrait photography |
| 9:16 | Vertical video, stories, full-screen mobile |
| 1.91:1 | Link previews (Open Graph 1200x630) |

- Set `object-position` to keep the subject in frame; for important crops, art-direct.
- Always give images `width` and `height` attributes (or `aspect-ratio`) so the browser reserves space and the page does not shift.

## Art direction and resolution switching

Resolution switching (same crop, right file size):

```html
<img src="/img/team-1200.avif"
     srcset="/img/team-600.avif 600w, /img/team-1200.avif 1200w, /img/team-2000.avif 2000w"
     sizes="(min-width: 1024px) 58vw, 100vw"
     width="2000" height="1333" alt="..." loading="lazy" decoding="async">
```

Art direction (different crop per layout):

```html
<picture>
  <source media="(min-width: 1024px)" srcset="/img/hero-wide.avif" width="2400" height="1028">
  <source media="(min-width: 640px)" srcset="/img/hero-4x3.avif" width="1600" height="1200">
  <img src="/img/hero-4x5.avif" width="1080" height="1350" alt="..." fetchpriority="high">
</picture>
```

- The hero image is usually the Largest Contentful Paint element: no `loading="lazy"` on it, add `fetchpriority="high"`, and size it for the real layout width.
- Keep the alt text meaning identical across crops.
- Art-direct when the subject would be lost or the text overlay would collide in the default crop.

## Safe areas and viewport units

```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
```

```css
.app-bar { padding-top: max(var(--space-3), env(safe-area-inset-top)); }
.bottom-bar { padding-bottom: max(var(--space-3), env(safe-area-inset-bottom)); }
.full-height { min-block-size: 100dvh; }   /* dynamic viewport: accounts for mobile browser toolbars */
```

- Use `env(safe-area-inset-*)` for notches, rounded corners and home indicators when the layout extends to the edges.
- `100vh` on mobile includes the area behind browser toolbars; use `dvh` (dynamic), `svh` (smallest) or `lvh` (largest) instead.
- Fixed bottom bars and floating buttons must clear the home indicator and must not cover focused fields (WCAG 2.2 SC 2.4.11).

## Input and capability

```css
@media (pointer: coarse) { :root { --row-height: 3rem; } }          /* touch: larger rows */
@media (hover: hover) { .card:hover { box-shadow: var(--shadow-md); } }   /* hover only where it exists */
```

- Do not hide information behind hover on touch devices.
- Respect `prefers-reduced-motion` for layout transitions (see the `motion` skill).

## Zoom, reflow and text spacing

- 200% zoom and 400% zoom (reflow at 320px width) must work without horizontal scrolling for text content (WCAG 2.2 SC 1.4.4 and 1.4.10). Two-dimensional content such as maps and data tables may scroll.
- Overriding text spacing to line-height 1.5, paragraph spacing 2x font size, letter spacing 0.12em and word spacing 0.16em must not clip or overlap text (SC 1.4.12). Avoid fixed heights on text containers.

## Native apps

iOS size classes (compact and regular) and Android window size classes drive app layouts; see the `native-app-design` skill for platform specifics. The same recomposition logic applies: list-detail becomes two panes at expanded widths, bottom navigation becomes a navigation rail.

## Responsive checklist

- Breakpoints chosen where content breaks; components use container queries where possible.
- Reading and focus order match the visual order at every width.
- No essential content hidden on phones; tables have a phone strategy.
- Images have dimensions, `srcset`/`sizes`, and art-directed crops where needed; hero not lazy-loaded.
- Safe areas and dynamic viewport units handled; bars clear the home indicator.
- 320px reflow, 200% zoom and text-spacing overrides pass.
