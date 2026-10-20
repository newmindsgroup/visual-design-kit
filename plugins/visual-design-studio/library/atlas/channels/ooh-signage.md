---
id: channel.ooh-signage
axis: channel
name: Out-of-Home and Digital Signage
aliases: [ooh, billboard, outdoor advertising, transit advertising, digital signage, dooh, poster site, bus shelter, kiosk screen]
summary: Billboards, transit and digital screens read in seconds from distance; one idea, huge type, high contrast and ruthless copy cuts matter more than detail.
tags: [ooh, billboard, outdoor, transit, digital signage, dooh, poster, large format, legibility, viewing distance]
pairs_with: [style.swiss-international, style.bold-geometric-sport, style.neo-brutalist, style.fashion-editorial-didone, style.kinetic-experimental-type, industry.automotive-mobility, industry.food-beverage-cpg, industry.events-conferences, archetype.hero, archetype.jester]
avoid_with: [style.data-dense-utilitarian, style.art-nouveau-ornamental, style.maximalist-eclectic]
version_timestamp: 2026-10-20 02:01:01 UTC
---

# Out-of-Home and Digital Signage

## Formats and specs

Media owners publish their own templates and technical specifications; the owner's spec sheet is final. Figures are as of 2026 and vary by country and network; confirm with the media owner (for example Clear Channel, JCDecaux, Lamar, Ocean Outdoor) and the industry bodies (OAAA in the US, Outsmart in the UK).

| Format | Typical size | File and resolution | Notes |
| --- | --- | --- | --- |
| US bulletin (static or digital) | About 14x48 ft (4.3x14.6 m) | Vector or raster at reduced scale (for example 1:10) at roughly 100-150 ppi effective; ask the printer | Template shows trim, bleed and unseen frame area |
| US poster / 30-sheet | Roughly 10x22 ft visible area (sources cite 10 ft 5 in to 10 ft 6 in by 22 ft 8 in) | CMYK PDF at 1:4 or 1:10 scale, 100-150 ppi effective | Sizes vary by operator; verify with the owner |
| UK 6-sheet (street furniture) | 1200x1800 mm nominal; visible area slightly smaller | CMYK PDF with 3-5 mm bleed; 150-300 ppi at final size | Often backlit; check luminance and white points |
| UK 48-sheet / 96-sheet | About 6x3 m / 12x3 m | CMYK PDF at 1:4 scale, 100-150 ppi | Roadside; viewing from 30-100 m |
| Digital panels (urban, transit, mall) | Pixel grids vary; 1920x1080 (16:9) and 1080x1920 (9:16) are common | MP4 H.264 or JPEG/PNG, sRGB, 24-30 fps, no audio; static or 6-10 s loops | Large digital bulletins use different pixel counts; always take the owner's pixel spec |
| Digital indoor screens | 1920x1080 or 3840x2160, landscape or portrait | H.264 MP4, HTML5 or images; sRGB; 30 fps | Keep a 5% margin for overscan and mounts |
| Transit / vehicle wraps | Template per vehicle model | Vector with 100+ mm bleed, 100-150 ppi at full size | Allow for windows, doors, seams, vents |
| Dwell time | Roadside 5-8 seconds as a vendor rule of thumb; transit shelters and mall screens 10-30 s | | Design for the shortest realistic view |

Legibility rules of thumb (vendor guidance, not standards; test mockups at real viewing distance):

- Comfortable letter height about 1 inch (25 mm) of cap height per 10 ft (3 m) of viewing distance; the limit of legibility for bold sans is roughly 1 inch per 30 ft. A message read at 150 ft wants letters 15 inches tall.
- Seven words or fewer for roadside; one image, one idea, a large brand mark.
- Aim for 7:1 or higher contrast between text and ground for distance viewing (a common starting point); avoid mid-tone pairings.
- Keep critical content inside the central 80-85% of the face, away from frame and mount hardware.

Cap height by viewing distance (comfortable at 1 in per 10 ft; limit at 1 in per 30 ft):

| Viewing distance | Comfortable letter height | Limit of legibility |
| --- | --- | --- |
| 30 ft (9 m), shelter or street | 3 in (75 mm) | 1 in (25 mm) |
| 100 ft (30 m), city street | 10 in (250 mm) | 3.3 in (85 mm) |
| 200 ft (60 m), arterial road | 20 in (500 mm) | 6.7 in (170 mm) |
| 300 ft (90 m), highway bulletin | 30 in (750 mm) | 10 in (250 mm) |
| 500 ft (150 m), highway, large bulletin | 50 in (1.25 m) | 17 in (420 mm) |

