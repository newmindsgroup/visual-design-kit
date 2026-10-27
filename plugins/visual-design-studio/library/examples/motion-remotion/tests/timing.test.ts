// Visual Design Kit, MIT. Tests for a Remotion example; Remotion itself is NOT MIT (see README.md "Remotion license").
// Version-Timestamp: 2026-10-23 20:12:12 UTC
import {test} from 'node:test';
import assert from 'node:assert/strict';
import {activeCue, checkCue, holdSeconds, maxFlashesPerSecond, msToFrames, staggerFrames, wrapLines} from '../src/lib/timing.ts';
import {kineticSchedule, socialBeats} from '../src/lib/schedules.ts';

test('msToFrames rounds half up like the Python builder', () => {
  assert.equal(msToFrames(320, 30), 10);
  assert.equal(msToFrames(480, 30), 14);
  assert.equal(msToFrames(120, 60), 7);
  assert.equal(msToFrames(50, 30), 2);
  assert.throws(() => msToFrames(100, 0));
});

test('hold time is 1s + words / 3, at least 1.5s, +50% with numbers', () => {
  assert.equal(holdSeconds('One'), 1.5);
  assert.equal(holdSeconds('one two three four five six'), 3);
  assert.equal(holdSeconds('Save 30% today'), 3);
});

test('wrapLines never splits words and respects the limit', () => {
  const lines = wrapLines('Every launch starts with one clear sentence.', 32);
  assert.deepEqual(lines, ['Every launch starts with one', 'clear sentence.']);
  assert.ok(lines.every((l) => l.length <= 32));
  assert.deepEqual(wrapLines('Supercalifragilistic', 5), ['Supercalifragilistic']);
});

test('checkCue flags long, fast and short cues', () => {
  assert.deepEqual(checkCue({startMs: 0, endMs: 2800, text: 'Every launch starts with one clear sentence.'}, 42).problems, []);
  const fast = checkCue({startMs: 0, endMs: 1000, text: 'This caption has far too many characters for one second.'}, 42);
  assert.ok(fast.problems.some((p) => p.includes('chars/s')));
  const short = checkCue({startMs: 0, endMs: 500, text: 'Hi'}, 42);
  assert.ok(short.problems.some((p) => p.includes('min')));
  const three = checkCue({startMs: 0, endMs: 7000, text: 'one two three four five six seven eight nine ten eleven twelve'}, 16);
  assert.ok(three.problems.some((p) => p.includes('lines')));
});

test('activeCue finds the cue on screen', () => {
  const cues = [{startMs: 0, endMs: 1000, text: 'a'}, {startMs: 1200, endMs: 2000, text: 'b'}];
  assert.equal(activeCue(cues, 500), 0);
  assert.equal(activeCue(cues, 1100), -1);
  assert.equal(activeCue(cues, 1999), 1);
});

test('flash counter applies the 3 per second ceiling (WCAG 2.3.1)', () => {
  assert.equal(maxFlashesPerSecond([0, 10, 20], 30), 3);
  assert.equal(maxFlashesPerSecond([0, 7, 14, 21], 30), 4);
  assert.equal(maxFlashesPerSecond([0, 30, 60, 90], 30), 1);
  assert.equal(maxFlashesPerSecond([], 30), 0);
});

test('stagger caps the last start at 300ms', () => {
  assert.deepEqual(staggerFrames(3, 50, 30), [0, 2, 3]);
  const many = staggerFrames(20, 50, 30);
  assert.equal(many[many.length - 1], msToFrames(300, 30));
});

test('default kinetic copy fits the 8s hold rule', () => {
  const plan = kineticSchedule('Design that ships finished', 'Tokens drive every frame, from brand to broadcast.', 480, 320, 8000);
  assert.equal(plan.lines.length, 2);
  assert.ok(plan.fits);
  const tooLong = kineticSchedule('A headline that is far too long to read', 'and a subhead that keeps going and going well past any reasonable reading time for eight seconds', 480, 320, 8000);
  assert.equal(tooLong.fits, false);
});

test('default social beats meet the hold rule and hook limits', () => {
  const {beats, problems} = socialBeats('Your brand, in every format', ['One token file', 'Six video formats', 'Zero manual resizing'], 'Start with the kit', 15000);
  assert.deepEqual(problems, []);
  assert.equal(beats.length, 5);
  assert.equal(beats[0].startMs, 0);
  assert.equal(beats[beats.length - 1].endMs, 15000);
  assert.ok(socialBeats('This hook is much too long for a first frame', [], 'Go', 15000).problems.length > 0);
});
