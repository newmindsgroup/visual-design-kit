// Version-Timestamp: 2026-10-20 02:52:00 UTC
// Unit tests (node:test, no browser). Node >= 22.18 strips TypeScript types, so plain .ts helpers import directly.
import assert from 'node:assert/strict';
import { readdir, readFile } from 'node:fs/promises';
import path from 'node:path';
import test from 'node:test';
import { fileURLToPath } from 'node:url';
import { cx, variants } from '../src/lib/cx.ts';
import { nextSort, selectionState, sortRows } from '../src/lib/sort.ts';
import { compare, sourceDir } from '../scripts/sync-tokens.mjs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const read = (rel) => readFile(path.join(root, rel), 'utf8');

async function sourceFiles(dir = 'src', exts = ['.ts', '.tsx', '.css']) {
  const out = [];
  for (const entry of await readdir(path.join(root, dir), { withFileTypes: true })) {
    const rel = path.join(dir, entry.name);
    if (entry.isDirectory()) out.push(...(await sourceFiles(rel, exts)));
    else if (exts.includes(path.extname(entry.name))) out.push(rel);
  }
  return out;
}
// Byte-for-byte copies of the kit's token build; checked by the freshness test instead.
const SYNCED = new Set(['src/styles/tokens.css', 'src/styles/tailwind.css']);

// ---------------------------------------------------------------------------------------------------------
// Token wiring

test('token copies in src/styles match library/tokens/dist (run `npm run sync-tokens` if this fails)', async (t) => {
  const results = await compare();
  if (results.every((r) => r.status === 'missing-source')) {
    t.skip(`no token source at ${sourceDir} (outside the kit); committed copies are used as-is`);
    return;
  }
  for (const r of results) assert.equal(r.status, 'fresh', `${r.file} is ${r.status}`);
});

