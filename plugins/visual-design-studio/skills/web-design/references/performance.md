# Performance and Core Web Vitals

Version-Timestamp: 2026-10-20 02:04:32 UTC

Performance is a design decision: the hero image, the fonts, the video, the tag manager and the animation library are all chosen in design. Set budgets before the first comp, mark the LCP element on every template, and judge success by field data from real users.

## Core Web Vitals thresholds

Assessed at the 75th percentile of page loads, separately for mobile and desktop (web.dev, as of 2026). A page passes when all three are "good" at p75.

| Metric | Measures | Good | Needs improvement | Poor |
| --- | --- | --- | --- | --- |
| LCP (Largest Contentful Paint) | Loading: when the largest image or text block renders | 2.5 s or less | 2.5-4.0 s | Over 4.0 s |
| INP (Interaction to Next Paint) | Responsiveness: latency of interactions across the visit | 200 ms or less | 200-500 ms | Over 500 ms |
| CLS (Cumulative Layout Shift) | Visual stability: unexpected movement | 0.1 or less | 0.1-0.25 | Over 0.25 |

INP replaced FID as a Core Web Vital on 12 March 2024. Supporting metrics: TTFB good at 0.8 s or less, FCP good at 1.8 s or less. Thresholds and definitions are revised occasionally; confirm at web.dev/articles/vitals before quoting them in a contract.

Design targets with margin: LCP 2.0 s, INP 150 ms, CLS 0.05 at p75 on mobile.

## Lab versus field data

| | Field (real users) | Lab (synthetic) |
| --- | --- | --- |
| Sources | Chrome UX Report (CrUX) via PageSpeed Insights, Search Console and the CrUX API; your own RUM with Google's `web-vitals` library | Lighthouse, Chrome DevTools Performance panel, WebPageTest |
| Strength | What users actually experienced, across devices and networks; what Google uses for page experience | Reproducible, debuggable, available before launch |
| Weakness | 28-day rolling window in CrUX; Chrome users only; needs enough traffic; new pages have none | One device and network profile; cannot measure INP (Total Blocking Time is a proxy) |
| Use for | Pass/fail and prioritization | Diagnosing causes and preventing regressions in CI |

A Lighthouse score of 100 does not mean users have a fast experience; third-party scripts, personalization and real devices often make field INP and LCP worse. Collect RUM from launch day so you do not wait 28 days for CrUX.

## Budgets (kit starting points, not standards)

| Resource | Marketing and content page | App-like page |
| --- | --- | --- |
| JavaScript (compressed, initial route) | 150 KB or less | About 300 KB, code-split by route |
| CSS (compressed) | 50 KB or less, critical CSS inlined | 100 KB or less |
| LCP image | 200 KB or less (AVIF/WebP), rendered within 2.0 s | Same |
| Total page weight on first load | About 1 MB | About 1.5-2 MB |
| Web fonts | 2 families, 4 WOFF2 files or fewer, about 100 KB total | Same |
| Third-party scripts | 3-5 vendors, each with an owner and a reason | Same |
| Requests before first render | As few as possible; no render-blocking third parties | Same |

Halve the budgets for `audience.low-bandwidth-entry-devices`. Enforce budgets in CI (Lighthouse CI assertions or bundle-size checks) so they survive after launch.

## LCP: what to do

Break LCP into its four parts (web.dev): time to first byte, resource load delay, resource load duration, and element render delay. In a well-optimized page, most time goes to TTFB and the download itself, and each delay is a small fraction.

1. **TTFB:** static generation or edge caching for HTML; a CDN; avoid redirect chains; keep server work off the critical path.
2. **Load delay:** make the LCP image discoverable in the HTML (an `img` element, not a CSS background or a client-rendered component); add `fetchpriority="high"`; never `loading="lazy"` on it; preload it only if it is discovered late: `<link rel="preload" as="image" imagesrcset="..." imagesizes="..." fetchpriority="high">`.
3. **Load duration:** AVIF or WebP at the right size via `srcset` and `sizes`; an image CDN with automatic format negotiation.
4. **Render delay:** no render-blocking JavaScript in the head (`defer` or `type="module"`); inline critical CSS; avoid hiding the hero behind a client-side A/B test or an entrance animation that starts at opacity 0.
5. **Text LCP:** if the LCP is a headline, the web font matters: preload it and use `font-display: swap` with metric-matched fallbacks.

