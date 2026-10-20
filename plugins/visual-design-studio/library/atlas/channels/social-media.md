---
id: channel.social-media
axis: channel
name: Social Media
aliases: [social, social content, instagram, tiktok, linkedin, youtube, reels, stories, social posts, social ads]
summary: Feed, story and short-video formats where a 1-3 second hook, platform-native framing and mobile-sized type decide whether anyone stops; specs change often.
tags: [social, instagram, tiktok, linkedin, youtube, reels, stories, carousel, thumbnails, hooks]
pairs_with: [style.playful-bubbly, style.collage-mixed-media, style.editorial-magazine, style.vibrant-gradient-saas, style.kinetic-experimental-type, audience.teens-gen-z, industry.ecommerce-dtc, industry.media-entertainment-streaming, archetype.jester, archetype.creator]
avoid_with: [style.art-nouveau-ornamental, style.classic-luxury-serif]
version_timestamp: 2026-10-20 02:01:01 UTC
---

# Social Media

## Formats and specs

Platform specs change often and sources disagree. Values are as of 2026 and compiled from platform help pages and vendor guides; confirm against Meta Business Help (Ads Guide), TikTok Creative Center and Business Help, LinkedIn Marketing Solutions (Ad specs), YouTube Help and X Business before production. Always preview in the app.

| Placement | Size and ratio | Notes |
| --- | --- | --- |
| Instagram feed post | 1080x1350 (4:5) preferred; 1080x1080 (1:1); 1080x566 (1.91:1) | 4:5 takes the most feed space. Profile grid previews have changed crop over time (square, then reportedly 3:4); keep the subject central and verify in app |
| Instagram Reels / Stories, Facebook Reels / Stories, TikTok, YouTube Shorts | 1080x1920 (9:16) | Meta Reels ads guidance: keep text clear of about 14% top, 35% bottom, 6% sides (269 / 672 / 65 px); Stories ads about 14% top and 20% bottom. TikTok sources vary (top 130-240 px, bottom 480-660 px, sides about 120 px); use the platform's safe-zone overlay. Minimum 540x960 for TikTok |
| Carousel | 1080x1350 or 1080x1080, 2-20 slides depending on platform | Consistent crop across slides; first slide is the hook; swipe cue on slide 1 |
| LinkedIn single image ad / post | 1200x627 (1.91:1) or 1200x1200 (1:1) | Company page cover has changed (1128x191 older, 1512x256 reported newer); verify in Page settings |
| Link preview (Open Graph, X large card) | 1200x630 (1.91:1), under 5 MB | Absolute HTTPS URL; platforms cache, so re-scrape after changes |
| YouTube thumbnail | 1280x720 (16:9), 640 px minimum width, 2 MB or less, JPG/PNG/GIF/WebP | Timestamp badge covers the bottom-right corner |
| YouTube video | 1920x1080 or 3840x2160; H.264 High profile MP4, AAC-LC 48 kHz; about 8 Mbps (1080p 24-30fps SDR) or 12 Mbps (48-60fps) | YouTube Help "recommended upload encoding settings" |
| Pinterest pin | 1000x1500 (2:3) | Taller than 2:3 may be truncated |
| Profile image | Circular crop; supply 400x400 or larger, subject within the central 70% | Logos need a simplified avatar version |
| Color and export | sRGB; JPEG quality 80-90 for photos, PNG for flat graphics and text; MP4 H.264 for video | Platforms recompress, so avoid fine gradients and tiny text |

## Structure and hierarchy

- **Hook first:** the first 1-3 seconds (video) or first slide (carousel) must show the subject, the promise or the visual tension. Put the logo small and late in video unless brand recognition is the point.
- **Content system:** define 3-6 repeatable templates (announcement, quote, product, how-to, behind-the-scenes, data) with locked brand devices (color field, type style, corner mark) and flexible imagery. Plan a grid for the profile: alternate dense and sparse posts if the grid is visible.
- **Hierarchy per post:** one focal point, one message of 7 words or fewer on the image, supporting detail in the caption. Carousels: one idea per slide, 5-10 slides, final slide with the CTA.
- **Video pacing:** change something every 2-3 seconds; vertical framing with subject in the central safe area; captions burned in or as native captions for sound-off viewing.
- **Platform voice:** LinkedIn favors clear takeaways and data; Instagram and TikTok favor people, process and trends; YouTube favors a promise plus a strong thumbnail. Adapt, do not crosspost unchanged.

