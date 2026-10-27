// Visual Design Kit, MIT. Part of a Remotion example; Remotion itself is NOT MIT (see README.md "Remotion license").
// Version-Timestamp: 2026-10-23 20:12:12 UTC
//
// 15s vertical social video, 1080x1920. Hook on screen from frame 0 (no logo intro),
// three points, then an end card. All text, logo and CTA stay inside the 9:16 safe box
// from the kit's social formats reference (organic: 880x1280 at 60,220; paid: 855x980 at 65,269).
// Set showSafeArea to true to draw the box while reviewing; never render it for delivery.
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {CaptionBlock} from '../components/CaptionBlock.tsx';
import {Mark} from '../components/Mark.tsx';
import {enter, useBrandFonts, useTheme, type BrandProps} from '../lib/motion.ts';
import {scaleVerticalSafe, VERTICAL_SAFE} from '../lib/safe-areas.ts';
import {socialBeats} from '../lib/schedules.ts';
import {activeCue, CAPTION_RULES, type Cue} from '../lib/timing.ts';

export interface SocialVerticalProps extends BrandProps {
  hook: string;
  points: string[];
  cta: string;
  placement: 'organic' | 'paid';
  showSafeArea: boolean;
  cues: Cue[];
}

export const SocialVertical: React.FC<SocialVerticalProps> = (props) => {
  const frame = useCurrentFrame();
  const {fps, width, height, durationInFrames} = useVideoConfig();
  const theme = useTheme(props);
  useBrandFonts(theme);
  const {durationMs: d, ease: e} = theme;
  const reduced = props.reducedMotion;
  const ms = (frame / fps) * 1000;
  const safe = scaleVerticalSafe(VERTICAL_SAFE[props.placement], width, height);
  const {beats} = socialBeats(props.hook, props.points, props.cta, (durationInFrames / fps) * 1000);
  const current = Math.max(0, activeCue(beats, ms));
  const beat = beats[current];
  const isHook = current === 0;
  const isEnd = current === beats.length - 1;
  // The hook is legible on frame 0: it only settles (scale 104% to 100%), it never fades in.
  const t = isHook ? 1 : enter(frame, fps, beat.startMs, d.slower, e.emphasizedDecelerate, reduced);
  const settle = isHook && !reduced ? 1.04 - 0.04 * enter(frame, fps, 0, d.slower, e.emphasizedDecelerate, false) : 1;
  const headSize = Math.round(width * (isHook ? 0.1 : 0.085));
  return (
    <AbsoluteFill style={{backgroundColor: isEnd ? theme.color.accent : theme.color.canvas}}>
      <div
        style={{
          position: 'absolute',
          left: safe.x,
          top: safe.y,
          width: safe.width,
          height: safe.height,
          display: 'flex',
          flexDirection: 'column',
          justifyContent: isEnd ? 'center' : 'flex-start',
          alignItems: isEnd ? 'center' : 'flex-start',
          gap: headSize * 0.5,
        }}
      >
        {isEnd ? (
          <Mark size={Math.round(width * 0.28)} ring={theme.color.onAccent} diamond={theme.color.onAccent} dot={theme.color.onAccent} ringDraw={1} diamondIn={1} dotIn={1} />
        ) : (
          <div style={{width: headSize * 1.2, height: Math.max(6, headSize * 0.1), backgroundColor: theme.color.accent}} />
        )}
        <div
          style={{
            fontFamily: theme.font.displayStack,
            fontWeight: 700,
            fontSize: headSize,
            lineHeight: 1.05,
            letterSpacing: '-0.02em',
            textAlign: isEnd ? 'center' : 'left',
            color: isEnd ? theme.color.onAccent : theme.color.fg,
            opacity: t,
            transform: reduced ? undefined : `translateY(${(1 - t) * 48}px) scale(${settle})`,
            transformOrigin: 'left top',
          }}
        >
          {beat.text}
        </div>
      </div>
      {!isEnd ? (
        <CaptionBlock
          cues={props.cues}
          ms={ms}
          theme={theme}
          safe={safe}
          maxChars={CAPTION_RULES.maxCharsVertical}
          fontSize={Math.round(width * 0.052)}
        />
      ) : null}
      {props.showSafeArea ? (
        <div
          style={{
            position: 'absolute',
            left: safe.x,
            top: safe.y,
            width: safe.width,
            height: safe.height,
            outline: '4px dashed #ff00ff',
          }}
        />
      ) : null}
    </AbsoluteFill>
  );
};
