// Visual Design Kit, MIT. Uses Remotion, which is NOT MIT (see README.md "Remotion license").
// Under the v5 terms, `npx remotion still` counts as automation (metered renders). Check your license first.
// Version-Timestamp: 2026-10-23 20:12:12 UTC
//
// Static poster frames: the reduced-motion fallback, video poster and social cover for each composition.
// Usage: npm run stills [-- --browser-executable=/path/to/chrome-headless-shell]
import {spawnSync} from 'node:child_process';

export const POSTERS = [
  {id: 'LogoReveal', frame: -1, out: 'logo-reveal-poster.png'},
  {id: 'KineticType', frame: 180, out: 'kinetic-type-poster.png'},
  {id: 'LowerThird', frame: 90, out: 'lower-third-poster.png'},
  {id: 'SocialVertical', frame: 0, out: 'social-vertical-cover.png'},
  {id: 'SocialVertical', frame: -1, out: 'social-vertical-end-card.png'},
  {id: 'Captions', frame: 30, out: 'captions-poster.png'},
  {id: 'LottieInRemotion', frame: -1, out: 'lottie-in-remotion-poster.png'},
];

const extra = process.argv.slice(2);
let failed = 0;
for (const poster of POSTERS) {
  const args = ['remotion', 'still', 'src/index.ts', poster.id, `out/stills/${poster.out}`, `--frame=${poster.frame}`, ...extra];
  console.log(`> npx ${args.join(' ')}`);
  const result = spawnSync('npx', args, {stdio: 'inherit'});
  if (result.status !== 0) failed++;
}
process.exit(failed ? 1 : 0);
