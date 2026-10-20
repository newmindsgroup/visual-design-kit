---
id: audience.low-bandwidth-entry-devices
axis: audience
name: Low Bandwidth and Entry-Level Devices
aliases: [low bandwidth, slow network, 2g 3g, emerging markets, entry-level android, android go, feature phone, kaios, data saver, lite apps]
summary: Users on slow, metered networks and 1-3 GB RAM phones; design text-first pages under about 500 KB, 48px targets, 7:1 contrast, offline tolerance and honest data costs.
tags: [low bandwidth, performance, android go, emerging markets, data saver, offline, pwa, feature phone, lite]
pairs_with: [style.civic-plain, style.flat-material, style.web-brutalist, style.data-dense-utilitarian, market.india-south-asia, market.sub-saharan-africa, market.southeast-asia, market.latin-america-spanish, industry.fintech-banking, tier.value]
avoid_with: [style.glass-spatial, style.skeuomorphic-tactile, style.kinetic-experimental-type, style.vibrant-gradient-saas, style.retro-futurism-synthwave]
version_timestamp: 2026-10-20 02:08:35 UTC
---

# Low Bandwidth and Entry-Level Devices

## Who and what they need

- **Who:** prepaid mobile-data users in emerging markets, rural and remote users everywhere, people on shared or hand-me-down phones, students on school Chromebooks, travelers on airplane or event Wi-Fi, and anyone whose data plan is nearly spent.
- **Devices:** Android phones with 1-3 GB RAM and slow CPUs (Android Go class), older iPhones, KaiOS feature phones (about 240x320 screens, D-pad navigation), cracked or low-brightness LCDs used outdoors.
- **Needs:** pages that load in seconds and work when the connection drops, no surprise data spend, large legible controls, offline-safe forms, and alternatives to the app (SMS, USSD, WhatsApp, voice) when the app is too big to install.
- **Overlaps:** with low literacy (icons plus words, local languages), with older devices, and with value-tier pricing; mobile money and QR payments are often the commerce rail.
- **Lighthouse reference profile:** mobile emulation throttles to roughly 1.6 Mbps down, 150ms round trip and 4x CPU slowdown; treat it as a floor, not an extreme.

## Design defaults

| Variable | Default for this audience | General default | Source or reasoning |
| --- | --- | --- | --- |
| Page budget | First view: HTML plus CSS plus JS plus fonts about 350-500 KB transferred; JS 150 KB compressed or less; hero image 100 KB or less | No budget | Alex Russell, "The Performance Inequality Gap" (budget guidance; verify current numbers); web.dev performance budgets |
| Core Web Vitals | LCP 2.5s or less, INP 200ms or less, CLS 0.1 or less at the 75th percentile on a throttled mid-range device | Same targets | web.dev Core Web Vitals thresholds |
| Minimum body text | 16-18px system font stack or one subset variable font (about 30-50 KB WOFF2) | 16px | Avoid font downloads for scripts that system fonts already cover |
| Target size | 48px minimum with 8px gaps; primary actions in the lower half | 44px | Imprecise cheap touchscreens, one-handed use; Material 48dp |
| Contrast | 7:1 body; no light weights; avoid thin gray; do not assume OLED dark mode saves power | 4.5:1 | Sunlight glare and low-contrast LCD panels; WCAG 1.4.6 |
| Reading level | Grade 5-8 in the user's language; short strings; support transliteration and local scripts | Grade 8 | plainlanguage.gov; many users read in a second language |
| Line length | 35-60 characters, single column, 360px baseline viewport, reflow to 320px | 60-75ch | WCAG 1.4.10; common low-end viewport |
| Motion | None or CSS transforms and opacity only, 150ms or less; no autoplay video, Lottie or parallax; honor reduced motion and Save-Data | 120-240ms | Long tasks over 50ms block input on weak CPUs |
| Information density | Text-first, 3 images or fewer above the fold, no carousels, inline SVG icons | Medium | Bytes are cost for the user |
| Session and connection | Assume drops: queue writes, retry with backoff, idempotent requests, keep form state locally, resume uploads | Online-first | Service workers and Background Sync |
| Error tolerance | Very high: optimistic UI with pending state, offline banner that explains what still works, no lost carts or drafts, timeouts 30s or more | Standard | Intermittent connectivity |
| App size | Install under about 10-20 MB for lite apps; split downloads; show size before large downloads | App-store typical | Android Go and "Lite" app guidance (verify current Google Play guidance) |

