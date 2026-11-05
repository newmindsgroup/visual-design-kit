# Media for the web: hero video, posters and cut-outs

Version-Timestamp: 2026-11-05 18:10:00 UTC

Adapted from MotionSites claude-skill (MIT), see NOTICE.md.

Cinematic pages are carried by their media, so choose it before the layout. This reference covers sourcing, generating and preparing hero video loops, poster frames and transparent cut-outs for the web. Rights, provenance and AI rules come from [AI image generation](ai-image-generation.md) and the kit's [asset licenses](../../../library/knowledge/ASSETS-LICENSES.md); performance budgets from `web-design`'s [performance](../../web-design/references/performance.md). The recipes that play this media are in [video and media](../../../library/knowledge/web-techniques/video-and-media.md).

## Sourcing order

1. **The client's assets:** footage, product photography, renders, GLB models. Ask once when the brief clearly needs them; do not block on it otherwise. Confirm the client holds the rights for web use (model and property releases for people and places).
2. **Generated media,** when an image, video or 3D tool is available and the brief allows AI imagery for the role (backgrounds, abstract or stylized scenes, concept objects). Never fake product photos, customers, testimonials or events. Use the formulas below, written with `prompt-engineering-expert` when installed.
3. **Licensed stock** under a license recorded in the provenance file, when the client approves it.
4. **No media:** a type-, gradient- and motion-led page (a mega word with micro-labels, monochrome with grain and one static light falloff at 8 % alpha or less, a dot grid at 5 %, a large inline-SVG mark). No grey placeholder boxes, random stock or lorem-picsum.

Check every URL before relying on it (a ranged GET, or `render_review.mjs`, which reports failed requests and video errors). Never invent URLs or file paths. Never use media showing recognizable people, characters, celebrities, logos, packaging or other brands without a release or license.

## What makes hero media work

- **One subject, one continuous shot, no cuts.** Slow movement: a gentle orbit, drift, float, turn in place or slow push-in. Nothing enters or leaves the frame.
- **Loopable:** the end matches the start, or the loop is hidden with a fade, a boomerang or a crossfade.
- **Edges fall off to one flat color** that becomes the page background, so no seam and no overlay are needed.
- **A defined empty zone** (left half, top 35-40 %, or a bottom band) where the copy sits for the entire loop.
- **A restrained palette:** 2-3 hues plus one luminous highlight (rim light, glow, sunset band) against a dark or neutral field.
- **A cinematic grade:** 24 fps, soft volumetric light, shallow depth of field; often a CGI render or illustration rather than stock.
- **No text, logos, UI or watermark** inside the footage. Live type goes in the layout.
- **Paired stills** (spotlight reveal, parallax layers) are pixel-aligned: the same composition in two materials, or separated layers.

Archetypes that work: an isolated object on a studio sweep that reads as a void (glass, chrome, silk, a floating island); a stylized 3D character on a saturated flat backdrop; a painterly landscape with a low horizon and a tiny figure; a surreal minimal scene; a studio product or fashion shot on white; abstract terrain with a single rim glow.

## Generating stills and loops

Workflow: generate a still keyframe (16:9, 2K or more), animate it image-to-video for 5-10 s, make it loop, then prepare it with the commands below and pull a poster from the first frame.

Still (keyframe) formula:

```text
[shot type] of [ONE subject], [material and finish], [pose or state],
placed in the [right third | lower half | centre-bottom], occupying about 30% of the frame,
[studio sweep backdrop | environment] that falls off to pure [#000000 | #FFFFFF | brand hex] at all edges,
[lighting: soft rim light | volumetric haze | single warm key],
palette limited to [2-3 colors], [one luminous highlight],
[style: photoreal CGI render | 35mm film still, shallow depth of field | hand-painted background | high-key studio],
large empty negative space on the [left half | top 40%] reserved for a headline,
no text, no logos, no UI, no watermark, 16:9.
```

Motion (image-to-video) formula:

```text
Single continuous shot, no cuts. Camera: [locked | very slow push-in about 5% | slow 15-degree orbit].
Subject: [rotates slowly in place | floats gently | grass sways | fabric ripples | light pulses softly].
Nothing enters or leaves the frame; background stays flat [color]; lighting constant.
Slow and calm, about half real-time. 24 fps, 8-10 seconds, loop: last frame matches first.
```

Cut-out sets: "full body [subject] isolated on flat [chroma color], even studio light, 3:4, consistent style across the set", then remove the background and export WebP with alpha.

Rules from [AI image generation](ai-image-generation.md) apply unchanged: describe attributes, never a living artist's name or style; no other brands' logos, products or characters; no identifiable real people without written consent; keep the provenance record (tool, model and version, date, prompt, references and their rights, edits, approver) and preserve C2PA Content Credentials through export, because the encode steps below strip metadata unless you carry it over.

Checks before using generated media:

- Look at frames at 0 %, 50 % and 100 %: the text zone is empty in all three.
- The edges equal the page background.
- No stray text, extra limbs or artifacts.
- The loop seam is invisible after three plays.

If a check fails, fix it with `object-position` or oversizing, or regenerate. Do not hide it under a dark overlay.

## Budgets

