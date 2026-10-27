---
type: llm
weight: 1
---

Passes if the response gives a working ffmpeg command that reads interview.mp4, drops the video (`-vn`, or a .wav output that carries audio only), resamples to 16 kHz (`-ar 16000`), downmixes to mono (`-ac 1`) and writes a WAV, typically with `pcm_s16le`. Fails if it omits the sample rate or the mono downmix.
