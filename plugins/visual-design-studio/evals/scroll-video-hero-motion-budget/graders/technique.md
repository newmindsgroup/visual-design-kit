---
type: llm
weight: 3
---

Passes only if the response specifies a working scroll-scrub mechanism:
- Scroll progress mapped to video time on a sticky or pinned stage with a scroll runway (for example a section several viewports tall), smoothed with a lerp around 0.1-0.15 per frame, and no autoplay.
- Seeks guarded so the decoder is not flooded (seek only when the video is not already seeking, or a pre-extracted canvas frame cache or image sequence).
- A scrub-ready encode with short keyframe intervals (for example `-g 1` to `-g 6`, all-intra, or an image sequence) and a smaller mobile version.
- A poster or first frame that paints before the video, and a touch or small-screen fallback.

Fails if it simply autoplays the clip or binds `currentTime` to every scroll event with no smoothing or seek guard.