| Asset | Default | Change when |
| --- | --- | --- |
| Poster frame | WebP (or AVIF), 1920 px wide, 200 KB or less; it is the reduced-motion still and usually the LCP element | Text-only heroes: no poster needed |
| Desktop hero loop | H.264 MP4, 1920x1080, 24 fps, no audio, 6-12 s, 2-5 MB (CRF 26-28); a VP9 WebM as a second `<source>` is optional | The video is the product (a film, a demo): up to about 8 MB, or HLS for longer clips |
| Mobile loop | 960 px wide, CRF 28, 1 MB or less; play only when the video is the product, otherwise show the poster | Save-Data or a 2G/3G connection: poster only |
| Scrub clip | Short GOP (`-g 6`, or `-g 1` all-intra), 960 px, 15 MB or less loaded fully before scrubbing | Never autoplay a scrub clip |
| Cut-out | WebP with alpha, 500 KB or less, sized to its largest rendered height at 2x | Many cut-outs on one page: 1x plus `srcset` |
| 3D model | GLB 3-5 MB with Draco and WebP textures at 1-2K, plus a PNG fallback render | See [3D](3d.md) |

## Preparing video (ffmpeg)

Each command below was run with ffmpeg 6.1 on a test clip before publication.

```sh
# Web MP4: H.264, 1080p, 24 fps, no audio, fast start
ffmpeg -i in.mp4 -an -vf "scale=1920:-2,fps=24" -c:v libx264 -preset slow -crf 26 -pix_fmt yuv420p -movflags +faststart hero.mp4
# Mobile version
ffmpeg -i in.mp4 -an -vf "scale=960:-2,fps=24" -c:v libx264 -preset slow -crf 28 -pix_fmt yuv420p -movflags +faststart hero-mobile.mp4
# Optional VP9 WebM, listed first as a <source> where it is smaller
ffmpeg -i in.mp4 -an -vf "scale=1920:-2,fps=24" -c:v libvpx-vp9 -crf 36 -b:v 0 -row-mt 1 hero.webm
# Poster: first frame as WebP
ffmpeg -i hero.mp4 -frames:v 1 -vf "scale=1920:-2" -c:v libwebp -quality 80 poster.webp
# Loop: crossfade the last second into the first (for an 8 s clip; the result is 7 s)
ffmpeg -i in.mp4 -filter_complex "[0]split[a][b];[a]trim=1:8,setpts=PTS-STARTPTS[main];[b]trim=0:1,setpts=PTS-STARTPTS[head];[main][head]xfade=transition=fade:duration=1:offset=6[v]" -map "[v]" -an -c:v libx264 -pix_fmt yuv420p loop.mp4
# Boomerang: forward then reversed (doubles the length; keep sources 3-5 s)
ffmpeg -i in.mp4 -filter_complex "[0:v]split[a][b];[b]reverse[r];[a][r]concat=n=2:v=1:a=0[out]" -map "[out]" -an -c:v libx264 -crf 20 -pix_fmt yuv420p -movflags +faststart boomerang.mp4
# Scrub-ready: keyframe every 6 frames so seeks land instantly
ffmpeg -i in.mp4 -an -c:v libx264 -crf 20 -g 6 -keyint_min 6 -pix_fmt yuv420p -movflags +faststart scrub.mp4
# Cut-out: PNG with alpha to WebP with alpha
ffmpeg -i cutout.png -c:v libwebp -quality 85 -lossless 0 cutout.webp
```

`reverse` buffers the whole clip in memory; keep boomerang sources short. FFmpeg builds can be GPL; running them is fine, redistributing binaries is not (see [asset licenses](../../../library/knowledge/ASSETS-LICENSES.md)).

## Placing media

- **Background video:** `position:absolute; inset:0; width:100%; height:100%; object-fit:cover`, with `muted loop playsinline`, a `poster`, `aria-hidden="true"` when decorative, and `preload="metadata"` until you decide to autoplay (desktop and fast connections). Fade it in on `loadeddata`. A visible pause control is required for loops longer than 5 s (WCAG 2.2.2).
- **Focal control:** `object-position` (for example `70% center`), oversize to 110-120 % (top-aligned) or translate, so the subject lands away from the text.
- **Mobile:** re-aim `object-position`, or move the media below the text in a square or 4:5 frame with a reserved `aspect-ratio`.
- **Cut-outs:** `object-fit: contain; object-position: bottom`, sized by viewport height, `draggable="false"`, `pointer-events: none`, preloaded with `new Image()`.
- **Tiles:** a rounded container with `overflow: hidden` and a fixed aspect ratio; hover and focus zoom 1.05 over 700 ms; a bottom gradient only where text sits on the tile.
- **HLS (`.m3u8`):** native playback where `video.canPlayType('application/vnd.apple.mpegurl')` succeeds, otherwise hls.js (Apache-2.0, pinned in the [technique index](../../../library/knowledge/web-techniques/INDEX.md#libraries-and-licenses)).
- **Alt text:** decorative media gets `alt=""` or `aria-hidden="true"`; meaningful images get alt text that states their purpose.

## Hand-off record

For each media file record: source (client, generated, licensed), license or release, provenance for generated media, encode settings, sizes, poster path and the reduced-motion behavior. Tell the client which files are stand-ins to replace before launch.
