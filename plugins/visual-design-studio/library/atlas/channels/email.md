---
id: channel.email
axis: channel
name: Email
aliases: [email design, newsletter, html email, email campaign, transactional email, email template, edm]
summary: HTML email built for inconsistent clients (Outlook, Gmail, Apple Mail) and dark mode, where a single column, tested code, one clear CTA and small file size beat visual ambition.
tags: [email, newsletter, html email, outlook, gmail, dark mode, transactional, template, deliverability, mjml]
pairs_with: [style.editorial-magazine, style.corporate-modern, style.flat-material, style.quiet-minimal, industry.ecommerce-dtc, industry.saas-b2b, industry.fashion-apparel, industry.nonprofit-ngo, archetype.sage, archetype.everyperson]
avoid_with: [style.glass-spatial, style.kinetic-experimental-type, style.soft-ui-neumorphic]
version_timestamp: 2026-10-20 02:01:01 UTC
---

# Email

## Formats and specs

Email client behavior changes quietly. Values are as of 2026; verify support at caniemail.com and test in real clients (Litmus, Email on Acid) before every template release.

| Item | Spec | Notes |
| --- | --- | --- |
| Container width | 600px (600-640px range) centered; fluid below 480px; single column on mobile | Desktop preview panes can be narrower than 600 |
| Gmail clipping | Gmail clips messages whose HTML exceeds about 102 KB and shows "[Message clipped]" | Figure comes from ESP documentation, not Google's own help; counts HTML only (including tracking links and inline CSS), not image files. Target under 80-100 KB |
| Body text | 16px (14px minimum), line-height 1.5; web-safe stack with brand font as progressive enhancement | iOS Mail enlarges text under about 13px unless text-size-adjust is set |
| Buttons | 44-48px tall, 16px+ text, "bulletproof" HTML (padding on a table cell or link), VML fallback for classic Outlook | Never image-only buttons |
| Images | 2x resolution (1200px wide for a 600px slot); JPG for photos, PNG for transparency and flat art; GIF for simple animation; avoid WebP and SVG for compatibility | Always set width, height, alt, and `display: block` |
| Animated GIF | Under 1 MB (ideally 500 KB), 10-15 fps, first frame carries the message | Older desktop Outlook for Windows (2007-2016) shows only the first frame; newer versions vary, so test in the client mix you target |
| Color | sRGB; hex colors; test dark mode | Apple Mail, Outlook and Gmail apps invert or re-map colors in different ways |
| Subject and preheader | Subject about 30-50 characters (mobile shows roughly 30-40); preheader 40-100 characters | Control preheader text; pad it so body copy does not leak into previews |
| Layout code | Nested tables, inline CSS, `role="presentation"`, `lang` attribute | Classic Outlook for Windows uses the Word rendering engine and Microsoft supports it to at least 2029 (verify); the new Outlook uses a web-based engine |
| Sender requirements | SPF, DKIM, DMARC; one-click unsubscribe (RFC 8058); low spam-complaint rate | Gmail and Yahoo bulk-sender rules from 2024 (verify current thresholds) |
| Fonts | Web fonts work in Apple Mail and iOS Mail; Gmail and Outlook fall back | Pick a fallback stack with similar metrics |

## Structure and hierarchy

- **One email, one job:** a single primary CTA, repeated at most twice. Secondary links sit lower and read as text links.
- **Inverted pyramid:** logo 120-180px wide (not a large banner), headline 24-32px, one-sentence lead, hero image or product block, supporting modules, CTA, footer. The main message and CTA appear within the first 600px of height.
- **Module library:** build 8-12 reusable modules (header, hero, text, feature row 2-up and 3-up stacking on mobile, product grid, testimonial, CTA band, footer) so campaigns assemble without redesign.
- **Transactional vs marketing:** receipts, password resets and notices use plain structure, clear subject lines and prominent key data (order number, amount, date). Marketing may carry imagery and promotion. Never hide required legal copy in an image.
- **Length:** newsletters can scroll three to five screens; promotional emails stay under two. Put "view in browser" and an accessible plain-text part in every send.

