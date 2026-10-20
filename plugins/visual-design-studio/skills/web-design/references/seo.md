# SEO

Version-Timestamp: 2026-10-20 02:04:32 UTC

Search engines reward pages that answer a real query well, load fast and are easy to crawl. Design decisions (headings, URLs, content depth, rendering, internal links) matter as much as metadata. Google's own documentation (developers.google.com/search) is the owning source; search features change often, so check it before promising a rich result.

## Semantic HTML

- One `h1` per page that states the topic; `h2`-`h4` in order without skipping levels for styling.
- Landmarks: `header`, `nav`, `main`, `article`, `aside`, `footer`.
- Real links (`a href`) for navigation, not click handlers on `div`s; crawlers follow `href`.
- Descriptive link text ("Compare pricing plans"), never "click here".
- `img` with meaningful `alt`; decorative images `alt=""`.
- `lang` on the `html` element; `time datetime` for dates; lists for lists; tables for tabular data.
- Content in HTML at first load (static or server-rendered). Google renders JavaScript, but later and less reliably; many other crawlers, including most AI crawlers, do not run JavaScript at all.

## Titles and meta descriptions

| Element | Default | Notes |
| --- | --- | --- |
| `title` | Unique per page, about 50-60 characters; primary topic first, brand last: "Payroll software for restaurants - Acme" | Google truncates by pixel width and may rewrite titles that do not match the page |
| Meta description | Unique, about 120-160 characters; summarizes the page and gives a reason to click | Not a ranking factor; Google often rewrites it from page content |
| Homepage title | Brand plus what you do: "Acme - Payroll for restaurants and cafes" | |
| Headings | `h1` close to the title wording; `h2`s as scannable answers to sub-questions | |

Templates in a CMS: generate titles from fields (`{product name} - {category} | {brand}`) with a manual override.

## URLs

- Lowercase, hyphen-separated, short, readable and stable: `/guides/restaurant-payroll/`.
- No session IDs or tracking parameters in canonical URLs; no dates unless the content is dated.
- One trailing-slash policy, enforced with redirects.
- Changing URLs needs 301 redirects from every old URL (see [launch checklist](launch-checklist.md)).

## Structured data (schema.org JSON-LD)

Google recommends JSON-LD. Mark up only what is visible on the page, and validate with Google's Rich Results Test and the Schema Markup Validator.

| Page | Types |
| --- | --- |
| Homepage | `Organization` (name, url, logo, sameAs social profiles, contactPoint), `WebSite` |
| Every page in a hierarchy | `BreadcrumbList` |
| Blog post or article | `Article` or `BlogPosting` (headline, author with url, datePublished, dateModified, image) |
| Product page | `Product` with `Offer` (price, priceCurrency, availability) and `AggregateRating` or `Review` only when real reviews are shown on the page |
| Local business | `LocalBusiness` subtype with address, geo, openingHours, telephone |
| Event | `Event` with startDate, location, offers, eventStatus |
| Software product | `SoftwareApplication` with offers and ratings when shown |
| Video | `VideoObject` with thumbnail, uploadDate, duration |

Google limited FAQ rich results to well-known authoritative government and health sites and removed How-to rich results in 2023; `FAQPage` markup is still valid schema but rarely produces a rich result.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Acme Payroll",
  "url": "https://www.example.com/",
  "logo": "https://www.example.com/images/logo-512.png",
  "sameAs": ["https://www.linkedin.com/company/example", "https://www.instagram.com/example"],
  "contactPoint": { "@type": "ContactPoint", "contactType": "customer support", "email": "help@example.com" }
}
</script>
```

## Crawling and indexing

- **robots.txt** controls crawling, not indexing. Do not block CSS or JavaScript. Reference the sitemap: `Sitemap: https://www.example.com/sitemap.xml`.
- **noindex** (meta robots or `X-Robots-Tag` header) keeps a page out of results; the page must remain crawlable for the tag to be seen.
- **XML sitemaps:** only canonical, indexable 200-status URLs; each file at most 50,000 URLs or 50 MB uncompressed, combined with a sitemap index; accurate `lastmod`. Submit in Google Search Console and Bing Webmaster Tools.
- **Status codes:** 200 for real pages, 301 for permanent moves, 404 or 410 for removed content, never a "soft 404" (a 200 page saying "not found").
- **Pagination:** plain linked pages with unique URLs; each page self-canonical (Google no longer uses `rel="next"`/`"prev"` as a signal).
- **Faceted navigation:** prevent infinite filter combinations from being crawled (canonical to the main listing, or `noindex` on low-value combinations, and avoid linking every combination).