## INP: what to do

- Keep the main thread free: split work into tasks under 50 ms; yield to the browser in long handlers (`scheduler.yield()` where supported, falling back to `setTimeout`).
- Ship less JavaScript: islands architecture (Astro) or server components; hydrate only interactive parts; remove unused libraries.
- Give immediate visual feedback in the event handler (pressed state), then do the heavy work.
- Debounce input handlers (search-as-you-type 200-300 ms); virtualize long lists.
- Avoid layout thrashing (reading layout after writing styles in a loop); use `content-visibility: auto` for long off-screen sections.
- Animate only `transform` and `opacity`.
- Audit third parties: chat widgets, A/B testing tools, tag managers and session replay are frequent INP problems.

## CLS: what to do

- `width` and `height` (or CSS `aspect-ratio`) on every image, video and iframe.
- Reserve space for ads, embeds, cookie banners and late content; overlay banners rather than pushing content down.
- Fonts: metric-matched fallbacks (`size-adjust`, `ascent-override`, `descent-override`, `line-gap-override`), generated by tools such as Fontaine or the framework's font tooling (Next.js `next/font`, Astro's fonts API).
- Never insert content above existing content unless the user asked for it.
- Skeletons that match the final layout.
- Animations with `transform`, not `top`, `height` or `margin`.

## Images

- Formats, `srcset`, `sizes` and art direction: see [responsive and fluid](responsive-and-fluid.md).
- Lazy-load everything below the first viewport (`loading="lazy"`), never the LCP image.
- Use an image CDN or build-time pipeline (Astro `<Image>`/`<Picture>`, Next.js `<Image>`, Cloudinary, Imgix) to generate sizes and formats automatically.
- Video: no autoplaying hero video on mobile data unless it is the product; a `poster` image, `preload="none"` or `"metadata"`, muted, `playsinline`, and a pause control. Compress to the smallest acceptable bitrate; use streaming (HLS) for long video.
- Third-party video embeds: use a facade (a static thumbnail with a play button that loads the player on click, as in `lite-youtube-embed`).

## Fonts

- WOFF2 only; self-host from the same origin when the license allows.
- Subset to the scripts you need (`unicode-range`), and drop unused weights; a variable font replaces 3 or more static weights.
- Preload at most 1-2 critical fonts (`<link rel="preload" as="font" type="font/woff2" crossorigin>`).
- `font-display: swap` for headings and body with metric-matched fallbacks; `optional` when CLS matters more than brand type on slow connections.
- Limit to 2 families. The `typography` skill handles selection and licensing.

## Third-party scripts

- Keep an inventory: vendor, purpose, owner, pages, size, consent category, and the date it was last reviewed. Remove what nobody owns.
- Load with `async` or `defer`, after consent where consent is required, and after the main content where possible.
- Facades for chat widgets, maps and video until the user interacts.
- `preconnect` to at most 2-3 critical third-party origins.
- Tag manager governance: no one-off tags without review; check total cost quarterly.
- Off-main-thread options (web workers via tools like Partytown) can help but break some scripts; test carefully.

## Caching and delivery

- Fingerprinted static assets: `Cache-Control: public, max-age=31536000, immutable`.
- HTML: short caching with revalidation, or edge caching with purge on deploy.
- Compression: Brotli for text assets; HTTP/2 or HTTP/3.
- Back/forward cache: avoid `unload` handlers and `Cache-Control: no-store` on HTML where possible, so Back is instant.
- Speculation Rules (Chromium) can prerender likely next pages; use conservative settings and exclude pages with side effects.

## Design-stage checklist

- [ ] LCP element marked on each template, with its weight budget.
- [ ] Fonts chosen with weights and subsets counted.
- [ ] Video and animation choices justified, with reduced-motion and low-data alternatives.
- [ ] Third-party tools listed with consent categories.
- [ ] Space reserved for every async element (banners, embeds, ads, chat).
- [ ] Interactions that need heavy JavaScript identified and alternatives considered.

## Verification

- Lighthouse on mobile for every template in CI, with budget assertions.
- WebPageTest on a mid-range Android device and a 4G profile for key pages.
- RUM with `web-vitals` reporting LCP, INP and CLS with attribution (which element, which interaction).
- CrUX and Search Console Core Web Vitals report 28 days after launch, and monthly thereafter.
