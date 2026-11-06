import json, sys
from playwright.sync_api import sync_playwright
INIT = r"""window.__s=[];new PerformanceObserver(l=>l.getEntries().forEach(e=>{if(!e.hadRecentInput)__s.push({v:+e.value.toFixed(4),t:Math.round(e.startTime),src:e.sources.map(s=>[(s.node&&s.node.nodeName)+":"+((s.node&&s.node.textContent)||"").slice(0,18),[s.previousRect.y,s.previousRect.height,s.previousRect.width],[s.currentRect.y,s.currentRect.height,s.currentRect.width]])})})).observe({type:'layout-shift',buffered:true});"""
with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome")
    for url in sys.argv[1:]:
        for run in range(2):
            ctx = b.new_context(viewport={"width": 1440, "height": 900}); pg = ctx.new_page(); cdp = ctx.new_cdp_session(pg)
            cdp.send("Emulation.setCPUThrottlingRate", {"rate": 4}); cdp.send("Network.enable")
            cdp.send("Network.setCacheDisabled", {"cacheDisabled": True})
            cdp.send("Network.emulateNetworkConditions", {"offline": False, "latency": 150, "downloadThroughput": 1.6e6/8, "uploadThroughput": 750e3/8})
            pg.add_init_script(INIT); pg.goto(url, wait_until="load"); pg.wait_for_timeout(3000)
            print(url, run, json.dumps(pg.evaluate("()=>[document.documentElement.className,__s]")))
            ctx.close()
    b.close()
