# Iconography

Version-Timestamp: 2026-10-20 02:07:10 UTC

Icons are a typeface for ideas: they work only when every glyph shares one grid, one stroke, one corner logic and one metaphor vocabulary. Pick a proven open-source family unless the brand genuinely needs its own, and draw custom icons to the same rules as the family they sit beside.

## Grid and keylines

Default canvas: 24x24 px with 2px padding, so artwork lives in the central 20x20.

| Keyline shape | Size on the 24px grid | Use for |
| --- | --- | --- |
| Circle | 20px diameter | Round objects (clock, globe, user head-and-shoulders) |
| Square | 18x18px | Boxy objects (calendar, image, app) |
| Portrait rectangle | 16x20px | Phones, documents, bottles |
| Landscape rectangle | 20x16px | Monitors, cards, cameras |

The circle is larger than the square because round shapes look smaller at the same size (the same optical logic as type overshoot). These keylines follow Material Design's system icon grid and are a common starting point across most icon sets.

Other grid rules:

- Snap anchor points to the pixel grid. With a 2px stroke, place stroke centerlines on whole-pixel coordinates so each stroke covers exactly 2 pixels; with a 1px stroke, place centerlines on half-pixel coordinates (x.5).
- Keep negative space between parallel strokes at least 2px at 24px (1.5px at 16px), or the gap closes on low-density screens.
- Allow small elements (badges, notification dots, arrows) to break the padding by up to 1px when needed, never the canvas.
- Keep visual weight consistent: a filled circle at 20px looks heavier than an outline square at 18px; compare icons in a row, not one at a time.

## Stroke, corners, caps and joins

| Property | Default | Notes |
| --- | --- | --- |
| Stroke width | 2px at 24px (Lucide, Feather and Tabler style) or 1.5px (Heroicons outline style) | One weight per set; scale proportionally for other sizes or use optical masters |
| Outer corner radius | 1-2px at 24px (Material uses 2px) | Sharp corners (0px) read technical; 3px+ reads soft and playful |
| Inner corner radius | Outer radius minus stroke width, or 0 | Keeps stroke width visually even around corners |
| Caps | Round for friendly products; square or butt for precise, technical ones | Never mix |
| Joins | Round with round caps; miter with square caps | Miter joins on acute angles need a miter limit or a bevel to avoid spikes |
| Angles | Prefer 0, 45 and 90 degrees; other angles only when the object requires it | Consistent angles make a set look engineered |
| Detail budget | 3-5 meaningful shapes per icon at 24px | Remove decoration before shrinking |

## Optical sizes

Scaling a 24px icon to 16px makes strokes too thin and gaps too tight; scaling to 48px makes it look empty. Draw or tune optical masters.

| Size | Stroke | Adjustments |
| --- | --- | --- |
| 16px | 1.5px (or 1px on whole pixels for crisp 1x) | Drop interior details, widen gaps, prefer filled forms for complex objects |
| 20px | 1.5-1.75px | Dense desktop UI; slightly simplified |
| 24px | 1.5-2px | The master |
| 32px | 2-2.5px | Can add one level of detail |
| 48px and up | Illustrative icons, can be duotone or use brand color | Treat as spot illustrations with icon geometry |

Material Symbols ships these adjustments as variable font axes (fill, weight, grade and optical size); use the optical-size axis rather than plain scaling.

## Filled vs outline

- **Outline** is the default for navigation, toolbars and actions.
- **Filled** marks the selected or active state (tab bars and navigation rails in iOS and Material both use this), and works better at 16px where outlines close up.
- **Duotone** (two tones or an accent fill) suits marketing pages and feature lists, not dense UI.
- Never mix outline and filled icons in one toolbar unless filled means "selected".
- Do not use color alone for state; pair it with fill, weight or a label.

## Choosing metaphors

Use established conventions; novelty in icons costs comprehension.

| Concept | Convention | Notes |
| --- | --- | --- |
| Search | Magnifying glass | Universal |
| Settings | Gear | Sliders for filter or adjust, not for settings |
| Home | House | |
| Notifications | Bell | |
| Delete | Trash can | Confirm or allow undo for destructive actions |
| Edit | Pencil | |
| Add | Plus | |
| More actions | Three dots (horizontal or vertical) | One orientation per product |
| Share | Platform convention: iOS square with up arrow; Android three connected nodes | Follow the platform in native apps |
| Save | Floppy disk is still understood; a bookmark means "save for later" | Pick one meaning per product |
| Download / upload | Arrow into or out of a tray | |
| External link | Arrow leaving a square | |

Rules:

