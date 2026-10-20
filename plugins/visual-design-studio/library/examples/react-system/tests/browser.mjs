// Version-Timestamp: 2026-10-20 02:52:00 UTC
// Browser QA for the built specimen (dist/). Run `npm run build` first, then:
//   PLAYWRIGHT_MODULE=/path/to/node_modules/playwright AXE_SCRIPT=/path/to/axe-core/axe.min.js \
//   CHROME_EXECUTABLE=/path/to/chromium node tests/browser.mjs
// Env: PLAYWRIGHT_MODULE (default "playwright"), AXE_SCRIPT (required), CHROME_EXECUTABLE (optional),
// BASE_URL (optional; otherwise dist/ is served on a free port), QA_OUTPUT (default qa-output/),
// QA_GREP (optional regular expression: run only checks whose name matches).
import assert from 'node:assert/strict';
import { mkdir, writeFile } from 'node:fs/promises';
import { createRequire } from 'node:module';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { startServer } from './static-server.mjs';

const require = createRequire(import.meta.url);
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const out = path.resolve(root, process.env.QA_OUTPUT || 'qa-output');
await mkdir(out, { recursive: true });

const server = process.env.BASE_URL ? null : await startServer(path.join(root, 'dist'));
const base = process.env.BASE_URL || server.url;
const browser = await chromium.launch({
  headless: true,
  ...(process.env.CHROME_EXECUTABLE ? { executablePath: process.env.CHROME_EXECUTABLE } : {}),
});

const THEMES = ['light', 'dark', 'high-contrast'];
const BRANDS = ['meridian', 'ember'];
const PAGES = ['index', 'billing'];
const WIDTHS = [
  { name: 'desktop', width: 1440, height: 1000 },
  { name: 'mobile', width: 390, height: 844, isMobile: true, hasTouch: true },
];
const AXE_TAGS = ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'];

const results = [];
const pageErrors = [];
const external = [];
const grep = process.env.QA_GREP ? new RegExp(process.env.QA_GREP) : null;
async function record(name, fn) {
  if (grep && !grep.test(name)) return;
  try {
    const details = await fn();
    results.push({ name, pass: true, details });
  } catch (error) {
    results.push({ name, pass: false, error: String(error?.stack || error).split('\n').slice(0, 30).join('\n') });
  }
}
function monitor(page) {
  page.on('pageerror', (e) => pageErrors.push(`${page.url()}: ${e}`));
  page.on('console', (m) => {
    if (m.type() === 'error') pageErrors.push(`${page.url()}: console.error ${m.text()}`);
  });
  page.on('request', (r) => {
    const url = r.url();
    if (!url.startsWith(base) && !url.startsWith('data:') && !url.startsWith('blob:')) external.push(url);
  });
}
const url = (page, params = {}) => `${base}/${page}.html?${new URLSearchParams({ theme: 'light', brand: 'meridian', dir: 'ltr', ...params })}`;

async function settle(page) {
  await page.evaluate(() => document.fonts.ready);
  // The billing usage card loads after 900ms; wait so axe and screenshots see the settled screen.
  await page.waitForTimeout(1200);
}

async function axe(page) {
  if (!process.env.AXE_SCRIPT) throw new Error('AXE_SCRIPT is not set; point it at axe-core/axe.min.js (4.10.x).');
  if (!(await page.evaluate(() => Boolean(window.axe)))) await page.addScriptTag({ path: process.env.AXE_SCRIPT });
  const result = await page.evaluate(async (tags) => window.axe.run(document, { runOnly: { type: 'tag', values: tags } }), AXE_TAGS);
  return result.violations.map((v) => ({ id: v.id, impact: v.impact, help: v.help, nodes: v.nodes.slice(0, 5).map((n) => n.target.join(' ')) }));
}

async function noOverflow(page) {
  const [scrollWidth, innerWidth] = await page.evaluate(() => [document.documentElement.scrollWidth, window.innerWidth]);
  assert.ok(scrollWidth <= innerWidth, `horizontal overflow: scrollWidth ${scrollWidth} > ${innerWidth}`);
}