## Canonicals

- Every indexable page has a self-referencing absolute canonical: `<link rel="canonical" href="https://www.example.com/guides/restaurant-payroll/">`.
- Duplicates (tracking parameters, print versions, sort orders) point to the main URL.
- Canonical, sitemap, internal links and hreflang all use the same version of each URL (protocol, host, trailing slash).
- Prefer 301 redirects over canonicals when the duplicate does not need to exist (http to https, non-www to www).

## International sites and hreflang

- URL structure: subdirectories (`/de/`, `/fr-ca/`) are simplest to manage; ccTLDs give the strongest country signal; avoid automatic redirects based on IP or browser language, and offer a visible language switcher instead.
- `hreflang` values are ISO 639-1 language codes with optional ISO 3166-1 alpha-2 region codes: `en`, `en-GB`, `pt-BR`, `es-419` (Latin American Spanish).
- Each language version lists all versions including itself, and links must be reciprocal; add `x-default` for the fallback or selector page.
- Implement in the HTML head, HTTP headers (for PDFs) or the XML sitemap; pick one method.

```html
<link rel="alternate" hreflang="en-us" href="https://www.example.com/en-us/pricing/">
<link rel="alternate" hreflang="en-gb" href="https://www.example.com/en-gb/pricing/">
<link rel="alternate" hreflang="de" href="https://www.example.com/de/preise/">
<link rel="alternate" hreflang="x-default" href="https://www.example.com/pricing/">
```

- Translate titles, descriptions, URLs (slugs) and structured data, not only body copy. The `web-localization` deep process covers the rest.

## Open Graph and social cards

```html
<meta property="og:type" content="website">
<meta property="og:site_name" content="Acme Payroll">
<meta property="og:title" content="Payroll software for restaurants">
<meta property="og:description" content="Run payroll in 10 minutes a week, with tips and shifts handled.">
<meta property="og:url" content="https://www.example.com/">
<meta property="og:image" content="https://www.example.com/og/home-1200x630.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Acme payroll dashboard showing this week's shifts">
<meta name="twitter:card" content="summary_large_image">
```

- Image 1200x630px (1.91:1), PNG or JPEG, ideally under about 1 MB, with key text inside a central safe area because some platforms crop to square or 2:1.
- Generate per-page OG images from a template (title, brand, image) at build time.
- Check with each platform's debugger (Facebook Sharing Debugger, LinkedIn Post Inspector) before launch; platforms cache aggressively. Specs change; confirm current sizes on each platform.

## Content and internal linking

- One page per distinct search intent; merge thin, overlapping pages.
- Answer the query early on the page, then go deep; use descriptive `h2`s that match sub-questions.
- Link related pages with descriptive anchor text; important pages get links from the navigation and from relevant content.
- Show authors, dates and sources on informational content (signals of experience, expertise, authoritativeness and trust in Google's quality rater guidelines).
- Avoid intrusive interstitials on mobile that cover content on arrival.

## Page experience signals

Core Web Vitals (see [performance](performance.md)), HTTPS, mobile-friendly responsive design, and no intrusive interstitials are part of Google's page experience guidance. They rarely outrank relevance, but they decide close calls and affect conversion regardless.

## AI search and crawlers (volatile, as of 2026)

- Google states that pages eligible for normal search are eligible for its AI features; no special markup is required.
- AI crawlers identify themselves in robots.txt user agents (for example GPTBot, ClaudeBot, Google-Extended for Gemini training); decide per client whether to allow them, and document the choice.
- `llms.txt` is a community proposal, not a standard that major search engines have committed to; treat it as optional.
- Server-rendered, well-structured HTML with clear headings, facts and sources is the best preparation for every kind of crawler.

## Measurement

- Google Search Console: coverage and indexing, Core Web Vitals, queries and click-through rate per page, sitemaps, manual actions.
- Bing Webmaster Tools for Bing and the services that use its index.
- Track organic landing pages and conversions in analytics; annotate releases and migrations.
