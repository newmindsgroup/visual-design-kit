// Visual Design Kit, MIT. Part of a Remotion example; Remotion itself is NOT MIT (see README.md "Remotion license").
// Version-Timestamp: 2026-10-23 20:12:12 UTC
//
// Pure scheduling for the compositions, so the timing rules are unit-tested without rendering.
import {holdSeconds, wordCount, wrapLines} from './timing.ts';

export const LINE_STAGGER_MS = 100;
export const HEADLINE_MAX_CHARS = 22;

/** Kinetic headline plan in ms. `fits` is false when the hold rule cannot fit before the exit. */
export function kineticSchedule(headline: string, subhead: string, lineMs: number, exitMs: number, totalMs: number) {
  const lines = wrapLines(headline, HEADLINE_MAX_CHARS);
  const subStart = lineMs + LINE_STAGGER_MS * (lines.length - 1) + 120;
  const settled = subStart + lineMs;
  const hold = holdSeconds(`${headline} ${subhead}`) * 1000;
  const exitStart = totalMs - exitMs;
  return {lines, subStart, settled, hold, exitStart, fits: settled + hold <= exitStart};
}

export interface Beat {
  text: string;
  startMs: number;
  endMs: number;
}

/**
 * Split a vertical social video into a hook, the points and an end card.
 * The hook is on screen from frame 0 (no logo intro); the end card gets at least 2.5s;
 * the points share the middle and each must meet the hold rule.
 */
export function socialBeats(hook: string, points: string[], cta: string, totalMs: number, hookMs = 3000, endMs = 3000) {
  const middle = totalMs - hookMs - endMs;
  const each = points.length ? middle / points.length : 0;
  const beats: Beat[] = [{text: hook, startMs: 0, endMs: hookMs}];
  points.forEach((text, i) => beats.push({text, startMs: hookMs + i * each, endMs: hookMs + (i + 1) * each}));
  beats.push({text: cta, startMs: totalMs - endMs, endMs: totalMs});
  const problems = beats
    .filter((b) => b.endMs - b.startMs < holdSeconds(b.text) * 1000)
    .map((b) => `"${b.text}" needs ${holdSeconds(b.text).toFixed(1)}s, has ${((b.endMs - b.startMs) / 1000).toFixed(1)}s`);
  if (wordCount(hook) > 7) problems.push(`hook has ${wordCount(hook)} words (keep it to 7 or fewer)`);
  if (endMs < 2500) problems.push('end card under 2.5s');
  return {beats, problems};
}