// Radix moves roving focus in a setTimeout after keydown; retry assertions briefly instead of sleeping.
async function eventually(check, timeout = 1500) {
  const start = Date.now();
  for (;;) {
    try {
      return await check();
    } catch (error) {
      if (Date.now() - start > timeout) throw error;
      await new Promise((r) => setTimeout(r, 25));
    }
  }
}

const activeInfo = (page) =>
  page.evaluate(() => {
    const el = document.activeElement;
    return { tag: el?.tagName, name: el?.getAttribute('aria-label') || el?.textContent?.trim().slice(0, 40), inDialog: Boolean(el?.closest('[role="dialog"],[role="alertdialog"]')) };
  });

try {
  // 1. Every page x width x theme x brand: axe, overflow, screenshot.
  for (const viewport of WIDTHS) {
    const context = await browser.newContext({ viewport: { width: viewport.width, height: viewport.height }, isMobile: viewport.isMobile, hasTouch: viewport.hasTouch });
    const page = await context.newPage();
    monitor(page);
    for (const name of PAGES) {
      for (const brand of BRANDS) {
        for (const theme of THEMES) {
          await record(`${name} ${viewport.width}px ${brand} ${theme}: axe clean, no horizontal overflow`, async () => {
            await page.goto(url(name, { theme, brand }));
            await settle(page);
            assert.equal(await page.evaluate(() => document.documentElement.dataset.theme), theme);
            assert.equal(await page.evaluate(() => document.documentElement.dataset.brand), brand);
            await noOverflow(page);
            const violations = await axe(page);
            await page.screenshot({ path: path.join(out, `${name}-${viewport.width}-${brand}-${theme}.png`), fullPage: true });
            assert.deepEqual(violations, []);
          });
        }
      }
      await record(`${name} ${viewport.width}px right-to-left: axe clean, no overflow, mirrored layout`, async () => {
        await page.goto(url(name, { dir: 'rtl' }));
        await settle(page);
        await noOverflow(page);
        const violations = await axe(page);
        await page.screenshot({ path: path.join(out, `${name}-${viewport.width}-meridian-light-rtl.png`), fullPage: true });
        assert.deepEqual(violations, []);
        if (viewport.width >= 1024) {
          const sel = name === 'index' ? 'nav[aria-label="Components"]' : 'nav[aria-label="Workspace settings"]';
          const [navX, mainX] = await page.evaluate((s) => [document.querySelector(s).getBoundingClientRect().x, document.querySelector('main').getBoundingClientRect().x], sel);
          assert.ok(navX > mainX, 'side navigation should sit on the right in RTL');
        }
      });
    }
    await context.close();
  }

  const context = await browser.newContext({ viewport: { width: 1440, height: 1000 } });
  const page = await context.newPage();
  monitor(page);

  // 2. Dialog: focus moves in, Tab is trapped, Escape closes, focus returns to the trigger.
  await record('dialog traps focus, closes on Escape and returns focus (form dialog)', async () => {
    await page.goto(url('index'));
    await settle(page);
    const trigger = page.getByRole('button', { name: 'Invite member' });
    await trigger.focus();
    await page.keyboard.press('Enter');
    const dialog = page.getByRole('dialog', { name: 'Invite a member' });
    await dialog.waitFor();
    assert.equal(await dialog.getAttribute('aria-modal'), 'true');
    assert.match(await page.evaluate(() => document.activeElement.getAttribute('type') ?? ''), /email/, 'initial focus on the email field');
    await page.waitForTimeout(400);
    await page.screenshot({ path: path.join(out, 'overlay-dialog-form.png') });
    for (let i = 0; i < 12; i++) {
      await page.keyboard.press('Tab');
      assert.equal((await activeInfo(page)).inDialog, true, `Tab ${i + 1} left the dialog`);
    }
    for (let i = 0; i < 12; i++) {
      await page.keyboard.press('Shift+Tab');
      assert.equal((await activeInfo(page)).inDialog, true, `Shift+Tab ${i + 1} left the dialog`);
    }
    await page.keyboard.press('Escape');
    await dialog.waitFor({ state: 'detached' });
    assert.equal(await trigger.evaluate((el) => el === document.activeElement), true, 'focus returned to trigger');
  });

  await record('alertdialog starts on the safe action, ignores outside clicks, Escape returns focus', async () => {
    await page.goto(url('index'));
    await settle(page);
    const trigger = page.locator('button[aria-haspopup="dialog"]', { hasText: 'Delete project' });
    await trigger.focus();
    await page.keyboard.press('Enter');
    const dialog = page.getByRole('alertdialog');
    await dialog.waitFor();
    assert.equal((await activeInfo(page)).name, 'Keep project');
    await page.waitForTimeout(400);
    await page.screenshot({ path: path.join(out, 'overlay-alertdialog.png') });
    await page.mouse.click(5, 5);
    assert.equal(await dialog.isVisible(), true, 'outside click must not dismiss a confirmation');
    await page.keyboard.press('Escape');
    await dialog.waitFor({ state: 'detached' });
    assert.equal(await trigger.evaluate((el) => el === document.activeElement), true);
  });

  await record('overflowing dialog body becomes a named, focusable scroll region', async () => {
    await page.setViewportSize({ width: 1440, height: 600 });
    await page.goto(url('index'));
    await settle(page);
    await page.getByRole('button', { name: 'Read the terms' }).click();
    const region = page.getByRole('region', { name: 'Subscription terms' });
    await region.waitFor();
    assert.equal(await region.getAttribute('tabindex'), '0');
    await page.keyboard.press('Escape');
    await page.setViewportSize({ width: 1440, height: 1000 });
  });

  // 3. Tabs: arrow keys, Home, End, disabled tab skipped, RTL mirrored.
  await record('tabs move with arrow keys, Home and End', async () => {
    await page.goto(url('index'));
    await settle(page);
    const list = page.getByRole('tablist', { name: 'Project views' });
    const tab = (name) => list.getByRole('tab', { name });
    await tab('Overview').focus();
    await page.keyboard.press('ArrowRight');
    await eventually(async () => {
      assert.equal(await tab(/Activity/).getAttribute('aria-selected'), 'true');
      assert.equal(await tab(/Activity/).evaluate((el) => el === document.activeElement), true);
    });
    await page.keyboard.press('End');
    await eventually(async () => assert.equal(await tab(/Files/).getAttribute('aria-selected'), 'true', 'End skips the disabled Archive tab'));
    await page.keyboard.press('Home');
    await eventually(async () => assert.equal(await tab('Overview').getAttribute('aria-selected'), 'true'));
    await page.keyboard.press('ArrowLeft');
    await eventually(async () => assert.equal(await tab(/Files/).getAttribute('aria-selected'), 'true', 'ArrowLeft wraps to the last enabled tab'));
    await page.keyboard.press('Tab');
    assert.equal(await page.evaluate(() => document.activeElement.getAttribute('role')), 'tabpanel', 'Tab moves into the panel');
  });

  await record('tabs mirror arrow keys in RTL', async () => {
    await page.goto(url('index', { dir: 'rtl' }));
    await settle(page);
    const list = page.getByRole('tablist', { name: 'Project views' });
    await list.getByRole('tab', { name: 'Overview' }).focus();
    await page.keyboard.press('ArrowLeft');
    await eventually(async () => assert.equal(await list.getByRole('tab', { name: /Activity/ }).getAttribute('aria-selected'), 'true'));
  });

  // 4. Other keyboard contracts.
  await record('checkbox, switch, radio and select work from the keyboard', async () => {
    await page.goto(url('index'));
    await settle(page);
    const renewals = page.getByRole('checkbox', { name: 'Renewal reminders' });
    await renewals.focus();
    await page.keyboard.press('Space');
    assert.equal(await renewals.getAttribute('aria-checked'), 'true');
    assert.equal(await page.getByRole('checkbox', { name: 'All billing email' }).getAttribute('aria-checked'), 'true', 'parent becomes checked when all children are');
    const seat = page.getByRole('switch', { name: 'Seat limit alerts' }).first();
    await seat.focus();
    await page.keyboard.press('Space');
    assert.equal(await seat.getAttribute('aria-checked'), 'true');
    const card = page.getByRole('radio', { name: 'Card ending 4242' });
    await card.focus();
    // Radix checks a radio when focus arrives while an arrow key is held; hold it like a person would.
    await page.keyboard.down('ArrowDown');
    await page.waitForTimeout(60);
    await page.keyboard.up('ArrowDown');
    await eventually(async () => assert.equal(await page.getByRole('radio', { name: 'Bank transfer on invoice' }).getAttribute('aria-checked'), 'true'));
    const country = page.getByRole('combobox', { name: /Billing country/ });
    await country.focus();
    await page.keyboard.press('Enter');
    await page.getByRole('listbox').waitFor();
    await page.waitForTimeout(300);
    await page.screenshot({ path: path.join(out, 'overlay-select-open.png') });
    await page.keyboard.type('Ire', { delay: 40 });
    await eventually(async () => assert.match(await page.evaluate(() => document.activeElement?.textContent ?? ''), /Ireland/));
    await page.keyboard.press('Enter');
    await page.getByRole('listbox').waitFor({ state: 'detached' });
    assert.match(await country.innerText(), /Ireland/);
    assert.equal(await country.evaluate((el) => el === document.activeElement), true, 'focus returns to the trigger');
  });

  await record('tooltip opens on focus and Escape dismisses it', async () => {
    await page.goto(url('index'));
    await settle(page);
    const button = page.getByRole('button', { name: 'Copy link' });
    await button.focus();
    const tip = page.getByRole('tooltip', { name: 'Copy link' });
    await tip.waitFor({ timeout: 3000 });
    await page.waitForTimeout(300);
    await button.screenshot({ path: path.join(out, 'overlay-tooltip-trigger.png') });
    await page.screenshot({ path: path.join(out, 'overlay-tooltip.png') });
    await page.keyboard.press('Escape');
    await tip.waitFor({ state: 'detached' });
  });

  await record('toast announces through a status region and offers its action', async () => {
    await page.goto(url('index'));
    await settle(page);
    await page.getByRole('button', { name: 'Archive with undo' }).click();
    const toast = page.locator('[data-slot="toast"]').first();
    await toast.waitFor();
    // Radix announces each toast through a separate live region (role=status) instead of the list item.
    await page.locator('[role="status"]', { hasText: '3 invoices archived' }).first().waitFor({ state: 'attached', timeout: 2000 });
    await page.waitForTimeout(500);
    await page.screenshot({ path: path.join(out, 'overlay-toast.png') });
    await page.keyboard.press('F8');
    assert.ok(await page.evaluate(() => Boolean(document.activeElement?.closest('[data-slot="toast-viewport"]'))), 'F8 moves focus to notifications');
    await toast.getByRole('button', { name: 'Undo' }).click();
    await page.locator('[data-slot="toast"]', { hasText: 'Invoices restored' }).waitFor();
  });

  await record('data table sorts with aria-sort and selects rows', async () => {
    await page.goto(url('index'));
    await settle(page);
    const table = page.getByRole('table', { name: 'Invoices, Harbor Studio' });
    const amount = table.getByRole('columnheader', { name: /Amount/ });
    await amount.getByRole('button').click();
    assert.equal(await amount.getAttribute('aria-sort'), 'descending');
    assert.equal(await table.getByRole('columnheader', { name: /Date/ }).getAttribute('aria-sort'), null, 'only one header carries aria-sort');
    const amounts = await table.locator('tbody tr td:last-child').allInnerTexts();
    assert.equal(amounts[0].trim(), '$4,320.00');
    assert.equal(amounts.at(-1).trim(), 'Pending', 'missing values sort last');
    const numericAlign = await table.locator('tbody tr td:last-child').first().evaluate((el) => [getComputedStyle(el).textAlign, getComputedStyle(el).fontVariantNumeric]);
    assert.equal(numericAlign[0], 'end');
    assert.match(numericAlign[1], /tabular-nums/);
    await table.getByRole('checkbox', { name: 'Select all rows' }).click();
    await page.getByText('8 selected', { exact: true }).waitFor();
  });

  // 5. Keyboard reachability and visible focus on every control.
  for (const [name, width] of [['index', 1440], ['index', 390], ['billing', 1440], ['billing', 390]]) {
    await record(`${name} ${width}px: Tab reaches every control and each shows a focus indicator`, async () => {
      await page.setViewportSize({ width, height: 900 });
      await page.goto(url(name));
      await settle(page);
      const expected = await page.evaluate(() => {
        const selector = 'a[href], button, input, select, textarea, [tabindex], [contenteditable="true"]';
        const list = [];
        let n = 0;
        for (const el of document.querySelectorAll(selector)) {
          if (el.matches(':disabled') || el.closest('[inert]') || el.closest('[aria-hidden="true"]')) continue;
          if (el.getAttribute('tabindex') === '-1') continue;
          // Roving-focus containers (Radix radiogroup, tablist) forward focus to their active item.
          if (el.matches('[role="radiogroup"], [role="tablist"]')) continue;
          if (el.tagName === 'INPUT' && el.type === 'hidden') continue;
          const style = getComputedStyle(el);
          const rect = el.getBoundingClientRect();
          // sr-only skip links count: they become visible on focus.
          const srOnly = el.classList.contains('sr-only');
          if (!srOnly && (style.visibility === 'hidden' || style.display === 'none' || rect.width === 0 || rect.height === 0)) continue;
          if (el.closest('[hidden]')) continue;
          el.setAttribute('data-qa-stop', String(n++));
          list.push({ id: el.getAttribute('data-qa-stop'), label: (el.getAttribute('aria-label') || el.textContent || el.getAttribute('placeholder') || el.tagName).trim().slice(0, 50) });
        }
        return list;
      });
      const reached = new Set();
      const noRing = [];
      for (let i = 0; i < expected.length + 25; i++) {
        await page.keyboard.press('Tab');
        const info = await page.evaluate(() => {
          const el = document.activeElement;
          if (!el || el === document.body) return null;
          const ringOn = (node, pseudo) => {
            if (!node) return false;
            const s = getComputedStyle(node, pseudo);
            return s.outlineStyle !== 'none' && parseFloat(s.outlineWidth) >= 2;
          };
          const ring =
            ringOn(el) ||
            ringOn(el, '::after') ||
            ringOn(el.querySelector('[data-slot="checkbox-box"],[data-slot="radio-circle"]')) ||
            ringOn(el.parentElement) ||
            ringOn(el.parentElement?.parentElement);
          return { id: el.getAttribute('data-qa-stop'), ring, label: (el.getAttribute('aria-label') || el.textContent || el.tagName).trim().slice(0, 50) };
        });
        if (!info) continue;
        if (info.id !== null) reached.add(info.id);
        if (!info.ring) noRing.push(info.label);
      }
      const missed = expected.filter((e) => !reached.has(e.id)).map((e) => e.label);
      assert.deepEqual(missed, [], 'controls never reached with Tab');
      assert.deepEqual([...new Set(noRing)], [], 'focused controls without a visible focus indicator');
      return { tabStops: expected.length };
    });
  }

  // 6. Billing flows composed from the parts.
  await record('billing: change plan dialog, Escape returns focus, confirm shows a toast with Undo', async () => {
    await page.setViewportSize({ width: 1440, height: 1000 });
    await page.goto(url('billing'));
    await settle(page);
    const trigger = page.getByRole('button', { name: 'Change plan' });
    await trigger.click();
    const dialog = page.getByRole('dialog', { name: 'Change plan' });
    await dialog.waitFor();
    await page.keyboard.press('Escape');
    await dialog.waitFor({ state: 'detached' });
    assert.equal(await trigger.evaluate((el) => el === document.activeElement), true);
    await trigger.click();
    await dialog.getByRole('radio', { name: 'Business' }).click();
    await page.waitForTimeout(400);
    await page.screenshot({ path: path.join(out, 'billing-change-plan-dialog.png') });
    await dialog.getByRole('button', { name: 'Confirm change' }).click();
    await dialog.waitFor({ state: 'detached' });
    await page.locator('[data-slot="toast"]', { hasText: 'Plan changed to Business' }).waitFor();
    assert.match(await page.locator('#plan-title').innerText(), /Business/);
  });

  await record('billing: invalid form shows a focused error summary linked to fields', async () => {
    await page.getByRole('tab', { name: 'Payment details' }).click();
    await page.getByRole('button', { name: 'Save billing details' }).click();
    const summary = page.locator('#billing-error-summary');
    await summary.waitFor();
    await page.waitForFunction(() => document.activeElement?.id === 'billing-error-summary');
    assert.match(await page.title(), /^Error: /);
    await page.locator('#billing-details-title').scrollIntoViewIfNeeded();
    await page.screenshot({ path: path.join(out, 'billing-form-errors.png'), fullPage: true });
    const email = page.getByRole('textbox', { name: /Billing email/ });
    assert.equal(await email.getAttribute('aria-invalid'), 'true');
    const describedBy = (await email.getAttribute('aria-describedby')).split(' ');
    assert.ok(describedBy.length === 2, 'hint and error are both linked');
    await summary.getByRole('link', { name: /email address in the correct format/ }).click();
    assert.equal(await email.evaluate((el) => el === document.activeElement), true);
    await email.fill('accounts@harbor.studio');
    assert.equal(await email.getAttribute('aria-invalid'), null, 'error clears on edit once fixed');
  });

  await record('billing: banner action moves to Payment details and focuses Replace card', async () => {
    await page.goto(url('billing'));
    await settle(page);
    await page.getByRole('button', { name: 'Update card' }).click();
    await page.waitForFunction(() => document.activeElement?.textContent?.trim() === 'Replace card');
    assert.equal(await page.getByRole('tab', { name: 'Payment details' }).getAttribute('aria-selected'), 'true');
  });

  await context.close();

  // 7. Reduced motion collapses transitions and animations to the token value (0.01ms) or none.
  await record('prefers-reduced-motion disables transitions and animations', async () => {
    const normal = await browser.newContext({ viewport: { width: 1440, height: 1000 } });
    const p1 = await normal.newPage();
    await p1.goto(url('index'));
    const baseline = await p1.locator('[data-slot="button"]').first().evaluate((el) => getComputedStyle(el).transitionDuration);
    assert.equal(baseline, '0.12s', 'baseline uses --duration-fast');
    await normal.close();

    const reduced = await browser.newContext({ viewport: { width: 1440, height: 1000 }, reducedMotion: 'reduce' });
    const p2 = await reduced.newPage();
    monitor(p2);
    await p2.goto(url('index'));
    await settle(p2);
    const seconds = (value) => Math.max(...value.split(',').map((v) => parseFloat(v)));
    const durations = await p2.evaluate(() =>
      [...document.querySelectorAll('[data-slot="button"], [data-slot="switch"], [data-slot="switch-thumb"], [data-slot="tabs-trigger"], [data-slot="checkbox-box"]')].map(
        (el) => getComputedStyle(el).transitionDuration,
      ),
    );
    assert.ok(durations.length > 20);
    for (const d of durations) assert.ok(seconds(d) <= 0.0001, `transition-duration ${d} should be 0.01ms or less`);
    assert.equal(await p2.locator('[data-slot="skeleton"]').first().evaluate((el) => getComputedStyle(el).animationName), 'none');
    await p2.getByRole('button', { name: 'Invite member' }).click();
    const dialog = p2.locator('[data-slot="dialog"]');
    await dialog.waitFor();
    assert.ok(seconds(await dialog.evaluate((el) => getComputedStyle(el).animationDuration)) <= 0.0001, 'dialog entrance is instant');
    await p2.keyboard.press('Escape');
    await reduced.close();
  });

  await record('no page errors, console errors or external requests', async () => {
    assert.deepEqual(pageErrors, []);
    assert.deepEqual([...new Set(external)], []);
  });
} finally {
  await browser.close();
  await server?.close();
  await writeFile(path.join(out, 'results.json'), JSON.stringify({ base, results, pageErrors, external }, null, 2));
}

for (const r of results) console.log(`${r.pass ? 'PASS' : 'FAIL'} ${r.name}${r.pass ? '' : `\n  ${r.error}`}`);
const failed = results.filter((r) => !r.pass).length;
console.log(`\n${results.length - failed} passed, ${failed} failed. Screenshots and results.json in ${path.relative(root, out)}/`);
if (failed) process.exitCode = 1;
