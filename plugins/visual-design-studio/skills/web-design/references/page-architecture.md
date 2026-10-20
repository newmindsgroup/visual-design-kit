# Page architecture

Version-Timestamp: 2026-10-20 02:04:32 UTC

Every page has one job, one primary action and a sequence of sections that answers the visitor's questions in the order they ask them: What is this? Is it for me? Does it work? Can I trust it? What does it cost? What do I do next? Wireframe with real copy; section order is a hypothesis to test, not a template to fill.

## Landing page anatomy

| # | Section | Job | Defaults |
| --- | --- | --- | --- |
| 1 | Header | Orient, offer the CTA | Logo, 0-5 links (none on paid-traffic pages), primary CTA button at the right |
| 2 | Hero | Say what it is, for whom, and the outcome | Headline 6-12 words; one supporting sentence of 15-25 words; primary CTA plus optional secondary text link; a real product visual, demo or proof; risk reducer under the CTA ("No credit card required") |
| 3 | Proof strip | Instant credibility | 4-8 customer logos with permission, or a single specific stat ("Used by 2,400 clinics"), or a rating with source |
| 4 | Problem | Show you understand the situation | 2-3 pains in the customer's words, from research |
| 5 | How it works | Reduce perceived effort | 3 steps with short labels and visuals |
| 6 | Benefits and features | Turn features into outcomes | 3-6 blocks: outcome headline, one-sentence explanation, product visual; alternate media sides sparingly |
| 7 | Deep proof | Convince the skeptic | Testimonial with name, role, company and photo (with consent); a mini case study with a number; third-party reviews |
| 8 | Objections | Remove the last doubts | FAQ of 5-8 real questions from sales and support; security, pricing, migration, support |
| 9 | Pricing or offer | Make the commitment concrete | Plan summary or "From $X/month" with a link to pricing |
| 10 | Final CTA | Ask again, clearly | Restated outcome, the same primary CTA, the risk reducer |
| 11 | Footer | Utility and trust | Contact, legal pages, cookie settings, social links, address where required |

For short, impulse or low-price offers, compress to hero, proof, benefits, CTA. For complex B2B offers, add security, integrations, ROI and role-based sections.

## Section patterns

| Pattern | Use for | Watch for |
| --- | --- | --- |
| Split hero (text 5-6 columns, media 6-7 of 12) | Product sites with a strong visual | Media must show the product, not abstract shapes |
| Full-bleed image or video hero | Brand, hospitality, fashion, luxury | Text contrast over imagery (scrim with `--color-overlay-scrim`); LCP weight; pause control for video |
| Text-only hero with large type | Editorial, Swiss, brutalist and typographic directions | Needs a typographic idea, not just big Inter |
| Zigzag feature rows | 3-5 features with visuals | Monotony beyond 4 rows; vary with a full-width block |
| Bento grid | Many small features at a glance | Equal-sized tiles with icons is the generic look; vary scale and use real UI crops |
| Stats band | 3-4 strong, sourced numbers | Unsourced or vanity numbers |
| Logo cloud | Social proof | Logos without permission; more than 2 rows |
| Testimonial carousel | Many quotes | Auto-rotation needs pause (WCAG 2.2.2); a static grid of 3 often works better |
| Comparison table | Versus competitors or plans | Fairness and accuracy; claims must be substantiated |
| Interactive demo or calculator | Complex products, pricing | Performance cost; keyboard access |
| Timeline or process | Services, onboarding, history | Long vertical scroll on mobile |
| Sticky storytelling (scroll-driven) | Flagship launches | Reduced-motion alternative; content must work without the effect |

## Homepage

The homepage routes, it rarely converts directly.

- One sentence that says what the organization does and for whom.
- Paths to the 3-5 top tasks or audiences (from top-tasks research), visible without scrolling on desktop.
- Proof (customers, numbers, awards) and the latest or most important content.
- For multi-product companies: a product chooser by need, not by internal product names.
- Avoid rotating hero carousels: later slides get little attention and the rotation fails people who need more time; use one strong message and secondary tiles.

## Product and feature pages

**SaaS feature page:** problem, how this feature solves it (with real UI), proof specific to the feature, integration and setup details, related features, CTA.

**Ecommerce product detail page:**

- Gallery of 5-8 images including scale, detail and in-use shots, plus video where useful; zoom on desktop, swipe on mobile.
- Title, price (with any unit price required in the market), rating summary linked to reviews, variant selectors (swatches with names, size guide), stock and delivery date estimate.
- Add to cart as the primary button; sticky on mobile once the original scrolls out of view.
- Details in accordions or tabs: description, specs, materials and care, shipping and returns.
- Reviews with filters and photos; cross-sells below the fold.
- Baymard Institute's product page research is the deepest public source on these details.

## Pricing page

Structure: headline that frames value, billing toggle, 3-4 plan cards, comparison table, enterprise contact, FAQ, final CTA. UI details (plan cards, toggles, tax display) are in `ui-design` [flows](../../ui-design/references/flows.md); persuasion limits are in [conversion](conversion.md).

## About page

- The origin and the reason the company exists, in 2-3 short paragraphs, not a corporate timeline.
- Real team photos (consented) with names and roles; leadership bios for B2B.
- Values only with evidence (what you did because of each value).
- Proof: customers, press, certifications, impact numbers with sources.
- Careers link, contact, location, company details.

## Blog and article pages

| Element | Default |
| --- | --- |
| Measure | 60-75ch (`--measure-body` to `--measure-wide`) |
| Body size | 18-21px for long-form, line-height 1.6-1.7 (`--line-height-relaxed`) |
| Headings | Descriptive H2s every 200-400 words; anchor links on hover and focus |
| Table of contents | For articles over about 1,500 words; sticky in a side column on desktop |
| Byline | Author with link to bio, published and updated dates |
| Media | Images at content width or wider with captions; code blocks with copy |
| End of article | Related posts (3), newsletter or product CTA, share links |
| Index page | Featured post, category filters, search, cards with title, excerpt, date and reading time |

Inline CTAs inside long articles work best when relevant to the article topic; place at most one mid-article and one at the end.

## CTA design

- **Label:** verb + outcome, specific to the offer: "Start free trial", "Book a 20-minute demo", "Get the price list". Avoid "Submit", "Learn more" and "Click here".
- **One primary per view:** a filled button in `--color-accent-default`; secondary as an outline button or text link. Two equal buttons split attention.
- **Size:** 44-48px tall, horizontal padding `--space-5` to `--space-6`, `--font-size-md` semibold.
- **Microcopy under the CTA** answers the main anxiety: "Free for 14 days. Cancel anytime." or "No credit card required."
- **Repetition:** on long pages, repeat the primary CTA after major proof sections and at the end; keep the label identical.
- **Contrast:** text 4.5:1 on the button, button 3:1 against the background.
- First-person labels ("Start my trial") sometimes test better and sometimes not; treat that as a test, not a rule.

## Wireframing rules

- Real headlines and copy at real lengths; no lorem ipsum.
- Annotate each section with its job and the question it answers.
- Mobile wireframe first for content order; desktop composition second.
- Mark the LCP element on each template so performance work starts in design.
- Use the IDs from the sitemap (`2.1 Product detail`) so design, CMS and analytics share names.
