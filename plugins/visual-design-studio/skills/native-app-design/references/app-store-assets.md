# App store assets (as of 2026)

Version-Timestamp: 2026-10-20 02:08:24 UTC

Apple figures were read from App Store Connect Help ("Screenshot specifications", "App preview specifications"), the App Review Guidelines (updated 16 October 2026) and the HIG app icon page on 2026-10-20. Google Play figures for icons and adaptive icons come from developer.android.com; Play Console Help pages could not be fetched from this environment, so the Play screenshot, feature graphic and text limits are the long-standing published values marked "verify". Store specs change at least yearly: confirm in App Store Connect and Play Console before export.

## Apple App Store

### Screenshots

| Display class (Apple's label) | Example devices | Portrait px | Status |
| --- | --- | --- | --- |
| iPhone with Dynamic Island, medium display | iPhone 15 to 18 Pro, iPhone 17 | 1206x2622 or 1179x2556 | Listed under "Required device sizes": at least one iPhone screenshot here |
| iPhone with Dynamic Island, large display | iPhone Air, 14 to 18 Pro Max, 15/16 Plus | 1320x2868, 1290x2796 or 1260x2736 | Recommended master; App Store Connect scales down from the highest resolution you supply |
| iPhone with Face ID, large display | iPhone 11 Pro Max to 14 Plus | 1284x2778 or 1242x2688 | Required only if no Dynamic Island large set is provided |
| iPhone with Face ID, medium display | iPhone X to 14, 16e, 17e | 1170x2532, 1125x2436 or 1080x2340 | Optional, scaled otherwise |
| iPhone with Home button | 5.5 in and 4.7 in models | 1242x2208; 750x1334 | Optional |
| iPhone Duo | Outer and inner displays | 1398x2034 (outer, matches the native panel); 2007x2853 (inner, larger than the native 1878x2670 panel, so native captures must be scaled; reported by developers, verify in App Store Connect) | Required from April 2027 for apps built with the iOS 27.1 SDK or later; supplying them adds an "optimized for iPhone Duo" badge (verify) |
| iPad 13-inch | iPad Pro and Air 13-inch | 2064x2752 or 2048x2732 | Required if the app runs on iPad |
| iPad 11-inch | iPad, iPad Air, iPad mini | 1668x2420, 1668x2388, 1640x2360 or 1488x2266 | Optional |

- Landscape uses the same numbers swapped. Formats: JPEG or PNG, **no alpha or transparency**. 1 to 10 screenshots per display size and localization.
- Apple's page is slightly inconsistent about which iPhone set is required (the "Required" list names the medium Dynamic Island display while the Face ID large entry refers to the large Dynamic Island set). Default: export a 1320x2868 master and a 1206x2622 set, and check App Store Connect's upload page for the project.
- Mac, Apple TV, Vision Pro and Watch apps have their own required sizes on the same page.

### App previews (video)

- 15-30 seconds, up to 500MB, H.264 (10-12 Mbps target) or ProRes 422 HQ, up to 30fps, stereo AAC 256kbps at 44.1 or 48kHz. Formats .mov, .m4v, .mp4. Up to 3 previews per display size and localization (verify).
- Screen capture of the app itself only (App Review 2.3.4); narration and text overlays allowed. Choose the poster frame (default at 5 seconds). Previews play before screenshots.

### Icon and metadata

- Icon: 1024x1024px layered icon from Icon Composer with default, dark, clear and tinted appearances (see [iOS HIG](ios-hig.md)). The flattened store image has no transparency.
- Text limits: app name 30 characters (App Review 2.3.7); subtitle 30; promotional text 170; keywords 100; description 4,000 (verify the last three in App Store Connect).
- Metadata must suit a 4+ audience even if the app is rated higher (2.3.8); no prices or unverifiable claims in names, subtitles or screenshots (2.3.7).
- Screenshots must show the app in use, not only title art, login or splash screens (2.3.3).
- Other surfaces: custom product pages (variants for campaigns and audiences), in-app events cards, product page optimization (A/B tests), Accessibility Nutrition Labels. WWDC26 "Enhance your presence on the App Store" describes new image and video placements on product pages, search results and Apple Ads; check App Store Connect for their current specs.

## Google Play

| Asset | Spec | Notes |
| --- | --- | --- |
| App icon | 512x512px, 32-bit PNG, sRGB, max 1024KB, full square | Play applies the mask (radius 30% of icon size) and shadow; do not add them (developer.android.com icon spec) |
| Feature graphic | 1024x500px, JPEG or 24-bit PNG, no alpha | Required to publish; used as video cover and in collections. Keep key content centered; avoid text near edges (verify) |
| Phone screenshots | 2-8 per device type; JPEG or 24-bit PNG, no alpha; each side 320-3,840px; long side no more than twice the short side | For recommendation and promotion eligibility, provide at least 4 screenshots at 1080px or more, e.g. 1080x1920 portrait or 1920x1080 landscape (verify) |
| Tablet screenshots | 7-inch and 10-inch sets, same format rules | Needed for tablet visibility and large-screen badges; show real tablet layouts, not phone screenshots padded (verify) |
| Chromebook, Wear OS, TV, Android XR | Separate sets | Each form factor has its own requirements |
| Promo video | YouTube URL, public or unlisted, no ads, no age restriction | Plays from the feature graphic (verify) |
| Text | Title 30 characters; short description 80; full description 4,000 | No emoji spam, ranking claims or calls to download in the title (verify) |

- Show Android UI only: no iOS status bars, Dynamic Island or iPhone frames in Play assets.
- Adaptive launcher icon (108dp layers, 66dp safe zone, monochrome layer) is separate from the 512px store icon; see [Android Material 3](android-material3.md).
- Store listing experiments test icons, screenshots and descriptions; custom store listings target countries or campaigns.

## Screenshot design defaults (both stores)

| Decision | Default | Change when |
| --- | --- | --- |
| Count | 5-8 per device class; the first 3 carry the story because search results show them | Simple utility: 3-4 |
| Order | 1: core value in action; 2: the main workflow; 3: differentiator; 4-6: supporting features; last: trust (security, awards, reviews only if verifiable) | Games: lead with gameplay |
| Caption | 3-7 words, benefit-led, about 64-96px cap-height type on a 1320px-wide canvas (a common starting point), top third | Localize every caption; allow 30-40% text expansion for German, Finnish and similar |
| UI area | 60-75% of the canvas is real app UI | Never show UI that does not exist |
| Frames | Device frames optional; Apple's official bezels or none | Play: no Apple hardware |
| Status bar | Clean: full battery and signal, neutral time, no personal notifications | |
| Background | Brand color or subtle gradient behind UI; consistent across the set so it reads as a panorama | Dark-mode set if the app is dark-first |
| Accessibility | Caption contrast 4.5:1; no essential info in tiny UI text | |
| Data | Realistic, localized sample content; no real customer data or personal information | |

Generic failures: five near-identical screenshots of the same screen, lorem-like captions ("Unlock your potential"), marketing illustrations with no UI, phone frames tilted in 3D on every slide, text too small to read in search results, and US-only content in localized listings.

## Localization

- Localize screenshots, captions and previews for every market where the listing is localized; both stores fall back to another language otherwise, which reads as neglect.
- Re-capture UI in each language rather than translating only captions; check RTL locales (Arabic, Hebrew) for mirrored layouts.
- Use market-appropriate sample content: names, currencies, addresses and date formats from the market, with fictional data.
- Check the atlas market entries (`python3 ../../../library/scripts/atlas.py query "<market>"` from this folder) for color and imagery conventions before reusing a US set.

## Icon production checklist

1. Design on the platform grids: Apple's icon template at 1024px, Android's 108dp adaptive canvas with the 66dp safe zone.
2. Test at 29pt/40pt (iOS Settings and Spotlight) and 48dp (Android launcher) for silhouette recognition; one strong shape survives, fine detail does not.
3. Check every appearance: iOS default, dark, clear and tinted; Android themed (monochrome) icon on light and dark wallpapers.
4. Compare beside the top 20 icons in the category on a real home screen; distinctness matters more than detail.
5. Export: Icon Composer `.icon` file for Apple; adaptive icon XML with foreground, background and monochrome layers for Android; a separate 512px Play store icon.

## Export checklist

1. Build screenshots from the real app (simulator or device capture at native resolution), then compose in Figma or a script. Keep one master file per locale.
2. Export at exact pixel sizes; flatten; strip alpha; use sRGB as the safe default for both stores.
3. Name files by store, device class, locale and order (`ios_6-9_en-US_01.png`).
4. Verify in App Store Connect and Play Console upload previews, then on a real device listing after release.
