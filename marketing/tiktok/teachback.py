"""Blind teach-back: can someone who doesn't code explain deeper after one watch of a short?

  python3 teachback.py <label> [short ...]     writes teachback/<label>.json and prints a score per short

The reader is Codex (a different model family from the writer), run in an empty folder with a read-only sandbox,
given only one short's words in the order they appear: spoken lines and on-screen text. It answers four
questions in its own words. Each answer is scored against KEY by the concepts it has to contain, so the
pass mark is fixed before anyone reads the answers.
"""
import json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).parent

PERSONA = ("You are an adult who uses ChatGPT now and then for everyday things. You don't write code and you "
           "have never heard of this product. You just watched a 40-second TikTok once. Below is everything that "
           "was said and shown on screen, in order. Answer from this alone, in plain words, as you would explain "
           "it to a friend. If something wasn't clear, say so instead of guessing.")
QUESTIONS = {
    "what": "What is this thing?",
    "does": "What does it actually do for you?",
    "who": "Who is it for?",
    "next": "If you wanted to try it, what would you do next?",
}
# Each answer passes when every group has at least one match (case-insensitive regex).
KEY = {
    "what": [r"\b(ai|chatgpt|claude|assistant|agent)\b", r"add-?on|tool|skill|plug-?in|extension|instruction|helper|app|feature"],
    "does": [r"rewrit|re-?word|rephras|improv|turns?|upgrad|better|fills? in|adds?", r"request|question|prompt|ask|task",
             r"expert|professional|specialist|pro\b"],
    # Widened in round 2 (3 Nov 2026): "people who want better AI answers" is the right answer, worded differently.
    "who": [r"anyone|anybody|everyone|people (who|that) (use|ask)|people using|ai users|use (ai|chatgpt)|everyday"
            r"|people (who|that) want [^.]*\b(ai|chatgpt|assistant)"],   # round 6: any "people who want <better> AI answers"
    "next": [r"install|add|paste|copy|download|type|get|go to|visit|open", r"deeper"],
}
FAIL_WHO = r"^(?!.*\b(anyone|anybody|everyone)\b).*\b(only|just)?\s*(developers|programmers|coders)\b"


def words_of(script, end):
    """Everything said and shown, in order, the way compose.py puts it on screen."""
    out = [f"[on screen] {script['headline']}"]
    out += [f"[voice] {l}" for l in script["sparse"]]
    out.append(f"[on screen] {script.get('band') or '/deeper ' + script['request'][0].lower() + script['request'][1:].rstrip('.?')}")
    out += [f"[voice] {l}" for l in script["sketch"]]
    if any(l.startswith("It adds what") for l in script["sketch"]):
        out.append("[on screen] 1 What an expert would do  2 What to start from  3 Which tools to use  4 How to check it worked")
    for said, caption in script["objects"]:
        out += [f"[voice] {said}", f"[on screen, in red] ^ {caption}"]
    out += [f"[voice] {l}" for l in script["colour"]] + [f"[on screen] {script['payoff']}"]
    out += [f"[voice] {end}", "[on screen] Ask for the version an expert would ask for.",
            "[on screen] Free. Paste deeper into ChatGPT, Claude or Gemini, then type /deeper and your prompt.",
            "[on screen] deeper.tools/start", "[on screen] Get deeper's instructions"]
    return "\n".join(out)


def ask(text):
    # Plain JSON in the reply keeps the call simple; stdin is closed below so codex exec never waits on it.
    prompt = (f"{PERSONA}\n\n--- the video ---\n{text}\n--- end ---\n\nAnswer each question in one or two sentences. "
              "Reply with only a JSON object with the keys " + ", ".join(QUESTIONS) + ".\n"
              + "\n".join(f"{k}: {q}" for k, q in QUESTIONS.items()))
    with tempfile.TemporaryDirectory() as tmp:
        out = pathlib.Path(tmp) / "answer.txt"
        for attempt in range(3):                           # a reader that hangs gets another go, then fails loudly
            try:
                subprocess.run(["codex", "exec", "--skip-git-repo-check", "--ephemeral", "-s", "read-only", "-C", tmp,
                                "-o", str(out), prompt], check=True, capture_output=True, timeout=240,
                               stdin=subprocess.DEVNULL)          # with stdin open, codex exec waits to read it
                reply = out.read_text()
                return json.loads(reply[reply.index("{"):reply.rindex("}") + 1])
            except (subprocess.TimeoutExpired, ValueError):
                print("  reader failed, retrying", flush=True)
        raise SystemExit("Codex did not answer after three tries")


def score(answers):
    marks = {}
    for k, groups in KEY.items():
        a = answers.get(k, "").lower()
        ok = all(re.search(g, a) for g in groups)
        if k == "who" and re.search(FAIL_WHO, a):
            ok = False
        marks[k] = ok
    return marks


def main(label, shorts):
    scripts = json.loads((HERE / "scripts.json").read_text())
    shorts = shorts or [k for k in scripts if not k.startswith("_")]
    res = {}
    for s in shorts:
        ans = ask(words_of(scripts[s], scripts["_end"]))
        marks = score(ans)
        res[s] = dict(score=sum(marks.values()), marks=marks, answers=ans)
        print(f"{s}: {res[s]['score']}/4 {marks}")
        for k, v in ans.items():
            print(f"   {k}: {v}")
    (HERE / "teachback").mkdir(exist_ok=True)
    (HERE / "teachback" / f"{label}.json").write_text(json.dumps(res, indent=1) + "\n")


if sys.argv[1] == "--words":          # print what the reader is given for one short, without asking anyone
    scripts = json.loads((HERE / "scripts.json").read_text())
    print(words_of(scripts[sys.argv[2]], scripts["_end"]))
else:
    main(sys.argv[1], sys.argv[2:])
