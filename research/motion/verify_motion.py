"""Checks the motion build at http://localhost:8787 against the plan's limits. Prints one line per check."""
import json, sys
from playwright.sync_api import sync_playwright

URL = "http://localhost:8787/"
OUT = sys.argv[1]
res = {}

INIT = r"""
window.__lcp = []; window.__cls = 0; window.__frames = []; window.__beacons = [];
new PerformanceObserver(l => l.getEntries().forEach(e => __lcp.push({t: Math.round(e.startTime), el: e.element && (e.element.tagName + "." + e.element.className + ":" + e.element.textContent.slice(0,15)), size: e.size}))).observe({type: 'largest-contentful-paint', buffered: true});
new PerformanceObserver(l => l.getEntries().forEach(e => { if (!e.hadRecentInput) __cls += e.value; })).observe({type: 'layout-shift', buffered: true});
let last = performance.now(); (function f(now) { __frames.push(now - last); last = now; if (now < 2500) requestAnimationFrame(f); })(last);
const sb = navigator.sendBeacon.bind(navigator); navigator.sendBeacon = (u, d) => { d && d.text && d.text().then(t => __beacons.push(t)); return sb(u, d); };
"""

with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome")

    # 1-4: motion on, throttled like Lighthouse mobile (4x CPU, slow 4G-ish).
    for w, h in ((375, 812), (1440, 900)):
        ctx = b.new_context(viewport={"width": w, "height": h}, reduced_motion="no-preference")
        pg = ctx.new_page(); csp = []
        pg.on("console", lambda m: csp.append(m.text) if "Content Security Policy" in m.text else None)
        cdp = ctx.new_cdp_session(pg)
        cdp.send("Emulation.setCPUThrottlingRate", {"rate": 4})
        cdp.send("Network.enable"); cdp.send("Network.emulateNetworkConditions", {"offline": False, "latency": 150, "downloadThroughput": 1.6e6 / 8, "uploadThroughput": 750e3 / 8})
        pg.add_init_script(INIT)
        r = pg.goto(URL, wait_until="load")
        pg.wait_for_timeout(3000)
        d = pg.evaluate("""() => ({cls: document.documentElement.className, lcp: __lcp, clsv: __cls,
            frames: __frames.slice(1), running: document.getAnimations().filter(a => a.playState === 'running').length,
            copy: (() => { const b = document.querySelector('[data-copy]').getBoundingClientRect(); return [Math.round(b.y), Math.round(b.bottom)]; })()})""")
        f = d.pop("frames")
        d["long_frames"] = sum(1 for x in f if x > 16.7 * 1.5)  # rAF jitter allowance: a dropped frame shows as ~33 ms
        d["max_frame"] = round(max(f), 1); d["csp_errors"] = csp; d["csp_hash_in_header"] = "sha256-" in (r.headers.get("content-security-policy") or "")
        res[f"throttled-{w}"] = d
        ctx.close()

    # 5: storyboard frames, seeked exactly, and the end state for the pixel diff.
    for w, h in ((375, 812), (1440, 900)):
        ctx = b.new_context(viewport={"width": w, "height": h}, reduced_motion="no-preference")
        pg = ctx.new_page(); pg.goto(URL, wait_until="networkidle"); pg.wait_for_timeout(200)
        for t in (0, 340, 450, 600, 730):
            pg.evaluate(f"() => document.getAnimations().forEach(a => {{ a.pause(); a.currentTime = {t}; }})")
            pg.wait_for_timeout(80)
            pg.screenshot(path=f"{OUT}/frame-{w}-{t}.png", clip={"x": 0, "y": 0, "width": w, "height": 640 if w == 375 else 720})
        pg.evaluate("() => document.getAnimations().forEach(a => a.finish())"); pg.wait_for_timeout(100)
        pg.screenshot(path=f"{OUT}/end-{w}.png", clip={"x": 0, "y": 0, "width": w, "height": 640 if w == 375 else 720})
        ctx.close()
        ctx = b.new_context(viewport={"width": w, "height": h}); pg = ctx.new_page()
        pg.goto("https://deeper.tools/", wait_until="networkidle"); pg.wait_for_timeout(1500)
        pg.screenshot(path=f"{OUT}/live-{w}.png", clip={"x": 0, "y": 0, "width": w, "height": 640 if w == 375 else 720}); ctx.close()

    # 6: reduced motion, before and after a tab click.
    ctx = b.new_context(viewport={"width": 1440, "height": 900}, reduced_motion="reduce"); pg = ctx.new_page()
    pg.goto(URL, wait_until="networkidle"); pg.wait_for_timeout(500)
    a0 = pg.evaluate("() => [document.documentElement.className, document.getAnimations().length, getComputedStyle(document.querySelector('h1 .w')).opacity]")
    pg.locator('[role="tab"]').nth(1).click(); pg.wait_for_timeout(100)
    res["reduce"] = {"html_class": a0[0], "anims_load": a0[1], "words_opacity": a0[2], "anims_after_tab": pg.evaluate("() => document.getAnimations().length")}
    ctx.close()

    # 7: no JavaScript: the static hero, words visible, demo rows visible.
    ctx = b.new_context(viewport={"width": 1440, "height": 900}, java_script_enabled=False); pg = ctx.new_page()
    pg.goto(URL, wait_until="networkidle")
    res["no-js"] = pg.evaluate("() => [getComputedStyle(document.querySelector('h1 .w')).opacity, getComputedStyle(document.querySelector('.inserts li')).opacity]")
    ctx.close()

    # 8: forced colours: bar hidden, real underline back.
    ctx = b.new_context(viewport={"width": 1440, "height": 900}, forced_colors="active"); pg = ctx.new_page()
    pg.goto(URL, wait_until="networkidle"); pg.wait_for_timeout(1200)
    res["forced-colors"] = pg.evaluate("() => [getComputedStyle(document.querySelector('h1 .w'), '::after').display, getComputedStyle(document.querySelector('h1 .ins')).textDecorationLine]")
    ctx.close()

    # 9: demo: rows hidden until in view, then play once; a tab click replays.
    ctx = b.new_context(viewport={"width": 1440, "height": 900}); pg = ctx.new_page()
    pg.goto(URL, wait_until="networkidle"); pg.wait_for_timeout(1000)
    before = pg.evaluate("() => [document.querySelector('.panel:not([hidden])').classList.contains('play'), getComputedStyle(document.querySelector('.panel:not([hidden]) .inserts li')).opacity]")
    pg.locator(".panel:not([hidden]) .inserts").scroll_into_view_if_needed(); pg.wait_for_timeout(150)
    mid = pg.evaluate("() => [document.querySelector('.panel:not([hidden])').classList.contains('play'), document.querySelector('.panel:not([hidden])').getAnimations({subtree:true}).map(a => [a.effect.getTiming().duration, a.effect.getTiming().delay])]")
    pg.wait_for_timeout(800)
    pg.locator('[role="tab"]').nth(2).click(); pg.wait_for_timeout(60)
    tab = pg.evaluate("() => document.querySelector('.panel:not([hidden])').getAnimations({subtree:true}).filter(a => a.playState === 'running').length")
    res["demo"] = {"before_scroll_play_opacity": before, "on_scroll": mid, "running_after_tab_click": tab}
    ctx.close()

    # 10: Copy at t = 100 ms: clicked during the motion, copied and counted.
    ctx = b.new_context(viewport={"width": 375, "height": 812}, permissions=["clipboard-read", "clipboard-write"]); pg = ctx.new_page()
    pg.add_init_script(INIT)
    beacons = []
    pg.on("request", lambda r: beacons.append(r.post_data) if r.url.endswith("/api/e") else None)
    pg.goto(URL, wait_until="domcontentloaded"); pg.wait_for_timeout(100)
    pg.locator("[data-copy]").first.click(); pg.wait_for_timeout(400)
    res["copy_at_100ms"] = {"clipboard": pg.evaluate("() => navigator.clipboard.readText()"), "beacons": beacons, "label": pg.locator("[data-copy] .long").text_content()}
    ctx.close()
    b.close()

print(json.dumps(res, indent=1))
