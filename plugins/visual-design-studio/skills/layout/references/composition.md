# Composition

Version-Timestamp: 2026-10-20 02:07:10 UTC

Composition decides what is seen first, second and third, and whether the whole feels intentional. These are perception heuristics with long practice behind them, not laws; check every rule against the rendered result.

## Hierarchy

- Plan three levels per view: **primary** (the one thing), **secondary** (supporting), **tertiary** (details, metadata, legal). More levels flatten into noise.
- Tools, strongest first: size, position (top and start of reading direction), value contrast, weight, color, isolation (space around), motion.
- Contrast between levels must be obvious. Typical ratios: marketing headline 3-6x body size; product UI page title 1.5-2.5x body; editorial display up to 10x.
- **Squint test:** blur the screenshot (or step back). The primary element must still dominate, and the secondary group must still read as a group.

## Focal point

- One focal point per view. Two equal focal points split attention and both lose.
- Make it win with at least two of: largest size, highest contrast, most isolation, a face or the product, the only saturated color.
- Place it on a strong position: a rule-of-thirds intersection, an asymmetric column start, or slightly above the geometric center (the optical center).
- Point at it: gaze direction in photos, lines, diagonals, arrows and the reading path should lead to the focal point and then to the action.

## Visual weight

| Heavier | Lighter |
| --- | --- |
| Larger | Smaller |
| Darker value on light grounds (lighter value on dark grounds) | Close to the background value |
| Saturated, warm color | Desaturated, cool color |
| Detailed texture, photography, faces | Flat fields, empty space |
| Isolated | Crowded |
| Dense text blocks | Single lines |
| Irregular shapes | Regular, familiar shapes |

Use it to balance: a large, light image can balance a small, dark, dense text block.

## Asymmetric balance

- Symmetry is stable, formal and static: invitations, luxury, institutional, ceremonial work.
- Asymmetry is dynamic and modern, and needs more skill. Balance like a lever: a heavy element close to the center balances a light one far from it; a block of empty space has weight too.
- Common recipe on 12 columns: headline on columns 1-5 at display size, image on 6-12 bleeding off the edge, body text under the headline on 1-4, lots of untouched space top right.
- Check: cover one half of the layout with your hand. Each half should feel incomplete without the other, not empty.

## Scale contrast

- Big jumps create drama and clarity: a 120px number next to 14px labels reads instantly.
- Small jumps (24px heading over 18px body) look like a mistake. Either make the difference clearly visible (at least 1.5x) or make the sizes equal and use weight or color.
- Use scale contrast once or twice per view. A page where every section has a giant headline has no giant headline.
- Scale signals tier: luxury pairs very large type or images with very small text and a lot of space; value retail uses many medium-large elements close together.

## Whitespace

- **Macro whitespace** (margins, section spacing, empty columns) sets the mood and tier. **Micro whitespace** (line spacing, padding, letter spacing) sets readability.
- Put whitespace in blocks, not evenly sprinkled. One large empty area is calmer and more confident than the same area spread as many small gaps.
- More whitespace raises perceived value and focus but lowers information density; decide from the audience (experts want density, first-time visitors want focus).
- Empty space must look intended: align its edges to the grid.

## Alignment

- Use 2-4 vertical alignment axes per view: the main text edge, an image edge, a secondary column edge, perhaps a centered axis for a hero.
- Prefer edge alignment (start) to center alignment for anything over 3 lines.
- Align type by its visible edges: cap height and baseline for headings next to images, not the text box.
- Hang bullets, quotes and large initial capitals outside the text edge so the text column stays straight.
- Mixed centered and left-aligned blocks on one screen look accidental unless the centered block is clearly a separate zone (hero, footer, modal).

## Reading patterns

| Pattern | When | Design response |
| --- | --- | --- |
| F-pattern | Text-heavy pages; users scan the first lines and down the left edge (Nielsen Norman Group eyetracking research) | Front-load headings and first words; use meaningful subheads; put key links at the start of lines |
| Layer-cake | Pages with clear subheadings | Make subheads informative enough to read alone |
| Z-pattern | Sparse pages: hero, ads, posters | Logo top-left, secondary item top-right, diagonal to the focal content, call to action bottom-right |
| Gutenberg diagram | Evenly distributed content | Strongest start top-left, natural end bottom-right; put the action at the terminal area |
| Spotted | Users hunting for a specific item (price, date, button) | Make those items visually distinct and consistently placed |

In RTL languages mirror the patterns: start top-right. In vertical Japanese editorial, reading runs top-to-bottom, right-to-left.

## Gestalt principles

| Principle | Use | Failure |
| --- | --- | --- |
| Proximity | Group related items with less space between them | Equal spacing makes groups dissolve |
| Similarity | Same style means same role (all links one color) | A decorative element styled like a button |
| Common region | A background or border groups items (cards, panels) | Cards inside cards inside cards |
| Continuity | Aligned items read as a sequence | Broken alignment in a list or timeline |
| Closure | Implied shapes complete themselves (logos, icons) | Gaps too large to close |
| Figure-ground | Clear separation of object and background | Text over a busy photo |
| Common fate | Elements that move together belong together | Unrelated items animating in unison |
| Uniform connectedness | Lines or connectors bind items more strongly than proximity | Connectors that cross and tangle |

## Optical adjustments

- **Optical center:** place a single centered element slightly above the geometric center (a few percent of the height) or it looks low.
- **Overshoot:** round and pointed forms must extend slightly beyond flat ones to look the same size. Type designers overshoot O and A past the baseline and cap height; icon grids do the same: in Material's 24dp grid, a circle keyline is 20dp while a square is 18dp.
- **Play and arrow icons:** shift a play triangle a little toward its point so its visual center sits in the circle.
- **Vertical centering in buttons:** center on cap height (or x-height for lowercase labels), not the line box; adjust by 1-2px if needed.
- **Edges:** a photo with a light background next to a text block needs a slightly larger gap or a subtle edge to read as aligned.
- **Large type spacing:** display headlines need tighter tracking and leading than the scale suggests (see the `typography` skill).

## Composition recipes

| Recipe | Character | Fits |
| --- | --- | --- |
| Asymmetric split (5+7 or 4+8) | Modern, confident | Most marketing pages, Swiss and editorial styles |
| Full-bleed image with text in a calm area | Emotional, immersive | Hospitality, fashion, outdoor, campaigns |
| Typographic poster (type is the image) | Bold, direct | Events, culture, launches, neo-brutalist |
| Centered symmetrical | Formal, ceremonial | Luxury, invitations, institutional |
| Modular grid of varied cells | Rich, browsable | Portfolios, editorial homepages, product overviews (avoid identical "bento" cells by default) |
| Broken grid and layered collage | Energetic, handmade | Youth, music, fashion, maximalist and collage styles |
| Split screen (50/50) | Comparison, duality | Before/after, two audiences, sign-in pages |

The generic AI layout is a centered hero, a gradient blob, and three identical icon cards. If that is the draft, recompose: choose a real focal point, an asymmetric split, a distinctive image or number, and unequal card widths that reflect unequal importance.

## Critique questions

1. What is seen first? Is it what matters most?
2. Can you find three clear levels of hierarchy, and no more?
3. Do groups read as groups when blurred?
4. How many alignment axes are there? Can any be removed?
5. Is whitespace in deliberate blocks?
6. Does anything compete with the focal point that should not?
7. Does the composition still work at the narrowest and widest sizes?
