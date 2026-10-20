# Launch checklist

Version-Timestamp: 2026-10-20 02:04:32 UTC

Run this on the production build at the production URL (or an identical staging environment) before announcing anything. Record each check as passed, failed or not applicable, with the evidence. A failed check is fixed or explicitly accepted by the client; it is never marked passed. The deep process for client launches is the [release draft skill](../../../library/draft-skills/design-web-release/SKILL.md).

## Content

- [ ] No placeholder content: search the build for "lorem", "ipsum", "TODO", "TBD", "example.com", "Your Name", "{{", "xxx".
- [ ] Every page proofread; names, prices, dates, phone numbers and addresses checked against the source.
- [ ] Every image has correct alt text (or `alt=""` if decorative); no unlicensed stock or AI images with visible artifacts.
- [ ] All internal and external links work (run a crawler such as Screaming Frog or a link checker).
- [ ] Forms submit, arrive at the right inbox or CRM, send the confirmation message, and show success and error states.
- [ ] Legal and regulated claims (pricing, guarantees, testimonials, health or financial statements) approved by the client.

## Cross-browser and devices

- [ ] Latest two versions of Chrome, Safari (macOS and iOS), Firefox and Edge; Samsung Internet if analytics shows Android traffic.
- [ ] A real iPhone and a mid-range Android phone, not only emulators.
- [ ] Widths 320, 375, 390, 768, 1024, 1280, 1440 and 1920px; landscape on phones and tablets.
- [ ] Light and dark mode if supported; print styles for pages people print (recipes, invoices, articles).
- [ ] Sticky headers, menus, modals and carousels work with touch, mouse and keyboard.

## Accessibility (WCAG 2.2 AA)

- [ ] axe-core (browser extension or CI) on every template and key state: zero critical and serious issues.
- [ ] Keyboard only: every link, button, menu, form, modal and carousel works; focus is always visible and never hidden under sticky UI or the cookie banner; no traps; logical order; skip link works.
- [ ] Screen reader pass: VoiceOver with Safari (macOS or iOS) and NVDA with Firefox or Chrome on the homepage, a content page, a form and the main conversion flow.
- [ ] 200% text zoom and 400% browser zoom (reflow at 320px) without loss of content.
- [ ] Contrast of all text and UI states; information not conveyed by color alone.
- [ ] `prefers-reduced-motion` respected; autoplaying motion over 5 seconds can be paused.
- [ ] Videos captioned; audio has transcripts.
- [ ] Page `lang` set; unique page titles; one `h1`; heading order logical.
- [ ] Accessibility statement published where required (EU public sector; services in scope of the European Accessibility Act).

Full criteria: `ui-design` [accessibility](../../ui-design/references/accessibility.md).

## Performance

- [ ] Lighthouse mobile on every template: no regressions against the budgets in [performance](performance.md).
- [ ] LCP element identified per template, not lazy-loaded, `fetchpriority="high"`, served as AVIF or WebP at the right size.
- [ ] Fonts self-hosted WOFF2, subset, at most 1-2 preloaded.
- [ ] Third-party scripts load after consent and do not block rendering; chat, video and map embeds use facades.
- [ ] Caching headers: fingerprinted assets immutable for a year; HTML short or revalidated.
- [ ] RUM (`web-vitals`) installed so field data starts on day one.

## SEO

- [ ] Staging `noindex` and password protection removed from production; robots.txt allows crawling and lists the sitemap.
- [ ] Unique `title` and meta description on every indexable page.
- [ ] Self-referencing absolute canonicals; `hreflang` complete and reciprocal on multilingual sites.
- [ ] XML sitemap with only canonical 200-status URLs; submitted in Google Search Console and Bing Webmaster Tools.
- [ ] Structured data validated in the Rich Results Test (Organization, BreadcrumbList, Article or Product as relevant).
- [ ] Search Console property verified (domain property preferred) before launch day.

Details: [SEO](seo.md).

## Redirects (redesigns and migrations)

- [ ] Redirect map from every old URL with traffic, backlinks or rankings to the most relevant new URL (export old URLs from the old sitemap, analytics and Search Console).
- [ ] 301 (permanent) redirects, one hop only, no chains or loops.
- [ ] Protocol and host normalized: http to https, one of www or non-www, one trailing-slash policy.
- [ ] Old PDFs, images and campaign URLs handled.
- [ ] After launch: monitor 404s in server logs and Search Console daily for two weeks and add missing redirects.

## Error pages

- [ ] 404 page returns HTTP 404 (not 200), keeps the site header and footer, explains in plain words, and offers search, the top destinations and a contact route.
- [ ] 500 and maintenance pages exist, are lightweight and do not depend on the failing system.
- [ ] Form error, payment failure and offline states tested.

