// Visual Design Kit, MIT. Part of a Remotion example; Remotion itself is NOT MIT (see README.md "Remotion license").
// Version-Timestamp: 2026-10-23 20:12:12 UTC
//
// Every composition takes {brand, mode, reducedMotion}. Switch brand and mode with --props, e.g.
//   npx remotion render src/index.ts LogoReveal out/ember-dark.mp4 --props='{"brand":"ember","mode":"dark"}'
import React from 'react';
import {Composition} from 'remotion';
import {Captions, type CaptionsProps} from './compositions/Captions.tsx';
import {KineticType, type KineticTypeProps} from './compositions/KineticType.tsx';
import {LogoReveal, type LogoRevealProps} from './compositions/LogoReveal.tsx';
import {LottieInRemotion, type LottieInRemotionProps} from './compositions/LottieInRemotion.tsx';
import {LowerThird, type LowerThirdProps} from './compositions/LowerThird.tsx';
import {SocialVertical, type SocialVerticalProps} from './compositions/SocialVertical.tsx';
import {defaultBrandProps} from './lib/motion.ts';
import type {Cue} from './lib/timing.ts';

export const FPS = 30;

const landscapeCues: Cue[] = [
  {startMs: 300, endMs: 3100, text: 'Every launch starts with one clear sentence.'},
  {startMs: 3300, endMs: 6100, text: 'Captions stay inside title-safe and hold still.'},
  {startMs: 6300, endMs: 9000, text: 'Two lines at most, cut on the cue.'},
];

const verticalCues: Cue[] = [
  {startMs: 3200, endMs: 6000, text: 'Set the tokens once.'},
  {startMs: 6200, endMs: 9000, text: 'Every format follows them.'},
  {startMs: 9200, endMs: 11800, text: 'Then export to spec.'},
];

export const RemotionRoot: React.FC = () => (
  <>
    <Composition
      id="LogoReveal"
      component={LogoReveal}
      durationInFrames={5 * FPS}
      fps={FPS}
      width={1920}
      height={1080}
      defaultProps={{...defaultBrandProps, wordmark: ''} satisfies LogoRevealProps}
    />
    <Composition
      id="KineticType"
      component={KineticType}
      durationInFrames={8 * FPS}
      fps={FPS}
      width={1920}
      height={1080}
      defaultProps={
        {
          ...defaultBrandProps,
          headline: 'Design that ships finished',
          subhead: 'Tokens drive every frame, from brand to broadcast.',
        } satisfies KineticTypeProps
      }
    />
    <Composition
      id="LowerThird"
      component={LowerThird}
      durationInFrames={6 * FPS}
      fps={FPS}
      width={1920}
      height={1080}
      defaultProps={{...defaultBrandProps, name: 'Alex Rivera', role: 'Head of Design', transparent: false} satisfies LowerThirdProps}
    />
    <Composition
      id="SocialVertical"
      component={SocialVertical}
      durationInFrames={15 * FPS}
      fps={FPS}
      width={1080}
      height={1920}
      defaultProps={
        {
          ...defaultBrandProps,
          hook: 'Your brand, in every format',
          points: ['One token file', 'Six video formats', 'Zero manual resizing'],
          cta: 'Start with the kit',
          placement: 'organic',
          showSafeArea: false,
          cues: verticalCues,
        } satisfies SocialVerticalProps
      }
    />
    <Composition
      id="Captions"
      component={Captions}
      durationInFrames={10 * FPS}
      fps={FPS}
      width={1920}
      height={1080}
      defaultProps={{...defaultBrandProps, cues: landscapeCues} satisfies CaptionsProps}
    />
    <Composition
      id="LottieInRemotion"
      component={LottieInRemotion}
      durationInFrames={4 * FPS}
      fps={FPS}
      width={1920}
      height={1080}
      defaultProps={{...defaultBrandProps, animation: 'logo-reveal', loop: false} satisfies LottieInRemotionProps}
    />
  </>
);
