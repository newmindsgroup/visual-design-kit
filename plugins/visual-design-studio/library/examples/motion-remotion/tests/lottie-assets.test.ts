// Visual Design Kit, MIT. Tests for a Remotion example; Remotion itself is NOT MIT (see README.md "Remotion license").
// Version-Timestamp: 2026-10-23 20:12:12 UTC
import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readdirSync, readFileSync} from 'node:fs';

const dir = new URL('../public/lottie/', import.meta.url);

test('bundled Lottie files are the portable subset @remotion/lottie needs', () => {
  const files = readdirSync(dir).filter((f) => f.endsWith('.json'));
  assert.deepEqual(files.sort(), ['icon-morph.json', 'loader.json', 'logo-reveal.json', 'underline-sweep.json']);
  for (const file of files) {
    const text = readFileSync(new URL(file, dir), 'utf8');
    const data = JSON.parse(text);
    for (const key of ['fr', 'w', 'h', 'op']) assert.equal(typeof data[key], 'number', `${file} ${key}`);
    assert.ok(data.op > data.ip, file);
    assert.ok(!/"x":"/.test(text), `${file} contains an expression`);
    assert.ok(!/"ty":5\b/.test(text), `${file} contains a text layer`);
    assert.ok(text.length < 100 * 1024, `${file} is over 100KB`);
  }
});
