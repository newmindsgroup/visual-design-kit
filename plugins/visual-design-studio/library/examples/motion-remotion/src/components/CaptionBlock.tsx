// Visual Design Kit, MIT. Part of a Remotion example; Remotion itself is NOT MIT (see README.md "Remotion license").
// Version-Timestamp: 2026-10-23 20:12:12 UTC
//
// Burned-in (open) captions: 2 lines maximum, wrapped at a character limit, a solid
// inverse box for at least 4.5:1 contrast, anchored to the bottom of a safe box.
// Captions do not animate in; they cut on cue, which is what readers expect.
import React from 'react';
import type {Theme} from '../lib/theme.ts';
import type {Box} from '../lib/safe-areas.ts';
import {activeCue, checkCue, type Cue} from '../lib/timing.ts';

export interface CaptionBlockProps {
  cues: Cue[];
  ms: number;
  theme: Theme;
  safe: Box;
  maxChars: number;
  fontSize: number;
}

export const CaptionBlock: React.FC<CaptionBlockProps> = ({cues, ms, theme, safe, maxChars, fontSize}) => {
  const index = activeCue(cues, ms);
  if (index < 0) return null;
  const {lines} = checkCue(cues[index], maxChars);
  return (
    <div
      style={{
        position: 'absolute',
        left: safe.x,
        width: safe.width,
        top: safe.y,
        height: safe.height,
        display: 'flex',
        alignItems: 'flex-end',
        justifyContent: 'center',
        pointerEvents: 'none',
      }}
    >
      <div
        style={{
          backgroundColor: theme.color.inverse,
          color: theme.color.fgInverse,
          fontFamily: theme.font.bodyStack,
          fontWeight: 600,
          fontSize,
          lineHeight: 1.25,
          textAlign: 'center',
          padding: `${fontSize * 0.2}px ${fontSize * 0.45}px`,
          borderRadius: fontSize * 0.18,
          maxWidth: '100%',
        }}
      >
        {lines.slice(0, 2).map((line, i) => (
          <div key={i}>{line}</div>
        ))}
      </div>
    </div>
  );
};
