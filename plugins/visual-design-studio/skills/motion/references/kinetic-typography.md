# Kinetic typography

Version-Timestamp: 2026-10-20 01:59:37 UTC

Kinetic type works when the motion delivers the words and then gets out of the way. Set the static typography first (see the typography skill), then animate phrases, and hold every complete message long enough to read twice.

## Hold times

- **Reading-rate anchor:** adults silently read static English non-fiction at about 238 words per minute on average, roughly 4 words per second (Brysbaert, "How many words do we read per minute?", *Journal of Memory and Language*, 2019; a meta-analysis of 190 studies). Text competing with footage, music and motion reads slower.
- **Rule of thumb (practitioner convention, not a standard):** hold = 1s + words ÷ 3, counted from the moment the line is fully legible. The animation-in time does not count. Minimum 1.5-2s for any on-screen line.
- **Second check:** read the line aloud twice at a normal pace while it is on screen. If you cannot, the hold is too short.
- Add 50% for numbers, prices, URLs, dates and anything the viewer must act on.
- Second-language audiences, children and older adults read slower; add 25-50%.

| Words on screen | Minimum hold | Comfortable hold |
| --- | --- | --- |
| 1-3 (tagline, single word) | 1.5s | 2s |
| 4-6 | 2.5s | 3s |
| 7-10 | 3.5s | 4.5s |
| 11-15 | 4.5s | 6s |
| 16 or more | Split into two cards | Split into two cards |

Legal supers in advertising are regulated in many markets (for example, Clearcast publishes legibility and hold guidance for UK TV ads). Verify current rules with the clearance body and counsel; do not treat this table as compliance.

Animate-in: 300-700ms per line. Exit: 200-400ms, or a cut. In a 15-second spot, budget no more than 3-4 text cards.

## Techniques

| Technique | Feel | Timing defaults | Use and risk |
| --- | --- | --- | --- |
| Line mask reveal (text rises from behind a clip) | Editorial, precise | 400-700ms per line; 80-120ms line stagger; easeOutExpo cubic-bezier(0.16, 1, 0.3, 1) | Safest default for headlines |
| Word-by-word | Rhythmic, spoken | 300-500ms per word; 30-80ms stagger, or synced to the voice-over | Lyrics, quotes, VO emphasis |
| Character cascade | Playful | 10-30ms per character; whole word done within 600ms | Short display words only; unreadable on long lines |
| Tracking in | Luxury, cinematic | letter-spacing 0.3em to 0.05em over 1-2s, ease-out | Titles and idents; keep the final tracking set for legibility |
| Scale punch | Energetic, sport | 110% to 100% in 150-250ms, on the beat | One word per beat; check flash limits on hard cuts |
| Typewriter | Technical, narrative | 30-60 characters per second; cursor blink about 1Hz | Terminal and story contexts; avoid on marketing heroes |
| Scramble or split-flap | Data, travel, tech | Resolves within 600ms | Never for text that must be read immediately |
| Variable-font axis | Fluid, expressive | wght or wdth change over 400-1000ms | Needs a variable font, such as Roboto Flex or Inter (both OFL) |
| Kinetic layout (words as objects with physics) | Experimental | Varies | Final layout must settle into a readable hold |
| Text on a path, 3D extrusion | Spectacle | Varies | Legibility drops fast; hold it flat at the end |

Pick one primary technique per piece and at most one accent technique. Animate semantic units (phrases, lines, key words), not arbitrary characters.

## Legibility