test('every CSS custom property the code reads is defined by the tokens or system.css', async () => {
  const defined = new Set();
  for (const file of ['src/styles/tokens.css', 'src/styles/system.css', 'src/styles/index.css']) {
    for (const m of (await read(file)).matchAll(/(--[a-z0-9-]+)\s*:/g)) defined.add(m[1]);
  }
  const missing = [];
  for (const file of await sourceFiles('src', ['.ts', '.tsx', '.css'])) {
    if (SYNCED.has(file)) continue;
    const text = await read(file);
    for (const m of text.matchAll(/(?:var\(|\()(--[a-z][a-z0-9-]*)/g)) {
      const name = m[1];
      if (name.startsWith('--radix-') || name.startsWith('--tw-') || defined.has(name)) continue;
      missing.push(`${file}: ${name}`);
    }
  }
  assert.deepEqual([...new Set(missing)], []);
});

test('no raw color values in components, app code or system CSS', async () => {
  const offenders = [];
  for (const file of await sourceFiles()) {
    if (SYNCED.has(file)) continue;
    const text = await read(file);
    for (const m of text.matchAll(/#[0-9a-fA-F]{3,8}\b|\b(?:rgba?|hsla?|oklch|oklab|lab|lch|hwb)\(/g)) offenders.push(`${file}: ${m[0]}`);
  }
  assert.deepEqual(offenders, []);
});

// ---------------------------------------------------------------------------------------------------------
// Class lint: every class compiles against the token theme, with no arbitrary values or physical sides.

/** String literals inside a balanced (...) or {...} starting at `open`, skipping comparison operands and option keys. */
function literalsFrom(text, open) {
  const pairs = { '(': ')', '{': '}', '[': ']' };
  const stack = [];
  const out = [];
  const optionKeys = /\b(?:variant|size|tone|layout|state|padding|interactive|iconOnly|fullWidth|shape|mode|role|type|orientation|side|align)\s*:\s*$/;
  for (let i = open; i < text.length; i++) {
    const ch = text[i];
    if (ch === '/' && text[i + 1] === '/') {
      i = text.indexOf('\n', i);
      if (i < 0) break;
      continue;
    }
    if (ch === "'" || ch === '"' || ch === '`') {
      let j = i + 1;
      while (j < text.length && text[j] !== ch) j += text[j] === '\\' ? 2 : 1;
      const literal = text.slice(i + 1, j);
      const before = text.slice(Math.max(0, i - 40), i);
      const skip = /(?:===|!==|==|!=)\s*$/.test(before) || optionKeys.test(before) || (ch === '`' && literal.includes('${'));
      if (!skip) out.push(literal);
      i = j;
      continue;
    }
    if (pairs[ch]) stack.push(pairs[ch]);
    else if (ch === stack.at(-1)) {
      stack.pop();
      if (stack.length === 0) break;
    } else if (stack.length === 0 && (ch === ';' || ch === '\n')) break;
  }
  return out;
}

function classLists(text) {
  const lists = [];
  for (const m of text.matchAll(/className="([^"]*)"/g)) lists.push(m[1]);
  for (const m of text.matchAll(/\bclassName=\{/g)) lists.push(...literalsFrom(text, m.index + m[0].length - 1));
  for (const m of text.matchAll(/\b(?:cx|variants)\(/g)) lists.push(...literalsFrom(text, m.index + m[0].length - 1));
  for (const m of text.matchAll(/\bconst \w*(?:Class|Classes)\b[^=]*=\s*/g)) {
    const start = m.index + m[0].length;
    const open = text.slice(start).search(/[({'"`]/);
    lists.push(...literalsFrom(text, start + open));
  }
  return lists;
}

/** Splits "md:hover:bg-accent" into variants and the utility, ignoring colons inside brackets and parentheses. */
function utilityOf(token) {
  let depth = 0;
  let last = 0;
  for (let i = 0; i < token.length; i++) {
    if (token[i] === '[' || token[i] === '(') depth++;
    else if (token[i] === ']' || token[i] === ')') depth--;
    else if (token[i] === ':' && depth === 0) last = i + 1;
  }
  return token.slice(last);
}

const PHYSICAL = /^-?(?:pl|pr|ml|mr|left|right|border-l|border-r|rounded-l|rounded-r|rounded-tl|rounded-tr|rounded-bl|rounded-br|scroll-ml|scroll-mr|scroll-pl|scroll-pr)(?:-|$)|^text-(?:left|right)$|^(?:float|clear)-(?:left|right)$/;
const PALETTE = /^(?:bg|text|border|ring|outline|fill|stroke|from|via|to|divide|decoration|caret|accent|shadow)-(?:slate|gray|zinc|neutral|stone|red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|violet|purple|fuchsia|pink|rose|white|black)(?:-\d+)?(?:\/\d+)?$/;

test('every class in the source compiles to the token theme; no arbitrary values, palette colors or physical sides', async () => {
  const { __unstable__loadDesignSystem } = await import('tailwindcss');
  const css = await read('src/styles/index.css');
  const design = await __unstable__loadDesignSystem(css, {
    base: path.join(root, 'src/styles'),
    async loadStylesheet(id, base) {
      const file = id === 'tailwindcss' ? path.join(root, 'node_modules/tailwindcss/index.css') : path.resolve(base, id);
      return { path: file, base: path.dirname(file), content: await readFile(file, 'utf8') };
    },
  });
  const problems = [];
  let checked = 0;
  const markers = /^(?:group|peer)(?:\/[\w-]+)?$/; // state markers, not utilities
  for (const file of await sourceFiles('src', ['.tsx', '.ts'])) {
    if (file.startsWith(path.join('src', 'lib'))) continue; // helpers; examples in comments are not classes
    const tokens = new Set(classLists(await read(file)).flatMap((list) => list.split(/\s+/)).filter(Boolean));
    const list = [...tokens].filter((token) => !markers.test(token));
    const compiled = design.candidatesToCss(list);
    list.forEach((token, i) => {
      checked++;
      const utility = utilityOf(token);
      if (!compiled[i]) problems.push(`${file}: "${token}" does not compile`);
      if (utility.includes('[')) problems.push(`${file}: "${token}" uses an arbitrary value; use a token utility or (--token)`);
      if (PHYSICAL.test(utility)) problems.push(`${file}: "${token}" is a physical side; use logical (ps/pe/ms/me/start/end)`);
      if (PALETTE.test(utility)) problems.push(`${file}: "${token}" uses Tailwind's default palette`);
    });
  }
  assert.ok(checked > 300, `expected to check the whole class vocabulary, saw ${checked}`);
  console.log(`# checked ${checked} class tokens`);
  assert.deepEqual(problems, []);
});

test('package.json pins exact versions (no ^ or ~ ranges)', async () => {
  const pkg = JSON.parse(await read('package.json'));
  const ranges = Object.entries({ ...pkg.dependencies, ...pkg.devDependencies }).filter(([, v]) => !/^\d+\.\d+\.\d+$/.test(v));
  assert.deepEqual(ranges, []);
});

// ---------------------------------------------------------------------------------------------------------
// Props-to-class helpers

test('cx joins truthy values and flattens arrays', () => {
  assert.equal(cx('a', false, null, undefined, '', ['b', ['c', false]], 0, 'd'), 'a b c 0 d');
  assert.equal(cx(), '');
  assert.equal(cx('  padded  ', 'x'), 'padded x');
});

test('variants maps props to classes with defaults, booleans and compound rules', () => {
  const button = variants({
    base: 'base',
    variants: {
      variant: { primary: 'v-primary', ghost: 'v-ghost' },
      size: { sm: 's-sm', md: 's-md' },
      iconOnly: { true: 'icon', false: '' },
    },
    compoundVariants: [
      { iconOnly: false, size: 'sm', class: 'px-sm' },
      { iconOnly: true, size: 'sm', class: 'w-sm' },
    ],
    defaultVariants: { variant: 'primary', size: 'md', iconOnly: false },
  });
  assert.equal(button(), 'base v-primary s-md');
  assert.equal(button({ size: 'sm' }), 'base v-primary s-sm px-sm');
  assert.equal(button({ variant: 'ghost', size: 'sm', iconOnly: true, className: 'extra' }), 'base v-ghost s-sm icon w-sm extra');
  assert.deepEqual(button.options, { variant: ['primary', 'ghost'], size: ['sm', 'md'], iconOnly: ['true', 'false'] });
  // Unknown option values are a type error in TypeScript and throw at runtime.
  assert.throws(() => button({ variant: 'tertiary' }), /unknown variant="tertiary"/);
});

// ---------------------------------------------------------------------------------------------------------
// DataTable sorting and selection

const rows = [
  { id: 'r1', name: 'Alpha', qty: 0, date: null },
  { id: 'r3', name: 'Beta', qty: null, date: '2026-09-02' },
  { id: 'r2', name: 'Beta', qty: 12, date: '2026-09-01' },
  { id: 'r4', name: 'beta 10', qty: 3, date: '2026-08-30' },
  { id: 'r5', name: 'beta 9', qty: 12, date: '2026-10-01' },
];
const ids = (list) => list.map((r) => r.id);

test('sortRows: numbers ascending and descending, missing values last both ways, ties by id', () => {
  assert.deepEqual(ids(sortRows(rows, (r) => r.qty, 'ascending', (r) => r.id)), ['r1', 'r4', 'r2', 'r5', 'r3']);
  assert.deepEqual(ids(sortRows(rows, (r) => r.qty, 'descending', (r) => r.id)), ['r2', 'r5', 'r4', 'r1', 'r3']);
});

test('sortRows: strings use a numeric, case-insensitive collator; input is not mutated', () => {
  const copy = [...rows];
  assert.deepEqual(ids(sortRows(rows, (r) => r.name, 'ascending', (r) => r.id)), ['r1', 'r2', 'r3', 'r5', 'r4']);
  assert.deepEqual(rows, copy);
  assert.deepEqual(ids(sortRows(rows, (r) => r.date, 'descending', (r) => r.id)), ['r5', 'r3', 'r2', 'r4', 'r1']);
});

test('nextSort: new column starts at its first direction, same column toggles', () => {
  assert.deepEqual(nextSort(null, 'amount'), { column: 'amount', direction: 'ascending' });
  assert.deepEqual(nextSort(null, 'date', 'descending'), { column: 'date', direction: 'descending' });
  assert.deepEqual(nextSort({ column: 'date', direction: 'descending' }, 'date'), { column: 'date', direction: 'ascending' });
  assert.deepEqual(nextSort({ column: 'date', direction: 'ascending' }, 'amount'), { column: 'amount', direction: 'ascending' });
});

test('selectionState drives the header checkbox: none, some (mixed), all', () => {
  assert.equal(selectionState([], new Set()), false);
  assert.equal(selectionState(['a', 'b'], new Set()), false);
  assert.equal(selectionState(['a', 'b'], new Set(['a', 'z'])), 'indeterminate');
  assert.equal(selectionState(['a', 'b'], new Set(['a', 'b', 'z'])), true);
});
