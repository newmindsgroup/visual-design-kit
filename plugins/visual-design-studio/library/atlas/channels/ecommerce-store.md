---
id: channel.ecommerce-store
axis: channel
name: E-commerce Store
aliases: [online store, webshop, shop, storefront, dtc store, product page, checkout, shopify store]
summary: Online stores where product imagery, price clarity, trust and a short path to checkout drive revenue; every screen is judged on add-to-cart and completed orders.
tags: [ecommerce, pdp, product page, checkout, cart, catalog, conversion, merchandising, shopify, retail]
pairs_with: [style.editorial-magazine, style.quiet-minimal, style.flat-material, style.handcrafted-organic, industry.ecommerce-dtc, industry.fashion-apparel, industry.beauty-cosmetics, industry.food-beverage-cpg, tier.mid-market, archetype.everyperson]
avoid_with: [style.kinetic-experimental-type, style.web-brutalist, audience.low-bandwidth-entry-devices]
version_timestamp: 2026-10-20 02:01:01 UTC
---

# E-commerce Store

## Formats and specs

Marketplace and platform image rules change; confirm against Shopify, Amazon Seller Central (Product image style guide), Google Merchant Center and the store platform's current documentation before shooting. Figures below are as of 2026.

| Item | Spec | Notes |
| --- | --- | --- |
| Product image ratio | 1:1 or 4:5 (portrait) consistent across the catalog | Fix one ratio; mixed ratios break grids |
| Product image size | 2048x2048 px master (Shopify guidance; platform limits vary, about 4,500-5,000 px and 20 MB, verify); minimum 1000 px on the longest side for zoom | Export 1600-2400 px; serve responsive sizes |
| Formats | JPEG (quality 75-85) or WebP/AVIF delivered through the platform CDN; PNG only for graphics | sRGB |
| Amazon main image | Pure white background (RGB 255,255,255), product fills about 85% of the frame, 1000 px or more on the longest side (1600+ recommended), no text or badges | Verify per category in Seller Central |
| Gallery | 5-8 images: hero, angle, detail, scale or in-use, packaging, size or fit, lifestyle; add one short video (10-30s) | Consistent lighting and crop |
| Color accuracy | Shoot with a color target; calibrate; show swatches as photographed product, not flat hex | Returns drop when color matches |
| Core Web Vitals | LCP 2.5s or less (product image is usually the LCP element), INP 200ms or less, CLS 0.1 or less at p75 | Reserve image space with aspect-ratio |
| Product title and URL | Title 60-70 chars visible in results; descriptive URL slug | Structured data (Product, Offer, AggregateRating) |
| Buttons and targets | Add to cart 48-56px high, full width on mobile; 44px+ for variant chips | Sticky add-to-cart bar on mobile |
| Checkout | Guest checkout, address autocomplete, express wallets (Apple Pay, Google Pay, PayPal, Shop Pay), 1-page or 3-step flow | Show total cost before payment |

## Structure and hierarchy

- **Architecture:** home, category or collection pages, search, product detail page (PDP), cart, checkout, account and order tracking, help and returns. Navigation by shopping task (category, occasion, gender, concern), with search always visible.
- **Listing pages:** 2 columns mobile, 3-4 desktop; card shows image, name, price, rating and key variant cue; filters as a left rail or a bottom sheet with active-filter chips; sort options clear; show result count and pagination or "load more" with position retention.
- **PDP order (above the fold):** image gallery, title, price (and compare-at price), rating count, variant selectors with stock state, primary CTA, delivery estimate and return policy line, trust badges. Below: description, specs, size guide, reviews, Q&A, related products.
- **Cart and checkout:** persistent mini-cart, edit quantity, shipping threshold progress, promo field collapsed. Checkout: contact, delivery, payment, review; order summary visible; errors inline; each step shows total and next action.
- **Trust:** return and shipping policy visible before checkout, secure payment marks, real reviews with dates and verified labels, contact route, tax and duty clarity.
- **Merchandising hierarchy:** one hero per page; promotional banners limited to one primary and one secondary per screen.

