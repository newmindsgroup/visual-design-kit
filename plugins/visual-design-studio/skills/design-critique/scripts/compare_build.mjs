#!/usr/bin/env node
// Version-Timestamp: 2026-10-20 10:29:19 UTC
// Agent-Attribution: computer=vm; tool=Claude Code; version=2.1.304; timestamp=2026-10-20 10:29:19 UTC
//
// compare_build.mjs: compare an approved design render with the built page, pixel by pixel and style by style.
// Node 18+. No bundled dependencies: Playwright is resolved at runtime (same rules as render_review.mjs).
// The pixel diff runs inside Chromium on a canvas, so no image library is needed.
//
//   node compare_build.mjs <approved-file-or-url> <built-file-or-url> [--widths 390,1440] [--threshold 0.02]
//                          [--out DIR] [--mask selector,...]
//
// Run with --help for every option. Exit codes: 0 within threshold, 1 above threshold (or style drift with
// --strict-styles), 2 usage or runtime error.

import { createRequire } from 'node:module';
import { createReadStream, existsSync, mkdirSync, statSync, writeFileSync } from 'node:fs';
import { basename, dirname, extname, join, relative, resolve, sep } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import http from 'node:http';

const VERSION = '0.6.0';

const HELP = `compare_build.mjs ${VERSION}: pixel and computed-style comparison of an approved design and its build.

Usage
  node compare_build.mjs <approved-file-or-url> <built-file-or-url> [options]

Options
  --widths LIST          Comma list of widths or WxH sizes (default 390,1440)
  --height PX            Viewport height for plain widths (default 900)
  --threshold N          Max share of changed pixels per width, 0-1 or a percent like 2% (default 0.02)
  --out DIR              Output folder (default ./build-fidelity/<built-name>)
  --mask LIST            Comma list of selectors painted over in both screenshots (repeatable)
  --viewport-only        Compare the first viewport instead of the full page
  --element SELECTOR     Compare one element (first match) in both pages instead of the page, e.g. #pricing
  --max-height PX        Clip full-page captures at this height (default 16000)
  --color-tolerance N    Per-pixel YIQ color distance 0-1 before a pixel counts as changed (default 0.05; 0.1 lets
                         a #FF5B3A -> #E0452A swap pass, so raise it only for cross-renderer comparisons)
  --include-aa           Count anti-aliased edge pixels as changes (default: ignored)
  --regions N            Largest changed regions reported per width (default 8)
  --serve                Serve local files over http://127.0.0.1 (needed for fetch() and ES modules)
  --root DIR             Root folder for --serve when a page loads ../ assets (default: each file's folder)
  --wait MS              Settle time after fonts load (default 400)
  --dpr N                Device pixel ratio (default 1)
  --color-scheme M       light or dark (default light)
  --motion               Keep animations running (default: prefers-reduced-motion and animations disabled)
  --strict-styles        Also exit 1 when matched elements show computed-style drift
  --help                 Show this help

Matching for style drift
  Elements are paired by id or data-testid. Compared: font family, size, weight, line height, letter spacing,
  color, background color, padding, margin, gap, border radius, border width and color, rendered width and height.

Environment
  PLAYWRIGHT_MODULE      Path to a playwright (or playwright-core) package folder or its index.js
  PLAYWRIGHT_CHROMIUM    Chromium or headless_shell executable to launch
`;

function fail(message, code = 2) {
  process.stderr.write(`compare_build: ${message}\n`);
  process.exit(code);
}

function parseThreshold(value) {
  const text = String(value).trim();
  const n = text.endsWith('%') ? parseFloat(text) / 100 : parseFloat(text);
  if (!Number.isFinite(n) || n < 0 || n > 1) fail(`bad --threshold "${value}"; use 0.02 or 2%`);
  return n;
}

