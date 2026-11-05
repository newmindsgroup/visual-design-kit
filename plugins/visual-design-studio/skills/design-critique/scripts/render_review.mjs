#!/usr/bin/env node
// Version-Timestamp: 2026-11-05 17:59:47 UTC
// Agent-Attribution: computer=vm; tool=Claude Code; version=2.1.318; timestamp=2026-11-05 17:59:47 UTC
// 0.6.0 adds the first-paint frame (--early), video readiness and broken-image reports, ported from the QA ideas in
// scripts/shoot.py. Adapted from MotionSites claude-skill (MIT), see NOTICE.md.
//
// render_review.mjs: render an HTML/SVG artifact at real viewport sizes and collect review evidence.
// Node 18+. No bundled dependencies: Playwright and axe-core are resolved at runtime.
//
//   node render_review.mjs <file-or-url> [--widths 390,768,1440] [--out DIR] [--full-page]
//
// Run with --help for every option. Evidence is a lead for a human-quality critique, not a verdict:
// look at every screenshot before scoring.

import { createRequire } from 'node:module';
import { existsSync, mkdirSync, readFileSync, statSync, writeFileSync, createReadStream } from 'node:fs';
import { basename, dirname, extname, join, relative, resolve, sep } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import http from 'node:http';

const VERSION = '0.6.0';
const SCRIPT_DIR = dirname(fileURLToPath(import.meta.url));
const DEFAULT_WRAP_SELECTOR = 'h1,h2,h3,h4,h5,h6,p,li,blockquote,figcaption,dt,dd,[data-wrap]';

const HELP = `render_review.mjs ${VERSION}: render, screenshot and inspect an artifact at real sizes.

Usage
  node render_review.mjs <file-or-url> [options]

Options
  --widths LIST        Comma list of widths or WxH sizes (default 390,768,1440). Example: 1080x1350
  --height PX          Viewport height for plain widths (default 900)
  --out DIR            Output folder (default ./render-review/<name>)
  --full-page          Capture the full scroll height instead of the first viewport
  --serve              Serve a local file over http://127.0.0.1 (needed for fetch() and ES modules)
  --root DIR           Root folder for --serve (default: the file's folder)
  --wait MS            Settle time after fonts load (default 400)
  --early MS           Also capture a first-paint frame MS after navigation starts (350 is a good value) to
                       catch a white flash before CSS, fonts or media arrive. Saved as <name>-<size>-early.png
  --video-wait MS      Wait up to MS for every <video> to have a frame or an error before measuring (default 3000)
  --exclude SELECTOR   Skip matching subtrees in contrast, wrap and axe checks (repeatable)
  --wrap-selector SEL  Elements checked for single-word last lines (default ${DEFAULT_WRAP_SELECTOR})
  --dpr N              Device pixel ratio for screenshots (default 1)
  --color-scheme M     light or dark (default light)
  --reduced-motion     Emulate prefers-reduced-motion: reduce
  --no-axe             Skip axe-core even when it resolves
  --strict             Exit 2 on page overflow, clipped text, contrast failures, serious/critical axe
                       violations, failed requests, broken images or video errors (codec-unsupported excepted)
  --help               Show this help

Environment
  PLAYWRIGHT_MODULE    Path to a playwright (or playwright-core) package folder
  PLAYWRIGHT_CHROMIUM  Chromium or headless_shell executable to launch
  AXE_SCRIPT           Path to axe.min.js (otherwise axe-core is resolved like Playwright)
`;

function fail(message, code = 1) {
  process.stderr.write(`render_review: ${message}\n`);
  process.exit(code);
}

function parseArgs(argv) {
  const opts = { widths: '390,768,1440', height: 900, fullPage: false, serve: false, wait: 400, early: 0, videoWait: 3000, exclude: [],
    wrapSelector: DEFAULT_WRAP_SELECTOR, dpr: 1, colorScheme: 'light', reducedMotion: false, axe: true, strict: false };
  const positional = [];
  const needValue = (i, flag) => { if (i + 1 >= argv.length) fail(`${flag} needs a value`); return argv[i + 1]; };
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    switch (arg) {
      case '--help': case '-h': process.stdout.write(HELP); process.exit(0); break;
      case '--widths': opts.widths = needValue(i, arg); i += 1; break;
      case '--height': opts.height = Number(needValue(i, arg)); i += 1; break;
      case '--out': opts.out = needValue(i, arg); i += 1; break;
      case '--full-page': opts.fullPage = true; break;
      case '--serve': opts.serve = true; break;
      case '--root': opts.root = needValue(i, arg); i += 1; break;
      case '--wait': opts.wait = Number(needValue(i, arg)); i += 1; break;
      case '--early': opts.early = Number(needValue(i, arg)); i += 1; break;
      case '--video-wait': opts.videoWait = Number(needValue(i, arg)); i += 1; break;
      case '--exclude': opts.exclude.push(needValue(i, arg)); i += 1; break;
      case '--wrap-selector': opts.wrapSelector = needValue(i, arg); i += 1; break;
      case '--dpr': opts.dpr = Number(needValue(i, arg)); i += 1; break;
      case '--color-scheme': opts.colorScheme = needValue(i, arg); i += 1; break;
      case '--reduced-motion': opts.reducedMotion = true; break;
      case '--no-axe': opts.axe = false; break;
      case '--strict': opts.strict = true; break;
      default:
        if (arg.startsWith('--')) fail(`unknown option ${arg} (see --help)`);
        positional.push(arg);
    }
  }
  if (positional.length !== 1) fail('give exactly one file or URL (see --help)');
  opts.target = positional[0];
  opts.sizes = opts.widths.split(',').map((token) => token.trim()).filter(Boolean).map((token) => {
    const match = token.match(/^(\d+)(?:x(\d+))?$/i);
    if (!match) fail(`bad size "${token}"; use 390 or 1080x1350`);
    return { width: Number(match[1]), height: match[2] ? Number(match[2]) : opts.height, label: token.toLowerCase() };
  });
  if (!opts.sizes.length) fail('no widths given');
  if (!['light', 'dark'].includes(opts.colorScheme)) fail('--color-scheme must be light or dark');
  if (!Number.isFinite(opts.early) || opts.early < 0) fail('--early needs a number of milliseconds, for example 350');
  if (!Number.isFinite(opts.videoWait) || opts.videoWait < 0) fail('--video-wait needs a number of milliseconds');
  return opts;
}

