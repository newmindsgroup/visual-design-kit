---
id: channel.video-motion
axis: channel
name: Video and Motion
aliases: [video, motion graphics, brand film, explainer, animation, title sequence, video ad, lottie, kinetic type]
summary: Time-based work from brand films and ads to UI animation and social video, where aspect ratio, frame rate, codec, loudness and caption choices must be fixed before the first frame.
tags: [video, motion graphics, animation, brand film, explainer, codec, loudness, captions, lottie, after effects]
pairs_with: [style.kinetic-experimental-type, style.retro-futurism-synthwave, style.glass-spatial, style.illustrative-narrative, style.bold-geometric-sport, industry.media-entertainment-streaming, industry.gaming-esports, industry.ai-products, archetype.magician, archetype.hero]
avoid_with: [audience.low-bandwidth-entry-devices]
version_timestamp: 2026-10-20 02:01:01 UTC
---

# Video and Motion

## Formats and specs

Delivery specs are set by the destination. Confirm with the broadcaster, platform or festival before mastering (YouTube Help, Netflix Partner Help Center, EBU, ATSC, Meta and TikTok creative specs). Figures are as of 2026.

| Item | Spec | Notes |
| --- | --- | --- |
| Resolution and ratio | 16:9 1920x1080 (HD) master; 3840x2160 (UHD) for premium delivery; 9:16 1080x1920; 4:5 1080x1350; 1:1 1080x1080 | Design once, protect for crops: keep action in the central 1:1 where reframing is needed |
| Frame rate | 24 / 23.976 (cinematic), 25 (PAL regions), 29.97 / 30 (NTSC regions, web), 50, 59.94 / 60 (sports, UI capture) | Keep the source rate; avoid conversion; motion graphics at 24-30 fps feels filmic, 60 fps for UI |
| Delivery codec | H.264 (AVC) High profile MP4, 4:2:0, 8-bit, closed GOP, moov atom first; H.265 / HEVC and AV1 where supported | YouTube recommends about 8 Mbps for 1080p SDR at 24-30 fps and 12 Mbps at 48-60 fps, AAC-LC audio at 48 kHz |
| Master and intermediate | Apple ProRes 422 HQ (4444 for alpha), DNxHR HQ/HQX; image sequences (EXR, PNG) for VFX | Archive masters; deliver compressed files |
| Color | SDR: Rec.709 (gamma 2.4 for broadcast, sRGB for web screen capture); HDR: Rec.2020 with PQ (HDR10) or HLG; Display P3 for Apple devices | Tag the file; do not mix color spaces in one timeline |
| Audio | 48 kHz, 24-bit master; AAC-LC 192-384 kbps stereo for delivery; 5.1 for cinema and broadcast when required | Mix for sound-off first |
| Loudness | Broadcast: EBU R128 at -23 LUFS integrated (tolerance about 0.5-1 LU), true peak -1 dBTP; US ATSC A/85 at -24 LKFS (plus or minus 2 dB), true peak about -2 dBTP; online platforms typically normalize around -14 LUFS | Verify the destination's spec; mastering louder than the platform target gains nothing |
| Safe areas | Title safe about 90% and action safe about 93% (legacy broadcast); vertical platforms: keep text clear of top 14% and bottom 20-35% for UI overlays | Use the platform's safe-zone guides |
| Captions | SRT or WebVTT sidecar files, about 32-42 characters per line (Netflix allows 42), two lines maximum, 1-6 seconds on screen; open captions burned in for social | WCAG 1.2.2 captions (A), 1.2.5 audio description (AA) |
| Photosensitivity | No more than 3 flashes in any one second (WCAG 2.3.1); test broadcast with a Harding-type analyzer | Avoid saturated red flashes and high-contrast strobing |
| Web video | MP4 H.264 plus WebM / AV1, poster frame, `preload="metadata"`, muted autoplay with `playsinline` for ambient loops, hero loops under 2-5 MB | Use Lottie / dotLottie or Rive for vector UI animation |
| UI animation | 100-200ms feedback, 200-320ms transitions, 400-600ms entrances; easing `cubic-bezier(0.2, 0, 0, 1)` | See kit tokens `--duration-*` and `--ease-*` |

## Structure and hierarchy