## Favicons and app icons

```html
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/manifest.webmanifest">
<meta name="theme-color" content="#0b5f66">
```

- [ ] `favicon.ico` 32x32 for legacy browsers; `icon.svg` for modern ones (it can switch colors with `prefers-color-scheme`); `apple-touch-icon.png` 180x180 with a solid background; manifest icons at 192x192 and 512x512, plus a 512x512 maskable icon with the mark inside the central safe zone.
- [ ] Icons are legible at 16px: simplify the logo to a mark if needed (the `brand-identity` skill covers small-size variants).
- [ ] `theme-color` matches the brand surface (the value above is an example).

## Open Graph and social previews

- [ ] Every page has `og:title`, `og:description`, `og:url`, `og:image` (1200x630) and `twitter:card` set to `summary_large_image`.
- [ ] Per-page OG images for key pages and articles, with text in the safe central area.
- [ ] Checked in the Facebook Sharing Debugger and LinkedIn Post Inspector; caches refreshed after fixes.

## Analytics and measurement

- [ ] Analytics fires on every page, respects consent, and excludes internal traffic.
- [ ] Conversion events (form submit, sign-up, purchase, demo booked, key clicks) fire once each and carry useful parameters.
- [ ] UTM conventions documented for campaigns.
- [ ] Consent Mode or equivalent signals pass correctly where Google tags are used.
- [ ] A dashboard with the agreed KPIs exists and the client can open it.

## Legal and compliance pages

Confirm requirements with counsel for the specific business and jurisdiction.

- [ ] Privacy policy matching the actual data collection, tools and retention.
- [ ] Cookie policy and a footer link that reopens cookie settings; banner tested with "Reject all" (no non-essential tags fire).
- [ ] Terms of use or terms of sale; returns and refund policy for stores.
- [ ] Imprint (Impressum) with legally required provider details for sites aimed at Germany and Austria.
- [ ] Company details where required (for UK companies: registered name, number and registered office).
- [ ] Accessibility statement where required (see above).
- [ ] Opt-out links ("Do Not Sell or Share My Personal Information") and Global Privacy Control handling where US state laws apply.

## Security

Response headers (check with Mozilla HTTP Observatory or securityheaders.com):

| Header | Starting value | Notes |
| --- | --- | --- |
| `Strict-Transport-Security` | `max-age=63072000; includeSubDomains` | Add `preload` only after every subdomain serves HTTPS |
| `Content-Security-Policy` | `default-src 'self'; script-src 'self' 'nonce-...'; object-src 'none'; base-uri 'self'; frame-ancestors 'self'; upgrade-insecure-requests` | Start with `Content-Security-Policy-Report-Only`, add each third party deliberately, then enforce |
| `X-Content-Type-Options` | `nosniff` | |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | |
| `Permissions-Policy` | `camera=(), microphone=(), geolocation=()` | Allow only features the site uses |
| `X-Frame-Options` | `SAMEORIGIN` | Legacy fallback for `frame-ancestors` |

- [ ] HTTPS everywhere with automatic certificate renewal; no mixed content.
- [ ] Cookies set by the site use `Secure`, `HttpOnly` where possible, and `SameSite=Lax` or stricter.
- [ ] Forms protected against spam (honeypot field, rate limiting, or an accessible challenge such as Cloudflare Turnstile), with server-side validation.
- [ ] Admin and CMS logins use strong authentication (passkeys or MFA); default accounts removed.
- [ ] Dependencies and plugins updated; no secrets in client bundles or the repository.
- [ ] `/.well-known/security.txt` with a contact for vulnerability reports (RFC 9116).

## Operations

- [ ] DNS TTL lowered 24-48 hours before cutover; records documented; email (MX, SPF, DKIM, DMARC) untouched or re-verified.
- [ ] Backups (code, content, CMS database, media) and a tested restore.
- [ ] Rollback plan: previous deployment can be restored in minutes; who decides and how.
- [ ] Uptime monitoring and error tracking with alerts to a named person.
- [ ] Client handover: editor guide, logins transferred, support terms.

## After launch

| When | Check |
| --- | --- |
| Launch day | Smoke test all key flows on production; forms and analytics events arrive; no 5xx errors |
| First week | 404s and redirects; Search Console coverage and sitemap processing; consent rates; conversion baseline |
| Day 28 | Core Web Vitals field data in CrUX and Search Console at p75; organic traffic against the pre-launch baseline |
| Quarterly | Third-party script audit, accessibility regression pass, content freshness, dependency updates |

Ongoing improvement follows the [maintenance draft skill](../../../library/draft-skills/design-web-maintenance/SKILL.md).
