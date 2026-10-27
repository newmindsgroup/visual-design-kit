# Presentations and decks

Version-Timestamp: 2026-10-27 12:00:00 UTC

A presented deck is a backdrop for a speaker: one idea per slide, a headline that states the point, evidence big enough to read from the back row, and the detail in the speaker notes. A reading deck, sent as a PDF, is a document in landscape and follows different rules. Decide which one you are making first. For the channel overview see the atlas entry [presentation](../../../library/atlas/channels/presentation.md).

## Canvas

| Item | Default | Notes |
| --- | --- | --- |
| Aspect ratio | 16:9 | 4:3 only when the venue requires it; 1:1 or 4:5 for decks posted to social |
| Pixel size | 1920x1080 | 3840x2160 for 4K screens and LED walls |
| PowerPoint | Widescreen 13.333x7.5in | At 1920px wide, 1pt = 2px |
| Google Slides | 16:9 default 10x5.625in | The page is 25% narrower than PowerPoint widescreen, so the same point size looks about a third larger; multiply the point sizes below by 0.75 |
| Keynote | 1920x1080 | |
| Reading deck | 16:9 or A4/Letter landscape | Designed for screens and print, read without a presenter |

## Type sizes

Values for 1920x1080 (PowerPoint widescreen equivalents in points; for Google Slides' default page multiply the points by 0.75):

| Role | Presented deck | Reading deck |
| --- | --- | --- |
| Statement or big number | 120-200px (60-100pt) | 72-120px (36-60pt) |
| Slide headline | 72-108px (36-54pt), 1-2 lines | 48-64px (24-32pt) |
| Body | 48-64px (24-32pt) | 24-32px (12-16pt) |
| Labels, chart text | 36-40px (18-20pt) minimum | 20-24px (10-12pt) |
| Source and footnotes | 28-32px (14-16pt) | 18-20px (9-10pt) |

Never set presented text below 18pt (36px). Guy Kawasaki's 10/20/30 rule (10 slides, 20 minutes, 30pt minimum) is a useful extreme for pitches.

Line length: 40-60 characters for body; headlines under about 15 words.

## One idea per slide

- **Headline as assertion:** write the takeaway as a full sentence (fictional example: "Claims paid on first submission rose from 71% to 94%"), not a topic label ("Results"). This is the assertion-evidence approach (Michael Alley).
- **Evidence under it:** one chart, image, diagram or short list that proves the headline.
- **Word budget:** presented slides about 25-40 words including the headline; reading-deck pages up to about 80-150 words.
- **Bullets:** if used at all, 3-5 per slide, one line each, parallel grammar. Better: convert them into a diagram, a table or three separate slides.
- **Pace:** about 1-2 minutes per slide as a common starting point; a 20-minute talk is 10-20 slides, plus appendix.

## Grid and layout

- Margins: 96-120px left and right (5-6% of width), 72-96px top and bottom. Keep logos, footers and page numbers inside them; projectors and LED walls crop edges.
- 12-column grid with 24-32px gutters; 8px baseline.
- Fixed headline position and size across content slides, so the eye knows where to look and the title does not jump between slides.
- Leave the top-right corner and bottom strip lighter when presenting over video calls, where participant thumbnails and controls often cover them.
- Generous empty space; align everything to the grid; one accent color for emphasis.

Master layouts to build:

| Layout | Use |
| --- | --- |
| Title | Opening: title, subtitle, presenter, date |
| Agenda | 3-5 sections |
| Section divider | Large section title, optional image |
| Statement | One sentence or one number, full slide |
| Headline + chart | Data slides |
| Headline + full-bleed image | Emotion, context |
| Two-column comparison | Before/after, option A/B |
| Three-up | Three parallel points or products |
| Quote | Customer or expert voice with attribution |
| Process or timeline | 3-6 steps |
| Table | Up to 6-8 rows presented |
| Team | Photos at consistent crops |
| Closing | One call to action, contact |
| Appendix | Dense backup material, reading-deck rules |

Build them as real slide-master layouts with placeholders, theme colors and theme fonts, not as pasted shapes. In PowerPoint, map the brand palette to the theme slots (Dark 1, Light 1, Dark 2, Light 2, Accent 1-6, hyperlink) so charts and SmartArt pick up brand colors automatically.

## Data slides

- One chart per slide; the headline states what the chart shows.
- Highlight the series that matters in the accent color; gray out the rest.
- Direct labels instead of legends; remove gridlines, 3D, shadows and decorative fills.
- Start bar charts at zero; show units; round numbers to the precision that matters.
- Chart labels at least 36px (18pt); thin lines at least 3-4px so they survive projectors.
- Source line on the slide (14-16pt), full methodology in the notes.
- Build sequentially (one series, then the next) only when the narrative needs it.
- See the data-visualization skill for chart choice and palettes.
- **Canva exception:** native charts and SmartArt do not survive a PPTX import into Canva. When the deck's editable home is Canva, build a Canva-safe version with charts as images plus editable text labels (`library/examples/deck-pptx`, `--canva-safe`), and keep native charts for the PowerPoint version. Test both before promising fidelity.

## Images

- Full-bleed images at least 1920px wide (3840px for 4K), cropped for the slide.
- Text over images needs a scrim or a clean area, with computed contrast.
- Avoid stock clichés and clip art; use the brand's photography and one icon family.
- Compress images for sharing (about 150-220ppi equivalent, often under 200KB each).

## Speaker notes

- Write the talk in the notes: opening line, the point, the evidence, the transition to the next slide.
- At roughly 130-150 spoken words per minute, a 1-2 minute slide carries about 130-300 words of notes; keep it to key phrases if the speaker improvises.
- Put sources, definitions and backup numbers in the notes so the slide stays clean.
- Mark timing checkpoints ("by slide 8: 10 minutes").
- Rehearse in presenter view on the presenting machine.

## Accessibility

- Unique, descriptive slide titles on every slide (screen readers navigate by title; hide a title off-slide only if the design demands it).
- Correct reading order (PowerPoint Selection Pane or Reading Order pane).
- Alt text for meaningful images and charts; mark decorative images as decorative.
- Contrast of at least 4.5:1 for all text; aim for 7:1 because projectors wash out pastels and light grays.
- Never use color alone to encode meaning; add labels or patterns.
- Live captions or subtitles when presenting online or to large audiences (PowerPoint and Google Slides both offer live captions).
- Transitions: none, fade or morph at 0.3-0.5s; no spins, bounces or fly-ins. Reduce motion for audiences sensitive to it.
- Export a tagged PDF for distribution.

## Fonts and files

- Use fonts available on every presenting machine, embed them where the app supports it, or use cloud decks with web fonts (Google Slides supports Google Fonts). OFL families such as Inter, IBM Plex, Source Serif 4 and DM Sans avoid licensing problems.
- Test the deck on the actual presenting machine and screen.
- Deliver the editable file (PPTX, Keynote or Google Slides), a PDF, and the template file with master layouts.
- Keep decks under about 25MB for email; link large decks.
- Embedded video: MP4 H.264, 1080p; test playback in the venue.

## Tools

PowerPoint, Keynote, Google Slides, Figma Slides and Pitch all handle master layouts. For generated decks, code tools such as python-pptx or the Google Slides API can build slides from a master template. If a deck-building skill or a slides artifact type is available in the session, use it with these rules; this repository does not bundle one.

## Investor pitch structure

A common 10-15 slide order: problem, solution, why now, market, product, traction, business model, competition, go-to-market, team, financials, the ask. Lead with traction if it is the strongest evidence.

## Common failures

- Topic-label headlines ("Q3 Results") → assertion headlines.
- Twelve bullets at 14pt → one idea, big type, notes for detail.
- Each slide laid out by hand → master layouts with placeholders.
- Charts pasted as screenshots from a spreadsheet → native or redrawn charts in brand style with direct labels.
- Logo on every slide in the corner, large → small or absent on content slides.
- Fonts swapped on the presenting machine → embedded, cloud or OFL fonts, tested.
- A reading deck presented live → split into a presented deck plus a leave-behind PDF.