function parseArgs(argv) {
  const opts = { widths: '390,1440', height: 900, threshold: 0.02, mask: [], fullPage: true, element: null, maxHeight: 16000,
    colorTolerance: 0.05, includeAA: false, regions: 8, serve: false, wait: 400, dpr: 1, colorScheme: 'light',
    motion: false, strictStyles: false };
  const positional = [];
  const needValue = (i, flag) => { if (i + 1 >= argv.length) fail(`${flag} needs a value`); return argv[i + 1]; };
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    switch (arg) {
      case '--help': case '-h': process.stdout.write(HELP); process.exit(0); break;
      case '--widths': opts.widths = needValue(i, arg); i += 1; break;
      case '--height': opts.height = Number(needValue(i, arg)); i += 1; break;
      case '--threshold': opts.threshold = parseThreshold(needValue(i, arg)); i += 1; break;
      case '--out': opts.out = needValue(i, arg); i += 1; break;
      case '--mask': opts.mask.push(...needValue(i, arg).split(',').map((s) => s.trim()).filter(Boolean)); i += 1; break;
      case '--viewport-only': opts.fullPage = false; break;
      case '--element': opts.element = needValue(i, arg); i += 1; break;
      case '--max-height': opts.maxHeight = Number(needValue(i, arg)); i += 1; break;
      case '--color-tolerance': opts.colorTolerance = Number(needValue(i, arg)); i += 1; break;
      case '--include-aa': opts.includeAA = true; break;
      case '--regions': opts.regions = Number(needValue(i, arg)); i += 1; break;
      case '--serve': opts.serve = true; break;
      case '--root': opts.root = needValue(i, arg); i += 1; break;
      case '--wait': opts.wait = Number(needValue(i, arg)); i += 1; break;
      case '--dpr': opts.dpr = Number(needValue(i, arg)); i += 1; break;
      case '--color-scheme': opts.colorScheme = needValue(i, arg); i += 1; break;
      case '--motion': opts.motion = true; break;
      case '--strict-styles': opts.strictStyles = true; break;
      default:
        if (arg.startsWith('--')) fail(`unknown option ${arg} (see --help)`);
        positional.push(arg);
    }
  }
  if (positional.length !== 2) fail('give exactly two targets: <approved> <built> (see --help)');
  [opts.approved, opts.built] = positional;
  opts.sizes = opts.widths.split(',').map((t) => t.trim()).filter(Boolean).map((token) => {
    const match = token.match(/^(\d+)(?:x(\d+))?$/i);
    if (!match) fail(`bad size "${token}"; use 390 or 1080x1350`);
    return { width: Number(match[1]), height: match[2] ? Number(match[2]) : opts.height, label: token.toLowerCase() };
  });
  if (!opts.sizes.length) fail('no widths given');
  if (!['light', 'dark'].includes(opts.colorScheme)) fail('--color-scheme must be light or dark');
  if (!(opts.colorTolerance >= 0 && opts.colorTolerance <= 1)) fail('--color-tolerance must be between 0 and 1');
  if (!(opts.maxHeight >= 100)) fail('--max-height must be 100 or more');
  return opts;
}

// ---------- dependency resolution (mirrors render_review.mjs) ----------

function requireFrom(dir) { return createRequire(join(dir, 'noop.js')); }

async function loadPlaywright() {
  const tried = [];
  const pick = (mod) => (mod && mod.chromium ? mod : mod && mod.default && mod.default.chromium ? mod.default : null);
  const env = process.env.PLAYWRIGHT_MODULE;
  if (env) {
    try { const mod = pick(requireFrom(process.cwd())(resolve(env))); if (mod) return mod; tried.push(`PLAYWRIGHT_MODULE=${env}: no chromium export`); }
    catch (error) { tried.push(`PLAYWRIGHT_MODULE=${env}: ${error.message.split('\n')[0]}`); }
  }
  for (const name of ['playwright', 'playwright-core']) {
    try { const mod = pick(await import(name)); if (mod) return mod; } catch (error) { tried.push(`import('${name}'): ${error.code || error.message.split('\n')[0]}`); }
    try { const mod = pick(requireFrom(process.cwd())(name)); if (mod) return mod; } catch (error) { tried.push(`require('${name}') from cwd: ${error.code || error.message.split('\n')[0]}`); }
  }
  fail(`Playwright not found.\n  Install it where you run this script:  npm install playwright && npx playwright install chromium\n  or point to an existing copy:           PLAYWRIGHT_MODULE=/abs/path/node_modules/playwright\n  Tried:\n    ${tried.join('\n    ')}`);
  return null;
}

// ---------- targets and the optional static server ----------

