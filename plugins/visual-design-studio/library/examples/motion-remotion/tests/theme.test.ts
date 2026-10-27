// Visual Design Kit, MIT. Tests for a Remotion example; Remotion itself is NOT MIT (see README.md "Remotion license").
// Version-Timestamp: 2026-10-23 20:12:12 UTC
import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {contrastRatio, hexToLottie, parseMs, selectTheme, type ResolvedTokens} from '../src/lib/theme.ts';

const tokensUrl = new URL('../../../tokens/dist/tokens.resolved.json', import.meta.url);
const tokens = JSON.parse(readFileSync(tokensUrl, 'utf8')) as ResolvedTokens;

test('default theme comes from the kit defaults', () => {
  const theme = selectTheme(tokens);
  assert.equal(theme.brand, tokens.defaultBrand);
  assert.equal(theme.mode, tokens.defaultMode);
  assert.match(theme.color.accent, /^#[0-9a-f]{6}$/i);
});

test('brand and mode switch the values', () => {
  const light = selectTheme(tokens, 'meridian', 'light');
  const dark = selectTheme(tokens, 'meridian', 'dark');
  const ember = selectTheme(tokens, 'ember', 'light');
  assert.notEqual(light.color.canvas, dark.color.canvas);
  assert.notEqual(light.font.display, ember.font.display);
  assert.equal(light.brandName, 'Meridian');
});

test('motion tokens resolve to numbers and bezier curves', () => {
  const theme = selectTheme(tokens);
  assert.equal(theme.durationMs.fast, 120);
  assert.equal(theme.durationMs.slower, 480);
  assert.deepEqual(theme.ease.standard, [0.2, 0, 0, 1]);
  for (const curve of Object.values(theme.ease)) {
    assert.equal(curve.length, 4);
    assert.ok(curve[0] >= 0 && curve[0] <= 1 && curve[2] >= 0 && curve[2] <= 1);
  }
});

test('unknown brand or mode fails loudly', () => {
  assert.throws(() => selectTheme(tokens, 'nope'), /Unknown brand/);
  assert.throws(() => selectTheme(tokens, 'meridian', 'sepia'), /Unknown mode/);
});

test('every brand and mode keeps text and captions at 4.5:1 or better', () => {
  for (const brand of Object.keys(tokens.values)) {
    for (const mode of Object.keys(tokens.values[brand])) {
      const t = selectTheme(tokens, brand, mode);
      const pairs: Array<[string, string, string]> = [
        ['fg on canvas', t.color.fg, t.color.canvas],
        ['muted on canvas', t.color.fgMuted, t.color.canvas],
        ['caption box', t.color.fgInverse, t.color.inverse],
        ['on-accent end card', t.color.onAccent, t.color.accent],
        ['lower third', t.color.fgMuted, t.color.surface],
      ];
      for (const [label, fg, bg] of pairs) {
        assert.ok(contrastRatio(fg, bg) >= 4.5, `${brand}/${mode} ${label}: ${contrastRatio(fg, bg).toFixed(2)}`);
      }
    }
  }
});

test('font stacks quote multi-word families', () => {
  const theme = selectTheme(tokens, 'meridian', 'light');
  assert.ok(theme.font.displayStack.startsWith('"Schibsted Grotesk"'));
});

test('parseMs and hexToLottie match lottie_build.py', () => {
  assert.equal(parseMs('320ms'), 320);
  assert.equal(parseMs('1.2s'), 1200);
  assert.deepEqual(hexToLottie('#006c6c'), [0, 0.4235, 0.4235, 1]);
  assert.deepEqual(hexToLottie('#fff'), [1, 1, 1, 1]);
  assert.deepEqual(hexToLottie('#00000080'), [0, 0, 0, 0.502]);
});
