// Visual Design Kit, MIT. Part of a Remotion example; Remotion itself is NOT MIT (see README.md "Remotion license").
// Version-Timestamp: 2026-10-23 20:12:12 UTC
//
// 5s at 1920x1080: the mark builds in about 0.8s, the wordmark follows, then a long hold
// (an ident is a brand moment: up to 3s of motion, the rest legible stillness).
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {Mark} from '../components/Mark.tsx';
import {enter, useBrandFonts, useTheme, type BrandProps} from '../lib/motion.ts';

export interface LogoRevealProps extends BrandProps {
  wordmark: string;
}

export const LogoReveal: React.FC<LogoRevealProps> = (props) => {
  const frame = useCurrentFrame();
  const {fps, width} = useVideoConfig();
  const theme = useTheme(props);
  useBrandFonts(theme);
  const {durationMs: d, ease: e} = theme;
  const reduced = props.reducedMotion;
  const stagger = 160;
  const ringDraw = enter(frame, fps, 0, d.slower, e.emphasizedDecelerate, reduced);
  const diamondIn = enter(frame, fps, reduced ? 0 : stagger, d.slow, e.emphasizedDecelerate, reduced);
  const dotIn = enter(frame, fps, reduced ? 0 : stagger * 2, d.moderate, e.emphasizedDecelerate, reduced);
  const wordIn = enter(frame, fps, reduced ? 0 : stagger * 2 + d.moderate, d.slower, e.decelerate, reduced);
  const markSize = Math.round(width * 0.17);
  return (
    <AbsoluteFill style={{backgroundColor: theme.color.canvas, alignItems: 'center', justifyContent: 'center'}}>
      <div style={{display: 'flex', alignItems: 'center', gap: markSize * 0.18, opacity: reduced ? ringDraw : 1}}>
        <Mark
          size={markSize}
          ring={theme.color.accent}
          diamond={theme.color.fg}
          dot={theme.color.accent}
          ringDraw={reduced ? 1 : ringDraw}
          diamondIn={reduced ? 1 : diamondIn}
          dotIn={reduced ? 1 : dotIn}
        />
        <div
          style={{
            fontFamily: theme.font.displayStack,
            fontWeight: 650,
            fontSize: markSize * 0.42,
            letterSpacing: '-0.02em',
            color: theme.color.fg,
            opacity: wordIn,
            transform: reduced ? undefined : `translateX(${(1 - wordIn) * -24}px)`,
          }}
        >
          {props.wordmark || theme.brandName}
        </div>
      </div>
    </AbsoluteFill>
  );
};
