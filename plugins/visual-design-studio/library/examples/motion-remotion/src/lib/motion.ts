// Visual Design Kit, MIT. Part of a Remotion example; Remotion itself is NOT MIT (see README.md "Remotion license").
// Version-Timestamp: 2026-10-23 20:12:12 UTC
//
// Remotion-side helpers: theme from props, token easing, eased progress, reduced-motion handling.
import {Easing, interpolate, staticFile} from 'remotion';
import {loadFont} from '@remotion/fonts';
import {selectTheme, type Bezier, type Theme} from './theme.ts';
import {msToFrames} from './timing.ts';
import {TOKENS} from './tokens-data.ts';

export interface BrandProps {
  /** Token brand, e.g. "meridian" or "ember". */
  brand: string;
  /** Token mode: "light", "dark" or "high-contrast". */
  mode: string;
  /** Render the reduced-motion variant: no spatial movement, fades of 200ms or less. */
  reducedMotion: boolean;
  [key: string]: unknown;
}

export const defaultBrandProps: BrandProps = {brand: TOKENS.defaultBrand, mode: TOKENS.defaultMode, reducedMotion: false};

export const useTheme = (props: {brand?: string; mode?: string}): Theme => selectTheme(TOKENS, props.brand, props.mode);

export const ease = (curve: Bezier) => Easing.bezier(curve[0], curve[1], curve[2], curve[3]);

/** 0 to 1 progress for a move that starts at `startMs` and lasts `durationMs`, eased by a token curve. */
export function progress(frame: number, fps: number, startMs: number, durationMs: number, curve: Bezier): number {
  const start = msToFrames(startMs, fps);
  const end = start + Math.max(1, msToFrames(durationMs, fps));
  return interpolate(frame, [start, end], [0, 1], {
    easing: ease(curve),
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
}

/**
 * Enter value for an element. Full motion: eased 0 to 1 over the token duration.
 * Reduced motion: an opacity-only fade of at most 200ms, and callers drop translation and scale.
 */
export function enter(frame: number, fps: number, startMs: number, durationMs: number, curve: Bezier, reduced: boolean): number {
  if (reduced) return progress(frame, fps, startMs, Math.min(200, durationMs), [0, 0, 1, 1]);
  return progress(frame, fps, startMs, durationMs, curve);
}

// OFL fonts bundled in public/fonts with their licenses. The family names match the token stacks.
const FONT_FILES: Record<string, string> = {
  'Schibsted Grotesk': 'fonts/schibsted-grotesk/schibsted-grotesk-latin-wght-normal.woff2',
  'Source Sans 3': 'fonts/source-sans-3/source-sans-3-latin-wght-normal.woff2',
  Fraunces: 'fonts/fraunces/fraunces-latin-opsz-normal.woff2',
  Figtree: 'fonts/figtree/figtree-latin-wght-normal.woff2',
};

const requested = new Set<string>();

/** Load the theme's display and body fonts once; loadFont holds the render until they are ready. */
export function useBrandFonts(theme: Theme): void {
  for (const family of [theme.font.display, theme.font.body]) {
    const file = FONT_FILES[family];
    if (!file || requested.has(family)) continue;
    requested.add(family);
    loadFont({family, url: staticFile(file), weight: '100 900', display: 'block'}).catch((error) => {
      console.warn(`Font ${family} failed to load; falling back to the token stack`, error);
    });
  }
}
