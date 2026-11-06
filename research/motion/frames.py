import json
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome")
    for w, h in ((1440, 900),)*10:
        ctx = b.new_context(viewport={"width": w, "height": h}); pg = ctx.new_page(); cdp = ctx.new_cdp_session(pg)
        pg.goto("http://localhost:8787/", wait_until="networkidle"); pg.wait_for_timeout(1500)
        cdp.send("Emulation.setCPUThrottlingRate", {"rate": 4})
        r = pg.evaluate("""() => new Promise(res => { const hero = [...document.querySelectorAll('h1 .w')].flatMap(e => e.getAnimations({subtree:true}));
          const all = document.getAnimations().filter(a => a.effect.target.closest && a.effect.target.closest('h1')); 
          const fr = []; let last = performance.now();
          all.forEach(a => { a.cancel(); a.play(); });
          (function f(now) { fr.push(+(now - last).toFixed(1)); last = now; if (fr.length < 60) requestAnimationFrame(f); else res({n: all.length, frames: fr.slice(1)}); })(last); })""")
        f = r["frames"]; print([i for i,x in enumerate(f) if x>17.7], f[:6]); print(w, "hero animations:", r["n"], "frames:", len(f), "over 16.7ms (with 1ms jitter):", sum(x > 17.7 for x in f), "max:", max(f))
        ctx.close()
    b.close()
