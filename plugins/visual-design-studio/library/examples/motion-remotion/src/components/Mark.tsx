// Visual Design Kit, MIT. Part of a Remotion example; Remotion itself is NOT MIT (see README.md "Remotion license").
// Version-Timestamp: 2026-10-23 20:12:12 UTC
//
// Original geometric placeholder mark (ring, diamond, dot). Same geometry as the
// lottie_build.py logo-reveal preset. Replace it with the client's licensed mark.
import React from 'react';

export interface MarkProps {
  size: number;
  ring: string;
  diamond: string;
  dot: string;
  /** 0-1: how much of the ring is drawn. */
  ringDraw: number;
  /** 0-1: diamond scale-in, rotation and wipe. */
  diamondIn: number;
  /** 0-1: dot scale-in. */
  dotIn: number;
}

export const Mark: React.FC<MarkProps> = ({size, ring, diamond, dot, ringDraw, diamondIn, dotIn}) => {
  const c = size / 2;
  const r = (size * 0.62) / 2;
  const circumference = 2 * Math.PI * r;
  const half = (size * 0.3) / 2;
  const dotR = (size * 0.08) / 2;
  const diamondScale = 0.6 + 0.4 * diamondIn;
  const wipeTop = half - 2 * half * diamondIn;
  return (
    <svg width={size} height={size} viewBox={`0 0 ${size} ${size}`} aria-hidden="true">
      <defs>
        <clipPath id="mark-wipe">
          <rect x={-half} y={wipeTop} width={half * 2} height={half - wipeTop} />
        </clipPath>
      </defs>
      <circle
        cx={c}
        cy={c}
        r={r}
        fill="none"
        stroke={ring}
        strokeWidth={size * 0.045}
        strokeLinecap="round"
        strokeDasharray={circumference}
        strokeDashoffset={circumference * (1 - ringDraw)}
        transform={`rotate(-90 ${c} ${c})`}
        opacity={ringDraw > 0 ? 1 : 0}
      />
      <g transform={`translate(${c} ${c}) rotate(${-45 * (1 - diamondIn)}) scale(${diamondScale})`}>
        <path d={`M0 ${-half} L${half} 0 L0 ${half} L${-half} 0 Z`} fill={diamond} clipPath="url(#mark-wipe)" />
      </g>
      <circle cx={c} cy={c} r={dotR * dotIn} fill={dot} />
    </svg>
  );
};
