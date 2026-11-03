"""Builds one HyperFrames project per short from shorts.json. Run: python3 build.py, then render each folder.

Layout follows TikTok's 1080x1920 safe band: text only between y=168 and y=1330, nothing under the right-hand rail.
"""
import html, json, pathlib, shutil

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parents[1]
FONTS = ROOT / "site/node_modules/@fontsource"
CLI = "hyperframes@0.8.173"
END = 5.0  # seconds the end card holds

FONT_FILES = {
    "sg-400.woff2": "schibsted-grotesk/files/schibsted-grotesk-latin-400-normal.woff2",
    "sg-600.woff2": "schibsted-grotesk/files/schibsted-grotesk-latin-600-normal.woff2",
    "sg-700.woff2": "schibsted-grotesk/files/schibsted-grotesk-latin-700-normal.woff2",
    "sg-500i.woff2": "schibsted-grotesk/files/schibsted-grotesk-latin-500-italic.woff2",
    "jbm-400.woff2": "jetbrains-mono/files/jetbrains-mono-latin-400-normal.woff2",
}

CSS = """
@font-face { font-family: "Schibsted Grotesk"; font-weight: 400; src: url(assets/fonts/sg-400.woff2); }
@font-face { font-family: "Schibsted Grotesk"; font-weight: 600; src: url(assets/fonts/sg-600.woff2); }
@font-face { font-family: "Schibsted Grotesk"; font-weight: 700; src: url(assets/fonts/sg-700.woff2); }
@font-face { font-family: "Schibsted Grotesk"; font-weight: 500; font-style: italic; src: url(assets/fonts/sg-500i.woff2); }
@font-face { font-family: "JetBrains Mono"; font-weight: 400; src: url(assets/fonts/jbm-400.woff2); }
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { width: 1080px; height: 1920px; overflow: hidden; background: #ffffff; }
#root { width: 1080px; height: 1920px; position: relative; font-family: "Schibsted Grotesk", sans-serif; color: #141414; }
.scene { position: absolute; left: 88px; top: 196px; width: 820px; }
.hook { font-weight: 700; font-size: 90px; line-height: 1.04; letter-spacing: -0.035em; }
.task { margin-top: 40px; font-size: 56px; line-height: 1.3; letter-spacing: -0.015em; }
.ins { margin-top: 20px; display: flex; gap: 22px; align-items: baseline; color: #d0241b; font-style: italic; font-weight: 500; font-size: 54px; line-height: 1.15; letter-spacing: -0.02em; }
.ins img { width: 36px; height: 36px; flex: none; transform: translateY(4px); }
.payoff { margin-top: 40px; font-weight: 600; font-size: 60px; line-height: 1.15; letter-spacing: -0.03em; }
.intro { margin-top: 44px; font-size: 44px; line-height: 1.35; color: #5b5f66; }
.cols { margin-top: 56px; display: grid; grid-template-columns: 1fr 150px 150px; column-gap: 12px; font-size: 32px; color: #5b5f66; }
.row { display: grid; grid-template-columns: 1fr 150px 150px; column-gap: 12px; align-items: baseline; padding: 26px 0; border-top: 2px solid #e3e5e8; }
.row .label { font-size: 40px; line-height: 1.2; }
.row .num { font-family: "Schibsted Grotesk", sans-serif; font-size: 72px; font-weight: 600; letter-spacing: -0.03em; }
.row .num.new { color: #d0241b; }
.small { margin-top: 48px; font-size: 38px; line-height: 1.35; color: #5b5f66; }
#end { top: 420px; }
#end .mark { width: 520px; height: auto; }
#end .line { margin-top: 70px; font-size: 52px; line-height: 1.25; letter-spacing: -0.02em; font-weight: 600; }
#end .cmd { margin-top: 48px; background: #f4f5f6; border-radius: 8px; padding: 30px 32px; font-family: "JetBrains Mono", monospace; font-size: 34px; }
#end .then { margin-top: 30px; font-size: 40px; color: #5b5f66; }
"""


def esc(s):
    return html.escape(s, quote=True)