// ---------- dependency resolution ----------

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

function loadAxeSource() {
  if (process.env.AXE_SCRIPT) {
    if (!existsSync(process.env.AXE_SCRIPT)) return { source: null, note: `AXE_SCRIPT=${process.env.AXE_SCRIPT} does not exist` };
    return { source: readFileSync(process.env.AXE_SCRIPT, 'utf8'), path: process.env.AXE_SCRIPT };
  }
  const bases = [process.cwd(), SCRIPT_DIR];
  if (process.env.PLAYWRIGHT_MODULE) bases.push(dirname(resolve(process.env.PLAYWRIGHT_MODULE)));
  for (const base of bases) {
    try { const path = requireFrom(base).resolve('axe-core/axe.min.js'); return { source: readFileSync(path, 'utf8'), path }; } catch { /* try next */ }
  }
  return { source: null, note: 'axe-core not found: npm install axe-core, or set AXE_SCRIPT=/abs/path/axe.min.js' };
}

// ---------- local static server (only with --serve) ----------

const MIME = { '.html': 'text/html; charset=utf-8', '.htm': 'text/html; charset=utf-8', '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8', '.mjs': 'text/javascript; charset=utf-8', '.json': 'application/json; charset=utf-8',
  '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.gif': 'image/gif', '.webp': 'image/webp',
  '.avif': 'image/avif', '.ico': 'image/x-icon', '.woff': 'font/woff', '.woff2': 'font/woff2', '.ttf': 'font/ttf', '.otf': 'font/otf',
  '.mp4': 'video/mp4', '.webm': 'video/webm', '.pdf': 'application/pdf', '.txt': 'text/plain; charset=utf-8', '.md': 'text/plain; charset=utf-8' };

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

// ---------- in-page diagnostics (serialized into the page; must stay self-contained) ----------

