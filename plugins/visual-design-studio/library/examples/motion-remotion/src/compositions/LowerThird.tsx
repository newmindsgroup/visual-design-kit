// Visual Design Kit, MIT. Part of a Remotion example; Remotion itself is NOT MIT (see README.md "Remotion license").
// Version-Timestamp: 2026-10-23 20:12:12 UTC
//
// 6s lower third inside 16:9 title-safe. Accent bar wipes in, name and role rise on
// ease.emphasized-decelerate, hold, then exit on ease.accelerate one token step shorter.
// Render with alpha (ProRes 4444) using props/lower-third-alpha.json for overlay in an editor.
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {enter, progress, useBrandFonts, useTheme, type BrandProps} from '../lib/motion.ts';
import {titleSafe} from '../lib/safe-areas.ts';

export interface LowerThirdProps extends BrandProps {
  name: string;
  role: string;
  /** Transparent background for alpha renders. */
  transparent: boolean;
}

export const LowerThird: React.FC<LowerThirdProps> = (props) => {
  const frame = useCurrentFrame();
  const {fps, width, height, durationInFrames} = useVideoConfig();
  const theme = useTheme(props);
  useBrandFonts(theme);
  const {durationMs: d, ease: e} = theme;
  const reduced = props.reducedMotion;
  const totalMs = (durationInFrames / fps) * 1000;
  const bar = enter(frame, fps, 200, d.slower, e.emphasizedDecelerate, reduced);
  const nameIn = enter(frame, fps, reduced ? 200 : 320, d.slower, e.emphasizedDecelerate, reduced);
  const roleIn = enter(frame, fps, reduced ? 200 : 420, d.slower, e.emphasizedDecelerate, reduced);
  const exitMs = d.slow;
  const exit = progress(frame, fps, totalMs - exitMs - 200, reduced ? Math.min(200, exitMs) : exitMs, e.accelerate);
  const safe = titleSafe(width, height);
  const nameSize = Math.round(height * 0.05);
  return (
    <AbsoluteFill style={{backgroundColor: props.transparent ? 'transparent' : theme.color.canvas}}>
      <div
        style={{
          position: 'absolute',
          left: safe.x,
          bottom: height - (safe.y + safe.height),
          display: 'flex',
          alignItems: 'stretch',
          gap: nameSize * 0.45,
          opacity: 1 - exit,
          transform: reduced ? undefined : `translateX(${exit * -40}px)`,
        }}
      >
        <div
          style={{
            width: Math.max(6, Math.round(nameSize * 0.14)),
            backgroundColor: theme.color.accent,
            transformOrigin: 'center bottom',
            transform: reduced ? undefined : `scaleY(${bar})`,
            opacity: reduced ? bar : 1,
          }}
        />
        <div
          style={{
            backgroundColor: theme.color.surface,
            padding: `${nameSize * 0.32}px ${nameSize * 0.6}px`,
            borderRadius: 8,
            overflow: 'hidden',
          }}
        >
          <div
            style={{
              fontFamily: theme.font.displayStack,
              fontWeight: 700,
              fontSize: nameSize,
              lineHeight: 1.1,
              color: theme.color.fg,
              opacity: nameIn,
              transform: reduced ? undefined : `translateY(${(1 - nameIn) * 40}%)`,
            }}
          >
            {props.name}
          </div>
          <div
            style={{
              fontFamily: theme.font.bodyStack,
              fontSize: Math.round(nameSize * 0.56),
              lineHeight: 1.3,
              color: theme.color.fgMuted,
              opacity: roleIn,
              transform: reduced ? undefined : `translateY(${(1 - roleIn) * 40}%)`,
            }}
          >
            {props.role}
          </div>
        </div>
      </div>
    </AbsoluteFill>
  );
};
