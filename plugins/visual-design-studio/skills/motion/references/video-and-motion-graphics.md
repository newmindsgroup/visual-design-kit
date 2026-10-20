# Video and motion graphics

Version-Timestamp: 2026-10-20 01:59:37 UTC

Rendered motion (ads, social, explainers, idents, display loops) is judged frame by frame and on the target player. Plan it in boards, build it in an editable timeline (After Effects or code with Remotion), deliver it to spec and check loudness, captions, safe areas and flashing before anyone calls it done. Platform specs change; confirm them against the platform's current help pages (as of 2026).

## Pre-production

1. **Script and beat sheet:** one line per beat with voice-over, on-screen text, duration and purpose.
2. **Storyboard:** one frame per beat with framing, motion direction, transition and timing in seconds and frames.
3. **Style frames:** 2-3 hero frames at final quality, approved before animation starts.
4. **Animatic:** timed boards with scratch voice-over and music. Lock the timing here; re-timing finished animation is expensive.
5. **Production, review and delivery:** review at full playback speed on the target device, never only from scrubbing.

## After Effects project structure

- **Folders:** `00_Render` (final comps only), `01_Scenes`, `02_Elements`, `03_Assets` (footage, audio, vectors), `04_Guides`, `99_Old`.
- **Comp names:** `PROJ_Deliverable_1920x1080_25p_v03`. Put the frame rate and size in the name, and set them to the delivery spec from the start.
- **Main comp is the edit:** each scene is a precomp; reusable elements (logo lockup, lower third, end card) are single precomps reused everywhere, so a change happens once.
- **Null rigs:** one `CTRL` null per scene carries Slider, Point, Color and Checkbox Controls; layers parent to nulls; a camera parented to a null orbits cleanly.
- **Guides:** a guide layer with title-safe and platform-safe overlays, plus markers on voice-over beats.
- **Expressions** use the JavaScript engine (the default since After Effects 16.0). Keep them short and readable, and drive the numbers from controls.

## Expression snippets

```js
// Organic drift: 1.5 wiggles per second, up to 12px. Horizontal only: [wiggle(1.5, 12)[0], value[1]]
wiggle(1.5, 12)
```

```js
// Looping wiggle that joins cleanly every 4 seconds
freq = 1; amp = 12; loopTime = 4;
t = time % loopTime;
w1 = wiggle(freq, amp, 1, 0.5, t);
w2 = wiggle(freq, amp, 1, 0.5, t - loopTime);
linear(t, 0, loopTime, w1, w2)
```

```js
loopOut("cycle")     // repeat the keyframes
loopOut("pingpong")  // forward, then backward
loopOut("offset")    // repeat while accumulating (counters, walk cycles)
```

```js
// Follow-through: trail the layer above by 3 frames
delay = 3 * thisComp.frameDuration;
thisComp.layer(index - 1).transform.position.valueAtTime(time - delay)
```

```js
// Overshoot settle after the last keyframe (apply to Position or Scale)
amp = thisComp.layer("CTRL").effect("Overshoot")("Slider") / 100; freq = 2.5; decay = 6;
n = 0;
if (numKeys > 0) { n = nearestKey(time).index; if (key(n).time > time) n--; }
if (n > 0) {
  t = time - key(n).time;
  v = velocityAtTime(key(n).time - thisComp.frameDuration / 10);
  value + v * amp * Math.sin(freq * t * 2 * Math.PI) / Math.exp(decay * t);
} else value;
```

```js
// Opacity: fade in over 12 frames from the layer's in point
ease(time, inPoint, inPoint + 12 * thisComp.frameDuration, 0, 100)
```

Translate easing tokens into the graph editor through keyframe influence: `--ease-standard` is roughly 20% outgoing influence on the first key and 100% incoming influence on the last; `--ease-emphasized-decelerate` is roughly 5% outgoing influence with a high outgoing speed (a steep start) and 90% incoming influence. Check against the [motion specimen](motion-specimen.html).

## Essential Graphics and MOGRT templates

