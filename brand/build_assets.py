"""Build the deeper mark, wordmark, icons and social cards from one source of geometry.

Needs fontTools (with brotli), rsvg-convert and ImageMagick.
Usage: python3 brand/build_assets.py
"""
import pathlib
import subprocess

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "assets"
FONTS = ROOT.parent / "site/node_modules/@fontsource/schibsted-grotesk/files"
RED, INK, WHITE = "#D0241B", "#141414", "#FFFFFF"


def caret(x, y, w, h, t):
    """Filled caret, apex at (x + w/2, y), feet flat at y + h, legs t thick across the leg."""
    import math
    half = w / 2
    foot = t / math.sin(math.atan2(h, half))          # horizontal width of each foot
    inner = t / math.sin(math.atan2(half, h))         # inner apex drop below the outer apex
    pts = [(x, y + h), (x + half, y), (x + w, y + h), (x + w - foot, y + h),
           (x + half, y + inner), (x + foot, y + h)]
    return "M" + " L".join(f"{a:.2f},{b:.2f}" for a, b in pts) + " Z"


def mark_svg(fill=RED):
    # 16 px grid: 12 wide, 9 tall, 3 thick, raised 1 px from centre.
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16">'
            f'<path fill="{fill}" d="{caret(2, 2.5, 12, 9, 3)}"/></svg>')


def favicon_svg():
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16">'
            f'<rect width="16" height="16" rx="3" fill="{WHITE}"/>'
            f'<path fill="{RED}" d="{caret(2, 2.5, 12, 9, 3)}"/></svg>')


def wordmark_svg(ink=INK, red=RED):
    font = TTFont(FONTS / "schibsted-grotesk-latin-700-normal.woff2")
    upm = font["head"].unitsPerEm
    gs, cmap, hmtx = font.getGlyphSet(), font.getBestCmap(), font["hmtx"]
    tracking = -0.02 * upm
    paths, x, boxes = [], 0.0, []
    glyf = font["glyf"] if "glyf" in font else None
    for ch in "deeper":
        name = cmap[ord(ch)]
        pen = SVGPathPen(gs)
        gs[name].draw(pen)
        paths.append(f'<path transform="translate({x:.1f},0)" d="{pen.getCommands()}"/>')
        g = glyf[name] if glyf else None
        xmin, xmax = (g.xMin, g.xMax) if g is not None and hasattr(g, "xMin") else (0, hmtx[name][0])
        boxes.append((x + xmin, x + xmax))
        x += hmtx[name][0] + tracking
    width = x - tracking
    # Caret under the gap between "d" and "e": 0.42em wide, apex 0.08em below the baseline.
    gap = (boxes[0][1] + boxes[1][0]) / 2 + 0.03 * upm   # optical: the d stem pulls the eye left
    cw = 0.42 * upm
    ch_ = cw * 0.75
    apex = -0.08 * upm                              # font units are y-up; baseline is 0
    cpath = caret(gap - cw / 2, -apex, cw, ch_, cw * 0.25)
    asc = font["hhea"].ascent
    top, bottom = -asc * 0.78, -apex + ch_ + 0.04 * upm
    vb = f"0 {top:.0f} {width:.0f} {bottom - top:.0f}"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}">'
            f'<g fill="{ink}" transform="scale(1,-1)">{"".join(paths)}</g>'
            f'<path fill="{red}" d="{cpath}"/></svg>')


def run(*cmd):
    subprocess.run(cmd, check=True)


def main():
    OUT.mkdir(exist_ok=True)
    (OUT / "mark.svg").write_text(mark_svg())
    (OUT / "mark-mono.svg").write_text(mark_svg(INK))
    (OUT / "favicon.svg").write_text(favicon_svg())
    (OUT / "wordmark.svg").write_text(wordmark_svg())
    (OUT / "wordmark-dark.svg").write_text(wordmark_svg(ink="#EDEDED", red="#FF5A4E"))
    for size in (16, 32, 48):
        run("rsvg-convert", "-w", str(size), "-h", str(size), str(OUT / "favicon.svg"), "-o", str(OUT / f"favicon-{size}.png"))
    run("magick", str(OUT / "favicon-16.png"), str(OUT / "favicon-32.png"), str(OUT / "favicon-48.png"), str(OUT / "favicon.ico"))
    # Apple touch icon: red caret on white, 180 px, no transparency.
    run("rsvg-convert", "-w", "180", "-h", "180", "-b", WHITE, str(OUT / "mark.svg"), "-o", str(OUT / "apple-touch-icon.png"))
    run("rsvg-convert", "-w", "512", "-h", "512", str(OUT / "mark.svg"), "-o", str(OUT / "mark-512.png"))
    run("rsvg-convert", "-h", "160", str(OUT / "wordmark.svg"), "-o", str(OUT / "wordmark.png"))

    # Social cards: the single-pencil plate, wordmark and one line, set in the brand face.
    ttf = OUT / "_schibsted-600.ttf"
    f = TTFont(FONTS / "schibsted-grotesk-latin-600-normal.woff2"); f.flavor = None; f.save(ttf)
    plate = ROOT / "plates" / "pencil-space-b.jpg"
    for name, (w, h) in {"social-preview": (1280, 640), "og": (1200, 630)}.items():
        dest = OUT / f"{name}.png"
        run("magick", str(plate), "-resize", f"{w}x{h}^", "-gravity", "center", "-extent", f"{w}x{h}",
            "(", str(OUT / "wordmark.png"), "-resize", "x118", ")", "-gravity", "northwest",
            "-geometry", f"+{int(w * 0.30)}+{int(h * 0.30)}", "-composite",
            "-font", str(ttf), "-fill", INK, "-pointsize", str(int(h * 0.058)),
            "-annotate", f"+{int(w * 0.30)}+{int(h * 0.60)}", "Ask for the version an expert would ask for.",
            "-fill", "#5B5F66", "-pointsize", str(int(h * 0.036)),
            "-annotate", f"+{int(w * 0.30)}+{int(h * 0.71)}", "A free skill for AI agents. Same scope, better method.",
            str(dest))
    ttf.unlink()
    print("\n".join(sorted(p.name for p in OUT.iterdir())))


if __name__ == "__main__":
    main()
