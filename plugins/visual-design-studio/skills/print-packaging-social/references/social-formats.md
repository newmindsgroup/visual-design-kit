# Social formats and content design

Version-Timestamp: 2026-10-20 02:07:10 UTC

Social content is judged in the first frame and the first second, on a phone, usually with the sound off, under platform UI. Design every asset at the platform's native size, keep text out of the UI zones, and make the hook work as a still. For channel structure and QA see the atlas entry [social media](../../../library/atlas/channels/social-media.md).

## Formats as of 2026

Specs change often and platforms rarely publish everything. Values below were checked on 2026-10-20 against current third-party size guides and the platform help pages they cite. "Verified" means two or more consistent current sources; "unverified" means a single source, conflicting sources or no current confirmation. Confirm in the platform's help center, ads guide or creative center, and preview in the app, before production.

| Platform | Placement | Size (px) | Ratio | Notes | Status |
| --- | --- | --- | --- | --- | --- |
| Instagram | Feed portrait | 1080x1350 | 4:5 | Takes the most feed space; default for feed posts | Verified |
| Instagram | Feed square / landscape | 1080x1080 / 1080x566 | 1:1 / 1.91:1 | Landscape is small in feed; avoid for key content | Verified |
| Instagram | Profile grid preview | Crop of the feed post | 3:4 | Grid moved from squares to 3:4 tiles in early 2025; a 4:5 post loses a little on the left and right in the grid. 1080x1440 uploads are widely recommended but not confirmed by Meta | Verified (crop); unverified (1080x1440) |
| Instagram | Stories, Reels | 1080x1920 | 9:16 | Reels covers show as 3:4 in the grid: keep the title in the center | Verified |
| Instagram | Carousel | 1080x1350 or 1080x1080 | 4:5 or 1:1 | Up to 20 slides; the first slide's ratio applies to all | Verified |
| TikTok | Video, photo posts | 1080x1920 | 9:16 | UI overlays vary by app version and ad type; use TikTok's safe-zone overlay or ad preview | Verified (size); unverified (exact overlays) |
| YouTube | Video | 1920x1080 (3840x2160 for 4K) | 16:9 | | Verified |
| YouTube | Thumbnail | 1280x720, 2MB max | 16:9 | Timestamp badge covers the bottom right; test legibility at about 320x180 and 160x90 | Verified |
| YouTube | Shorts | 1080x1920 | 9:16 | Up to 3 minutes since October 2024 | Unverified for 2026 changes |
| YouTube | Channel banner | 2560x1440 | 16:9 | Only the central 1546x423 is visible on all devices | Verified |
| LinkedIn | Single image post or ad | 1200x627 | 1.91:1 | 1080x1080 or 1200x1200 square also common; portrait 1080x1350 performs well on mobile | Verified (1200x627); unverified (square vs portrait advice) |
| LinkedIn | Document (PDF carousel) | 1080x1350 per page | 4:5 | Upload as PDF | Unverified |
| LinkedIn | Company page cover | 1128x191 | about 5.9:1 | Larger sizes (4200x700, 1512x256) also reported; check Page settings | Unverified |
| X | In-stream image | 1200x675 (or 1600x900) | 16:9 | Portrait and square images are cropped in the timeline preview | Verified (1200x675); unverified (1600x900) |
| X | Header / profile | 1500x500 / 400x400 | 3:1 / 1:1 | Profile displays as a circle | Verified |
| Facebook | Feed | 1080x1350 or 1080x1080 | 4:5 or 1:1 | | Verified |
| Facebook | Stories, Reels | 1080x1920 | 9:16 | Keep text out of roughly the top and bottom 250px | Verified |
| Facebook | Page cover | 851x315 | about 2.7:1 | Desktop shows about 820x312; mobile crops to about 640x360: center key content | Verified |
| Pinterest | Standard pin | 1000x1500 | 2:3 | Taller than 2:3 may be truncated in feed | Verified |
| Pinterest | Video pin | 1080x1920 | 9:16 | | Unverified |
| Threads | Image post, carousel | 1080x1350 | 4:5 | Up to 10 images per carousel; landscape about 1200x628 | Verified (4:5, 10 images); unverified (landscape) |
| Open Graph | Link preview (`og:image`) | 1200x630, under 5MB | 1.91:1 | Meta needs at least 600x315 for the large card; X's large card crops to 2:1, so keep content inside the central 1200x600 | Verified |
| Regional | Xiaohongshu (RED), WeChat, LINE, KakaoTalk | Varies | Varies | Xiaohongshu favors 3:4 portrait (1080x1440); check each platform's own guidance | Unverified |

## Safe areas for 9:16

On a 1080x1920 canvas, platform UI covers the top (account name, close and sound buttons), the right edge (like, comment, share rail) and especially the bottom (caption, music, call-to-action button, "Sponsored" label).