const MIME = { '.html': 'text/html; charset=utf-8', '.htm': 'text/html; charset=utf-8', '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8', '.mjs': 'text/javascript; charset=utf-8', '.json': 'application/json; charset=utf-8',
  '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.gif': 'image/gif', '.webp': 'image/webp',
  '.avif': 'image/avif', '.ico': 'image/x-icon', '.woff': 'font/woff', '.woff2': 'font/woff2', '.ttf': 'font/ttf', '.otf': 'font/otf',
  '.mp4': 'video/mp4', '.webm': 'video/webm', '.txt': 'text/plain; charset=utf-8' };

function startServer(root) {
  return new Promise((resolveServer) => {
    const server = http.createServer((req, res) => {
      let path;
      try { path = resolve(root, `.${decodeURIComponent(new URL(req.url, 'http://x').pathname)}`); } catch { res.writeHead(400).end(); return; }
      if (path !== root && !path.startsWith(root + sep)) { res.writeHead(403).end(); return; }
      if (existsSync(path) && statSync(path).isDirectory()) path = join(path, 'index.html');
      if (!existsSync(path)) { res.writeHead(404).end(); return; }
      res.writeHead(200, { 'content-type': MIME[extname(path).toLowerCase()] || 'application/octet-stream', 'cache-control': 'no-store' });
      createReadStream(path).pipe(res);
    });
    server.listen(0, '127.0.0.1', () => resolveServer(server));
  });
}

async function resolveTarget(target, serve, rootOpt, servers) {
  if (/^https?:/i.test(target)) return { url: target, localFile: null };
  let localFile = target.startsWith('file:') ? fileURLToPath(target) : resolve(target);
  if (!existsSync(localFile)) fail(`file not found: ${localFile}`);
  if (statSync(localFile).isDirectory()) localFile = join(localFile, 'index.html');
  if (!existsSync(localFile)) fail(`file not found: ${localFile}`);
  if (!serve) return { url: pathToFileURL(localFile).href, localFile };
  const root = rootOpt ? resolve(rootOpt) : dirname(localFile);
  if (!localFile.startsWith(root + sep)) fail(`--root ${root} does not contain ${localFile}`);
  const server = await startServer(root);
  servers.push(server);
  return { url: `http://127.0.0.1:${server.address().port}/${relative(root, localFile).split(sep).map(encodeURIComponent).join('/')}`, localFile };
}

function slugFor(target, localFile) {
  if (localFile) {
    const name = basename(localFile, extname(localFile));
    return (name === 'index' ? basename(dirname(localFile)) : name).replace(/[^a-z0-9-]+/gi, '-').toLowerCase();
  }
  const u = new URL(target);
  return `${u.hostname}${u.pathname}`.replace(/[^a-z0-9-]+/gi, '-').replace(/^-|-$/g, '').toLowerCase() || 'page';
}

// ---------- capture ----------

async function settle(page, waitMs, motion) {
  await page.evaluate(async (keepMotion) => {
    const step = Math.max(200, Math.floor(window.innerHeight * 0.8));
    const max = Math.min(document.documentElement.scrollHeight, 60000);
    for (let y = 0; y < max; y += step) { window.scrollTo(0, y); await new Promise((r) => setTimeout(r, 40)); }
    window.scrollTo(0, 0);
    if (document.fonts) await document.fonts.ready;
    if (!keepMotion) {
      for (const animation of document.getAnimations ? document.getAnimations() : []) {
        try { const end = animation.effect && animation.effect.getComputedTiming().endTime; if (Number.isFinite(end)) animation.finish(); } catch { /* ignore */ }
      }
    }
  }, motion);
  await page.waitForTimeout(waitMs);
}