- Pair icons with text labels in navigation and for any action that is not one of the universal conventions. Icon-only buttons are acceptable only for well-known actions in repeated, space-constrained contexts, and always need an accessible name.
- Test unfamiliar icons with a name-the-icon test: show 5-8 people the icon without a label and ask what it does. If most people do not name it correctly, add a label or change the metaphor.
- Check cultural meaning in each market: hand gestures (thumbs up and the OK sign are offensive in some regions), mailboxes and phones vary by country, animals and colors carry local meaning, and in Japan and Korea a circle (maru) often means "correct" while a check mark can mean "wrong". Verify with local reviewers.
- Avoid religious, political and national symbols unless the product requires them.

## Accessibility

- Icon-only controls need an accessible name (`aria-label` or visually hidden text) and a target of at least 24x24 CSS px (44x44 recommended for touch); the icon itself can be smaller than the target.
- Meaningful icons need 3:1 contrast against adjacent colors (WCAG 2.2, 1.4.11 Non-text Contrast). For example, #6B7280 on white is 4.83:1 and passes; #9CA3AF on white is 2.54:1 and fails for icons that carry meaning.
- Decorative icons next to a text label: `aria-hidden="true"` so screen readers do not read them twice.
- Show focus on the control, not just a color change on the icon.

## SVG hygiene

```html
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"
     fill="none" stroke="currentColor" stroke-width="2"
     stroke-linecap="round" stroke-linejoin="round"
     aria-hidden="true" focusable="false">
  <circle cx="11" cy="11" r="7"/>
  <path d="m20 20-4-4"/>
</svg>
```

- Always set `viewBox="0 0 24 24"`; size with CSS or the `width` and `height` attributes, never by editing coordinates.
- Use `currentColor` for stroke or fill so icons inherit text color, hover states and dark mode.
- No transforms, no hidden layers, no embedded raster, no editor metadata, no inline `style` attributes, no fixed IDs that collide when icons repeat on a page. Run SVGO (or the set's build tooling) with 2-decimal precision.
- Merge shapes where possible; keep strokes as strokes in the source if the set's stroke width is meant to be adjustable, and expand them only when a consumer cannot handle strokes.
- Standalone meaningful SVGs get `role="img"` and a `<title>`; decorative ones get `aria-hidden="true"`.
- Deliver as individual SVGs plus a sprite (`<symbol>` elements used via `<use href="#icon-search"/>`) or framework components (for example `lucide-react`). Avoid icon fonts for UI; they fail when fonts are blocked and confuse screen readers. Variable icon fonts such as Material Symbols are the exception when used with proper labels.

## Open-source icon sets

Licenses verified against each project's LICENSE file in October 2026. Check the LICENSE at the version you ship and record it in the project's third-party notices.

| Set | License | Style | Notes |
| --- | --- | --- | --- |
| Lucide | ISC (icons derived from Feather are also covered by an MIT notice) | 24px grid, 2px stroke, round caps and joins | Community fork of Feather; large, actively maintained |
| Phosphor | MIT | Six weights: thin, light, regular, bold, fill, duotone | Good when one family must span UI and marketing |
| Heroicons | MIT | Outline 24px (1.5px stroke), solid 24px, mini 20px, micro 16px | From the makers of Tailwind CSS |
| Tabler Icons | MIT | 24px grid, 2px stroke (adjustable), outline plus filled subset | Very large set |
| Material Symbols | Apache-2.0 | Outlined, rounded and sharp styles; variable fill, weight, grade and optical size | Matches Material 3 Android and web apps |
| SF Symbols | Apple license, not open source | Tuned to San Francisco type weights and sizes | Use only in apps and mockups for Apple platforms; not in logos or on other platforms; some symbols are restricted to specific Apple features |

Mixing sets: do not. If one set lacks an icon, draw it to that set's grid, stroke and corner rules, or switch sets.

## Designing a custom set

1. Inventory the metaphors the product needs (often 40-120 for an app).
2. Draw 6 key icons first to set the style: a round object, a boxy object, a person, an arrow, a complex object and an abstract concept.
3. Lock the rules in a one-page spec: grid, keylines, stroke, corner radii, caps, joins, angles, detail budget, filled-state rules.
4. Batch the rest against the spec; review on a sheet at 16, 20, 24 and 32px on light and dark backgrounds.
5. Name files by meaning, not appearance (`icon-delete.svg`, not `icon-trash.svg`), with aliases for search.

## Common failures

- Icons pulled from three sets → one family.
- 1px strokes in a 2px set → one stroke weight per size.
- Scaled-down 24px icons at 16px look broken → optical masters.
- Mystery-meat navigation (icons without labels) → labels in navigation.
- Icons recolored with hard-coded hex → `currentColor`.
- Emoji as icons → drawn icons; emoji render differently on every platform and read aloud as their names.
