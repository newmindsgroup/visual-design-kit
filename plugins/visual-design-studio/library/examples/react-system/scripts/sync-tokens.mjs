// Version-Timestamp: 2026-10-20 02:52:00 UTC
// Copies the kit's built token CSS into src/styles/ so the app (and any copy of it) builds without the kit.
//   node scripts/sync-tokens.mjs           copy when the source exists (runs before dev, build and test)
//   node scripts/sync-tokens.mjs --check   exit 1 if a copy differs from the source (CI)
// Source: ../../tokens/dist/ (override with TOKENS_DIST=/path/to/tokens/dist). Outside the kit the source is
// usually absent; the committed copies are then kept as they are.
import { readFile, writeFile, access } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
export const sourceDir = path.resolve(root, process.env.TOKENS_DIST ?? '../../tokens/dist');
export const targetDir = path.join(root, 'src/styles');
export const files = ['tokens.css', 'tailwind.css'];

async function exists(file) {
  try {
    await access(file);
    return true;
  } catch {
    return false;
  }
}

/** Returns one entry per file: { file, status: 'fresh' | 'stale' | 'missing-source' | 'missing-copy' }. */
export async function compare() {
  const out = [];
  for (const file of files) {
    const src = path.join(sourceDir, file);
    const dst = path.join(targetDir, file);
    if (!(await exists(src))) {
      out.push({ file, status: 'missing-source' });
      continue;
    }
    if (!(await exists(dst))) {
      out.push({ file, status: 'missing-copy' });
      continue;
    }
    const [a, b] = await Promise.all([readFile(src), readFile(dst)]);
    out.push({ file, status: a.equals(b) ? 'fresh' : 'stale' });
  }
  return out;
}

async function main() {
  const check = process.argv.includes('--check');
  const results = await compare();
  if (results.every((r) => r.status === 'missing-source')) {
    console.log(`sync-tokens: no token source at ${sourceDir}; keeping the committed copies in src/styles/.`);
    return;
  }
  if (check) {
    const bad = results.filter((r) => r.status !== 'fresh');
    for (const r of results) console.log(`${r.status.padEnd(14)} ${r.file}`);
    if (bad.length) {
      console.error('sync-tokens: copies are stale. Run `npm run sync-tokens` and commit src/styles/.');
      process.exitCode = 1;
    }
    return;
  }
  for (const r of results) {
    if (r.status === 'missing-source') {
      console.warn(`sync-tokens: ${r.file} missing in ${sourceDir}; kept the existing copy.`);
      continue;
    }
    if (r.status === 'fresh') continue;
    await writeFile(path.join(targetDir, r.file), await readFile(path.join(sourceDir, r.file)));
    console.log(`sync-tokens: updated src/styles/${r.file}`);
  }
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  await main();
}