def markup_scene(v):
    beats, items, t = [], [], 2.6
    for i, text in enumerate(v["insertions"]):
        items.append(f'<div id="ins{i}" class="ins"><img src="assets/mark.svg" alt="" /><span>{esc(text)}</span></div>')
        beats.append((f"#ins{i}", t))
        t += 2.1
    beats.append(("#payoff", t + 0.4))
    body = (
        f'<p id="hook" class="hook">{esc(v["hook"])}</p>'
        f'<p id="task" class="task">“{esc(v["task"])}”</p>'
        + "".join(items)
        + f'<p id="payoff" class="payoff">{esc(v["payoff"])}</p>'
    )
    return body, beats, t + 3.6


def data_scene(v):
    a, b = v["columns"]
    rows, beats, t = [], [("#cols", 2.4)], 2.8
    for i, (label, old, new) in enumerate(v["rows"]):
        rows.append(
            f'<div id="row{i}" class="row"><span class="label">{esc(label)}</span>'
            f'<span class="num">{esc(old)}</span><span class="num new">{esc(new)}</span></div>'
        )
        beats.append((f"#row{i}", t))
        t += 2.2
    beats.append(("#payoff", t + 0.4))
    body = (
        f'<p id="hook" class="hook">{esc(v["hook"])}</p>'
        f'<p id="intro" class="intro">{esc(v["intro"])}</p>'
        f'<div id="cols" class="cols"><span></span><span>{esc(a)}</span><span>{esc(b)}</span></div>'
        + "".join(rows)
        + f'<p id="payoff" class="small">{esc(v["payoff"])}</p>'
    )
    return body, beats, t + 4.2


def page(v):
    body, beats, main_len = (markup_scene if v["kind"] == "markup" else data_scene)(v)
    total = round(main_len + END, 2)
    tweens = "\n".join(
        f'      tl.fromTo("{sel}", {{ opacity: 0, y: 14 }}, {{ opacity: 1, y: 0, duration: 0.35, ease: "power2.out" }}, {at});'
        for sel, at in beats
    )
    return f"""<!doctype html>
<html lang="en" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>{CSS}</style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{total}" data-width="1080" data-height="1920">
      <div id="main" class="scene clip" data-start="0" data-duration="{main_len}" data-track-index="0">{body}</div>
      <div id="end" class="scene clip" data-start="{main_len}" data-duration="{END}" data-track-index="1">
        <img id="wordmark" class="mark" src="assets/wordmark.svg" alt="deeper" />
        <p id="endline" class="line">A free skill for Claude Code, Codex and Cursor.</p>
        <p id="endcmd" class="cmd">npx skills add EazyAccessEA/deeper</p>
        <p id="endthen" class="then">Then type /deeper and your task.</p>
      </div>
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
{tweens}
      tl.fromTo("#wordmark", {{ opacity: 0, y: 14 }}, {{ opacity: 1, y: 0, duration: 0.35 }}, {main_len});
      tl.fromTo(["#endline", "#endcmd", "#endthen"], {{ opacity: 0, y: 14 }}, {{ opacity: 1, y: 0, duration: 0.35, stagger: 0.5 }}, {main_len + 0.4});
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
"""


def main():
    shorts = json.loads((HERE / "shorts.json").read_text())
    for name, v in shorts.items():
        d = HERE / name
        (d / "assets/fonts").mkdir(parents=True, exist_ok=True)
        for out, src in FONT_FILES.items():
            shutil.copyfile(FONTS / src, d / "assets/fonts" / out)
        shutil.copyfile(ROOT / "brand/assets/mark.svg", d / "assets/mark.svg")
        shutil.copyfile(ROOT / "brand/assets/wordmark.svg", d / "assets/wordmark.svg")
        (d / "index.html").write_text(page(v))
        (d / "package.json").write_text(json.dumps({
            "name": f"deeper-{name}", "private": True, "type": "module",
            "scripts": {k: f"npx --yes {CLI} {k}" for k in ("check", "render")} | {"dev": f"npx --yes {CLI} preview"},
        }, indent=2) + "\n")
        print(name, "built")


main()