- **Size at 1920×1080 (landscape):** supers at least 40px; headlines 80-160px. On a phone, a 1920px frame shrinks to about 40-45% of its size, so 40px renders near 17pt.
- **Size at 1080×1920 (vertical social):** supers at least 48px; captions 48-64px. On a 390pt-wide phone, 48px renders at about 17pt.
- **Weight:** medium to bold for text over footage. Strokes thinner than about 2px at render size shimmer and break up under compression.
- **Contrast:** at least 4.5:1 (3:1 for large text), measured on the least favorable frame (WCAG 2.2 SC 1.4.3). Use a 40-60% black gradient scrim, a solid text box or a 2-4px stroke rather than hoping the footage cooperates.
- **Stillness:** text is stationary during its hold, or drifts no more than 1-2% of the frame width per second.
- **Line length:** 32-42 characters per line; one or two lines per card.
- **Case:** all caps slows reading; keep caps lines to 3-5 words.
- **Placement:** inside title-safe (90% of the frame) and clear of platform UI in social formats (see [video and motion graphics](video-and-motion-graphics.md)).
- **Broadcast:** avoid 1px horizontal lines and very fine serifs; they twitter on interlaced and scaled displays.

## Captions and subtitles

- Captions transcribe dialogue plus meaningful sound ("[door slams]"); subtitles translate dialogue. Open captions are burned into the picture; closed captions are a sidecar the viewer can switch on.
- **Formats:** SRT for simple delivery and social uploads; WebVTT for the web (`<track kind="captions">`, positioning and styling); SCC (CEA-608/708) for US broadcast; TTML or IMSC for streaming deliverables.
- **Line length:** 32 characters per row is the CEA-608 limit; Netflix's English guide allows 42. Two lines at most.
- **Duration:** about 5/6 of a second minimum and 7 seconds maximum per event (Netflix timed-text guidance).
- **Reading speed:** about 17-20 characters per second for adult content (Netflix English guidance cites up to 20, and 17 for children's programs); the BBC subtitle guidelines cite about 160-180 words per minute. Verify against the distributor's current style guide before delivery.
- Break lines at phrase boundaries, never between an article and its noun. Move captions to the top while a lower third is on screen.
- **Kinetic "karaoke" captions** for social: keep the line still, highlight the current word with color or weight, and never bounce every word. Keep them inside the safe zone and above the platform's UI.

```vtt
WEBVTT

00:00:01.000 --> 00:00:03.800
Every launch starts
with one clear sentence.

00:00:04.000 --> 00:00:06.500 line:10%
[upbeat music]
```

## Accessibility

- **WCAG 2.2 SC 2.2.2 Pause, Stop, Hide (Level A):** moving, blinking or scrolling content that starts automatically, lasts more than 5 seconds and appears alongside other content needs a way to pause, stop or hide it, unless the movement is essential. This covers looping kinetic headlines, marquees, auto-advancing carousels and background video with text.
- **SC 2.3.1 Three Flashes or Below Threshold (Level A):** nothing flashes more than three times in any one-second period, unless the flashes stay below the general and red flash thresholds. Watch strobing "SALE" text, beat-synced luminance flips and fast black/white cuts.
- **SC 2.3.3 Animation from Interactions (Level AAA):** users can disable motion triggered by interaction unless it is essential. Treat it as a default by honoring `prefers-reduced-motion`, even though it is AAA.
- **SC 1.2.2 Captions (Prerecorded), Level A; SC 1.2.4 Captions (Live), Level AA; SC 1.2.5 Audio Description (Prerecorded), Level AA:** if on-screen text carries information the audio does not, voice it or provide audio description.
- **Split text on the web:** screen readers can announce each span separately. Keep the full string as real text and hide the animated copy:

```html
<h1 class="headline">
  <span class="visually-hidden">Design anything, for anyone.</span>
  <span aria-hidden="true" class="split"><span>Design</span> <span>anything,</span> <span>for</span> <span>anyone.</span></span>
</h1>
```

  An `aria-label` on a plain `div` or `span` is not reliably announced. Use the hidden copy, or put the label on an element that accepts one (a heading or a landmark). GSAP's SplitText (3.13+) has an `aria` option that automates a version of this pattern; check what it outputs.
- **Reduced motion:** show the complete text at once, with at most a 150-200ms fade.
- **Flash testing:** for broadcast and large-format displays, run a recognized analyzer such as PEAT (Trace Research and Development Center, free) or Harding FPA (commercial; widely used for UK broadcast under Ofcom guidance). Record the tool, version, file tested and result.