// In-page: computed styles of elements keyed by id or data-testid. Must stay self-contained (serialized).
function collectKeyedStyles(maskSelectors) {
  const props = ['fontFamily', 'fontSize', 'fontWeight', 'fontStyle', 'lineHeight', 'letterSpacing', 'textTransform', 'color',
    'backgroundColor', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft', 'marginTop', 'marginRight', 'marginBottom',
    'marginLeft', 'rowGap', 'columnGap', 'borderTopLeftRadius', 'borderTopRightRadius', 'borderBottomRightRadius',
    'borderBottomLeftRadius', 'borderTopWidth', 'borderTopColor', 'boxShadow', 'opacity'];
  const masked = (el) => maskSelectors.some((sel) => { try { return Boolean(el.closest(sel)); } catch { return false; } });
  const out = {};
  const duplicates = [];
  for (const el of document.querySelectorAll('[id], [data-testid]')) {
    if (el.closest('svg') && el.localName !== 'svg') continue; // gradient and clip ids are not layout elements
    const key = el.getAttribute('data-testid') ? `[data-testid="${el.getAttribute('data-testid')}"]` : `#${el.id}`;
    if (out[key]) { duplicates.push(key); continue; }
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const style = {};
    for (const p of props) style[p] = cs[p];
    out[key] = { tag: el.localName, masked: masked(el), visible: cs.display !== 'none' && cs.visibility !== 'hidden' && r.width > 0 && r.height > 0,
      box: { x: Math.round(r.left + window.scrollX), y: Math.round(r.top + window.scrollY), width: Math.round(r.width), height: Math.round(r.height) }, style };
  }
  return { elements: out, duplicates: [...new Set(duplicates)] };
}

async function capture(browser, url, size, opts) {
  const context = await browser.newContext({ viewport: { width: size.width, height: size.height }, deviceScaleFactor: opts.dpr,
    colorScheme: opts.colorScheme, reducedMotion: opts.motion ? 'no-preference' : 'reduce' });
  const page = await context.newPage();
  const errors = [];
  page.on('pageerror', (error) => errors.push(`pageerror: ${error.message.split('\n')[0]}`));
  page.on('requestfailed', (request) => errors.push(`requestfailed: ${request.url().slice(0, 160)} (${request.failure() ? request.failure().errorText : 'unknown'})`));
  try {
    await page.goto(url, { waitUntil: 'load', timeout: 45000 });
    await settle(page, opts.wait, opts.motion);
    const docHeight = await page.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body ? document.body.scrollHeight : 0));
    const masks = opts.mask.map((sel) => page.locator(sel));
    const shot = { type: 'png', animations: opts.motion ? 'allow' : 'disabled', caret: 'hide', mask: masks, maskColor: '#FF00FF' };
    let clipped = false;
    let png;
    if (opts.element) {
      const target = page.locator(opts.element).first();
      if (!(await target.count())) throw new Error(`--element ${opts.element} matches nothing in ${url}`);
      png = await target.screenshot(shot);
    } else {
      if (opts.fullPage) {
        shot.fullPage = true;
        if (docHeight > opts.maxHeight) { shot.clip = { x: 0, y: 0, width: size.width, height: opts.maxHeight }; clipped = true; }
      }
      png = await page.screenshot(shot);
    }
    const origin = opts.element ? await page.locator(opts.element).first().evaluate((el) => { const r = el.getBoundingClientRect(); return { x: r.left + window.scrollX, y: r.top + window.scrollY }; }) : { x: 0, y: 0 };
    const styles = await page.evaluate(collectKeyedStyles, opts.mask);
    return { png, styles, docHeight, clipped, errors, origin };
  } finally {
    await context.close();
  }
}

// ---------- in-browser pixel diff (serialized into a blank page; must stay self-contained) ----------