- Open the master comp in the Essential Graphics panel, then add only what editors should change: source text, colors, sliders, checkboxes and dropdowns. Group and label them in plain language.
- Use **Responsive Design: Time** to protect the intro and outro, so editors can lengthen the template in Premiere Pro without stretching the animation.
- Use **Responsive Design: Position** to pin layers, so boxes and rules resize with the text.
- Expose nested properties with Master Properties instead of duplicating comps.
- Export a `.mogrt`. Lock logos and brand colors; list the required fonts and how editors get them (installed, or Adobe Fonts), and test with the longest real headline.

## Remotion (programmatic video in React)

Remotion renders each frame as a React component, so templates take props, data and code review like any other code. It suits data-driven and batch video (personalized clips, charts, changelog videos, localized variants). License: free for individuals, non-profits and companies with up to 3 employees; larger companies need a company license ([remotion.dev/license](https://www.remotion.dev/license)); the license is due to change with Remotion 5.0, so verify.

```ts
// src/index.ts
import { registerRoot } from 'remotion';
import { RemotionRoot } from './Root';
registerRoot(RemotionRoot);
```

```tsx
// src/Root.tsx
import { Composition } from 'remotion';
import { Title } from './Title';

export const RemotionRoot = () => (
  <Composition id="Title" component={Title} durationInFrames={150} fps={30} width={1920} height={1080}
    defaultProps={{ headline: 'One clear sentence.', accent: '#0E7C86' }} />
);
```

```tsx
// src/Title.tsx
import { AbsoluteFill, Easing, interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';

export type TitleProps = { headline: string; accent: string };

export const Title = ({ headline, accent }: TitleProps) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const enter = spring({ frame, fps, config: { damping: 200 } }); // settles without overshoot
  const exit = interpolate(frame, [durationInFrames - 15, durationInFrames], [1, 0], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.bezier(0.3, 0, 1, 1),
  });
  return (
    <AbsoluteFill style={{ backgroundColor: '#0B1215', justifyContent: 'center', padding: 160 }}>
      <h1 style={{ color: '#F4F7F7', fontSize: 120, lineHeight: 1.05, margin: 0,
        opacity: enter * exit, transform: `translateY(${interpolate(enter, [0, 1], [40, 0])}px)` }}>
        {headline}
      </h1>
      <div style={{ width: 160 * enter, height: 8, background: accent, marginTop: 40 }} />
    </AbsoluteFill>
  );
};
```

```sh
npx create-video@latest                      # scaffold a project
npx remotion studio                          # preview and scrub
npx remotion render src/index.ts Title out/title.mp4 --props='{"headline":"Launch day"}'
npx remotion render src/index.ts Title out/title.mov --codec=prores --prores-profile=4444 --image-format=png --pixel-format=yuva444p10le
```

Keep frames deterministic: use Remotion's `random(seed)` rather than `Math.random()`, load fonts before rendering (`@remotion/google-fonts` or `staticFile`), and lay out time with `<Sequence from={...}>`. Batch rendering uses `@remotion/renderer` (`selectComposition`, `renderMedia`) or Remotion Lambda.

## Export specs

| Deliverable | Format | Bitrate (a range, not a rule) | Notes |
| --- | --- | --- | --- |
| Edit master | ProRes 422 HQ, `.mov` | About 220 Mbps at 1080p29.97 (Apple ProRes white paper); roughly 4× at UHD | Archive and hand off this, not the H.264 |
| Master with alpha | ProRes 4444, `.mov` | About 330 Mbps at 1080p29.97 | Overlays, lower thirds, idents |
| YouTube and general upload, 1080p | H.264 High profile, MP4, fast start | 8 Mbps at 24-30fps, 12 Mbps at 48-60fps (YouTube's SDR recommendation) | AAC-LC 48kHz audio |
| UHD upload | H.264 or HEVC | 35-45 Mbps at 24-30fps, 53-68 Mbps at 48-60fps for H.264 | HEVC reaches similar quality at a lower bitrate; test the platform's ingest |
| Vertical social, 1080×1920 | H.264 MP4 | 10-20 Mbps | Platforms re-encode; upload higher than you think |
| Website background loop | H.264 MP4 plus AV1 or VP9 WebM | 1-3 Mbps, 720-1080p, 6-15s | No audio track, `muted playsinline`, poster frame, pause control |
| Broadcast | The broadcaster's spec sheet (for example DPP AS-11 in the UK) | Per spec | Legal range levels and loudness compliance |

- **Frame rate:** deliver at the source rate (see [timing and easing](timing-and-easing.md)). Convert 25↔30 or 24↔30 with proper frame-rate conversion, never by duplicating frames. Use 60fps for UI demos.
- **Color:** HD SDR is Rec.709 (BT.709 primaries, transfer and matrix). Tag files 1-1-1 so players do not shift the gamma. sRGB and Rec.709 share primaries, but broadcast viewing assumes BT.1886 (about gamma 2.4), so preview on the target class of display. Deliver HDR (Rec.2100 PQ or HLG) only when the brief asks for it, with an SDR version alongside.
- **Audio:** masters as 48kHz 24-bit WAV; delivery as AAC-LC 48kHz at 256-320 kbps stereo unless the spec says otherwise.

## Safe areas

| Frame | Rule |
| --- | --- |
| 16:9 broadcast and video | Title-safe 90% and action-safe 93% of the width and height, centered (SMPTE ST 2046-1). Many editors still default to the old 80% and 90% guides; update them. |
| 9:16 vertical social | Keep text and logos in a centered area clear of platform UI. As a rough guide, reserve the top 10-15%, the bottom 20-35% and a right-hand column of 10-15% for interface overlays. Confirm with each platform's current safe-zone template. |
| 1:1 and 4:5 feed | 5-8% margins; keep the key message in the middle 80% |
| Display loops and LED walls | Follow the venue's pixel map; keep text off module seams and bezels |

## Captions and loudness

- Captions: deliver SRT or WebVTT sidecars for web and YouTube, and burn in open captions for social autoplay. Timing and line rules are in [kinetic typography](kinetic-typography.md).
- Measure loudness with an ITU-R BS.1770 meter (built into Premiere Pro, DaVinci Resolve and Audition; or `ffmpeg -i mix.wav -af ebur128=peak=true -f null -`).

| Destination | Integrated loudness | True peak |
| --- | --- | --- |
| Streaming and social normalization | Commonly about -14 LUFS (Spotify, YouTube, Tidal and Amazon Music sit near it; Apple Music about -16) | -1 dBTP |
| European broadcast, EBU R128 | -23 LUFS ±0.5 LU (±1 LU for live) | -1 dBTP |
| US broadcast, ATSC A/85 (CALM Act) | -24 LKFS ±2 dB | -2 dBTP |
| Netflix | -27 LKFS ±2, dialogue-gated | -2 dBTP |
| Podcasts (Apple's recommendation) | -16 LUFS ±1 | -1 dBTP |

TikTok and Instagram do not publish fixed targets; mix to about -14 LUFS and check playback. LUFS and LKFS are the same measure under different names. Verify the current figures against the platform or broadcaster spec before mastering. Sound design itself is covered in [sound](sound.md).

## Stills to motion (2.5D)

- Separate the still into 3-5 depth layers (foreground, subject, midground, background, sky), and fill the plates behind the subject.
- Push the camera 3-8% over 4-8 seconds; give layers parallax ratios that increase toward the camera. Add slight drift (wiggle 0.3-0.5 per second, 2-4px) to stop it looking rigid.
- Never warp faces, products, logos or text; move them as rigid layers.

## Screen effects

Grain (2-5% opacity), light leaks, glows, particles and chromatic offsets must belong to the chosen style (see [motion system](motion-system.md)), not be added to every piece. License every stock overlay. Flash-check anything with luminance pulses or fast cuts (WCAG 2.2 SC 2.3.1; for broadcast, a recognized analyzer such as Harding FPA or PEAT). Watch the loop seam at full speed at least three times.
