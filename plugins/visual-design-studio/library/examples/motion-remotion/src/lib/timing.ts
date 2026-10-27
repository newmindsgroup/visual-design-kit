// Visual Design Kit, MIT. Part of a Remotion example; Remotion itself is NOT MIT (see README.md "Remotion license").
// Version-Timestamp: 2026-10-23 20:12:12 UTC
//
// Pure timing, caption and flash math. No Remotion imports, so `npm test` runs it directly.
// Rules come from the motion skill: hold 1s + words / 3 (at least 1.5s, +50% for numbers),
// captions at most 2 lines, 5/6s to 7s per event, 20 characters per second or less,
// and no more than 3 flashes in any one-second window (WCAG 2.2 SC 2.3.1).

/** Milliseconds to whole frames, rounding half up (matches lottie_build.py ms_to_frames). */
export function msToFrames(ms: number, fps: number): number {
  if (fps <= 0) throw new Error('fps must be positive');
  return Math.floor((ms * fps) / 1000 + 0.5);
}

export function secondsToFrames(seconds: number, fps: number): number {
  return msToFrames(seconds * 1000, fps);
}

export function wordCount(text: string): number {
  return text.trim().split(/\s+/).filter(Boolean).length;
}

/** Minimum on-screen hold, in seconds, once a line is fully legible. */
export function holdSeconds(text: string, opts: {numbersOrLegal?: boolean} = {}): number {
  const base = Math.max(1.5, 1 + wordCount(text) / 3);
  const hasNumbers = opts.numbersOrLegal ?? /\d/.test(text);
  return hasNumbers ? base * 1.5 : base;
}

/** Greedy word wrap at phrase-friendly spaces; never splits a word. */
export function wrapLines(text: string, maxChars: number): string[] {
  const words = text.trim().split(/\s+/).filter(Boolean);
  const lines: string[] = [];
  let line = '';
  for (const word of words) {
    const next = line ? `${line} ${word}` : word;
    if (next.length <= maxChars || !line) {
      line = next;
    } else {
      lines.push(line);
      line = word;
    }
  }
  if (line) lines.push(line);
  return lines;
}

export interface Cue {
  startMs: number;
  endMs: number;
  text: string;
}

export interface CueCheck {
  lines: string[];
  problems: string[];
}

export const CAPTION_RULES = {
  maxLines: 2,
  minMs: 833,
  maxMs: 7000,
  maxCharsPerSecond: 20,
  maxCharsLandscape: 42,
  maxCharsVertical: 32,
};

export function checkCue(cue: Cue, maxChars: number): CueCheck {
  const lines = wrapLines(cue.text, maxChars);
  const problems: string[] = [];
  const duration = cue.endMs - cue.startMs;
  if (lines.length > CAPTION_RULES.maxLines) problems.push(`${lines.length} lines (max ${CAPTION_RULES.maxLines})`);
  if (lines.some((l) => l.length > maxChars)) problems.push(`a word is longer than ${maxChars} characters`);
  if (duration < CAPTION_RULES.minMs) problems.push(`on screen ${duration}ms (min ${CAPTION_RULES.minMs}ms)`);
  if (duration > CAPTION_RULES.maxMs) problems.push(`on screen ${duration}ms (max ${CAPTION_RULES.maxMs}ms)`);
  const cps = cue.text.replace(/\s+/g, ' ').trim().length / (duration / 1000);
  if (cps > CAPTION_RULES.maxCharsPerSecond) problems.push(`${cps.toFixed(1)} chars/s (max ${CAPTION_RULES.maxCharsPerSecond})`);
  return {lines, problems};
}

/** Index of the cue on screen at `ms`, or -1. */
export function activeCue(cues: Cue[], ms: number): number {
  return cues.findIndex((c) => ms >= c.startMs && ms < c.endMs);
}

/**
 * Largest number of flashes in any one-second window, from the frames where a flash starts.
 * WCAG 2.2 SC 2.3.1 allows at most 3 (unless below the general and red flash thresholds,
 * which needs an analyzer such as PEAT to prove).
 */
export function maxFlashesPerSecond(flashFrames: number[], fps: number): number {
  const sorted = [...flashFrames].sort((a, b) => a - b);
  let best = 0;
  let start = 0;
  for (let end = 0; end < sorted.length; end++) {
    while (sorted[end] - sorted[start] >= fps) start++;
    best = Math.max(best, end - start + 1);
  }
  return best;
}

/** Stagger offsets in frames: `count` items, `stepMs` apart, capped so the last starts by `capMs`. */
export function staggerFrames(count: number, stepMs: number, fps: number, capMs = 300): number[] {
  const step = count > 1 ? Math.min(stepMs, capMs / (count - 1)) : 0;
  return Array.from({length: count}, (_, i) => msToFrames(i * step, fps));
}
