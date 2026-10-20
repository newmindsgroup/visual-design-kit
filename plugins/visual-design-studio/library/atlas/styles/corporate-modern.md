---
id: style.corporate-modern
axis: style
name: Corporate Modern / Enterprise Clean
aliases: [enterprise clean, corporate clean, business modern, b2b clean, enterprise design system, professional modern]
summary: Credible, systematized business design: one deep brand blue, cool neutrals, modular cards, restrained 6-8px radius and product-led imagery; trust through consistency rather than flair.
tags: [corporate, enterprise, b2b, clean, professional, blue, modular, trustworthy, saas]
pairs_with: [industry.saas-b2b, industry.fintech-banking, industry.insurance, industry.legal-professional-services, audience.b2b-buying-committee, archetype.ruler, archetype.sage, tier.mid-market, channel.presentation, channel.marketing-website]
avoid_with: [archetype.outlaw, archetype.jester, audience.children-under-13, industry.gaming-esports, tier.ultra-luxury]
version_timestamp: 2026-10-20 01:57:45 UTC
---

# Corporate Modern / Enterprise Clean

## Essence

Make a large organization look competent, current and safe to buy from. The style is a system more than a look: a controlled palette, a predictable component kit, product screenshots as proof, and copy that states outcomes. Think IBM Carbon, Atlassian, Microsoft Fluent, Workday, ServiceNow. It succeeds when a procurement committee, an engineer and an executive all read the same page as "serious and well run".

## Visual signature

- One brand hue (usually a deep blue, 255-262 in OKLCH hue) used for actions, links and key marks; everything else is cool gray.
- Light canvas, light-gray section bands (`#F4F6F9`), white cards with a 1px border and a very soft shadow.
- Modular layout: 12-column grid, feature rows of 2-4 cards, alternating text/screenshot bands, logo walls, proof numbers.
- Product UI screenshots in a browser or device frame, cropped to the one useful panel, not full-screen thumbnails.
- Sentence-case headings, 2-line maximum; a clear primary and secondary button per section.
- Subtle geometric accent shapes (circles, grid lines, tinted blocks) behind imagery instead of illustration.

## Token recipe

| Token | Value |
| --- | --- |
| Display font | Hanken Grotesk (OFL); Source Serif 4 (OFL) for editorial or analyst-style headlines; commercial: Graphik, Söhne, Aeonik |
| Body font | Source Sans 3 (OFL); Noto Sans (OFL) for multiscript products; commercial: Segoe UI Variable, Söhne Text |
| Mono (code, IDs) | Source Code Pro (OFL) or IBM Plex Mono (OFL) |
| Type scale ratio | 1.200 (minor third) for product UI; 1.250 for marketing pages; clamp display sizes between 36px and 64px |
| Body size / line-height | 16px / 1.5 in UI, 17-18px / 1.55-1.6 for marketing copy; measure 60-72ch |
| Display letter-spacing | -0.01em to -0.02em at 40px+; line-height 1.1-1.15; leave body at 0 |
| Caps / labels | 12-13px, semibold 600, +0.04em; use for eyebrows only, never whole paragraphs |
| Weights | 400 body, 600 UI emphasis and buttons, 700 display; no light (300) below 24px |
| Palette | Ink navy #0E1B2E (oklch 0.22 0.042 258); Brand blue #1B4F9E (oklch 0.44 0.14 259); Brand hover #153F80 (oklch 0.38 0.119 259); Sky tint #E8F0FB (oklch 0.95 0.017 256); Cloud surface #F4F6F9 (oklch 0.97 0.005 258); Slate text #4A5568 (oklch 0.45 0.034 261); Signal teal #0C7C7C (oklch 0.53 0.088 195); Amber #B45309 (oklch 0.56 0.146 49) |
| Accent proportion | Brand blue 5-10% of a page (buttons, links, key icons); teal and amber only for data series or status, never both on one component |
| Radius | 6-8px for buttons, inputs and cards; 12px for large containers; 9999px only for tags and avatars |
| Borders | 1px #D5DBE3 (oklch 0.89 0.013 256) for card edges; input borders #8895A7 (oklch 0.67 0.031 257) so controls meet 3:1 |
| Shadow / elevation | Two levels: `0 1px 2px rgb(14 27 46 / 0.06)` resting, `0 8px 24px rgb(14 27 46 / 0.10)` for menus and modals |
| Spacing density | 8px base; card padding 24px; section spacing 80-112px desktop, 48-64px mobile |
| Grid | 12 columns, max width 1200-1280px, gutter 24px; 8 columns at tablet, 4 at mobile |
| Motion | 150-250ms, cubic-bezier(0.2, 0, 0, 1); fade and 8px translate only; no spring or bounce |

## Composition and layout