## Structure and hierarchy

- **Three-element rule:** image or idea, headline, brand mark (plus a URL or short CTA only if memorable). Everything else is cut.
- **Reading order:** top-left to bottom-right is not guaranteed; make the headline, product and brand form a clear line using scale difference of at least 3:1.
- **Context:** consider the sight line (left, right, approach angle), speed (highway vs pedestrian), and surroundings. Pedestrian-level formats allow 15-25 words and small details; roadside does not.
- **Sequencing:** for digital, treat 6-10 seconds as 2-3 frames max; hold the final brand frame for at least 3 seconds. Plan roadside series ("teaser, then reveal") over multiple sites.
- **Time and place:** adapt copy by daypart, weather or location when the network supports dynamic content.

## Craft defaults

- Type: bold or semibold sans with generous tracking (+2% to +5% at large sizes), x-height large, no thin weights or script; capitals for 1-3 words, sentence case beyond. Fonts: Archivo, Barlow, Inter Tight, Atkinson Hyperlegible (OFL); commercial: Trade Gothic, Helvetica Now, Knockout.
- Color: two to three colors; saturated brand colors on flat fields; avoid gradients that band at distance; white backgrounds glare on lit digital screens, so consider a dark or colored ground.
- Imagery: one hero image cropped tight, readable as a silhouette; photographs need strong value contrast; avoid small details, fine rules and screenshots.
- Digital motion: slow, simple, 300-600ms transitions; no strobing or flashing above 3 per second; keep animation purposeful; do not rely on sound.
- Lighting and context: preview on a day background (sun glare) and at night (LED brightness); test against sky, brick and glass.
- Accessibility and safety: avoid distracting road users (no rapid motion on roadside digital; follow local advertising rules), keep contrast high, and use alt-text equivalents in digital kiosks.
- Interactive and QR: QR only where dwell time and signal allow (transit, shelters); code size at least 1 cm per 10 cm of viewing distance (rule of thumb), with a short URL fallback.

## Production and handoff

- Workflow: obtain the media owner's template and specs, create a layout at 1:10 or 1:4 scale, mock up on site photos, proof on the printer's color profile, send final files and a delivery schedule. The `print-packaging-social` skill covers OOH in the context of print and campaign production.
- Provide: CMYK or sRGB masters as required, fonts outlined, bleed and safe-zone markers, color reference (Pantone/CMYK), and a version list per site. For digital, deliver MP4 loops and a static fallback.
- Approvals: many jurisdictions regulate placement, illumination, alcohol/tobacco/gambling/financial claims and location; confirm with the media owner and counsel.
- Measurement: unique URL or QR, geo-fenced search, brand-lift or footfall studies as the client supports.
- Sustainability: favor recyclable PVC-free vinyl or paper for static; digital reduces waste but uses energy; choose energy-efficient screens and shorter loops.

## QA checklist

- [ ] The message is understood in under 5 seconds at the real viewing distance (test at 1:10 scale with a distance factor).
- [ ] 7 words or fewer; headline, image and brand are distinct at 3:1 scale difference.
- [ ] Contrast checked in sun glare and at night; no thin type, tiny logos or low-contrast taglines.
- [ ] Bleed and safe area follow the owner's template; no text near unseen frame areas.
- [ ] Digital files meet pixel, codec, frame rate and file-size specs; static fallback supplied.
- [ ] No flashing above 3 per second; motion is slow and legible.
- [ ] Legal copy, disclaimers and regulatory marks fit and are legible; claims checked by counsel.
- [ ] Site list, versions and run dates agreed with the media owner.

## Reference anchors

- OAAA (Outdoor Advertising Association of America) and Outsmart (UK) creative guidance
- Saul Bass and Paul Rand for reduction in graphic communication; Lester Beall and Cassandre's poster work
- Lamar, Clear Channel Outdoor and JCDecaux creative specification pages
- US Federal Highway Administration (FHWA) Manual on Uniform Traffic Control Devices and its sign-legibility research (traffic signs, not advertising) for viewing-distance context
- Apple "Shot on iPhone" outdoor campaign as a widely cited minimal OOH execution
