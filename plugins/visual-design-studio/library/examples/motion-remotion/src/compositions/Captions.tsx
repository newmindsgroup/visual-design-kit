// Visual Design Kit, MIT. Part of a Remotion example; Remotion itself is NOT MIT (see README.md "Remotion license").
// Version-Timestamp: 2026-10-23 20:12:12 UTC
//
// Caption styling reference at 1920x1080: 42 characters per line maximum, 2 lines,
// inside title-safe (90%), 48px semibold on the inverse token box. Swap `cues` for a
// transcript (e.g. parsed from SRT). Always also deliver the SRT or WebVTT sidecar.
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {CaptionBlock} from '../components/CaptionBlock.tsx';
import {Mark} from '../components/Mark.tsx';
import {useBrandFonts, useTheme, type BrandProps} from '../lib/motion.ts';
import {titleSafe} from '../lib/safe-areas.ts';
import {CAPTION_RULES, type Cue} from '../lib/timing.ts';

export interface CaptionsProps extends BrandProps {
  cues: Cue[];
}

export const Captions: React.FC<CaptionsProps> = (props) => {
  const frame = useCurrentFrame();
  const {fps, width, height} = useVideoConfig();
  const theme = useTheme(props);
  useBrandFonts(theme);
  const ms = (frame / fps) * 1000;
  return (
    <AbsoluteFill style={{backgroundColor: theme.color.surface, alignItems: 'center', justifyContent: 'center'}}>
      <div style={{opacity: 0.18}}>
        <Mark size={Math.round(height * 0.5)} ring={theme.color.accent} diamond={theme.color.fg} dot={theme.color.accent} ringDraw={1} diamondIn={1} dotIn={1} />
      </div>
      <CaptionBlock
        cues={props.cues}
        ms={ms}
        theme={theme}
        safe={titleSafe(width, height)}
        maxChars={CAPTION_RULES.maxCharsLandscape}
        fontSize={Math.round(height * 0.044)}
      />
    </AbsoluteFill>
  );
};
