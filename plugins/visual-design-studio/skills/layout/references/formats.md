# Formats and sizes

Version-Timestamp: 2026-10-20 02:07:10 UTC

Each format is its own composition with its own safe areas. Platform specs change; the values below are common as of 2026, so confirm current specs with the platform or printer before production. The atlas channel entries hold full specs and QA checklists: read them with `python3 ../../../library/scripts/atlas.py show <channel-id>`.

| Channel | Atlas ID |
| --- | --- |
| Marketing website | `channel.marketing-website` |
| Web application | `channel.web-app` |
| Native app | `channel.native-app` |
| E-commerce store | `channel.ecommerce-store` |
| Social media | `channel.social-media` |
| Email | `channel.email` |
| Print collateral | `channel.print-collateral` |
| Packaging | `channel.packaging` |
| Out-of-home and digital signage | `channel.ooh-signage` |
| Presentations | `channel.presentation` |
| Video and motion | `channel.video-motion` |
| Environmental and wayfinding | `channel.environmental-wayfinding` |

## Screens (CSS px)

| Class | Typical viewport widths | Design at |
| --- | --- | --- |
| Phones | 360-440 (common Android 360-412; recent iPhones 390-440) | 360 and 390-393; check 320 |
| Tablets | 744-1024 portrait, 1024-1366 landscape | 768 and 834 portrait, 1180-1366 landscape |
| Laptops | 1280-1536 (1366x768 and 1536x864 remain common on Windows) | 1280 and 1440 |
| Desktops | 1920+ | 1440 with a 1920 check; cap content at `--container-xl` |
| TV (10-foot UI) | 1920x1080 or 3840x2160 | Keep 5% inside each edge for overscan; text 24px+ at 1080p |

Icons and previews:

| Asset | Size |
| --- | --- |
| Favicon | SVG plus 32x32 PNG; 180x180 `apple-touch-icon`; 192 and 512 PNG in the web app manifest |
| iOS app icon | 1024x1024 master; the system applies the corner mask |
| Android adaptive icon | 108x108dp layers; keep the logo inside the central 66dp safe zone |
| Open Graph and link preview | 1200x630 (1.91:1); keep text within the center for square crops |

## Email

- Body width 600-640px, single column on phones; images at 2x for high-density screens.
- Live text for headlines and calls to action; images may be blocked by default in some clients.
- Details and client quirks: `channel.email` and the `print-packaging-social` skill.

## Print (trim sizes)

| Format | Millimetres | Inches | Notes |
| --- | --- | --- | --- |
| A3 | 297 x 420 | 11.7 x 16.5 | Posters, spreads of A4 |
| A4 | 210 x 297 | 8.3 x 11.7 | Reports, letters (ISO markets) |
| A5 | 148 x 210 | 5.8 x 8.3 | Booklets, flyers |
| A6 | 105 x 148 | 4.1 x 5.8 | Postcards |
| DL | 99 x 210 | 3.9 x 8.3 | Flyers (envelope DL is 110 x 220) |
| US Letter | 216 x 279 | 8.5 x 11 | Reports, letters (US, Canada) |
| US Legal | 216 x 356 | 8.5 x 14 | Legal documents |
| Tabloid / Ledger | 279 x 432 | 11 x 17 | Posters, spreads of Letter |
| Business card (EU) | 85 x 55 | 3.35 x 2.17 | |
| Business card (US) | 88.9 x 50.8 | 3.5 x 2 | |
| Business card (Japan) | 91 x 55 | 3.58 x 2.17 | |
| Business card (Australia) | 90 x 55 | 3.54 x 2.17 | |
| Posters (US) | 457 x 610, 610 x 914 | 18 x 24, 24 x 36 | Film one-sheets are 27 x 40 in |
| Posters (ISO) | A2 420 x 594, A1 594 x 841, A0 841 x 1189 | | |

Print production defaults (confirm with the printer):

- Bleed 3mm (0.125in); safe zone 3-5mm inside trim; binding allowances in [grids](grids.md).
- Images at 300 ppi at final size for close viewing; large posters viewed from a distance often work at 150 ppi; billboards far less. Ask the printer.
- CMYK in the printer's profile, or spot colors; rich black for large areas, 100K for small text (see the `color` skill's brand color reference).

