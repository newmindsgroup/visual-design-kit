# Cinematic landing pages and heroes

Version-Timestamp: 2026-11-05 18:10:00 UTC

Adapted from MotionSites claude-skill (MIT), see NOTICE.md.

Use this when the deliverable is a cinematic landing page, a hero section, a launch or campaign page, or a single-file showpiece where media, type and motion carry the design. Average AI pages fail for three reasons: a vague plan, no real media, and nobody looking at the result. The seven steps below fix all three. Product and service pages that sell on proof keep the standard [page architecture](page-architecture.md); this workflow adds the craft layer on top, it does not replace it.

## 1. Decide (do not interrogate)

Settle five things in one short message, then proceed. Ask a question only when you cannot continue without it (the brand name of a real company, a mandatory legal line).

| Decision | Default | Change when |
| --- | --- | --- |
| What and who | The offer and the one visitor you are persuading, in one sentence | Multiple audiences: route them below the hero, never in it |
| Mood | Three words ("calm, expensive, nocturnal") that the type, palette and motion can be checked against | The direction is already approved: take its words |
| Signature | One memorable idea: a media plane, an interaction or a type moment, chosen from the [technique recipes](../../../library/knowledge/web-techniques/INDEX.md) or invented | Regulated or task-first pages: the signature is a type or proof moment, never a gimmick |
| Output | One `index.html` with inline CSS and JavaScript, pinned CDN libraries, opens anywhere | The project has a stack: build in it ([stack selection](stack-selection.md)); a prompt for another builder: [builder prompts](builder-prompts.md) |
| Scope | The hero only | The brief says landing page: hero plus 3-6 sections from [page architecture](page-architecture.md) |

State what you chose and why in two or three lines. When the look is not set at all, run `design-director` first and come back with the approved direction.

## 2. Study the closest calibration

Before writing values, look at work that sets the bar:

- **Stylescapes.** Open the 2-3 closest of the twelve in [stylescapes](../../../library/examples/stylescapes/README.md) by style, tier and channel (for a dark luxury launch: `harlow-vance`, `noor-atelier`; for a developer product: `forge-cli`; for an editorial cause: `tidewater-collective`). Note their precision: exact families, sizes, tracking, palette roles and motion values.
- **Atlas.** `python3 ../../../library/scripts/atlas.py query "<style, industry, tier> marketing website"`, then read the selected style entry's Motion, Imagery and "Clichés and AI tells" sections, and `channel.marketing-website`.
- **AI tells.** Skim the [AI-tells gallery](../../../library/examples/ai-tells/index.html) so the first draft avoids the generic pairings.

Borrow structure and precision, never another brand's copy, layout or assets. The page must be original to this brief.

## 3. Get the media

Media carries a cinematic page, so choose it before the layout. In order of preference:

