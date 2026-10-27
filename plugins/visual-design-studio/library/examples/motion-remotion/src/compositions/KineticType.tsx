// Visual Design Kit, MIT. Part of a Remotion example; Remotion itself is NOT MIT (see README.md "Remotion license").
// Version-Timestamp: 2026-10-23 20:12:12 UTC
//
// 8s headline and subhead. Technique: line mask reveal (each line rises from behind a clip),
// duration.slower per line on ease.emphasized-decelerate, 100ms line stagger, then the subhead.
// Everything holds still for at least 1s + words / 3 before a short exit on ease.accelerate.
import React from 'react';
import {AbsoluteFill, getRemotionEnvironment, useCurrentFrame, useVideoConfig} from 'remotion';
import {enter, progress, useBrandFonts, useTheme, type BrandProps} from '../lib/motion.ts';
import {titleSafe} from '../lib/safe-areas.ts';
import {kineticSchedule, LINE_STAGGER_MS} from '../lib/schedules.ts';

export interface KineticTypeProps extends BrandProps {
  headline: string;
  subhead: string;
}

export const KineticType: React.FC<KineticTypeProps> = (props) => {
  const frame = useCurrentFrame();
  const {fps, width, height, durationInFrames} = useVideoConfig();
  const theme = useTheme(props);
  useBrandFonts(theme);
  const {durationMs: d, ease: e} = theme;
  const reduced = props.reducedMotion;
  const totalMs = (durationInFrames / fps) * 1000;
  const plan = kineticSchedule(props.headline, props.subhead, d.slower, d.slow, totalMs);
  const exit = reduced ? 0 : progress(frame, fps, plan.exitStart, d.slow, e.accelerate);
  const safe = titleSafe(width, height);
  const fontSize = Math.round(height * 0.11);
  return (
    <AbsoluteFill style={{backgroundColor: theme.color.canvas}}>
      <div
        style={{
          position: 'absolute',
          left: safe.x + safe.width * 0.06,
          top: safe.y,
          width: safe.width * 0.88,
          height: safe.height,
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
          opacity: 1 - exit,
          transform: `translateY(${exit * -32}px)`,
        }}
      >
        <h1
          style={{
            margin: 0,
            fontFamily: theme.font.displayStack,
            fontWeight: 700,
            fontSize,
            lineHeight: 1.05,
            letterSpacing: '-0.02em',
            color: theme.color.fg,
          }}
        >
          {plan.lines.map((line, i) => {
            const t = enter(frame, fps, reduced ? 0 : i * LINE_STAGGER_MS, d.slower, e.emphasizedDecelerate, reduced);
            return (
              <span key={i} style={{display: 'block', overflow: 'hidden', paddingBottom: fontSize * 0.08}}>
                <span
                  style={{
                    display: 'block',
                    opacity: reduced ? t : 1,
                    transform: reduced ? undefined : `translateY(${(1 - t) * 110}%)`,
                  }}
                >
                  {line}
                </span>
              </span>
            );
          })}
        </h1>
        <p
          style={{
            margin: `${fontSize * 0.35}px 0 0`,
            maxWidth: '32ch',
            fontFamily: theme.font.bodyStack,
            fontSize: Math.round(fontSize * 0.38),
            lineHeight: 1.35,
            color: theme.color.fgMuted,
            opacity: enter(frame, fps, reduced ? 0 : plan.subStart, d.slower, e.decelerate, reduced),
          }}
        >
          {props.subhead}
        </p>
        <div
          style={{
            marginTop: fontSize * 0.45,
            height: Math.max(4, Math.round(height * 0.006)),
            width: safe.width * 0.12,
            backgroundColor: theme.color.accent,
            transformOrigin: 'left center',
            transform: `scaleX(${enter(frame, fps, reduced ? 0 : plan.subStart + 120, d.slower, e.emphasizedDecelerate, reduced)})`,
          }}
        />
      </div>
      {!plan.fits && getRemotionEnvironment().isStudio ? (
        <div style={{position: 'absolute', top: 16, left: 16, color: 'red', fontSize: 24}}>
          Copy too long: the hold rule (1s + words / 3) does not fit before the exit
        </div>
      ) : null}
    </AbsoluteFill>
  );
};