### Platform design notes

| Platform | Content job | Design notes |
| --- | --- | --- |
| Instagram | Brand personality, product, community | 4:5 posts and carousels, Reels with native captions; consistent cover frames and highlight covers |
| TikTok | Entertainment-first discovery | Raw-feeling, vertical, face or product within 1 second, native sound and captions; polish less than story |
| LinkedIn | Professional proof and ideas | 1.91:1 or 1:1 images, document-style carousels, clear takeaways, data graphics with 4.5:1 contrast |
| YouTube | Search, depth, subscriptions | Thumbnail with 3-5 words and one face or object, consistent title style, Shorts for discovery |
| X | News, conversation | Large link cards, short text, image 16:9 or 1:1 |
| Pinterest | Planning and inspiration | 2:3 pins with clean text overlays, evergreen subjects, link to a destination |
| Facebook | Community, local, ads | Mixed formats, 4:5 video, community and event assets |

## Craft defaults

- Type size: a 1080 px-wide canvas appears about 390 pt wide on a phone, so 1 px is about 0.36 pt. Use 40 px or more for any overlay text (about 14 pt on screen) and 56-96 px for headlines.
- Contrast: 4.5:1 for text over images, achieved with a scrim or solid block; do not place text over busy detail. Check against light-mode and dark-mode UI chrome.
- Safe composition: keep faces and text inside the platform safe area; leave the lower 30% of 9:16 frames free for captions and UI.
- Color: saturate slightly for phone screens, but stay within sRGB; avoid thin colored text on colored fields.
- Motion: 200-400ms transitions, snappy cuts; kinetic type timed to audio; keep loops under 6-15 seconds; avoid flashing more than 3 times per second.
- Accessibility: alt text on every image, captions or subtitles on video (SRT/VTT or burned in plus native), CamelCase hashtags, avoid emoji strings, descriptive link text.
- Consistency: the same 2-3 brand colors, one display typeface, one illustration or photo style; the feed should read as one voice from a thumbnail.

## Production and handoff

- Build templates in Figma, Canva or After Effects with variables for text, color and crop; export at the largest accepted size. The `print-packaging-social` skill covers social formats in more depth; the `motion` skill covers video and kinetic type.
- Provide naming (platform_format_campaign_v01), caption copy decks, alt text, captions files, thumbnails, and an approvals-ready schedule. Provide 9:16, 4:5 and 1:1 cutdowns for paid campaigns.
- Paid ads: follow each platform's ad policies on text, claims and restricted categories; keep text overlay minimal and use captions for message.
- Disclosure: sponsored and influencer content needs clear material-connection disclosure (FTC Endorsement Guides in the US, ASA/CAP code in the UK); platforms increasingly require labels for AI-generated or altered media. Confirm requirements with counsel for the market.
- Community management: moderation guidelines, response templates, crisis protocol; store assets with usage rights for creators and music.

## QA checklist

- [ ] Each asset previewed on the actual platform (phone, light and dark mode) and in the profile grid.
- [ ] Text and faces sit inside the platform safe areas for all 9:16 placements.
- [ ] Text 40 px or larger on a 1080 canvas; contrast 4.5:1 over imagery.
- [ ] Captions or subtitles on all video; alt text written; no flashing above 3 per second.
- [ ] Hook visible in the first frame and the first slide; CTA clear.
- [ ] Colors consistent in sRGB; no banding in gradients after compression.
- [ ] Music and imagery licensed for commercial and paid use.
- [ ] Specs rechecked against the platform's current help page on the day of production.

## Reference anchors

- Meta Business Help Center "Ads Guide"; TikTok Creative Center; LinkedIn Marketing Solutions ad specifications; YouTube Help
- Duolingo, Liquid Death, Glossier, Nike and Netflix social accounts as commonly cited examples of platform-native brand voice
- Jonah Berger, *Contagious* (2013), for shareability principles
- Open Graph protocol (ogp.me) and X developer documentation for link-card metadata
- W3C WCAG 2.2, success criteria 1.2 (time-based media) and 2.3.1 (three flashes)