- Lead with a plain-language promise, one supporting sentence, one primary action, one secondary link. Put proof (logos, a metric, an analyst badge) directly under the fold.
- Build pages from 5-7 repeatable bands: hero, proof strip, 3-up capabilities, deep feature with screenshot, case study, security/compliance, closing call to action.
- Break the monotony with scale: alternate white and `#F4F6F9` bands, switch card layouts between 3-up and 2-up, and enlarge one metric to 64-96px per page.
- Keep navigation predictable: logo left, 4-6 top-level items, "Contact sales" and a login link right. Mega menus only for 20+ pages.
- App and dashboard views follow the same tokens at 14px density; see `style.data-dense-utilitarian` when tables dominate.

## Imagery and iconography

- Photography: real people at work in real offices or sites, natural light, candid crops. Avoid staged handshakes and glowing-globe stock.
- Product imagery carries the page; redact data and use realistic names, numbers and states, never lorem-like text.
- Icons: 1.5px outline on a 24px grid, rounded joins, one color (ink or brand), used to label capabilities rather than decorate.
- Illustration, when needed: flat geometric spot illustrations in the brand palette plus tints; no 3D blobs.
- Charts use the teal and amber series colors with direct labels; see `style.data-dense-utilitarian` for denser patterns.

## Motion

Quiet and functional. Fade and lift cards 8px on scroll entry (200ms, standard easing), animate hover on cards with a border-color change and shadow step (150ms), and use a 240ms height transition for accordions. Page transitions are cross-fades. Skip parallax, auto-playing carousels and looping hero video. Honor `prefers-reduced-motion` by removing translate and keeping opacity changes under 100ms.

## Fits and risks

- **Fits:** B2B software, fintech and insurance back offices, professional services, HR and payroll platforms, IT consultancies, logistics software, any buyer who needs consensus from many stakeholders (`audience.b2b-buying-committee`). Pairs with `archetype.ruler` and `archetype.sage` because order and expertise are the brand promise.
- **Risks:** it is the most common category look; a competitor in the same space probably looks nearly identical. Differentiate with one owned device (a distinctive accent hue, a signature layout move, an unusual photography crop) and with sharper copy.
- **Wrong for:** `archetype.outlaw` and `archetype.jester` brands, products for children, gaming, and `tier.ultra-luxury`, where polish without personality reads as discount. Consumer-warmth products (restaurants, hospitality) feel institutional in this style.

## Do and don't

- Do define the brand hue in OKLCH once and derive hover, active and tint steps by lightness (0.44, 0.38, 0.95) so contrast stays predictable.
- Do show real product states, specific numbers and named customers; specificity is the trust signal.
- Do keep a single type family pair and let size and weight carry hierarchy.
- Don't use more than two button styles per view or put three equal-weight calls to action in one band.
- Don't stack shadows, gradients and borders on the same card; pick one separator.
- Don't hide pricing, security or compliance pages behind forms when the buyer is evaluating.

## Clichés and AI tells

- Lazy version: Inter on white, an indigo-to-violet gradient hero, centered headline, three identical icon cards with 16px radius and shadow, a floating dashboard mockup with blurred blobs, "Unlock the power of your data".
- Stock "diverse team high-fiving" photography and generic globe or network illustrations.
- Fix: choose a non-default brand hue and name it, use an asymmetric hero (copy left across 5 columns, real product crop right bleeding off the edge), vary card sizes, write the headline as a specific outcome ("Close the month in 3 days"), and replace stock photos with customer sites, product crops or commissioned photography.

## Accessibility notes

- Brand blue #1B4F9E on white is 7.90:1 and on `#F4F6F9` is 7.30:1; white on hover blue #153F80 is 10.22:1. Sky tint with brand text is 6.88:1.
- Slate text #4A5568 is 7.53:1 on white and 6.95:1 on `#F4F6F9`; safe for secondary copy down to 14px.
- Signal teal on white at #0F8A8A is only 4.18:1, so the recipe uses #0C7C7C (5.01:1 on white, 4.63:1 on `#F4F6F9`). Check any lighter accent before putting text on it.
- Decorative card borders (#D5DBE3 on white is 1.39:1) do not count as control boundaries; form fields need the darker #8895A7 border (3.04:1).
- Keep a visible 2px focus ring in brand blue with a 2px offset; enterprise buyers often run accessibility audits (VPAT/ACR) during procurement.

## Reference anchors

- IBM Carbon Design System (carbondesignsystem.com)
- Atlassian Design System and Microsoft Fluent 2
- Salesforce Lightning Design System
- Stripe and Linear marketing pages as higher-craft variants of the same grammar
- *Refactoring UI* (Wathan and Schoger) for systemized spacing, color and hierarchy decisions