| Zone | Organic content (common baseline) | Paid ads (conservative, Meta Reels ads guidance) |
| --- | --- | --- |
| Top | Keep text below y = 220 | Keep text below y = 269 (14%) |
| Bottom | Keep text above y = 1500 (420px reserved) | Keep text above y = 1248 (35% reserved, 672px) |
| Left | 60px margin | 65px (6%) |
| Right | Keep text left of x = 940 (TikTok's action rail is about 120-160px wide) | Keep text left of x = 920 |
| Safe box | About 880x1280 starting at (60, 220) | About 855x980 starting at (65, 269) |

The TikTok figures are community measurements that vary by app version; Meta's percentages come from its Reels ads guidance. Use the platforms' official overlay templates when available. Faces and products may extend outside the safe box; text, logos, prices and calls to action may not.

For 4:5 feed posts, keep critical content inside the central 3:4 area (about 1012x1350) so the profile grid crop does not cut it.

## First-frame hook

- The first frame must work as a still: subject plus promise, readable on a phone at arm's length. It is also the thumbnail or cover in many grids.
- Start with motion or change in the first half second; no logo intro, no slow fade from black.
- Headline overlay on the first frame: 7 words or fewer, set large (64-96px cap height on a 1080 canvas), high contrast, inside the safe box.
- Lead with the outcome or the tension ("Your 3pm slump is a lunch problem"), not the brand.
- Faces looking toward the content or at the camera help in people-led categories; product-in-hand for products.
- Brand early but small: a consistent color, frame or type style identifies the brand better than an opening logo card.

## Captions and text

- Many viewers watch feed video with the sound off, so burn in captions or use the platform's auto-captions, and correct them.
- Burned-in caption style: 2 lines maximum, about 20-32 characters per line on vertical video, 48-64px on a 1080-wide canvas, a solid or semi-opaque box or a stroke for contrast of at least 4.5:1, inside the safe box, synced to speech.
- Upload a caption file (SRT or the platform's editor) as well, so captions are selectable, translatable and accessible.
- Keep post copy hashtags in the caption, not the image; use CamelCase hashtags (#BrandName) so screen readers pronounce them.
- Write alt text for images wherever the platform supports it (Instagram, X, LinkedIn, Facebook, Threads).

## Carousel structure

| Slide | Job | Design |
| --- | --- | --- |
| 1 | Hook: title plus promise, swipe cue | Biggest type; a visual element that bleeds off the right edge invites the swipe |
| 2 to n−1 | One point per slide, numbered | Same grid, type sizes and position on every slide; 20-40 words per slide |
| n | Summary plus one call to action, save or share prompt | Brand sign-off, handle |

- 5-10 slides is a common starting point; up to the platform limit only if each slide earns its place.
- Body text 36-48px minimum on 1080px wide; titles 64-110px.
- Design slides on one continuous artboard when using elements that cross slide edges, then export each 1080px section.
- Keep content in the central 3:4 area for Instagram grid previews.

## Templates and production

- Build a master template per format with locked safe-area guides, brand frame, logo position, type styles and editable text and image slots, with maximum character counts written on the template.
- Export at native size: sRGB; PNG for flat graphics and text-heavy images; JPEG at 80-90 quality for photos; MP4 H.264 with AAC audio for video, 30fps (or the source frame rate), at the platform's recommended bitrate.
- Avoid fine gradients, hairlines and tiny text; platform recompression destroys them.
- Name files by platform, placement and version: `campaign-ig-reel-cover-v3.png`.

## Platform tone

- **Instagram:** polished but human; strong single images and carousels; Reels for reach.
- **TikTok:** native, lo-fi, people-led, trend-aware; ads that look like ads get skipped.
- **YouTube:** thumbnails with a face or a clear object and 3-4 words; Shorts for discovery.
- **LinkedIn:** text-led posts, documents and data; professional but personal voice.
- **X:** fast, text-first, timely; images support a point.
- **Pinterest:** vertical, search-led, text overlays that name the idea.
- **Threads:** conversational, text-first, images as support.

## Accessibility

- Text overlays at 4.5:1 contrast against what is behind them (use a scrim or box over video).
- No flashing more than 3 times per second; warn before strobing content.
- Captions on every video with speech; describe meaningful sounds.
- Alt text on images; avoid text-only images for essential information.

## Common failures

- Key copy under the caption or action rail → safe-area overlay on every frame.
- A landscape TV ad cropped to 9:16 → reframe or reshoot for vertical.
- Ten-word first frame in 32px type → 7 words or fewer, 64px+.
- Carousel slides with different layouts → one grid, numbered slides.
- Uploading 4K vertical video with tiny text → native 1080x1920, large type.
- Specs copied from a three-year-old blog → verify against the platform and date the spec.
