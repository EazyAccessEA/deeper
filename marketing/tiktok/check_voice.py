"""Check every recorded line against its text, the way the YouTube project's check_vo.py does: transcribe offline
with Whisper large-v3 and fail any line under 0.95 word similarity or missing a number it should say.

  python3 check_voice.py <short> [...]     writes voice/<short>/check.json; exits 1 on any failure
"""
import difflib, json, os, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).parent
NUM = {w: str(i) for i, w in enumerate("zero one two three four five six seven eight nine ten".split())}
SAY = [(r"\bdeeper\b", "deeper"), (r"\bdot tools\b", "tools"), (r"deeper\.tools", "deeper tools"), (r"/deeper", "slash deeper"), (r"\bchat ?gpt\b", "chatgpt"), (r"\bkey words\b", "keywords"), (r"\bthirty\b", "30"), (r"colou?r", "color"),
       (r"\bforty-five\b", "45"), (r"\bseventy-five\b", "75"), (r"\bhundred and twenty-five\b", "125"),
       (r"\bone hundred (and )?twenty-five\b", "125")]


def words(s):
    s = s.lower().replace("’", "'").replace("'", "")
    for a, b in SAY:
        s = re.sub(a, b, s)
    s = re.sub(r"\b(\w+) point (\w+)\b", lambda m: f"{NUM.get(m[1], m[1])}.{NUM.get(m[2], m[2])}", s)
    s = re.sub(r"(?<!\d)\.|\.(?!\d)|[^a-z0-9. ]+", " ", s)       # keep the point inside 2.6
    return [NUM.get(w, w) for w in s.split()]


def main():
    bad = 0
    for short in sys.argv[1:]:
        d = HERE / "voice" / short
        lines = json.loads((d / "lines.json").read_text())
        out = []
        with tempfile.TemporaryDirectory() as tmp:
            for l in lines:
                subprocess.run(["mlx_whisper", str(d / l["file"]), "--model", "mlx-community/whisper-large-v3-mlx",
                                "--language", "en", "--output-dir", tmp, "--output-format", "txt"], check=True,
                               capture_output=True, env={**os.environ, "HF_HUB_OFFLINE": "1"})
                heard = (pathlib.Path(tmp) / (pathlib.Path(l["file"]).stem + ".txt")).read_text().strip()
                a, b = words(l["text"]), words(heard)
                sim = difflib.SequenceMatcher(None, a, b).ratio()
                missing = [n for n in re.findall(r"\d+(?:\.\d+)?", " ".join(a)) if n not in b]
                ok = sim >= 0.95 and not missing
                bad += not ok
                out.append(dict(file=l["file"], ok=ok, similarity=round(sim, 3), missing=missing, said=l["text"], heard=heard))
                print(f"{'pass' if ok else 'FAIL'} {short}/{l['file']} {sim:.3f} {heard if not ok else ''}")
        (d / "check.json").write_text(json.dumps(out, indent=1) + "\n")
    sys.exit(1 if bad else 0)


main()
