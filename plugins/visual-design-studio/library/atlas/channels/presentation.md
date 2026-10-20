---
id: channel.presentation
axis: channel
name: Presentations and Decks
aliases: [presentation, slide deck, pitch deck, keynote, powerpoint, google slides, sales deck, board deck, slides]
summary: Slides that support a speaker or a reader; 16:9 layouts with one message per slide, large type, strong templates and clear data stories beat dense documents on screen.
tags: [presentation, deck, slides, pitch, keynote, powerpoint, template, storytelling, data, 16:9]
pairs_with: [style.swiss-international, style.editorial-magazine, style.corporate-modern, style.quiet-minimal, style.bold-geometric-sport, industry.saas-b2b, industry.events-conferences, audience.b2b-buying-committee, archetype.sage, archetype.ruler]
avoid_with: [style.web-brutalist, style.maximalist-eclectic]
version_timestamp: 2026-10-20 02:01:01 UTC
---

# Presentations and Decks

## Formats and specs

| Item | Spec | Notes |
| --- | --- | --- |
| Aspect ratio | 16:9 at 1920x1080 px; PowerPoint widescreen 13.333x7.5 in; Keynote 1920x1080; Google Slides 16:9 default (10x5.625 in) | Use 4:3 (1024x768) only when a venue screen demands it; 16:10 for some laptops |
| High-resolution export | 3840x2160 for 4K screens and LED walls; PDF export for distribution | Confirm venue resolution with the AV team |
| Safe margins | 0.5-0.75 in (about 4-5%) on all sides; footers and logos inside | LED walls and projectors crop edges |
| Type sizes (projected) | Titles 36-54 pt; body 24-28 pt minimum; captions and source lines 14-16 pt; no body text below 18 pt | Sizes assume 13.333 in slide width; scale accordingly |
| Contrast | 7:1 or better for body in lit rooms (a common starting point); minimum 4.5:1 | Projectors wash out light grays and pastels |
| Images | 1920 px wide minimum for full-bleed, 3840 px for 4K; JPEG/PNG/SVG; sRGB | Compress to under about 200 KB each for easy sharing |
| Video | MP4 H.264, 1080p, 30 fps, AAC audio; embed or link; test in the venue | Autoplay and sound need AV checks |
| File size | Under 25 MB for email; use a share link or PDF for large decks | Embed fonts or export PDF; avoid unlicensed fonts |
| Fonts | Fonts available on all target machines: system fonts or fonts embedded; consider OFL families (Inter, IBM Plex, Source Serif 4, DM Sans) | Cloud decks (Google Slides) support Google Fonts |
| Export formats | PPTX for editing, PDF for reading, Keynote for Apple events; notes pages for handouts | A4 or Letter handout layout for print |

## Structure and hierarchy

- **Message first:** one message per slide, written as a sentence (an "action title" of 8-14 words, two lines maximum) and supported by one visual or one table.
- **Narrative arc:** situation, tension, resolution, ask. Pitch decks: problem, solution, product, market, traction, business model, team, ask (10-15 slides). Board and sales decks put the recommendation and the ask first, then evidence.
- **Pacing:** about one slide per minute is a common starting point; a presented slide should be understood in 3-5 seconds; reading decks (sent, not presented) can carry more text but need clear sections and page numbers.
- **Layout system:** a master with 8-12 layouts (title, section, one column, two column, big number, quote, image full-bleed, chart, table, comparison, timeline, closing) and a strict grid (12 columns, 0.5 in gutter). Use placeholders so content snaps to position.
- **Visual hierarchy:** headline, supporting visual, source note; a consistent location for each. Use color to direct attention (one highlight color per slide).
- **Data slides:** chart type chosen for the message (see `data-visualization`), direct labels, annotated takeaway, source and date.

### Master layout specs

