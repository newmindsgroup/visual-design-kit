// Visual Design Kit, MIT. Tests for a Remotion example; Remotion itself is NOT MIT (see README.md "Remotion license").
// Version-Timestamp: 2026-10-23 20:12:12 UTC
import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {actionSafe, contains, scaleVerticalSafe, titleSafe, VERTICAL_SAFE} from '../src/lib/safe-areas.ts';

test('16:9 title-safe is 90% and action-safe 93%, centered', () => {
  assert.deepEqual(titleSafe(1920, 1080), {x: 96, y: 54, width: 1728, height: 972});
  assert.deepEqual(actionSafe(1920, 1080), {x: 67, y: 38, width: 1786, height: 1004});
  assert.ok(contains(actionSafe(1920, 1080), titleSafe(1920, 1080)));
});

test('vertical boxes match the kit social formats reference', () => {
  const ref = readFileSync(new URL('../../../../skills/print-packaging-social/references/social-formats.md', import.meta.url), 'utf8');
  assert.ok(ref.includes('About 880x1280 starting at (60, 220)'), 'organic box changed in social-formats.md');
  assert.ok(ref.includes('About 855x980 starting at (65, 269)'), 'paid box changed in social-formats.md');
  assert.deepEqual(VERTICAL_SAFE.organic, {x: 60, y: 220, width: 880, height: 1280});
  assert.deepEqual(VERTICAL_SAFE.paid, {x: 65, y: 269, width: 855, height: 980});
  assert.ok(contains(VERTICAL_SAFE.organic, VERTICAL_SAFE.paid));
});

test('vertical boxes scale to other 9:16 sizes', () => {
  assert.deepEqual(scaleVerticalSafe(VERTICAL_SAFE.organic, 720, 1280), {x: 40, y: 147, width: 587, height: 853});
});