## Interaction and content

- **Progressive enhancement:** server-rendered HTML that works without JavaScript; forms submit with plain POST; enhance with small islands (Astro, htmx, Qwik) instead of hydrating whole pages.
- **PWA basics:** service worker with an offline shell, cached last-seen data, install prompt only after value is shown, background sync for queued actions.
- **Images:** AVIF or WebP with JPEG fallback, srcset with a 360-720px ceiling for mobile, quality 55-75, explicit width and height (no layout shift), lazy-load below the fold, prefer SVG and CSS shapes; never video as hero.
- **Third parties:** every tag manager, chat widget and font service costs bytes and CPU; load none by default, facade embeds (click-to-load video), self-host fonts.
- **Data honesty:** state sizes before downloads ("Video, 12 MB"), offer a data-saver toggle on by default when the Save-Data header is present, let users pick 240p/360p, and make downloads resumable.
- **Channel alternatives:** SMS and USSD flows, WhatsApp deep links and share cards, voice or IVR, QR codes, short links, OTP autofill (WebOTP); pay with mobile money, UPI or airtime where local.
- **KaiOS and D-pad:** linear focus order, visible focus on everything, softkey labels, no hover, no touch assumptions.
- **Language:** localized, short, concrete; avoid text embedded in images; let users switch language on the first screen.

## Visual tone

- **Flat, cheap to paint, high-contrast.** Avoid gradients, blur, large shadows and filters that stress weak GPUs.
- **Palette example:** ink #333333 (oklch 0.32 0 0) on white is 12.63:1; primary #0050B3 (oklch 0.45 0.171 258) 7.50:1; danger #B00020 (oklch 0.48 0.193 24) 7.33:1; success #1E6B2E (oklch 0.47 0.120 147) 6.57:1; surface #F5F5F5 holds #333333 at 11.59:1. #767676 is the lightest gray that still reaches 4.5:1 on white (4.54:1); #949494 drops to 3.03:1.
- **Type:** system-ui stack first; if a webfont is needed, one variable face (Noto Sans, Inter, Source Sans 3; OFL) subset by unicode-range. Noto covers most scripts as a fallback.
- **Brand assets:** SVG logo under 2 KB, CSS color blocks, icon sprite under 10 KB; one illustrative photo per page at most.
- **Tone:** practical and respectful; speak to the cost of data, not to the lack of it.

## Pitfalls

- Testing only on a developer laptop and fiber; test on a real low-end phone with throttling.
- A 5 MB hero video, web fonts for every script, and a 600 KB JavaScript bundle for a content page.
- Requiring an app install or Play Services for core tasks; ignoring feature phones where they matter.
- Assuming constant connectivity: lost carts, lost form data and spinners without timeout messages.
- Blocking the page behind cookie banners or chat widgets that cost more bytes than the content.
- Dark gray text on mid gray; tiny tap targets; hover-only interactions.
- Photos with embedded text that cannot be translated or read aloud.

## Regulatory and compliance notes

- **Data protection:** India DPDP Act 2023, Brazil LGPD, Nigeria Data Protection Act 2023, Kenya Data Protection Act 2019, South Africa POPIA and GDPR all shape consent notices; write them in plain local languages and keep banners light.
- **Telecom and messaging:** SMS sender registration and template approval (for example India's DLT), US TCPA consent for texts, and OTP rules vary by country.
- **Pricing and net neutrality:** India's TRAI barred differential data pricing in 2016 (Free Basics); zero-rating rules differ by market, so do not promise "free data" without checking.
- **Payments and identity:** mobile-money and e-KYC regulations, data-localization requirements (for example payment data in India; verify per market).
- **Accessibility:** WCAG 2.2 AA still applies; lightweight pages are easier to make accessible.

Confirm requirements with counsel for the specific product and jurisdiction.

## Reference anchors

- web.dev, Core Web Vitals and performance budgets; Chrome Lighthouse throttling documentation
- Alex Russell, "The Performance Inequality Gap" (Infrequently Noted)
- Google "Building for Billions" research and Android Go program; Facebook Lite, Twitter Lite (PWA), Spotify Lite, Google Go as lite-product references
- KaiOS developer documentation for D-pad interface design
- Low-tech Magazine's solar-powered website as an extreme low-weight reference
- GOV.UK frontend progressive-enhancement practice; Noto fonts (Google, OFL)
