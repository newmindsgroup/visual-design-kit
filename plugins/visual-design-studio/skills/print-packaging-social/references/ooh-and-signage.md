# Out-of-home and signage

Version-Timestamp: 2026-10-20 02:07:10 UTC

Out-of-home is read at distance, at speed and in bad light, by people who did not ask to see it. One idea, one image, a big brand and few words, sized from the real viewing distance. For format sizes and media-owner specs see the atlas entries [OOH and signage](../../../library/atlas/channels/ooh-signage.md) and [environmental and wayfinding](../../../library/atlas/channels/environmental-wayfinding.md).

## Viewing distance and letter height

Rules of thumb (sign-industry guidance, not standards; test mockups at real distance):

- **Impact:** about 25mm of cap height per 3m of viewing distance (1in per 10ft), roughly 8mm per meter.
- **Limit of legibility:** the United States Sign Council's recommended legibility index is about 30ft per inch of letter height for good conditions (roughly 2.8mm per meter). Multiply the distance a letter can serve by about 0.83 in moderately complex surroundings and 0.67 in highly complex ones; make all-caps letters about 15% taller than mixed case for the same legibility.

| Viewing distance | Cap height for impact | Minimum cap height (good conditions) |
| --- | --- | --- |
| 3m (10ft) | 25mm (1in) | 8mm (0.33in) |
| 10m (33ft) | 85mm (3.3in) | 28mm (1.1in) |
| 30m (100ft) | 250mm (10in) | 85mm (3.3in) |
| 50m (165ft) | 415mm (16.5in) | 140mm (5.5in) |
| 100m (330ft) | 830mm (33in) | 280mm (11in) |
| 150m (500ft) | 1250mm (50in) | 420mm (16.5in) |

Typeface: open apertures, generous x-height, medium to bold weights, moderate spacing (add 2-5% tracking at large sizes viewed from afar). Avoid condensed, light, script and high-contrast didone faces for anything that must be read quickly.

Mixed case reads faster for more than two or three words; all caps works for one or two short words.

## Viewing time

Time available = distance at which the message becomes legible ÷ speed.

| Context | Example | Time to read |
| --- | --- | --- |
| Motorway | Legible from 150m at 100km/h (27.8m/s) | About 5 seconds |
| Urban road | Legible from 100m at 50km/h (13.9m/s) | About 7 seconds |
| Pedestrian | Legible from 20m at walking pace (about 1.4m/s) | About 14 seconds |
| Dwell (platform, queue, waiting room) | Stationary | 30 seconds to several minutes |

Design for the shortest realistic case: drivers also need to watch the road.

## Word count and hierarchy

- **Roadside:** 7 words or fewer is a common rule; one headline, one image, the brand.
- **Street furniture and transit (pedestrian):** headline of up to 7 words plus a short support line and a call to action.
- **Dwell placements:** longer copy, sequences, QR codes and offers can work.
- **Brand:** large and in a consistent position; the logo or distinctive asset should be readable at the same distance as the headline. A common starting point is a logo height of 10-15% of the panel height.
- **No URLs or phone numbers roadside** unless they are very short and memorable; QR codes only where people stand still and close.
- **Image:** one focal subject, big and simple, cropped tight; detail is invisible at distance.
- **Thumbnail test:** view the design at 2-5% of its size (a 6m-wide billboard viewed at about 120-300px wide on screen) or from across the room; if the idea does not read, simplify.

## Contrast and color