| Layout | Grid and content | Type |
| --- | --- | --- |
| Title | Left-aligned title in columns 1-8; subtitle and date below; logo top-left | Title 54-72 pt, subtitle 24 pt |
| Section divider | Large number or word, one line of context | 72-120 pt numeral, 28 pt label |
| Content, one column | Action title plus a visual spanning 8-12 columns | Title 32-40 pt, body 24-28 pt |
| Content, two column | Equal or 5 + 7 split, visual on the right | Title 32-40 pt, body 24 pt |
| Big number | One metric centered or left, short explanation | Metric 120-200 pt, label 24 pt |
| Quote | Quote in 8 columns, attribution below | Quote 36-48 pt, attribution 18-20 pt |
| Chart | Chart spans 9-10 columns with takeaway at the side or top | Axis 14-16 pt, takeaway 24 pt |

## Craft defaults

- Typography: one sans family or a sans plus one serif for headlines; 3 sizes per slide (title, body, caption); left align; line height 1.15-1.3 for headlines and 1.3-1.4 for body; limit lines to 45-60 characters in text blocks.
- Color: neutral background (white, off-white or deep ink) plus one or two accents and a data palette that survives grayscale printing; dark backgrounds work in dim rooms, light backgrounds in bright rooms and for print.
- Imagery: full-bleed photographs with scrims for text; product shots with real UI (cropped, not scaled to illegibility); icons from one consistent set at 2x the text size.
- Motion: 200-400ms fade or push transitions, with one consistent style; "magic move" or morph for continuity; avoid spinning, bouncing and per-letter effects; animate builds only to control the speaker's pace.
- Dense reference material goes to an appendix, not onto the main slides.
- Accessibility: define reading order, alt text, 4.5:1 contrast, no meaning by color alone, captions for video; use large type for remote viewers (shared screens shrink slides).
- Brand compliance: logo placement fixed in the master, clear space around logos, no stretched or recolored logos.

## Production and handoff

- Build in the client's tool (PowerPoint, Keynote or Google Slides) with theme fonts, colors and layouts defined in the master; also provide Figma Slides or Canva versions when the team edits there. Prefer native charts for editable data; link or embed data sources.
- Deliver: template (.potx / .key), a style guide slide (fonts, colors, layouts, do and don't), a sample deck, an image library, and speaker notes with timings. The `print-packaging-social` skill covers deck production in more depth.
- Workflow for edits: avoid manual overrides on text boxes; use layouts, theme colors and styles so changes propagate.
- Remote and hybrid: test screen sharing at 1080p (compressed video), leave larger margins, and hold slides for at least 10 seconds when they carry data.
- Confidentiality: remove hidden slides, comments, metadata and embedded spreadsheets before sending; export PDF for external distribution.
- Licensing: stock imagery, fonts and icons must be licensed for the deck's distribution (including client-facing and public decks).

## QA checklist

- [ ] 16:9 at 1920x1080; fonts embedded or available; deck tested on the presentation machine and venue screen.
- [ ] Titles are full-sentence messages; one message per slide; no slide with more than about 40 words.
- [ ] Body text 24 pt or larger; captions 14 pt or larger; contrast at least 4.5:1 (target 7:1).
- [ ] Charts have axes labeled, units, direct labels, sources and dates; the takeaway is stated.
- [ ] Consistent master layouts, alignment, spacing, logo placement; no manual overrides.
- [ ] Animations and videos play offline; no autoplay surprises; slide numbers present.
- [ ] Metadata, comments, hidden slides and private data removed from shared files.
- [ ] PDF export checked: fonts, images, links and page order.

## Reference anchors

- Garr Reynolds, *Presentation Zen*; Nancy Duarte, *Slide:ology* and *Resonate*
- Barbara Minto, *The Pyramid Principle* (action titles and structure)
- Edward Tufte, *The Visual Display of Quantitative Information* (and his critique of slide software)
- Airbnb's 2009 seed pitch deck and Sequoia Capital's published pitch-deck outline as commonly cited structure references
- Apple Keynote event keynotes and TED stage design as references for staging and pace