## Out-of-home (verify with the media owner)

| Format | Size | Notes |
| --- | --- | --- |
| UK 48-sheet billboard | 6096 x 3048mm | 2:1 landscape |
| UK 6-sheet (bus shelter, street furniture) | 1200 x 1800mm | 2:3 portrait, often backlit |
| US bulletin | 14 x 48ft | Very short viewing time: 7 words or fewer is a common rule |
| Digital screens | Owner-specific pixel sizes, often 1080x1920 portrait or 1920x1080 landscape | Static readability in 5-10 seconds; motion limits vary by location and law |

## Presentations

| Tool or format | Canvas | Notes |
| --- | --- | --- |
| 16:9 (default) | 1920x1080px | The usual target for screens and projectors |
| PowerPoint widescreen | 13.333 x 7.5in (960 x 540pt) | Type sizes in points are half of Keynote's for the same look |
| Keynote wide | 1920 x 1080pt | |
| Google Slides widescreen | 10 x 5.625in | |
| 4:3 | 1024x768px | Older rooms and some print handouts |

Layout: 12-column grid, 80-120px side margins at 1920px, one idea per slide, body type sizes in the `typography` skill's defaults.

## Social media (as of 2026; verify current specs)

| Platform and placement | Size (px) | Ratio | Safe area and notes |
| --- | --- | --- | --- |
| Instagram feed, portrait | 1080 x 1350 | 4:5 | Profile grid previews crop to 3:4 (since 2025); 1080 x 1440 (3:4) fills both feed and grid; keep key content central |
| Instagram feed, square | 1080 x 1080 | 1:1 | |
| Instagram Stories and Reels | 1080 x 1920 | 9:16 | Keep text and logos out of roughly the top 250px and bottom 340px (platform UI) |
| TikTok | 1080 x 1920 | 9:16 | Keep clear of the bottom caption area and the right-side action buttons |
| YouTube video | 1920 x 1080 or 3840 x 2160 | 16:9 | |
| YouTube thumbnail | 1280 x 720 | 16:9 | Readable at about 320px wide; avoid the bottom-right timestamp corner |
| YouTube Shorts | 1080 x 1920 | 9:16 | Same safe-area logic as Reels |
| YouTube channel banner | 2560 x 1440 | | Text and logo inside the central 1546 x 423 safe area |
| LinkedIn feed image | 1200 x 627, or 1080 x 1080, or 1080 x 1350 | 1.91:1, 1:1, 4:5 | Company page cover 1128 x 191 |
| X (Twitter) in-feed image | 1600 x 900 | 16:9 | Header 1500 x 500 |
| Facebook feed | 1080 x 1350 or 1080 x 1080 | 4:5, 1:1 | Link previews 1200 x 630 |
| Pinterest pin | 1000 x 1500 | 2:3 | |

- Export sRGB, at the exact pixel size. Text inside images must also appear in the post text or alt text.
- Design each ratio as its own composition; never letterbox a 16:9 design into 9:16.
- Detailed specs, copy limits and QA: `channel.social-media` and the `print-packaging-social` skill.

## Video and motion

| Format | Size | Notes |
| --- | --- | --- |
| HD landscape | 1920 x 1080 | 16:9; 24, 25, 30 or 60 fps by market and content |
| 4K UHD | 3840 x 2160 | |
| Vertical | 1080 x 1920 | 9:16 for Reels, Shorts, TikTok, Stories |
| Square | 1080 x 1080 | Feeds |

- Safe areas: graphics inside about 90% of the frame (5% margin each side), action inside about 93% (EBU R 95 defines these for broadcast; most online video follows the same habit).
- Captions: burned-in or sidecar; keep them out of the platform UI zones. See the `motion` skill.

## Format checklist

- Exact pixel or trim size, color space and file type from the current platform or printer spec, dated.
- Bleed, safe zone and platform UI zones marked in the file.
- One composition per ratio, not a scaled copy.
- Text sizes checked at the real display size (thumbnail size for YouTube, arm's length for print, distance for signage).