async function pixelDiff({ a, b, tolerance, includeAA, maxRegions }) {
  const load = (src) => new Promise((ok, bad) => { const img = new Image(); img.onload = () => ok(img); img.onerror = () => bad(new Error('image decode failed')); img.src = src; });
  const [imgA, imgB] = await Promise.all([load(a), load(b)]);
  const w = Math.max(imgA.naturalWidth, imgB.naturalWidth);
  const h = Math.max(imgA.naturalHeight, imgB.naturalHeight);
  const pixels = (img) => {
    const c = document.createElement('canvas'); c.width = w; c.height = h;
    const ctx = c.getContext('2d', { willReadFrequently: true });
    ctx.drawImage(img, 0, 0);
    return ctx.getImageData(0, 0, w, h).data;
  };
  const pa = pixels(imgA); const pb = pixels(imgB);

  // YIQ color distance (perceptual, after Kotsarenko and Ramos 2010); alpha is blended over white.
  const maxDelta = 35215 * tolerance * tolerance;
  const blend = (c, alpha) => 255 + (c - 255) * alpha;
  const yiq = (d, i) => {
    const al = d[i + 3] / 255;
    const r = blend(d[i], al); const g = blend(d[i + 1], al); const bl = blend(d[i + 2], al);
    return [r * 0.29889531 + g * 0.58662247 + bl * 0.11448223, r * 0.59597799 - g * 0.2741761 - bl * 0.32180189, r * 0.21147017 - g * 0.52261711 + bl * 0.31114694];
  };
  const delta = (d1, i1, d2, i2, yOnly) => {
    const [y1, i_1, q1] = yiq(d1, i1); const [y2, i_2, q2] = yiq(d2, i2);
    const dy = y1 - y2;
    if (yOnly) return dy;
    const di = i_1 - i_2; const dq = q1 - q2;
    return 0.5053 * dy * dy + 0.299 * di * di + 0.1957 * dq * dq;
  };
  // Anti-aliasing test (after Vysniauskas 2009): a pixel is an AA edge when its 8 neighbours contain both a
  // darker and a brighter extreme and one of those extremes sits on a flat area in both images.
  const flatNeighbours = (d, x, y) => {
    const i0 = (y * w + x) * 4; let same = 0;
    for (let yy = Math.max(0, y - 1); yy <= Math.min(h - 1, y + 1); yy += 1) {
      for (let xx = Math.max(0, x - 1); xx <= Math.min(w - 1, x + 1); xx += 1) {
        if (xx === x && yy === y) continue;
        const j = (yy * w + xx) * 4;
        if (d[i0] === d[j] && d[i0 + 1] === d[j + 1] && d[i0 + 2] === d[j + 2] && d[i0 + 3] === d[j + 3]) same += 1;
        if (same > 2) return true;
      }
    }
    return false;
  };
  const antialiased = (d, x, y, other) => {
    const i0 = (y * w + x) * 4; let zeroes = (x === 0 || x === w - 1 || y === 0 || y === h - 1) ? 1 : 0;
    let min = 0; let max = 0; let minX = -1; let minY = -1; let maxX = -1; let maxY = -1;
    for (let yy = Math.max(0, y - 1); yy <= Math.min(h - 1, y + 1); yy += 1) {
      for (let xx = Math.max(0, x - 1); xx <= Math.min(w - 1, x + 1); xx += 1) {
        if (xx === x && yy === y) continue;
        const dd = delta(d, i0, d, (yy * w + xx) * 4, true);
        if (dd === 0) { zeroes += 1; if (zeroes > 2) return false; }
        else if (dd < min) { min = dd; minX = xx; minY = yy; }
        else if (dd > max) { max = dd; maxX = xx; maxY = yy; }
      }
    }
    if (min === 0 || max === 0) return false;
    return (flatNeighbours(d, minX, minY) && flatNeighbours(other, minX, minY)) || (flatNeighbours(d, maxX, maxY) && flatNeighbours(other, maxX, maxY));
  };

  const out = document.createElement('canvas'); out.width = w; out.height = h;
  const octx = out.getContext('2d');
  const diffImg = octx.createImageData(w, h);
  const od = diffImg.data;
  const CELL = 8;
  const gw = Math.ceil(w / CELL); const gh = Math.ceil(h / CELL);
  const grid = new Uint32Array(gw * gh);
  let changed = 0; let aa = 0;
  for (let y = 0; y < h; y += 1) {
    for (let x = 0; x < w; x += 1) {
      const i = (y * w + x) * 4;
      const same = pa[i] === pb[i] && pa[i + 1] === pb[i + 1] && pa[i + 2] === pb[i + 2] && pa[i + 3] === pb[i + 3];
      let hit = false; let isAA = false;
      if (!same && delta(pa, i, pb, i, false) > maxDelta) {
        if (!includeAA && (antialiased(pa, x, y, pb) || antialiased(pb, x, y, pa))) isAA = true; else hit = true;
      }
      if (hit) {
        changed += 1; grid[Math.floor(y / CELL) * gw + Math.floor(x / CELL)] += 1;
        od[i] = 230; od[i + 1] = 0; od[i + 2] = 60; od[i + 3] = 255;
      } else if (isAA) {
        aa += 1; od[i] = 255; od[i + 1] = 190; od[i + 2] = 0; od[i + 3] = 255;
      } else {
        const [yv] = yiq(pa, i); const v = 255 + (yv - 255) * 0.15; // faded approved render for context
        od[i] = v; od[i + 1] = v; od[i + 2] = v; od[i + 3] = 255;
      }
    }
  }
  // Group changed cells into regions (8-connected, one empty cell of slack so text lines merge into blocks).
  const seen = new Uint8Array(gw * gh);
  const regions = [];
  for (let start = 0; start < grid.length; start += 1) {
    if (!grid[start] || seen[start]) continue;
    const stack = [start]; seen[start] = 1;
    let x0 = gw; let y0 = gh; let x1 = 0; let y1 = 0; let count = 0;
    while (stack.length) {
      const c = stack.pop(); const cx = c % gw; const cy = (c - cx) / gw;
      count += grid[c]; x0 = Math.min(x0, cx); y0 = Math.min(y0, cy); x1 = Math.max(x1, cx); y1 = Math.max(y1, cy);
      for (let dy = -2; dy <= 2; dy += 1) for (let dx = -2; dx <= 2; dx += 1) {
        const nx = cx + dx; const ny = cy + dy;
        if (nx < 0 || ny < 0 || nx >= gw || ny >= gh) continue;
        const n = ny * gw + nx;
        if (grid[n] && !seen[n]) { seen[n] = 1; stack.push(n); }
      }
    }
    regions.push({ x: x0 * CELL, y: y0 * CELL, width: Math.min(w, (x1 + 1) * CELL) - x0 * CELL, height: Math.min(h, (y1 + 1) * CELL) - y0 * CELL, changedPixels: count });
  }
  regions.sort((p, q) => q.changedPixels - p.changedPixels);
  const top = regions.slice(0, maxRegions);
  octx.putImageData(diffImg, 0, 0);
  octx.strokeStyle = 'rgb(0, 90, 255)'; octx.lineWidth = 2;
  for (const r of top) octx.strokeRect(r.x + 1, r.y + 1, Math.max(1, r.width - 2), Math.max(1, r.height - 2));
  return { width: w, height: h, sizeA: [imgA.naturalWidth, imgA.naturalHeight], sizeB: [imgB.naturalWidth, imgB.naturalHeight],
    changed, antialiasedIgnored: aa, total: w * h, regionCount: regions.length, regions: top, png: out.toDataURL('image/png') };
}