function pageDiagnostics({ wrapSelector, exclude, limit }) {
  const vw = document.documentElement.clientWidth;
  const canvas = document.createElement('canvas');
  canvas.width = 1; canvas.height = 1;
  const ctx = canvas.getContext('2d', { willReadFrequently: true });
  const colorCache = new Map();
  const parseColor = (value) => {
    if (colorCache.has(value)) return colorCache.get(value);
    let out;
    const m = value.match(/^rgba?\(\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)$/);
    if (m) {
      const alpha = m[4] === undefined ? 1 : m[4].endsWith('%') ? parseFloat(m[4]) / 100 : parseFloat(m[4]);
      out = { r: +m[1], g: +m[2], b: +m[3], a: alpha };
    } else if (value === 'transparent') {
      out = { r: 0, g: 0, b: 0, a: 0 };
    } else {
      ctx.clearRect(0, 0, 1, 1); ctx.fillStyle = '#000'; ctx.fillStyle = value; ctx.fillRect(0, 0, 1, 1);
      const d = ctx.getImageData(0, 0, 1, 1).data;
      out = { r: d[0], g: d[1], b: d[2], a: d[3] / 255 };
    }
    colorCache.set(value, out);
    return out;
  };
  const blend = (top, bottom) => ({ r: top.r * top.a + bottom.r * (1 - top.a), g: top.g * top.a + bottom.g * (1 - top.a), b: top.b * top.a + bottom.b * (1 - top.a), a: 1 });
  const lum = (c) => { const ch = [c.r, c.g, c.b].map((v) => { const s = v / 255; return s <= 0.04045 ? s / 12.92 : ((s + 0.055) / 1.055) ** 2.4; }); return 0.2126 * ch[0] + 0.7152 * ch[1] + 0.0722 * ch[2]; };
  const ratio = (a, b) => { const [hi, lo] = [lum(a), lum(b)].sort((x, y) => y - x); return (hi + 0.05) / (lo + 0.05); };
  const hex = (c) => `#${[c.r, c.g, c.b].map((v) => Math.round(v).toString(16).padStart(2, '0')).join('')}`;
  const isExcluded = (el) => exclude.some((sel) => { try { return Boolean(el.closest(sel)); } catch { return false; } });
  const cssPath = (el) => {
    const parts = [];
    for (let n = el; n && n.nodeType === 1 && parts.length < 4; n = n.parentElement) {
      if (n.id) { parts.unshift(`${n.localName}#${CSS.escape(n.id)}`); break; }
      let part = n.localName + [...n.classList].slice(0, 2).map((c) => `.${CSS.escape(c)}`).join('');
      const siblings = n.parentElement ? [...n.parentElement.children].filter((c) => c.localName === n.localName) : [];
      if (siblings.length > 1) part += `:nth-of-type(${siblings.indexOf(n) + 1})`;
      parts.unshift(part);
      if (n.localName === 'body') break;
    }
    return parts.join(' > ');
  };
  const region = (el) => { const holder = el.closest('[id]'); return holder ? holder.id : ''; };
  const visible = (el) => {
    if (typeof el.checkVisibility === 'function' && !el.checkVisibility({ opacityProperty: true, visibilityProperty: true })) return false;
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility !== 'visible') return false;
    const r = el.getBoundingClientRect();
    return r.width > 1 && r.height > 1;
  };
  const ownText = (el) => [...el.childNodes].filter((n) => n.nodeType === 3).map((n) => n.textContent).join(' ').replace(/\s+/g, ' ').trim();
  const snippet = (text) => (text.length > 70 ? `${text.slice(0, 67)}...` : text);
  window.scrollTo(0, 0);
  const all = [...document.querySelectorAll('body *')];

  // 1. Horizontal overflow: page scroll width, then the outermost elements that stick out of the viewport.
  const docWidth = Math.max(document.documentElement.scrollWidth, document.body ? document.body.scrollWidth : 0);
  const offenders = [];
  const rootClip = ['hidden', 'clip'].includes(getComputedStyle(document.documentElement).overflowX) || (document.body && ['hidden', 'clip'].includes(getComputedStyle(document.body).overflowX));
  for (const el of all) {
    if (offenders.length >= limit) break;
    const r = el.getBoundingClientRect();
    if (!(r.width > 0 && r.height > 0) || (r.right <= vw + 1 && r.left >= -1) || r.right <= 0) continue; // fully off to the left = visually hidden pattern
    const cs = getComputedStyle(el);
    if (cs.position === 'fixed' || !visible(el)) continue;
    let contained = false; let clippedByRoot = false;
    for (let a = el.parentElement; a; a = a.parentElement) {
      const ox = getComputedStyle(a).overflowX;
      if (ox !== 'visible') {
        if (a === document.body || a === document.documentElement) clippedByRoot = true; else contained = true;
        break;
      }
    }
    if (contained || offenders.some((o) => o.el.contains(el))) continue;
    offenders.push({ el, selector: cssPath(el), region: region(el), left: Math.round(r.left), right: Math.round(r.right), width: Math.round(r.width), clippedByRoot, text: snippet(el.textContent.replace(/\s+/g, ' ').trim()) });
  }

  // 2. Single-word last lines. Same method as library/scripts/wrap-diagnostics.js: split text into \S+ words,
  //    take each word's client rects, group them into lines, flag 2+ lines whose last line holds one word.
  //    Differences: a word joins a line when its vertical center falls inside that line's box (instead of
  //    2px top buckets), so superscripts and mixed sizes on one baseline do not count as extra lines; only
  //    visible leaf text blocks are checked; excluded subtrees and visually hidden spans are skipped.
  const runts = [];
  const clippedText = [];
  let wrapChecked = 0;
  let candidates = [];
  try { candidates = [...document.querySelectorAll(wrapSelector)]; } catch { candidates = []; }
  for (const el of candidates) {
    if (isExcluded(el) || !visible(el)) continue;
    const elStyle = getComputedStyle(el);
    if (elStyle.display !== 'inline' && clippedText.length < limit
      && (el.scrollWidth > el.clientWidth + 1 || (elStyle.overflowY !== 'visible' && el.scrollHeight > el.clientHeight + 1))) {
      clippedText.push({ selector: cssPath(el), region: region(el), clipped: elStyle.overflowX !== 'visible' || elStyle.overflowY !== 'visible',
        textOverflow: elStyle.textOverflow, scrollWidth: el.scrollWidth, clientWidth: el.clientWidth, text: snippet((el.innerText || el.textContent).replace(/\s+/g, ' ').trim()) });
    }
    let nested = null;
    try { nested = el.querySelector(wrapSelector); } catch { nested = null; }
    if (nested) continue;
    wrapChecked += 1;
    const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    const rects = [];
    let node;
    while ((node = walker.nextNode())) {
      const parentRect = node.parentElement.getBoundingClientRect();
      if (parentRect.width <= 1 || parentRect.height <= 1) continue;
      for (const match of node.textContent.matchAll(/\S+/gu)) {
        const range = document.createRange();
        range.setStart(node, match.index); range.setEnd(node, match.index + match[0].length);
        for (const rect of range.getClientRects()) {
          if (rect.width && rect.height) rects.push({ top: rect.top, bottom: rect.bottom, word: match[0] });
        }
      }
    }
    rects.sort((a, b) => (b.bottom - b.top) - (a.bottom - a.top));
    const lines = [];
    for (const r of rects) {
      const mid = (r.top + r.bottom) / 2;
      const line = lines.find((l) => mid >= l.top && mid <= l.bottom);
      if (line) line.words.push(r.word); else lines.push({ top: r.top, bottom: r.bottom, words: [r.word] });
    }
    lines.sort((a, b) => a.top - b.top);
    if (lines.length > 1 && lines[lines.length - 1].words.length === 1 && runts.length < limit) {
      const heading = /^h[1-6]$/.test(el.localName) || el.getAttribute('role') === 'heading';
      runts.push({ selector: cssPath(el), region: region(el), kind: heading ? 'heading' : 'text', lines: lines.length,
        lastLine: lines[lines.length - 1].words[0], forcedBreak: Boolean(el.querySelector('br')), fontSize: elStyle.fontSize,
        text: snippet((el.innerText || el.textContent).replace(/\s+/g, ' ').trim()) });
    }
  }

  // 3 + 4. Fonts as declared, and contrast where the background resolves to solid colors.
  const declared = new Map();
  const media = [];
  for (const el of all) {
    if (/^(img|video|canvas|picture|iframe)$/.test(el.localName) || (el.localName === 'svg' && !el.closest('svg svg'))) {
      const r = el.getBoundingClientRect();
      if (r.width > 24 && r.height > 24) media.push({ el, r });
    } else if (getComputedStyle(el).backgroundImage !== 'none') {
      const r = el.getBoundingClientRect();
      if (r.width > 0 && r.height > 0) media.push({ el, r });
    }
  }
  const failures = new Map();
  const contrast = { textElements: 0, measured: 0, passed: 0, unmeasured: { backgroundImage: 0, overlapsMedia: 0, filterOrBlend: 0 }, unmeasuredExamples: [], approximate: 0, minRatio: null };
  for (const el of all) {
    const text = ownText(el);
    if (!text || /^(script|style|noscript|template|title|option)$/.test(el.localName) || !visible(el)) continue;
    const cs = getComputedStyle(el);
    const family = cs.fontFamily.split(',')[0].replace(/["']/g, '').trim();
    declared.set(family, (declared.get(family) || 0) + 1);
    if (isExcluded(el)) continue;
    contrast.textElements += 1;
    // Use the painted extent of the element's own text, not its box, for the overlap test.
    let box = null;
    for (const n of el.childNodes) {
      if (n.nodeType !== 3 || !n.textContent.trim()) continue;
      const range = document.createRange(); range.selectNodeContents(n);
      const r = range.getBoundingClientRect();
      if (!r.width || !r.height) continue;
      box = box ? { left: Math.min(box.left, r.left), right: Math.max(box.right, r.right), top: Math.min(box.top, r.top), bottom: Math.max(box.bottom, r.bottom) } : { left: r.left, right: r.right, top: r.top, bottom: r.bottom };
    }
    box = box || el.getBoundingClientRect();
    let reason = null; let approximate = false; const layers = [];
    for (let a = el; a; a = a.parentElement) {
      const s = getComputedStyle(a);
      if (s.backgroundImage !== 'none') { reason = 'backgroundImage'; break; }
      if ((s.filter && s.filter !== 'none') || (s.mixBlendMode && s.mixBlendMode !== 'normal') || (s.backdropFilter && s.backdropFilter !== 'none')) { reason = 'filterOrBlend'; break; }
      if (parseFloat(s.opacity) < 1) approximate = true;
      const bg = parseColor(s.backgroundColor);
      if (bg.a > 0) { layers.push({ color: bg, el: a }); if (bg.a >= 0.999) break; }
    }
    if (!reason) {
      const opaqueOwner = layers.length ? layers[layers.length - 1].el : document.documentElement;
      const hit = media.find(({ el: m, r }) => !m.contains(el) && !el.contains(m) && opaqueOwner.contains(m)
        && r.left < box.right && r.right > box.left && r.top < box.bottom && r.bottom > box.top);
      if (hit) reason = 'overlapsMedia';
    }
    if (reason) {
      contrast.unmeasured[reason] += 1;
      if (contrast.unmeasuredExamples.length < limit) contrast.unmeasuredExamples.push({ reason, selector: cssPath(el), region: region(el), color: cs.color, text: snippet(text) });
      continue;
    }
    let bg = { r: 255, g: 255, b: 255, a: 1 };
    for (let i = layers.length - 1; i >= 0; i -= 1) bg = blend(layers[i].color, bg);
    const fg = blend(parseColor(cs.color), bg);
    const value = ratio(fg, bg);
    const size = parseFloat(cs.fontSize); const weight = parseInt(cs.fontWeight, 10) || 400;
    const large = size >= 24 || (size >= 18.66 && weight >= 700);
    const required = large ? 3 : 4.5;
    contrast.measured += 1;
    if (approximate) contrast.approximate += 1;
    contrast.minRatio = contrast.minRatio === null ? value : Math.min(contrast.minRatio, value);
    if (value + 1e-6 >= required) { contrast.passed += 1; continue; }
    const key = `${hex(fg)}|${hex(bg)}|${Math.round(size)}|${weight}`;
    if (!failures.has(key)) {
      failures.set(key, { ratio: Math.round(value * 100) / 100, required, fg: hex(fg), bg: hex(bg), fontSize: `${Math.round(size * 10) / 10}px`, fontWeight: weight,
        exemptCandidate: el.closest(':disabled,[aria-disabled="true"]') ? 'disabled control' : null, approximate, count: 0, examples: [] });
    }
    const entry = failures.get(key);
    entry.count += 1;
    if (entry.examples.length < 3) entry.examples.push({ selector: cssPath(el), region: region(el), text: snippet(text) });
  }
  if (contrast.minRatio !== null) contrast.minRatio = Math.round(contrast.minRatio * 100) / 100;
  contrast.failures = [...failures.values()].sort((a, b) => a.ratio - b.ratio).slice(0, limit * 2);

  // 5. Media: video readiness and errors, images that failed to decode.
  const MEDIA_ERRORS = { 1: 'MEDIA_ERR_ABORTED', 2: 'MEDIA_ERR_NETWORK', 3: 'MEDIA_ERR_DECODE', 4: 'MEDIA_ERR_SRC_NOT_SUPPORTED' };
  const videos = [...document.querySelectorAll('video')].slice(0, limit).map((v) => ({
    selector: cssPath(v), region: region(v), src: (v.currentSrc || v.src || (v.querySelector('source') || {}).src || '').slice(0, 200),
    readyState: v.readyState, hasFrame: v.readyState >= 2, networkState: v.networkState, paused: v.paused, ended: v.ended,
    currentTime: Math.round(v.currentTime * 100) / 100, duration: Number.isFinite(v.duration) ? Math.round(v.duration * 100) / 100 : null,
    autoplay: v.autoplay, muted: v.muted, loop: v.loop, playsInline: v.playsInline, controls: v.controls, poster: v.poster || null,
    videoSize: v.videoWidth ? `${v.videoWidth}x${v.videoHeight}` : null,
    error: v.error ? { code: v.error.code, name: MEDIA_ERRORS[v.error.code] || 'unknown', message: (v.error.message || '').slice(0, 200) } : null,
  }));
  const brokenImages = [...document.images].filter((i) => i.complete && i.naturalWidth === 0 && (i.currentSrc || i.src))
    .slice(0, limit).map((i) => ({ selector: cssPath(i), region: region(i), src: (i.currentSrc || i.src).slice(0, 200), alt: i.getAttribute('alt') }));

  const faces = new Map();
  if (document.fonts) for (const face of document.fonts) faces.set(`${face.family}|${face.weight}|${face.style}`, { family: face.family.replace(/["']/g, ''), weight: face.weight, style: face.style, status: face.status });

  return {
    title: document.title,
    lang: document.documentElement.lang || null,
    viewportWidth: vw,
    documentWidth: docWidth,
    documentHeight: document.documentElement.scrollHeight,
    horizontalOverflow: docWidth > vw + 1,
    overflowOffenders: offenders.map(({ el, ...rest }) => rest),
    rootClipsOverflow: Boolean(rootClip),
    wrap: { checked: wrapChecked, singleWordLastLines: runts, textOverflow: clippedText },
    fonts: { declaredPrimary: [...declared.entries()].sort((a, b) => b[1] - a[1]).map(([family, elements]) => ({ family, elements })), faces: [...faces.values()] },
    contrast,
    media: { videos, brokenImages },
  };
}

// First-paint probe: what the browser paints behind the page before content arrives (serialized into the page).
function firstPaintProbe() {
  const bg = (el) => (el ? getComputedStyle(el).backgroundColor : null);
  const html = bg(document.documentElement); const body = bg(document.body);
  const transparent = (c) => !c || c === 'transparent' || /rgba\([^)]*,\s*0\)$/.test(c);
  return { readyState: document.readyState, htmlBackground: html, bodyBackground: body,
    paintedBackground: !transparent(html) ? html : !transparent(body) ? body : 'none set (browser default, usually white)' };
}

async function waitForVideos(page, timeoutMs) {
  if (!timeoutMs) return;
  await page.waitForFunction(() => [...document.querySelectorAll('video')].every((v) => v.readyState >= 2 || v.error || v.networkState === 3 || (!v.currentSrc && !v.src && !v.querySelector('source'))),
    null, { timeout: timeoutMs, polling: 100 }).catch(() => {});
}

async function settle(page, waitMs) {
  await page.evaluate(async () => {
    const step = Math.max(200, Math.floor(window.innerHeight * 0.8));
    const max = Math.min(document.documentElement.scrollHeight, 60000);
    for (let y = 0; y < max; y += step) { window.scrollTo(0, y); await new Promise((r) => setTimeout(r, 40)); }
    window.scrollTo(0, 0);
    if (document.fonts) await document.fonts.ready;
    for (const animation of document.getAnimations ? document.getAnimations() : []) {
      try { const end = animation.effect && animation.effect.getComputedTiming().endTime; if (Number.isFinite(end)) animation.finish(); } catch { /* ignore */ }
    }
  });
  await page.waitForTimeout(waitMs);
}

async function renderedFonts(context, page) {
  try {
    const cdp = await context.newCDPSession(page);
    await cdp.send('DOM.enable'); await cdp.send('CSS.enable');
    const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
    const { nodeIds } = await cdp.send('DOM.querySelectorAll', { nodeId: root.nodeId, selector: 'body, body *' });
    const totals = new Map();
    const ids = nodeIds.slice(0, 4000);
    for (let i = 0; i < ids.length; i += 64) {
      const batch = await Promise.all(ids.slice(i, i + 64).map((nodeId) => cdp.send('CSS.getPlatformFontsForNode', { nodeId }).catch(() => ({ fonts: [] }))));
      for (const { fonts } of batch) for (const f of fonts) {
        const entry = totals.get(f.familyName) || { family: f.familyName, glyphs: 0, webFont: Boolean(f.isCustomFont) };
        entry.glyphs += f.glyphCount; totals.set(f.familyName, entry);
      }
    }
    await cdp.detach();
    return { source: 'CSS.getPlatformFontsForNode', nodesInspected: ids.length, families: [...totals.values()].sort((a, b) => b.glyphs - a.glyphs) };
  } catch (error) {
    return { source: 'unavailable', note: `rendered-font inspection needs Chromium CDP: ${error.message.split('\n')[0]}`, families: [] };
  }
}

async function runAxe(page, source, exclude, preload) {
  await page.addScriptTag({ content: source });
  return page.evaluate(async ({ excludeList, preloadCss }) => {
    const context = excludeList.length ? { exclude: excludeList.map((sel) => [sel]) } : document;
    const result = await window.axe.run(context, { preload: preloadCss, runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa', 'best-practice'] }, resultTypes: ['violations', 'incomplete'] });
    return {
      version: window.axe.version,
      violations: result.violations.map((v) => ({ id: v.id, impact: v.impact, help: v.help, helpUrl: v.helpUrl, wcag: v.tags.filter((t) => /^wcag\d/.test(t)), nodes: v.nodes.length, targets: v.nodes.slice(0, 5).map((n) => n.target.join(' ')) })),
      needsReview: result.incomplete.map((v) => ({ id: v.id, impact: v.impact, help: v.help, nodes: v.nodes.length })),
    };
  }, { excludeList: exclude, preloadCss: preload });
}

function slugFor(target, localFile) {
  if (localFile) {
    const name = basename(localFile, extname(localFile));
    return (name === 'index' ? basename(dirname(localFile)) : name).replace(/[^a-z0-9-]+/gi, '-').toLowerCase();
  }
  const u = new URL(target);
  return `${u.hostname}${u.pathname}`.replace(/[^a-z0-9-]+/gi, '-').replace(/^-|-$/g, '').toLowerCase() || 'page';
}

async function main() {
  const opts = parseArgs(process.argv.slice(2));
  let url; let localFile = null; let server = null;
  if (/^(https?|file):/i.test(opts.target)) {
    url = opts.target;
    if (url.startsWith('file:')) localFile = fileURLToPath(url);
  } else {
    localFile = resolve(opts.target);
    if (!existsSync(localFile)) fail(`file not found: ${localFile}`);
    if (statSync(localFile).isDirectory()) localFile = join(localFile, 'index.html');
    if (!existsSync(localFile)) fail(`file not found: ${localFile}`);
    url = pathToFileURL(localFile).href;
  }
  if (opts.serve) {
    if (!localFile) fail('--serve works with local files only');
    const root = resolve(opts.root || dirname(localFile));
    if (!(localFile === root || localFile.startsWith(root + sep))) fail(`--root ${root} does not contain ${localFile}`);
    server = await startServer(root);
    url = `http://127.0.0.1:${server.address().port}/${relative(root, localFile).split(sep).map(encodeURIComponent).join('/')}`;
  }

  const slug = slugFor(opts.target, localFile);
  const outDir = resolve(opts.out || join(process.cwd(), 'render-review', slug));
  mkdirSync(outDir, { recursive: true });

  const playwright = await loadPlaywright();
  const axe = opts.axe ? loadAxeSource() : { source: null, note: 'skipped (--no-axe)' };
  let browser;
  try {
    browser = await playwright.chromium.launch({ headless: true, executablePath: process.env.PLAYWRIGHT_CHROMIUM || undefined });
  } catch (error) {
    if (server) server.close();
    fail(`could not launch Chromium: ${error.message.split('\n')[0]}\n  Install a browser with: npx playwright install chromium\n  or set PLAYWRIGHT_CHROMIUM=/abs/path/to/chrome-or-headless_shell`);
  }

  const pageOrigin = url.startsWith('http') ? new URL(url).origin : 'file://';
  const report = { tool: 'render_review.mjs', version: VERSION, generatedAt: new Date().toISOString(), input: opts.target, url,
    browser: `${browser.browserType().name()} ${browser.version()}`, options: { sizes: opts.sizes, fullPage: opts.fullPage, dpr: opts.dpr, early: opts.early, videoWait: opts.videoWait,
      colorScheme: opts.colorScheme, reducedMotion: opts.reducedMotion, exclude: opts.exclude, wrapSelector: opts.wrapSelector, served: Boolean(server) },
    axe: axe.source ? { source: axe.path } : { source: null, note: axe.note }, results: [],
    limits: [
      'Contrast is measured only where every layer behind the text is a solid color; text over images, gradients, filters or overlapping media is counted as unmeasured. Check those by eye or with a pixel picker.',
      'Single-word last lines are whitespace-based review candidates (same method as library/scripts/wrap-diagnostics.js), not typographic verdicts; forcedBreak marks deliberate <br> breaks.',
      'Finite CSS/Web animations are finished before measuring; scroll-triggered states are captured after one scroll pass.',
      'axe-core catches only part of WCAG issues (published estimates about 30-57%); keyboard, screen reader and zoom checks stay manual.',
      'Playwright\'s bundled Chromium has no H.264 or AAC decoder, so an MP4 hero can report MEDIA_ERR_SRC_NOT_SUPPORTED (code 4) here and still play in Chrome, Safari and Edge. Point PLAYWRIGHT_CHROMIUM at Google Chrome to test real playback, or judge that video from its poster.',
      'The early frame is one moment; a white flash can also come from a late-loading stylesheet or a media element without a background. Check paintedBackground and look at the PNG.',
    ] };

  for (const size of opts.sizes) {
    const context = await browser.newContext({ viewport: { width: size.width, height: size.height }, deviceScaleFactor: opts.dpr,
      colorScheme: opts.colorScheme, reducedMotion: opts.reducedMotion ? 'reduce' : 'no-preference', bypassCSP: true });
    const page = await context.newPage();
    const failedRequests = []; const external = new Set(); const consoleErrors = [];
    let listening = true; // stop recording once our own probes (axe) start
    const aborted = [];
    page.on('requestfailed', (r) => {
      if (!listening) return;
      const error = (r.failure() || {}).errorText || 'failed';
      // Media range requests the browser cancels itself report net::ERR_ABORTED; they are not broken assets.
      if (/ERR_ABORTED/.test(error)) aborted.push({ url: r.url(), resourceType: r.resourceType() }); else failedRequests.push({ url: r.url(), error, resourceType: r.resourceType() });
    });
    page.on('response', (r) => { if (listening && r.status() >= 400) failedRequests.push({ url: r.url(), status: r.status(), resourceType: r.request().resourceType() }); });
    page.on('request', (r) => { const u = r.url(); if (listening && /^https?:/.test(u) && !u.startsWith(pageOrigin)) external.add(new URL(u).origin); });
    page.on('console', (m) => { if (listening && m.type() === 'error' && consoleErrors.length < 20) consoleErrors.push(m.text().slice(0, 300)); });
    page.on('pageerror', (e) => { if (listening && consoleErrors.length < 20) consoleErrors.push(`pageerror: ${e.message.slice(0, 300)}`); });
    const entry = { size: size.label, width: size.width, height: size.height };
    try {
      if (opts.early) {
        await page.goto(url, { waitUntil: 'commit', timeout: 45000 });
        await page.waitForTimeout(opts.early);
        const earlyShot = join(outDir, `${slug}-${size.label}-early.png`);
        await page.screenshot({ path: earlyShot });
        entry.early = { atMs: opts.early, screenshot: earlyShot, ...(await page.evaluate(firstPaintProbe).catch((error) => ({ error: error.message.split('\n')[0] }))) };
        await page.waitForLoadState('load', { timeout: 45000 });
      } else {
        await page.goto(url, { waitUntil: 'load', timeout: 45000 });
      }
      await page.waitForLoadState('networkidle', { timeout: 5000 }).catch(() => {});
      await waitForVideos(page, opts.videoWait);
      await settle(page, opts.wait);
      Object.assign(entry, await page.evaluate(pageDiagnostics, { wrapSelector: opts.wrapSelector, exclude: opts.exclude, limit: 15 }));
      entry.fonts.rendered = await renderedFonts(context, page);
      const shot = join(outDir, `${slug}-${size.label}.png`);
      await page.screenshot({ path: shot, fullPage: opts.fullPage, animations: 'disabled' });
      entry.screenshot = shot;
      listening = false;
      if (axe.source) {
        try { entry.axe = await runAxe(page, axe.source, opts.exclude, url.startsWith('http')); } catch (error) { entry.axe = { error: error.message.split('\n')[0] }; }
      }
    } catch (error) {
      entry.error = error.message.split('\n')[0];
    }
    entry.requests = { failed: failedRequests.slice(0, 20), aborted: aborted.length, abortedExamples: aborted.slice(0, 5), externalOrigins: [...external] };
    if (entry.media) {
      // Chromium reports a missing file and an unsupported codec with the same code 4; the request log tells them apart.
      for (const v of entry.media.videos) {
        if (!v.error) continue;
        const requestFailed = failedRequests.some((f) => f.url === v.src);
        v.diagnosis = requestFailed ? 'source request failed (missing or blocked file)'
          : v.error.code === 4 ? 'format or codec not supported by this browser' : 'playback error';
        v.codecOnly = !requestFailed && v.error.code === 4;
      }
    }
    entry.consoleErrors = consoleErrors;
    report.results.push(entry);
    await context.close();
  }
  await browser.close();
  if (server) server.close();

  const reportPath = join(outDir, 'report.json');
  writeFileSync(reportPath, `${JSON.stringify(report, null, 2)}\n`);

  let blocking = 0;
  const lines = [`render_review ${VERSION}: ${opts.target}`, `  ${report.browser}; axe: ${axe.source ? 'on' : axe.note}`];
  for (const r of report.results) {
    if (r.error) { lines.push(`  ${r.size.padEnd(9)} ERROR ${r.error}`); blocking += 1; continue; }
    const runts = r.wrap.singleWordLastLines;
    const headingRunts = runts.filter((x) => x.kind === 'heading').length;
    const contrastFails = r.contrast.failures.filter((f) => !f.exemptCandidate).reduce((n, f) => n + f.count, 0);
    const unmeasured = Object.values(r.contrast.unmeasured).reduce((a, b) => a + b, 0);
    const serious = r.axe && r.axe.violations ? r.axe.violations.filter((v) => ['serious', 'critical'].includes(v.impact)) : [];
    const rendered = r.fonts.rendered.families;
    const families = (rendered.length ? rendered : r.fonts.declaredPrimary).map((f) => f.family);
    const declaredNames = r.fonts.declaredPrimary.map((f) => f.family.toLowerCase());
    const fallback = rendered.filter((f) => !f.webFont && !declaredNames.some((d) => f.family.toLowerCase().startsWith(d)));
    const boxOverflow = r.wrap.textOverflow;
    lines.push(`  ${r.size.padEnd(9)} overflow: ${r.horizontalOverflow ? `YES (${r.documentWidth}px > ${r.viewportWidth}px)` : r.overflowOffenders.some((o) => o.clippedByRoot) ? 'clipped by root' : 'none'}`
      + ` | text overflowing its box: ${boxOverflow.length}`
      + ` | single-word last lines: ${runts.length} (${headingRunts} in headings)`
      + ` | contrast: ${contrastFails} fail / ${r.contrast.measured} measured, ${unmeasured} unmeasured`
      + ` | axe: ${r.axe ? (r.axe.error ? `error (${r.axe.error})` : `${r.axe.violations.length} violations (${serious.length} serious+), ${r.axe.needsReview.length} to review`) : 'not run'}`);
    lines.push(`  ${''.padEnd(9)} fonts: ${families.slice(0, 6).join(', ') || 'none'}${families.length > 6 ? ` (+${families.length - 6})` : ''}`
      + `${r.requests.failed.length ? ` | failed requests: ${r.requests.failed.length}` : ''}${r.requests.externalOrigins.length ? ` | external: ${r.requests.externalOrigins.join(', ')}` : ''}`
      + `${r.consoleErrors.length ? ` | console errors: ${r.consoleErrors.length}` : ''}`
      + `${fallback.length ? ` | fallback glyphs (font not first in any stack): ${fallback.map((f) => `${f.family} x${f.glyphs}`).join(', ')}` : ''}`);
    const vids = r.media ? r.media.videos : [];
    const vidErrors = vids.filter((v) => v.error);
    const codecOnly = vidErrors.filter((v) => v.codecOnly);
    const brokenImgs = r.media ? r.media.brokenImages : [];
    if (vids.length || brokenImgs.length || r.early) {
      lines.push(`  ${''.padEnd(9)} ${vids.length ? `videos: ${vids.length} (${vids.filter((v) => v.hasFrame).length} with a frame, ${vids.filter((v) => !v.paused).length} playing, ${vidErrors.length} errors${codecOnly.length ? `, ${codecOnly.length} codec-unsupported in this browser` : ''})` : 'videos: 0'}`
        + ` | broken images: ${brokenImgs.length}`
        + `${r.early ? ` | first paint @${r.early.atMs}ms: ${r.early.paintedBackground || r.early.error} (${r.early.screenshot})` : ''}`);
      for (const v of vidErrors.slice(0, 3)) lines.push(`  ${''.padEnd(9)}   video ${v.error.name}, ${v.diagnosis}: ${v.src || v.selector}`);
      for (const v of vids.filter((x) => !x.error && !x.hasFrame).slice(0, 3)) lines.push(`  ${''.padEnd(9)}   video has no frame yet (readyState ${v.readyState}): ${v.src || v.selector}`);
      for (const i of brokenImgs.slice(0, 3)) lines.push(`  ${''.padEnd(9)}   broken image: ${i.src}`);
    }
    lines.push(`  ${''.padEnd(9)} screenshot: ${r.screenshot}`);
    for (const o of boxOverflow.slice(0, 3)) lines.push(`  ${''.padEnd(9)}   ${o.clipped ? 'clipped' : 'spills'} text (${o.scrollWidth}px in ${o.clientWidth}px): ${o.selector}`);
    for (const o of r.overflowOffenders.slice(0, 3)) lines.push(`  ${''.padEnd(9)}   off-canvas ${o.left}..${o.right}px${o.clippedByRoot ? ' (hidden by root overflow)' : ''}: ${o.selector}`);
    for (const runt of runts.filter((x) => x.kind === 'heading').slice(0, 3)) lines.push(`  ${''.padEnd(9)}   heading ends on "${runt.lastLine}"${runt.forcedBreak ? ' (has <br>)' : ''}: ${runt.selector}`);
    for (const f of r.contrast.failures.filter((x) => !x.exemptCandidate).slice(0, 3)) lines.push(`  ${''.padEnd(9)}   contrast ${f.ratio}:1 < ${f.required}:1 ${f.fg} on ${f.bg} ${f.fontSize}/${f.fontWeight}: ${f.examples[0].selector}`);
    for (const v of serious.slice(0, 3)) lines.push(`  ${''.padEnd(9)}   axe ${v.impact} ${v.id} x${v.nodes}: ${v.targets[0] || ''}`);
    if (r.horizontalOverflow || boxOverflow.some((o) => o.clipped) || contrastFails || serious.length || r.requests.failed.length
      || brokenImgs.length || vidErrors.length > codecOnly.length) blocking += 1;
  }
  lines.push(`  report: ${reportPath}`);
  process.stdout.write(`${lines.join('\n')}\n`);
  if (opts.strict && blocking) process.exit(2);
}

main().catch((error) => fail(error.stack || error.message));