- Aim for 7:1 or higher contrast between text and background for distance reading (a common starting point); never below 4.5:1.
- Luminance contrast matters, not hue contrast. Computed examples: yellow #FFD100 on near-black #111111 is 12.92:1; white on Swiss red #E30613 is 4.88:1 (acceptable for large type, weak at distance); red #E30613 on #111111 is only 3.87:1; brand red #D92D20 on green #1A7F37 is 1.05:1, effectively invisible.
- White text on bright orange (#FF6A00) is 2.87:1 and fails; use near-black (#111111, 6.58:1) on orange.
- Backlit panels and LED screens bloom: thin light-on-dark strokes thicken and fill in, so use heavier weights and wider spacing for reversed type.
- Check the design in grayscale and with color-vision simulation.

## Digital out-of-home and digital signage

### Slots and loops

- Ad slot lengths of about 5-15 seconds are common (6, 8, 10 or 15); loops shared by several advertisers often run 60-120 seconds or more. Take exact slot length, loop length and share of voice from the media owner.
- Roadside digital billboards: many jurisdictions forbid motion, transitions and video, and require a minimum hold per static image (often in the 6-10 second range). Confirm with the media owner and local authority before designing animation.
- Viewers arrive mid-loop. Every frame must stand alone, carry the brand and make sense without the frames before it.

### Dwell-based design

| Viewer | Dwell | Design |
| --- | --- | --- |
| Passing | Under 3s | One image, 5 words or fewer, brand on every frame |
| Approaching | 3-10s | Headline plus one support line, simple motion with a clear end state |
| Dwelling | 10s+ | Sequences, information, offers, QR codes, schedules |

- Hold each text frame long enough to be read twice: at least 3 seconds for a headline of up to 7 words is a common starting point, longer for more words.
- One movement at a time; motion should guide the eye to the message, not decorate.
- Static fallback frame for when playback fails.
- Flash safety: no more than 3 flashes per second (WCAG 2.3.1); avoid saturated red flashing and large high-contrast patterns that flicker; broadcast-style checks (for example ITU-R BT.1702) apply to video-heavy content.

### Resolution and pixel pitch

- Design at the screen's native pixel grid. LED billboards have low pixel counts: a 6x3m face at 10mm pitch is 600x300px; at 6mm pitch it is 1000x500px.
- Physical letter height = pixel height × pitch. At 10mm pitch, a 30px cap is 300mm tall: legible to about 100m, impactful to about 35m.
- Strokes at least 2-3px wide on LED; avoid hairlines, small serifs and fine textures that alias or shimmer.
- Rule of thumb: minimum comfortable viewing distance in meters is about the pixel pitch in millimeters, and 2-3 times that for a smooth image.
- Brightness changes between day and night are set by the operator; check that dark text on light grounds does not glare at night.
- Export to the owner's spec: exact pixel dimensions, MP4 H.264 or still images, frame rate, no audio unless stated, sRGB.

## Environmental and wayfinding signage

- Sign family: identification, directional, informational, regulatory; one type system and arrow set across all.
- Letter height from viewing distance (table above), placed at consistent mounting heights along sightlines.
- Arrows point in the direction of travel and sit on the side of the destination text they refer to; never more than about 5-7 destinations on one directional sign.
- Pictograms from a recognized set (for example the AIGA/DOT symbol signs) for public facilities.
- US accessibility: the 2010 ADA Standards for Accessible Design set visual character heights by viewing distance and mounting height (§703.5) and tactile sign rules (§703.2-703.4: raised characters 5/8in to 2in high, Grade 2 braille, baseline of tactile characters 48-60in above the floor). Other countries have their own codes. Confirm requirements with the project's accessibility consultant and local code.
- Non-glare (matte) finishes and high luminance contrast between characters and background; some codes specify minimum light reflectance value (LRV) differences, so check the applicable one, and check lighting on site.

## Production and handoff

- Use the media owner's template: trim, bleed, visible area and frame overlap differ by format.
- Large print formats are often supplied at reduced scale (1:4 or 1:10) with the resolution scaled up accordingly; follow the template.
- Color: CMYK to the printer's profile for paper posters; many large-format inkjet workflows prefer RGB or specific profiles; ask.
- Proof a section at 100% to check image quality, and a full reduced-scale proof for composition.
- For vehicles and wraps: template per model, keep text off door gaps, handles, windows and curves.

## QA checklist

1. Viewing distance and speed known; letter height checked against the table.
2. 7 words or fewer for roadside; one idea.
3. Contrast computed (7:1 target) and checked in grayscale.
4. Brand legible at the same distance as the headline.
5. Thumbnail test passed at 2-5% scale.
6. Digital: every frame stands alone, holds long enough, no flashing above 3 per second, static fallback exists.
7. Exported to the owner's exact spec and reopened.
8. Photographed or simulated in context (site photo, day and night).

## Common failures

- A print ad scaled up to a billboard → redesign for distance: fewer words, bigger type, one image.
- Thin, light type reversed on a backlit panel → heavier weight, more spacing.
- Long animation sequence that only works from the first frame → every frame stands alone.
- Low-contrast brand colors (orange with white, red on green) → compute contrast and change the pairing.
- QR codes on motorway billboards → only in dwell placements.

For client display projects with site surveys, scheduling and installed-screen checks, use the deep process skills [display discovery](../../../library/draft-skills/design-display-discovery/SKILL.md), [display content](../../../library/draft-skills/design-display-content/SKILL.md), [display production](../../../library/draft-skills/design-display-production/SKILL.md), [display evaluation](../../../library/draft-skills/design-display-evaluation/SKILL.md), [extreme formats](../../../library/draft-skills/design-screen-formats/SKILL.md), [loops](../../../library/draft-skills/design-screen-loops/SKILL.md) and [attention sequencing](../../../library/draft-skills/design-screen-attention/SKILL.md).