### Checkout form defaults

- Ask for email first, then delivery; offer guest checkout and invite account creation after purchase.
- Use correct `autocomplete` tokens (`shipping address-line1`, `postal-code`, `cc-number`) and `inputmode="numeric"` for card and postcode fields; inputs 16px+ to avoid mobile zoom.
- Address: country first, then fields in local order; autocomplete via a verified address service; phone optional unless required for delivery.
- Payment: wallets above the card form; card fields in the provider's hosted fields; accepted marks visible.
- Validation on blur with specific messages ("Postcode needs 5 digits"), never clearing entered data; focus the first invalid field on submit.
- Show delivery options with a date range and price ("Arrives Tue-Fri, free over $50"); show the final total, tax and shipping before the pay button.
- Confirmation page: order number, summary, delivery estimate, receipt email promise, next-step links.

## Craft defaults

- Photography does the selling: consistent background, light direction and crop; spend the budget on hero and detail shots first. Provide scale references; show texture and fit.
- Price: largest numeric element after the product image; sale price in the accent color with compare-at price struck through and a text label ("Sale") so color is not the only cue; show currency symbol and tax treatment (EU/UK shoppers expect VAT-inclusive consumer prices).
- Typography: a clear UI sans for product data (16px minimum body); tabular numerals for prices; brand display font on hero and editorial blocks only.
- Variant selectors: swatches with text labels, disabled out-of-stock states with "notify me", size charts in a sheet. Never reset selections after errors.
- Motion: 150-250ms; image zoom and gallery swipe feel immediate; subtle add-to-cart confirmation (cart badge bump, mini-cart slide) with reduced-motion fallback.
- Avoid dark patterns: no fake countdowns, pre-checked add-ons, hidden fees or confirm-shaming.

## Production and handoff

- Platforms: Shopify (Liquid or Hydrogen), BigCommerce, Adobe Commerce, WooCommerce or composable stacks. Design within the platform's theme and checkout customization limits; checkout is often locked to a hosted flow. The `web-design` skill covers performance, SEO and accessibility; `ui-design` covers pricing and checkout patterns.
- Provide a photography shot list, retouch guide and naming convention (SKU_angle_variant.jpg), plus a templated PDP, collection, cart and email set.
- Handle edge states: out of stock, backorder, pre-order, bundle, subscription, gift card, B2B pricing, long product names, 200+ variants, free-shipping thresholds.
- Instrument events (view item, add to cart, begin checkout, purchase) and A/B test hypotheses on one change at a time.
- Law and compliance: consumer-rights rules (EU withdrawal right and price-reduction indication under the Omnibus Directive, UK Consumer Rights Act), the US FTC rule on fake reviews and testimonials (2024), accessibility (ADA litigation risk; the European Accessibility Act covers e-commerce services in the EU from June 2025), PCI DSS via hosted payment fields, cookie consent. Confirm requirements with counsel for the markets served.

## QA checklist

- [ ] Product images pass the ratio, resolution and white-background rules of every marketplace used.
- [ ] Mobile PDP: CTA, price and delivery visible without scrolling past two screens; sticky CTA works with keyboard open.
- [ ] Out-of-stock, sold-out variant, error, empty cart, and failed payment states designed.
- [ ] Checkout completes with keyboard only and with a screen reader; autofill works.
- [ ] Prices consistent across list, PDP, cart, checkout and email; tax and shipping shown before payment.
- [ ] LCP image is not lazy-loaded; layout does not shift when reviews or recommendations load.
- [ ] Reviews, badges and urgency claims are truthful and verifiable.
- [ ] Order confirmation, shipping and return emails match the brand.

## Reference anchors

- Baymard Institute checkout and product page usability research (baymard.com)
- Shopify Polaris and Shopify theme documentation; Google Merchant Center product data specifications
- Amazon Seller Central image style guide (as a rule set, not a visual model)
- Aesop, Glossier, Allbirds, IKEA and Nike store experiences as widely cited benchmarks for product storytelling and merchandising
- Nielsen Norman Group e-commerce usability reports
