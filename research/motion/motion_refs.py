"""Reads the real animations on reference sites with document.getAnimations(). Prints JSON."""
import json, sys
from playwright.sync_api import sync_playwright

SITES = sys.argv[1:]
JS = r"""() => document.getAnimations().map(a => {
  const t = a.effect && a.effect.target; const tm = a.effect ? a.effect.getComputedTiming() : {};
  let props = [];
  try { props = [...new Set(a.effect.getKeyframes().flatMap(k => Object.keys(k).filter(x => !['offset','computedOffset','easing','composite'].includes(x))))]; } catch(e) {}
  const kfEase = (() => { try { return [...new Set(a.effect.getKeyframes().map(k => k.easing))].join('|'); } catch(e) { return ''; } })();
  return { type: a.constructor.name, name: a.animationName || a.transitionProperty || a.id || '', dur: Math.round(tm.duration || 0), delay: Math.round(tm.delay || 0),
    easing: (a.effect && a.effect.getTiming().easing) + (kfEase && kfEase !== 'linear' ? ' kf:' + kfEase : ''), iter: tm.iterations, props,
    el: t ? (t.tagName + (t.id ? '#' + t.id : '') + (typeof t.className === 'string' && t.className ? '.' + t.className.split(' ')[0].slice(0, 30) : '')) : '' };
})"""

def grab(page, label):
    out = []
    for ms in (300, 1200, 3000):
        page.wait_for_timeout(ms if not out else ms - 300)
        out += [dict(a, at=label) for a in page.evaluate(JS)]
    return out

res = {}
with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome")
    for url in SITES:
        row = {}
        for rm in ("no-preference", "reduce"):
            ctx = b.new_context(viewport={"width": 1440, "height": 900}, reduced_motion=rm)
            pg = ctx.new_page()
            try:
                pg.goto(url, wait_until="domcontentloaded", timeout=30000)
                anims = grab(pg, "load")
                for y in (900, 1800, 2700):
                    pg.mouse.wheel(0, 900); pg.wait_for_timeout(900)
                    anims += [dict(a, at=f"scroll{y}") for a in pg.evaluate(JS)]
            except Exception as e:
                anims = [{"error": str(e)[:200]}]
            ctx.close()
            seen, uniq = set(), []
            for a in anims:
                k = json.dumps({x: a.get(x) for x in ("type", "name", "dur", "delay", "easing", "iter", "props", "el")})
                if k not in seen: seen.add(k); uniq.append(a)
            row[rm] = uniq
        res[url] = row
    b.close()
print(json.dumps(res, indent=1))