// ---------- computed-style drift ----------

function normalizeColor(value) {
  const m = String(value).match(/^rgba?\(\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)$/);
  if (!m) return String(value).trim();
  const alpha = m[4] === undefined ? 1 : m[4].endsWith('%') ? parseFloat(m[4]) / 100 : parseFloat(m[4]);
  if (alpha === 0) return 'transparent';
  const hex = `#${[m[1], m[2], m[3]].map((v) => Math.round(+v).toString(16).padStart(2, '0')).join('')}`;
  return alpha === 1 ? hex : `${hex} / ${Math.round(alpha * 100)}%`;
}

const COLOR_PROPS = new Set(['color', 'backgroundColor', 'borderTopColor']);
const GROUPS = { padding: ['paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft'], margin: ['marginTop', 'marginRight', 'marginBottom', 'marginLeft'],
  gap: ['rowGap', 'columnGap'], borderRadius: ['borderTopLeftRadius', 'borderTopRightRadius', 'borderBottomRightRadius', 'borderBottomLeftRadius'] };

function sameValue(prop, a, b) {
  if (COLOR_PROPS.has(prop)) return normalizeColor(a) === normalizeColor(b);
  const na = parseFloat(a); const nb = parseFloat(b);
  if (/px$/.test(a) && /px$/.test(b) && Number.isFinite(na) && Number.isFinite(nb)) return Math.abs(na - nb) <= 0.5;
  if (prop === 'fontFamily') return a.replace(/["']/g, '').replace(/\s*,\s*/g, ',').toLowerCase() === b.replace(/["']/g, '').replace(/\s*,\s*/g, ',').toLowerCase();
  return a === b;
}

function styleDrift(approved, built) {
  const drift = [];
  const keysA = Object.keys(approved.elements); const keysB = new Set(Object.keys(built.elements));
  const onlyApproved = keysA.filter((k) => !keysB.has(k));
  const onlyBuilt = [...keysB].filter((k) => !approved.elements[k]);
  for (const key of keysA) {
    const ea = approved.elements[key]; const eb = built.elements[key];
    if (!eb || ea.masked || eb.masked) continue;
    if (ea.visible !== eb.visible) { drift.push({ key, tag: ea.tag, changes: [{ property: 'visible', approved: ea.visible, built: eb.visible }] }); continue; }
    if (!ea.visible) continue;
    const changes = [];
    const grouped = new Set(Object.values(GROUPS).flat());
    for (const [group, parts] of Object.entries(GROUPS)) {
      if (parts.some((p) => !sameValue(p, ea.style[p], eb.style[p]))) {
        changes.push({ property: group, approved: parts.map((p) => ea.style[p]).join(' '), built: parts.map((p) => eb.style[p]).join(' ') });
      }
    }
    for (const prop of Object.keys(ea.style)) {
      if (grouped.has(prop) || sameValue(prop, ea.style[prop], eb.style[prop])) continue;
      if (prop === 'borderTopColor' && parseFloat(ea.style.borderTopWidth) === 0 && parseFloat(eb.style.borderTopWidth) === 0) continue;
      const show = (v) => (COLOR_PROPS.has(prop) ? normalizeColor(v) : v);
      changes.push({ property: prop, approved: show(ea.style[prop]), built: show(eb.style[prop]) });
    }
    for (const dim of ['width', 'height']) {
      const da = ea.box[dim]; const db = eb.box[dim];
      if (Math.abs(da - db) > Math.max(2, da * 0.02)) changes.push({ property: dim, approved: `${da}px`, built: `${db}px` });
    }
    if (changes.length) drift.push({ key, tag: ea.tag, box: eb.box, changes });
  }
  return { matched: keysA.length - onlyApproved.length, onlyApproved, onlyBuilt, duplicates: [...new Set([...approved.duplicates, ...built.duplicates])], drift };
}

// Smallest matched element in the built page that contains the region's center: a name for the region.
function labelRegion(region, built, origin) {
  const cx = origin.x + region.x + region.width / 2; const cy = origin.y + region.y + region.height / 2;
  let best = null;
  for (const [key, el] of Object.entries(built.elements)) {
    const b = el.box;
    if (!el.visible || cx < b.x || cy < b.y || cx > b.x + b.width || cy > b.y + b.height) continue;
    if (!best || b.width * b.height < best.area) best = { key, area: b.width * b.height };
  }
  return best ? best.key : null;
}

// ---------- main ----------

async function main() {
  const opts = parseArgs(process.argv.slice(2));
  const servers = [];
  const approved = await resolveTarget(opts.approved, opts.serve, opts.root, servers);
  const built = await resolveTarget(opts.built, opts.serve, opts.root, servers);
  const outDir = resolve(opts.out || join(process.cwd(), 'build-fidelity', slugFor(opts.built, built.localFile)));
  mkdirSync(outDir, { recursive: true });

  const playwright = await loadPlaywright();
  let browser;
  try {
    browser = await playwright.chromium.launch({ headless: true, executablePath: process.env.PLAYWRIGHT_CHROMIUM || undefined });
  } catch (error) {
    servers.forEach((s) => s.close());
    fail(`could not launch Chromium: ${error.message.split('\n')[0]}\n  Install a browser with: npx playwright install chromium\n  or set PLAYWRIGHT_CHROMIUM=/abs/path/to/chrome-or-headless_shell`);
  }

  const report = { tool: `compare_build.mjs ${VERSION}`, createdAt: new Date().toISOString(), approved: approved.url, built: built.url,
    settings: { threshold: opts.threshold, colorTolerance: opts.colorTolerance, includeAA: opts.includeAA, fullPage: opts.fullPage,
      maxHeight: opts.maxHeight, element: opts.element, mask: opts.mask, dpr: opts.dpr, colorScheme: opts.colorScheme, motion: opts.motion }, widths: [] };
  let failed = false;
  try {
    const diffPage = await (await browser.newContext()).newPage();
    for (const size of opts.sizes) {
      const a = await capture(browser, approved.url, size, opts);
      const b = await capture(browser, built.url, size, opts);
      const toData = (buf) => `data:image/png;base64,${buf.toString('base64')}`;
      const diff = await diffPage.evaluate(pixelDiff, { a: toData(a.png), b: toData(b.png), tolerance: opts.colorTolerance, includeAA: opts.includeAA, maxRegions: opts.regions });
      const files = { approved: `${size.label}-approved.png`, built: `${size.label}-built.png`, diff: `${size.label}-diff.png` };
      writeFileSync(join(outDir, files.approved), a.png);
      writeFileSync(join(outDir, files.built), b.png);
      writeFileSync(join(outDir, files.diff), Buffer.from(diff.png.split(',')[1], 'base64'));
      const ratio = diff.changed / diff.total;
      const styles = styleDrift(a.styles, b.styles);
      const over = ratio > opts.threshold;
      const styleFail = opts.strictStyles && styles.drift.length > 0;
      if (over || styleFail) failed = true;
      report.widths.push({ size: size.label, pass: !over && !styleFail, changedRatio: Number(ratio.toFixed(6)), changedPercent: Number((ratio * 100).toFixed(3)),
        changedPixels: diff.changed, comparedPixels: diff.total, antialiasedIgnored: diff.antialiasedIgnored,
        imageSize: { approved: diff.sizeA, built: diff.sizeB, sizeMismatch: diff.sizeA[0] !== diff.sizeB[0] || diff.sizeA[1] !== diff.sizeB[1] },
        documentHeight: { approved: a.docHeight, built: b.docHeight }, clipped: a.clipped || b.clipped, regionCount: diff.regionCount,
        regions: diff.regions.map((r) => ({ ...r, element: labelRegion(r, b.styles, b.origin) })), styleDrift: styles,
        pageErrors: { approved: a.errors.slice(0, 10), built: b.errors.slice(0, 10) }, files });
    }
  } catch (error) {
    await browser.close(); servers.forEach((s) => s.close());
    fail(`comparison failed: ${error.message.split('\n')[0]}`);
  }
  await browser.close();
  servers.forEach((s) => s.close());
  writeFileSync(join(outDir, 'report.json'), `${JSON.stringify(report, null, 2)}\n`);

  const lines = [`compare_build ${VERSION}: ${opts.approved} -> ${opts.built}`, `threshold ${(opts.threshold * 100).toFixed(2)}% changed pixels; masks: ${opts.mask.join(', ') || 'none'}`];
  for (const w of report.widths) {
    lines.push(`${w.pass ? 'PASS' : 'FAIL'} ${w.size.padEnd(9)} ${w.changedPercent.toFixed(3)}% changed (${w.changedPixels}/${w.comparedPixels} px, ${w.antialiasedIgnored} AA ignored), ${w.regionCount} regions`
      + `${w.imageSize.sizeMismatch ? `, size ${w.imageSize.approved.join('x')} vs ${w.imageSize.built.join('x')}` : ''}${w.clipped ? ', clipped' : ''}`);
    for (const r of w.regions.slice(0, 5)) lines.push(`       region ${r.x},${r.y} ${r.width}x${r.height}: ${r.changedPixels} px${r.element ? ` in ${r.element}` : ''}`);
    const sd = w.styleDrift;
    lines.push(`       styles: ${sd.matched} matched elements, ${sd.drift.length} drifted, ${sd.onlyApproved.length} missing in build, ${sd.onlyBuilt.length} new in build`);
    for (const d of sd.drift.slice(0, 8)) lines.push(`         ${d.key}: ${d.changes.slice(0, 4).map((c) => `${c.property} ${c.approved} -> ${c.built}`).join('; ')}${d.changes.length > 4 ? ` (+${d.changes.length - 4})` : ''}`);
    const errs = w.pageErrors.approved.length + w.pageErrors.built.length;
    if (errs) lines.push(`       page errors: ${errs} (see report.json)`);
  }
  lines.push(`evidence: ${outDir}`);
  process.stdout.write(`${lines.join('\n')}\n`);
  process.exit(failed ? 1 : 0);
}

main().catch((error) => fail(error.stack || String(error)));