- **Story structure:** hook (first 1-3 seconds), promise, evidence or demonstration, payoff, brand and action. Social ads front-load the brand cue and message because skip and scroll decisions happen early.
- **Shot design:** one idea per shot, 2-4 seconds average for explainers, 1-2 seconds for fast social cuts, longer holds for emotional beats. Create a visual rhythm: wide, medium, close; alternate movement directions.
- **Brand motion language:** define 3-5 motion principles (speed, ease, direction, depth, sound) and map them to the brand's archetype: Hero uses fast ease-out and diagonals; Caregiver uses slow decelerations; Jester uses overshoot; Ruler uses restrained fades. Document logo animation (2-5 seconds), transitions, lower thirds and end cards.
- **Typography on screen:** kinetic type must be readable for the time shown: allow about 0.3 seconds per word plus 1 second, minimum.
- **Sound:** voice-over, music and effects layers; leave headroom; match the cut to the beat; always provide a silent-viewing version with captions.
- **Versioning:** plan cutdowns (30 / 15 / 6 seconds) and aspect ratios from the start; design in layers so crops and language changes are simple.

### Timing reference

| Element | Duration |
| --- | --- |
| Micro-interaction (hover, toggle, press) | 100-200ms |
| UI transition (screen, panel, menu) | 200-350ms |
| Hero entrance or brand reveal | 400-800ms |
| Lower third | 0.4s in, 4-6s hold, 0.4s out |
| Title card | 2-4s |
| Logo animation or sting | 2-5s |
| End card with CTA | 3-5s |
| Explainer shot | 2-4s average |
| Fast social cut | 1-2s |
| Ad lengths | 6s bumper, 15s, 30s, 60s |

## Craft defaults

- Type on video: sans-serif weights 500+ at 5-7% of frame height for headlines (54-76 px on 1080 tall), 3-4% for captions; stroke or shadow only if the background varies; contrast 4.5:1.
- Easing: avoid linear motion except for loops and progress bars; use ease-out for entrances (decelerate), ease-in for exits, ease-in-out for movement across the screen; stagger lists by 30-60ms.
- Timing: animate state changes in 200-400ms; hold finished frames for reading time (words per second guideline of 3-4 for on-screen text).
- Color: grade to a defined look (LUT) after conforming; check SDR and HDR versions separately; protect skin tones; avoid crushed blacks in dark UI.
- Camera and 3D: choose lens, depth of field and lighting that match the brand; keep CGI materials physically plausible; motion blur 180-degree shutter equivalent for filmic movement.
- Loop design: ambient loops join cleanly at the first and last frame, under 10 seconds, and pausable (WCAG 2.2.2 pause, stop, hide for motion over 5 seconds).
- Reduced motion: provide a still or slower variant for `prefers-reduced-motion`; avoid parallax and large-scale motion that can cause vestibular discomfort.

## Production and handoff

- Pipeline: brief, script, storyboard / animatic, style frames, design, animation (After Effects, Blender, Cinema 4D, Rive, Remotion, Figma motion), edit (Premiere Pro, DaVinci Resolve, Final Cut), color, sound mix, QC, delivery. The `motion` skill holds the deeper principles and pipeline guide.
- Hand off: project files with organized layers and named comps, fonts and licensed assets, a style frame deck, expressions and plugins list, LUTs, captions, music licenses, and render presets.
- UI animation handoff: Lottie / dotLottie JSON with a performance check (file under 100 KB for icons), Rive state machines, or CSS / GSAP / SwiftUI / Compose code with timing tokens; avoid After Effects effects that do not export.
- Delivery: run QC for black frames, loudness, safe areas, frame rate, audio sync, color, caption timing and file naming (campaign_version_ratio_duration_language).
- Rights: music, stock footage, talent releases, trademark clearance, and AI-generated media disclosure policies for the platform or broadcaster. Confirm with counsel.

## QA checklist

- [ ] Aspect ratio, resolution, frame rate and codec match the destination spec.
- [ ] Loudness measured (LUFS / LKFS and true peak) and within the target; dialog is intelligible on phone speakers.
- [ ] Captions present, accurate, synchronized; on-screen text readable with sound off.
- [ ] Text and logos inside safe areas for every aspect ratio and platform overlay.
- [ ] No flashing above 3 per second; motion respects reduced-motion alternatives.
- [ ] First 3 seconds hook; brand visible; CTA clear at the end for 2-3 seconds.
- [ ] No black frames, glitches, banding in gradients, or wrong color tags.
- [ ] Licenses, releases and credits documented.

## Reference anchors

- Disney's 12 principles of animation (Thomas and Johnston, *The Illusion of Life*, 1981)
- Material Design 3 motion guidance and Apple HIG motion guidance for UI animation
- EBU R128 (tech.ebu.ch) and ATSC A/85 loudness recommendations; ITU-R BS.1770 measurement
- YouTube Help "recommended upload encoding settings"; Netflix Partner Help Center delivery specifications
- Saul Bass title sequences, Pablo Ferro, and Imaginary Forces for title and motion design craft
