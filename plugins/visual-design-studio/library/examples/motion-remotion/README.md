# Motion: Remotion and Lottie production example

Version-Timestamp: 2026-10-23 20:12:12 UTC

Six token-driven video compositions in Remotion, plus portable Lottie files built by the kit's stdlib script and played inside Remotion. Brand and mode switch by prop; durations and easing come from the motion tokens. The method behind it is in the motion skill's [production pipeline](../../../skills/motion/references/production-pipeline.md).

## Remotion license

Remotion is not MIT. It is source-available under the Remotion License (https://github.com/remotion-dev/remotion/blob/main/LICENSE.md). Organizations with 4 or more people, counting contractors on the project, need a Remotion Company License (https://www.remotion.dev/docs/license). Rendering with `npx remotion render`/`renderMedia()` is metered as Automators use under the v5 terms. Users of this kit are responsible for their own license.

What that means in practice (sources: the Remotion License and License FAQ in the Remotion repository, read 2026-10-23):

- **Free License:** individuals, for-profit organizations of up to 3 people, non-profits, and evaluation. Headcount is the whole company, not the number of Remotion users. Contractors and agencies you hire on the project count toward it.
- **Company License** at 4 or more people. Under the published v5.0 terms: Creators $25 per seat per month; Automators $0.01 per render with a $100 per month minimum; Enterprise from $500 per month. The v5.0 terms take effect when Remotion 5.0 ships; the current v4.0 terms (remotion.pro/terms-4-0) could not be read for this kit, so verify which terms apply to you.
- **CLI renders are automation** in the v5 terms: `npx remotion render`, `npx remotion still`, `renderMedia()`, `renderStill()` and the `<Player>` are all listed.
- **Agencies:** if the client receives only the finished video, only the agency's headcount counts. If the client owns the project, the entity that owns the IP licenses it and both headcounts combine. Confirm your case with Remotion.
- This folder's own code is MIT. Remotion stays an npm dependency: never vendor or copy its source into a project. The bundled FFmpeg in `@remotion/compositor-*` is a GPL-2.0+ build; running it is fine, redistributing the binary is not covered by this kit.

## Requirements

- Node 22.12 or later (Remotion 4 needs Node 16+, Remotion 5 will need 22), npm 10 or later.
- Linux: glibc 2.35 or later; Alpine and NixOS are not supported. Remotion downloads Chrome Headless Shell into `node_modules` (`npx remotion browser ensure`). Install the shared libraries, not Chrome. Ubuntu 24.04:

```sh
sudo apt-get install -y libnss3 libdbus-1-3 libatk1.0-0 libgbm-dev libasound2t64 libxrandr2 \
  libxkbcommon-dev libxfixes3 libxcomposite1 libxdamage1 libpango-1.0-0 libcairo2 libcups2 libatk-bridge2.0-0
```

On Ubuntu 22.04 and Debian the audio package is `libasound2`. Source: remotion-dev/remotion `packages/docs/docs/miscellaneous/linux-dependencies.mdx`.

## Run

Copy this folder into a project you own before installing; do not install into the installed plugin. Inside the kit repository it works in place.

```sh
npm ci                     # exact pins: remotion and @remotion/* 4.0.538, react 19.3.0, lottie-web 5.13.0
npm test                   # token, timing, caption, safe-area and Lottie checks; no rendering, no browser
npm run typecheck          # tsc --noEmit
npx remotion browser ensure
npm run studio             # preview and scrub every composition
```

`src/lib/tokens-data.ts` is the only file that names the token source. In the kit it imports `../../tokens/dist/tokens.resolved.json`; in a copied project, point it at your own `tokens.resolved.json` (the same format, from `scripts/tokens.py build`). The OFL fonts for both demo brands are in `public/fonts/` with their `OFL.txt` files.

## Compositions

Every composition takes `brand` (`meridian`, `ember`), `mode` (`light`, `dark`, `high-contrast`) and `reducedMotion` (true renders a variant with no spatial movement and fades of 200ms or less).

| ID | Size, length | What it shows | Key props |
| --- | --- | --- | --- |
| `LogoReveal` | 1920x1080, 5s | Original geometric placeholder mark (ring, diamond, dot) builds in about 0.8s on `ease.emphasized-decelerate`, wordmark follows, long hold | `wordmark` (defaults to the brand name) |
| `KineticType` | 1920x1080, 8s | Line mask reveal at `duration.slower` per line, 100ms line stagger, subhead and accent rule, hold of at least 1s + words / 3, exit on `ease.accelerate` | `headline`, `subhead` |
| `LowerThird` | 1920x1080, 6s | Name and role inside title-safe (90%), exit one token step shorter than the enter | `name`, `role`, `transparent` |
| `SocialVertical` | 1080x1920, 15s | Hook legible on frame 0, three points, end card; text in the kit's 9:16 safe box | `hook`, `points`, `cta`, `placement` (`organic`, `paid`), `showSafeArea`, `cues` |
| `Captions` | 1920x1080, 10s | Burned-in captions: 42 characters per line, 2 lines, inverse token box at 4.5:1 or better, cut on cue | `cues` (`startMs`, `endMs`, `text`) |
| `LottieInRemotion` | 1920x1080, 4s | A file from `public/lottie/` played with `@remotion/lottie`; reduced motion freezes on the last frame | `animation`, `loop` |

The placeholder mark is original geometry for demonstration. Replace it with the client's licensed mark; never use a third-party logo.

## Render

Each render below is a metered render under the v5 terms once you are past evaluation. Switch brand and mode with `--props`:

```sh
npx remotion render src/index.ts LogoReveal out/logo-reveal.mp4
npx remotion render src/index.ts LogoReveal out/logo-ember-dark.mp4 --props='{"brand":"ember","mode":"dark"}'
npx remotion render src/index.ts KineticType out/kinetic-reduced.mp4 --props='{"reducedMotion":true}'
npm run render:lower-third          # ProRes 4444 with alpha for an editor
npx remotion render src/index.ts SocialVertical out/social-paid.mp4 --props='{"placement":"paid"}'
```

### Posters and reduced-motion stills

A video file cannot read `prefers-reduced-motion`. Ship a poster frame and, where the player allows, a reduced-motion variant:

```sh
npx remotion still src/index.ts LogoReveal out/logo-poster.png --frame=-1
npx remotion still src/index.ts SocialVertical out/social-cover.png --frame=0
npm run stills                       # every poster in scripts/stills.mjs into out/stills/
```

`--frame=-1` is the last frame. Use the poster as `<video poster>`, as the static image when the page detects reduced motion, and as the social cover.

### Encoding presets

Remotion's bundled FFmpeg (7.1 line) encodes H.264, H.265, VP8, VP9 and ProRes only. AV1 needs a separate FFmpeg pass. Platform specs change; rows marked verify must be checked against the platform's current help page before delivery.

| Destination | Canvas | Flags (Remotion CLI) | Notes |
| --- | --- | --- | --- |
| Edit master | Source size | `--codec=prores --prores-profile=hq` | Archive and hand off this, not the H.264 |
| Overlay with alpha | 1920x1080 | `--codec=prores --prores-profile=4444 --image-format=png --pixel-format=yuva444p10le` | Lower thirds, idents |
| YouTube 1080p | 1920x1080 | `--codec=h264 --video-bitrate=8M --audio-codec=aac` (12M at 48-60fps) | YouTube's SDR upload recommendation; verify at support.google.com/youtube/answer/1722171 |
| Instagram Reels, TikTok | 1080x1920 | `--codec=h264 --video-bitrate=15M --audio-codec=aac` | 10-20 Mbps; platforms re-encode. Verify each platform's current upload spec and safe zones |
| LinkedIn | 1920x1080 or 1080x1920 | `--codec=h264 --video-bitrate=10M --audio-codec=aac` | Verify file size, length and aspect limits at LinkedIn's video specs help page before delivery |
| Web hero loop | 1280x720 to 1920x1080, 6-15s | `--codec=h264 --video-bitrate=2M --muted` plus `--codec=vp9 --video-bitrate=1.5M --muted` (`.webm`) | No audio track, `muted playsinline`, poster frame, a pause control (WCAG 2.2.2) |

Default config (`remotion.config.ts`): H.264, `yuv420p`, JPEG frames at quality 92. Master audio at 48kHz; deliver loudness at about -14 LUFS for streaming and social (see the motion skill).

## Lottie

`public/lottie/*.json` are generated; do not edit them by hand:

```sh
npm run lottie            # python3 ../../scripts/lottie_build.py examples
python3 ../../scripts/lottie_build.py build ../../scripts/lottie_specs/logo-reveal.json -o public/lottie/logo-reveal.json --brand ember --mode dark
python3 ../../scripts/lottie_build.py validate public/lottie/*.json
```

Lottie colors are baked at build time from the tokens, so rebuild with `--brand` and `--mode` for another theme (or ship a dotLottie theme). The same files play on the web with `@lottiefiles/dotlottie-web` or `lottie-web`.

## Checked here

On 2026-10-23 (Linux x64, Node 22.22.0): `npm ci`, `npm test` (20 tests), `npx tsc --noEmit` passed, and one evaluation still (`LogoReveal`, last frame) rendered under the Free License evaluation clause using a locally installed Chromium headless shell, because the Chrome Headless Shell download host was unreachable from the sandbox. Full video renders, the alpha ProRes path and platform uploads were not run; render and watch them on your machine before delivery.