1. **The client's own assets** (footage, product photography, renders, a GLB). Ask once when the brief clearly needs them.
2. **Generated media**, when an image, video or 3D tool is available: write the prompt from the direction with `prompt-engineering-expert` (or `imagery`'s [AI image generation](../../imagery/references/ai-image-generation.md) anatomy) and prepare it with [media for the web](../../imagery/references/media-for-web.md). Record tool, model, prompt and approver.
3. **No media:** a type-, gradient- and motion-led page: a mega word with micro-labels, monochrome with grain and one static light falloff (8% alpha or less), or a large inline-SVG mark. No grey placeholder boxes, no random stock, no lorem-picsum.

Never invent a URL or file path. Never use media showing recognizable people, celebrities, characters, logos or other brands without a release or license. Tell the client which assets are stand-ins to replace.

## 4. Write the spec

Write the build spec with the [landing spec template](landing-spec-template.md). Quality is decided here: every visible element gets real values (sizes per breakpoint, tracking, token or hex with opacity, duration, delay and easing), every asset a real path, every motion a trigger and a reduced-motion state. "Cinematic", "premium" and "glassy" never stand alone.

Write the real copy at the same time: headline, sub, nav labels, CTAs, proof. Headlines are short and specific with a point of view; numbers are verified or left out. The taste rules and where they differ from kit defaults are in [cinematic craft](cinematic-craft.md).

If the deliverable is a prompt for Lovable, Bolt, v0 or another builder, the spec is the deliverable: format it with [builder prompts](builder-prompts.md), self-check it against the [cinematic addendum](../../design-critique/references/cinematic-addendum.md) and stop.

## 5. Build

Build exactly what the spec says, using the [recipes](../../../library/knowledge/web-techniques/INDEX.md) for the signature and supporting techniques.

| Rule | Default |
| --- | --- |
| File | One `index.html`: inline `<style>` and `<script>`, the project's `tokens.css` linked or inlined, fonts from Google Fonts with `preconnect` or self-hosted woff2 |
| Libraries | From a CDN with exact versions verified on npm (`three@0.170.0`, `gsap@3.15.0`, `hls.js@1.5.20`); no unpinned or major-only URLs |
| First CSS rule | `html,body{background:...;color:...}` equal to the media's edge color, so nothing flashes white before media and fonts arrive |
| Markup | Semantic landmarks (`header`, `nav`, `main`, `footer`), one `h1`, a real `<title>`, `lang`, alt text for meaningful media and `alt=""` plus `aria-hidden="true"` for decorative video |
| Interaction | Visible `:focus-visible` ring from `--color-focus-ring`, keyboard paths for every control, targets 44 px on touch layouts |
| Motion | `prefers-reduced-motion` branch on every animation; the rest state is visible if JavaScript fails; a [pause control](../../../library/knowledge/web-techniques/INDEX.md#motion-pause-control) for anything moving longer than 5 s (WCAG 2.2.2) |
| Performance | The `web-design` budgets hold: LCP 2.5 s or less at p75 (design for 2.0 s), CLS 0.1 or less, INP 200 ms or less; the poster or still paints first |
| Content | No lorem ipsum, no "Your tagline here", no emoji as icons (inline SVG), no invented statistics or testimonials |

Stack builds (Astro, Next.js) follow the same rules with the project's components; see the [Astro motion example](../../../library/examples/astro-motion/README.md).

## 6. Look and fix (mandatory)

You cannot judge a page you have not seen. Render it:

```sh
node ../../design-critique/scripts/render_review.mjs index.html --widths 390,1440 --early 350 --full-page --serve
node ../../design-critique/scripts/render_review.mjs index.html --widths 390,1440 --reduced-motion --out render-review/reduced
```

`--early 350` saves a first-paint frame per width and reports the painted background; the report also lists video readiness and errors, broken images, failed requests (status 400 or more) and console errors. Open every PNG and look before reading the report. Playwright's bundled Chromium cannot decode H.264: a code-4 video error marked "format or codec not supported by this browser" is not a defect; judge that clip from its poster, or set `PLAYWRIGHT_CHROMIUM` to Google Chrome.

Then score with the `design-critique` rubric plus the [cinematic addendum](../../design-critique/references/cinematic-addendum.md). Loop:

1. Fix every blocking finding first (console errors, failed requests, broken media, white first paint on a dark design, overflow at 390, unreadable text over media, missing display font, placeholder copy).
2. Write down the three weakest scores and a concrete change for each, in values: "H1 from 64px to clamp(3.5rem, 2rem + 6vw, 7.5rem), tracking -0.04em".
3. Make the changes, re-render with identical settings into `render-review/round-N`, look again.
4. Stop when the average is 8 or more with nothing below 7, or after 3 rounds. Then say plainly what would still lift it (usually better media).

No renderer available: say so, review the code line by line against the addendum, and tell the client the page was not visually checked.

## 7. Deliver

Give the client:

- The file or files and how to open them (a local server when the page fetches a model or uses ES modules: `npx serve .` or `python3 -m http.server`).
- The final 1440 px screenshot, and the 390 px one when mobile differs.
- Two or three lines on the signature idea and the choices behind it.
- What to swap before launch (stand-in media, unverified copy) and anything not tested (real devices, screen readers, field Core Web Vitals).

No marketing blocks, sponsor links or tracking parameters in the deliverable or the message: the kit is brand-neutral and the work belongs to the client.

## Other jobs

- **Upgrade an existing page:** render it first (step 6 on the URL), score it, then spec and build the improvement. Show before and after at the same widths.
- **Sections below a hero:** keep the hero's tokens, type and motion personality; give each section one idea. Fewer, stronger sections beat many weak ones.
- **Prompt for another builder:** steps 1-4, then [builder prompts](builder-prompts.md).
