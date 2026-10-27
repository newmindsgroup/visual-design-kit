// Version-Timestamp: 2026-10-23 20:10:44 UTC
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, readFile, rm } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { buildDeck, SLIDE_COUNT } from '../src/build-deck.mjs';
import { loadTokens } from '../src/tokens.mjs';
import { readZip } from './zip.mjs';

const slidesOf = (zip) => zip.names.filter((n) => /^ppt\/slides\/slide\d+\.xml$/.test(n));
const allSlideXml = (zip) => slidesOf(zip).map((n) => zip.read(n)).join('\n');

async function build(opts) {
  const dir = await mkdtemp(path.join(os.tmpdir(), 'deck-pptx-'));
  try {
    const result = await buildDeck({ ...opts, outDir: dir });
    const buf = await readFile(result.file);
    return { result, zip: readZip(buf), buf };
  } finally {
    await rm(dir, { recursive: true, force: true });
  }
}

test('PowerPoint-native deck has 10 slides, a master, native chart and tables', async () => {
  const { zip, buf } = await build({});
  assert.equal(buf.subarray(0, 2).toString(), 'PK');
  assert.equal(slidesOf(zip).length, SLIDE_COUNT);
  assert.ok(zip.names.some((n) => /^ppt\/slideMasters\/slideMaster\d+\.xml$/.test(n)), 'slide master present');
  assert.ok(zip.names.some((n) => /^ppt\/charts\/chart\d+\.xml$/.test(n)), 'native chart present');
  assert.match(allSlideXml(zip), /<a:tbl>/, 'native table present');
});

test('Canva-safe deck has 10 slides, no native charts or tables, chart as PNG', async () => {
  const { zip } = await build({ canvaSafe: true });
  assert.equal(slidesOf(zip).length, SLIDE_COUNT);
  assert.ok(!zip.names.some((n) => /^ppt\/charts\/.+\.xml$/.test(n)), 'no native charts (empty folder entries are fine)');
  assert.doesNotMatch(allSlideXml(zip), /drawingml\/2006\/chart/, 'no chart graphic frames');
  assert.ok(!zip.names.some((n) => /\.svg$/.test(n)), 'no SVG media (PptxGenJS cannot rasterize its PNG fallback in Node)');
  const xml = allSlideXml(zip);
  assert.doesNotMatch(xml, /<a:tbl>/, 'no native tables');
  assert.doesNotMatch(xml, /<dgm:|smartArt/i, 'no SmartArt');
  assert.ok(zip.names.some((n) => /^ppt\/media\/.+\.png$/.test(n)), 'chart image present');
});

test('colors and fonts come from the token file', async () => {
  const tok = await loadTokens();
  const accent = tok.values['color.accent.default'].slice(1).toUpperCase();
  const display = tok.values['font.family.display'][0];
  const { zip } = await build({ canvaSafe: true });
  const xml = allSlideXml(zip);
  assert.ok(xml.includes(`val="${accent}"`), `accent ${accent} used on slides`);
  assert.ok(xml.includes(`typeface="${display}"`), `display font ${display} named`);
  assert.match(zip.read('ppt/notesSlides/notesSlide1.xml'), /Fictional placeholder content/);
});

test('every brand in the token file builds', async () => {
  const data = JSON.parse(await readFile((await loadTokens()).file, 'utf8'));
  for (const brand of Object.keys(data.values)) {
    const { zip } = await build({ brand, systemFonts: true });
    assert.equal(slidesOf(zip).length, SLIDE_COUNT, brand);
  }
});
