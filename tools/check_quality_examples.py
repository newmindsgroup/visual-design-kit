#!/usr/bin/env python3
"""Browser checks for the fictional quality-benchmark examples, not aesthetic acceptance."""
# Version-Timestamp: 2026-09-16T18:27:08.062526-04:00
import argparse
from datetime import datetime
import asyncio
import json
import re
import sys
from pathlib import Path
from urllib.parse import urljoin

from playwright.async_api import async_playwright


WIDTHS = (320, 390, 768, 1024, 1440)
BRANDS = ("form", "tidal")


def page_url(base_url, path):
    return urljoin(base_url.rstrip("/") + "/", path)


def write_report(output, report):
    output.mkdir(parents=True, exist_ok=True)
    (output / "results.json").write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")


class Checks:
    def __init__(self, base_url, output):
        self.base_url = base_url
        self.output = output
        self.failures = []
        self.console = []
        self.results = []
        self.wrap_records = []

    def fail(self, check, detail, url=None):
        item = {"check": check, "detail": detail}
        if url:
            item["url"] = url
        self.failures.append(item)

    async def open_page(self, context, relative, width, reduced_motion="no-preference", block_fonts=False, block_timeline=False):
        page = await context.new_page()
        await page.set_viewport_size({"width": width, "height": 900})
        await page.emulate_media(reduced_motion=reduced_motion)
        location = page_url(self.base_url, relative)
        def console(message):
            if message.type != "error":
                return
            if (block_fonts or block_timeline) and "net::ERR_FAILED" in message.text:
                return
            self.console.append({"type": message.type, "text": message.text, "url": location})
        page.on("console", console)
        page.on("pageerror", lambda error: self.console.append({"type": "pageerror", "text": str(error), "url": location}))
        if block_fonts:
            await page.route("**/*.ttf", lambda route: route.abort())
        if block_timeline:
            await page.route("**/timeline.json", lambda route: route.abort())
        response = await page.goto(location, wait_until="networkidle")
        if response is None or response.status >= 400:
            self.fail("page_load", f"HTTP {response.status if response else 'no response'}", location)
        await page.evaluate("document.fonts.ready")
        return page, location

    async def capture(self, page, name):
        safe = re.sub(r"[^a-z0-9_.-]+", "-", name.lower())
        await page.screenshot(path=str(self.output / "screens" / f"{safe}.png"), full_page=True)

    async def overflow(self, page):
        return await page.evaluate("({scrollWidth:document.documentElement.scrollWidth, clientWidth:document.documentElement.clientWidth})")

    async def wrap_diagnostics(self, page, brand, variant, width, location):
        if not await page.evaluate("typeof window.inspectTextWrapping === 'function'"):
            await page.add_script_tag(url=page_url(self.base_url, "../../scripts/wrap-diagnostics.js"))
        diagnostics = await page.evaluate("window.inspectTextWrapping()")
        self.wrap_records.append({"brand": brand, "variant": variant, "width": width, "diagnostics": diagnostics})
        for item in diagnostics:
            if item["orphanCandidate"]:
                self.fail("wrap_orphan", f"{brand} {variant} at {width}px: {item['text']}", location)
            if item["overflow"]:
                self.fail("wrap_overflow", f"{brand} {variant} at {width}px: {item['text']}", location)

    async def text_bounds(self, page):
        return await page.evaluate("""() => [...document.querySelectorAll('#wordmark,#headline,#intro,#cta,[data-wrap]')].map(element => {
            const range=document.createRange(); range.selectNodeContents(element);
            const rects=[...range.getClientRects()].filter(rect => rect.width && rect.height);
            return {selector: element.id ? '#'+element.id : '[data-wrap]', text: element.textContent.trim(),
                overflow: element.scrollWidth > element.clientWidth + 1,
                visible: rects.length > 0,
                withinViewport: rects.every(rect => rect.left >= -1 && rect.right <= innerWidth + 1)};
        })""")

    async def check_specimens(self, context):
        for brand in BRANDS:
            candidate = None
            for width in WIDTHS:
                page, location = await self.open_page(context, f"specimen.html?brand={brand}", width)
                metrics = await self.overflow(page)
                if metrics["scrollWidth"] > metrics["clientWidth"] + 1:
                    self.fail("horizontal_overflow", f"{brand} candidate at {width}px: {metrics}", location)
                fonts = await page.evaluate("""() => ({
                    newsreader: document.fonts.check('400 32px Newsreader'),
                    archivo: document.fonts.check('400 16px Archivo'),
                    barlow: document.fonts.check('600 32px Barlow')
                })""")
                required = ("newsreader", "archivo") if brand == "form" else ("archivo", "barlow")
                for font in required:
                    if not fonts[font]:
                        self.fail("font_not_loaded", f"{brand} {font} at {width}px", location)
                snapshot = await page.evaluate("""() => ({
                    specimen: window.specimen,
                    copy: {intro: intro.textContent, cta: cta.textContent, caption: caption.textContent,
                           section: document.getElementById('section-title').textContent, rationale: rationale.textContent},
                    colors: {body: getComputedStyle(document.body).color, hero: getComputedStyle(document.querySelector('.hero')).backgroundColor,
                             headline: getComputedStyle(headline).color},
                    copyContainer: getComputedStyle(document.querySelector('.copy')).containerType,
                    productionClass: document.body.className
                })""")
                if snapshot["copyContainer"] != "inline-size":
                    self.fail("css_activation", f"{brand} candidate at {width}px has inactive copy container: {snapshot['copyContainer']}", location)
                if "generic" in snapshot["productionClass"] or "wrong" in snapshot["productionClass"]:
                    self.fail("control_class", f"candidate unexpectedly marked as control: {snapshot['productionClass']}", location)
                await self.wrap_diagnostics(page, brand, "candidate", width, location)
                if width == 320:
                    candidate = snapshot
                if width in {320, 1440}:
                    await self.capture(page, f"{brand}-candidate-{width}")
                await page.close()

                revised, revised_url = await self.open_page(context, f"specimen.html?brand={brand}&variant=revised", width)
                revised_metrics = await self.overflow(revised)
                if revised_metrics["scrollWidth"] > revised_metrics["clientWidth"] + 1:
                    self.fail("horizontal_overflow", f"{brand} revised at {width}px: {revised_metrics}", revised_url)
                revised_snapshot = await revised.evaluate("""() => ({
                    specimen: window.specimen,
                    copy: {intro: intro.textContent, cta: cta.textContent, caption: caption.textContent,
                           section: document.getElementById('section-title').textContent, rationale: rationale.textContent},
                    colors: {body: getComputedStyle(document.body).color, hero: getComputedStyle(document.querySelector('.hero')).backgroundColor,
                             headline: getComputedStyle(headline).color}
                })""")
                if width == 320:
                    if candidate["specimen"]["headline"] == revised_snapshot["specimen"]["headline"]:
                        self.fail("revision_headline", f"{brand} revision did not change headline", revised_url)
                    for key in ("product", "wordmark"):
                        if candidate["specimen"][key] != revised_snapshot["specimen"][key]:
                            self.fail("revision_invariant", f"{brand} changed {key}", revised_url)
                    if candidate["copy"] != revised_snapshot["copy"] or candidate["colors"] != revised_snapshot["colors"]:
                        self.fail("revision_invariant", f"{brand} changed non-headline copy or colors", revised_url)
                await self.wrap_diagnostics(revised, brand, "revised", width, revised_url)
                if width in {320, 1440}:
                    await self.capture(revised, f"{brand}-revised-{width}")
                await revised.close()

            await self.check_revision_fault_injections(context, brand)

    async def check_revision_fault_injections(self, context, brand):
        """Prove the invariant snapshot catches injected defects without source mutation."""
        selectors = {
            "wordmark": "document.querySelector('#wordmark').textContent = 'BROKEN'",
            "photo": "document.querySelector('#photo').src = 'assets/form.png?fault=1'",
            "palette": "document.querySelector('.hero').style.backgroundColor = 'rgb(255, 0, 255)'",
        }
        baseline_page, location = await self.open_page(context, f"specimen.html?brand={brand}", 390)
        baseline = await baseline_page.evaluate("""() => ({
            wordmark: wordmark.textContent, photo: photo.getAttribute('src'),
            hero: getComputedStyle(document.querySelector('.hero')).backgroundColor
        })""")
        await baseline_page.close()
        for name, injection in selectors.items():
            page, fault_url = await self.open_page(context, f"specimen.html?brand={brand}&variant=revised", 390)
            await page.evaluate(injection)
            fault = await page.evaluate("""() => ({
                wordmark: wordmark.textContent, photo: photo.getAttribute('src'),
                hero: getComputedStyle(document.querySelector('.hero')).backgroundColor
            })""")
            changed = fault != baseline
            if not changed:
                self.fail("revision_fault_detection", f"{brand} injected {name} fault escaped invariant snapshot", fault_url)
            await self.capture(page, f"{brand}-fault-{name}")
            await page.close()

    async def check_keyboard_and_spacing(self, context):
        page, location = await self.open_page(context, "specimen.html?brand=form", 320)
        await page.keyboard.press("Tab")
        skip = await page.evaluate("""() => { const item=document.activeElement, rect=item.getBoundingClientRect(); return {className:item.className, visible:rect.left >= 0 && rect.top >= 0}; }""")
        if skip["className"] != "skip" or not skip["visible"]:
            self.fail("keyboard_skip", f"Skip link is not the visible first focus target: {skip}", location)
        await page.keyboard.press("Enter")
        await page.focus("#cta")
        await page.keyboard.press("Enter")
        details = await page.evaluate("({hash:location.hash, focus:document.activeElement.id})")
        if details != {"hash": "#details", "focus": "details"}:
            self.fail("keyboard_cta", f"CTA did not move focus to details: {details}", location)
        await page.close()

        for brand in BRANDS:
            spacing_page, spacing_url = await self.open_page(context, f"specimen.html?brand={brand}", 320)
            await spacing_page.add_style_tag(content="*{line-height:1.5!important;letter-spacing:.12em!important;word-spacing:.16em!important}p{margin-bottom:2em!important}")
            spacing = await self.overflow(spacing_page)
            bounds = await self.text_bounds(spacing_page)
            if spacing["scrollWidth"] > spacing["clientWidth"] + 1 or any(item["overflow"] or not item["visible"] or not item["withinViewport"] for item in bounds):
                self.fail("text_spacing_reflow", f"{brand} 320px text spacing failure: {spacing}, bounds={bounds}", spacing_url)
            await self.capture(spacing_page, f"{brand}-text-spacing-320")
            await spacing_page.close()

        reflow, reflow_url = await self.open_page(context, "specimen.html?brand=tidal", 320)
        metrics = await self.overflow(reflow)
        if metrics["scrollWidth"] > metrics["clientWidth"] + 1:
            self.fail("reflow_320", f"320px CSS viewport overflows: {metrics}", reflow_url)
        await self.capture(reflow, "tidal-reflow-320")
        await reflow.close()

    async def check_typography_and_fallback(self, context):
        page, location = await self.open_page(context, "typography.html", 390)
        diagnostics = await page.evaluate("window.inspectTextWrapping()")
        by_text = {item["text"]: item for item in diagnostics}
        if not by_text.get("Three ways to meetit.", {}).get("orphanCandidate"):
            self.fail("wrap_diagnostic", "Known orphan control was not flagged", location)
        if not by_text.get("Required information is clipped here.", {}).get("overflow"):
            self.fail("wrap_diagnostic", "Known clipped control was not flagged", location)
        if by_text.get("Next", {}).get("orphanCandidate") or by_text.get("Next", {}).get("overflow"):
            self.fail("wrap_diagnostic", "Legitimate short label was falsely flagged", location)
        await self.capture(page, "typography-controls-390")
        await page.close()

        for brand in BRANDS:
            fallback, fallback_url = await self.open_page(context, f"specimen.html?brand={brand}", 320, block_fonts=True)
            font_faces = await fallback.evaluate("""() => [...document.fonts].map(face => ({family:face.family, status:face.status}))""")
            metrics = await self.overflow(fallback)
            bounds = await self.text_bounds(fallback)
            if metrics["scrollWidth"] > metrics["clientWidth"] + 1 or any(item["overflow"] or not item["visible"] or not item["withinViewport"] for item in bounds):
                self.fail("font_fallback_readability", f"{brand} fallback bounds failure: {metrics}, bounds={bounds}, faces={font_faces}", fallback_url)
            await self.capture(fallback, f"{brand}-font-fallback-320")
            await fallback.close()

    async def check_motion(self, context):
        page, location = await self.open_page(context, "motion.html", 1024)
        await page.evaluate("window.motionReady")
        initial = await page.evaluate("window.motionState()")
        if initial["running"] or initial["position"] != 0 or initial["reduced"]:
            self.fail("motion_initial", f"Unexpected normal initial state: {initial}", location)
        await page.click("#play")
        await page.wait_for_timeout(300)
        if not (await page.evaluate("window.motionState()"))["running"]:
            self.fail("motion_play", "Play did not start the sequence", location)
        await page.click("#play")
        await page.locator("#scrub").evaluate("input => { input.value='6'; input.dispatchEvent(new Event('input', {bubbles:true})); }")
        scrubbed = await page.evaluate("window.motionState()")
        if scrubbed["running"] or abs(scrubbed["position"] - 6) > 0.05:
            self.fail("motion_scrub", f"Scrub did not pause at six seconds: {scrubbed}", location)
        await page.evaluate("window.setMotionTime(0)")
        await page.click("#play")
        await page.wait_for_timeout(12250)
        looped = await page.evaluate("window.motionState()")
        if not looped["running"] or min(looped["position"], 12 - looped["position"]) > 0.75:
            self.fail("motion_full_clock_loop", f"Twelve-second loop did not return near opening state: {looped}", location)
        await page.click("#play")
        await self.capture(page, "motion-normal-loop")
        await page.close()

        reduced, reduced_url = await self.open_page(context, "motion.html", 1024, reduced_motion="reduce")
        state = await reduced.evaluate("({state:window.motionState(), disabled:document.querySelector('#play').disabled})")
        if not state["state"]["reduced"] or state["state"]["position"] != 9 or not state["disabled"]:
            self.fail("motion_reduced_initial", f"Unexpected reduced-motion initial state: {state}", reduced_url)
        await reduced.emulate_media(reduced_motion="no-preference")
        await reduced.wait_for_timeout(50)
        dynamic = await reduced.evaluate("({state:window.motionState(), disabled:document.querySelector('#play').disabled})")
        if dynamic["state"]["reduced"] or dynamic["state"]["position"] != 0 or dynamic["disabled"]:
            self.fail("motion_reduced_dynamic", f"Reduced-motion removal did not restore paused initial state: {dynamic}", reduced_url)
        await reduced.emulate_media(reduced_motion="reduce")
        await reduced.wait_for_timeout(50)
        restored = await reduced.evaluate("({state:window.motionState(), disabled:document.querySelector('#play').disabled})")
        if not restored["state"]["reduced"] or restored["state"]["position"] != 9 or not restored["disabled"]:
            self.fail("motion_reduced_dynamic", f"Reduced-motion change did not restore static final state: {restored}", reduced_url)
        await self.capture(reduced, "motion-reduced")
        await reduced.close()

        unavailable, unavailable_url = await self.open_page(context, "motion.html", 1024, block_timeline=True)
        await unavailable.evaluate("window.motionReady")
        fallback = await unavailable.evaluate("""() => ({
            disabled: document.querySelector('#play').disabled,
            status: document.querySelector('#status').textContent,
            state: window.motionState()
        })""")
        if not fallback["disabled"] or fallback["state"]["running"] or not fallback["status"].strip():
            self.fail("motion_timeline_fallback", f"Timeline failure did not leave a static readable fallback: {fallback}", unavailable_url)
        await self.capture(unavailable, "motion-timeline-unavailable")
        await unavailable.close()

    async def run(self):
        self.output.mkdir(parents=True, exist_ok=True)
        (self.output / "screens").mkdir(exist_ok=True)
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch()
            context = await browser.new_context()
            await self.check_specimens(context)
            await self.check_keyboard_and_spacing(context)
            await self.check_typography_and_fallback(context)
            await self.check_motion(context)
            await context.close()
            await browser.close()
        for item in self.console:
            self.fail("console_error", item["text"], item["url"])
        return {
            "Version-Timestamp": datetime.now().astimezone().isoformat(),
            "base_url": self.base_url,
            "screens": "screens",
            "known_controls": "Typography orphan and clipping controls are intentionally flagged and are not production examples.",
            "fictional_baseline": "The collection is fictional teaching material. Browser evidence supplies no approval or production authority.",
            "wrap_diagnostics": self.wrap_records,
            "browser_zoom": {"status": "not_run", "reason": "Playwright viewport reflow at 320px was exercised; native browser zoom is not exposed as a portable Chromium automation control."},
            "passes": not self.failures,
            "failures": self.failures,
            "console_errors": self.console,
            "assurance": "Rendered browser behavior only. This does not establish accessibility certification, aesthetic, client, hardware, or human acceptance."
        }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", default="http://127.0.0.1:17672/examples/quality-benchmark/", help="served quality-benchmark directory URL")
    parser.add_argument("--outdir", type=Path, default=Path("private/quality-020/browser"), help="JSON report and screenshot directory")
    args = parser.parse_args()
    checks = Checks(args.base_url, args.outdir)
    try:
        report = asyncio.run(checks.run())
    except Exception as exc:
        report = {"Version-Timestamp": datetime.now().astimezone().isoformat(), "base_url": args.base_url, "passes": False,
                  "failures": [{"check": "runner", "detail": f"{type(exc).__name__}: {exc}"}], "console_errors": []}
    write_report(args.outdir, report)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["passes"] else 1


if __name__ == "__main__":
    sys.exit(main())