### Type and spacing for a 600px template

| Element | Spec |
| --- | --- |
| Headline (H1) | 28-32px, line-height 1.2, weight 700 |
| Subhead (H2) | 20-24px, line-height 1.25 |
| Body | 16px, line-height 1.5, color at 4.5:1 or better |
| Small print and footer | 12-13px, line-height 1.4, never below 4.5:1 |
| Button | 16px bold, padding 14-16px vertical and 24-32px horizontal, radius 4-8px |
| Content padding | 24-40px between modules; 20-24px side padding (16px on mobile) |
| Hero image | 600px slot (1200px asset) under 200 KB; the image file does not count toward Gmail's HTML limit, but its URL does |
| Logo | 120-180px wide, with alt text and a text fallback color |

## Craft defaults

- Use live text for everything important; images with text must carry alt text and the email must still make sense with images blocked (many clients block by default).
- Contrast 4.5:1 for text, 3:1 for buttons against the background; underline links in body copy; do not rely on color for links.
- Dark mode: use transparent PNGs with a light stroke or glow for logos, avoid pure white image backgrounds, set `<meta name="color-scheme" content="light dark">` and `@media (prefers-color-scheme: dark)` overrides where supported, and test the forced-inversion path (Outlook, Gmail apps).
- Spacing: 24-40px between modules, 16px padding at mobile edges, 8px base grid. Keep rows to 1-2 columns on desktop; stack on mobile with `width: 100%` fluid tables.
- Limit to 1-2 typefaces (a web-safe fallback plus one brand face) and 3-4 type sizes.
- Motion is a bonus, never the carrier of information. Avoid AMP for Email unless the use case demands it.
- Voice: front-load the first 40 characters of the subject line and preheader; avoid all caps, excess punctuation and spam-trigger phrasing.

## Production and handoff

- Build with MJML, Maizzle or React Email, or in the ESP's editor (Mailchimp, Klaviyo, Braze, HubSpot, Customer.io); compile to inlined HTML. Provide Figma frames at 600px and 375px mobile, plus dark-mode previews.
- Host images on a CDN with absolute HTTPS URLs; slice minimal images; compress with Squoosh or ImageOptim; tag links with UTM parameters consistently.
- Dynamic content needs fallbacks for empty fields and long names; define character limits for subject, preheader, headline and button.
- Run seed-list and client-rendering tests, link checks and spam-score checks; validate accessibility: heading order, alt text, `lang`, plain-text alternative.
- Law and consent: CAN-SPAM (US: physical address, working unsubscribe honored within 10 business days, honest headers), GDPR and ePrivacy (EU and UK consent), CASL (Canada). Apple Mail Privacy Protection inflates open rates, so judge by clicks and conversions. Confirm requirements with counsel for the markets served.
- The `print-packaging-social` skill covers email production in more depth.

## QA checklist

- [ ] HTML weight under 100 KB (target 80 KB) so Gmail does not clip; test with real merge data.
- [ ] Renders in classic Outlook for Windows, new Outlook, Outlook for Mac, Gmail web and app, Apple Mail, iOS Mail, Yahoo and at least one Android client.
- [ ] Dark mode checked in Apple Mail, Gmail app and Outlook; logos legible.
- [ ] Images off: message, CTA and offer are still understood; alt text present.
- [ ] Links, UTM tags, unsubscribe and view-in-browser work; preheader is intentional.
- [ ] Mobile: single column, 16px text, 44px buttons, no horizontal scroll.
- [ ] Authentication (SPF, DKIM, DMARC) passes; plain-text part present.
- [ ] Screen reader pass: reading order, headings, descriptive link text.

## Reference anchors

- caniemail.com for client CSS and HTML support
- MJML (mjml.io), Maizzle and React Email documentation
- Litmus and Email on Acid blogs on dark mode and Outlook rendering; Really Good Emails for gallery inspiration
- Google Workspace and Yahoo sender guidelines; RFC 8058 (one-click unsubscribe)
- Email Markup Consortium accessibility reports on email
