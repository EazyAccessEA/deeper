"""Journal test runner. See README.md for the design; nothing here may change after FROZEN.txt is written.

  python3 run.py write            # 4 tasks x 4 arms x 2 runs -> runs/<task>-<arm>-<n>.md (skips existing)
  python3 run.py judge            # both judges, blind -> judgements/<judge>-<task>.json, key.json
"""
import concurrent.futures as cf, json, os, pathlib, random, re, subprocess, sys, tempfile, time

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parents[2]
RUNS, JUDGE = HERE / "runs", HERE / "judgements"
README = (HERE / "README.md").read_text()
SKILL = (ROOT / "skills/deeper/SKILL.md").read_text()
FELIX = re.search(r"^> (I want a deeper version.*)$", README, re.M).group(1)
FINAL = "Nobody can answer questions before you reply. Do the task now with what's provided, and state any assumptions you make."
FIELDS = {"cv": "recruiter and CV writer", "rent": "financial planner",
          "complaint": "customer service manager", "downloads": "IT support specialist"}
TASKS = list(FIELDS)
ARMS = ["plain", "persona", "felix", "deeper"]
WRITER, CLAUDE_JUDGE = "claude-opus-5-5", "claude-sonnet-5-5"
LEAKS = ["deeper", "felix", "worth knowing", "top professional", "rawest material", "act as"]


def fixture(task):
    first, rest = (HERE / "fixtures" / f"{task}.md").read_text().split("\n", 1)
    return first.removeprefix("Task: ").strip(), rest.strip()


def claude(prompt, model):
    env = {**os.environ, "CLAUDE_CODE_DISABLE_CLAUDE_MDS": "1"}
    with tempfile.TemporaryDirectory() as tmp:
        r = subprocess.run(["claude", "-p", prompt, "--model", model, "--setting-sources", "project",
                            "--strict-mcp-config", "--tools", "", "--system-prompt", "You are a helpful assistant."],
                           cwd=tmp, env=env, capture_output=True, text=True, timeout=900, stdin=subprocess.DEVNULL)
    if r.returncode or not r.stdout.strip():
        raise RuntimeError(r.stderr[-500:])
    return r.stdout.strip()


def codex(prompt):
    with tempfile.TemporaryDirectory() as tmp:
        out = pathlib.Path(tmp) / "reply.md"
        subprocess.run(["codex", "exec", "--skip-git-repo-check", "--ephemeral", "-s", "read-only", "-C", tmp,
                        "-o", str(out), prompt], check=True, capture_output=True, timeout=900,
                       stdin=subprocess.DEVNULL)  # with stdin open, codex exec waits to read it
        text = out.read_text().strip()
    if not text:
        raise RuntimeError("empty")
    return text


def retry(fn, *a, label=""):
    for i in range(3):
        try:
            return fn(*a)
        except Exception as e:  # logged, never judged on content
            log(f"{label}: attempt {i + 1} failed: {str(e)[:200]}")
            time.sleep(10)
    raise RuntimeError(f"{label}: failed 3 times")


def log(line):
    with open(RUNS / "log.txt", "a") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {line}\n")


def extract(reply):
    blocks = re.findall(r"```[^\n]*\n(.*?)```", reply, re.S)
    if blocks:
        return blocks[-1].strip(), "last fenced block"
    lines = reply.splitlines()
    idx = [i for i, l in enumerate(lines) if "prompt" in l.lower() and l.rstrip().endswith(":")]
    if idx:
        return "\n".join(lines[idx[-1] + 1:]).strip(), "after last 'prompt:' line"
    return reply.strip(), "whole reply"


def write_one(job):
    task, arm, n = job
    dest = RUNS / f"{task}-{arm}-{n}.md"
    if dest.exists():
        return f"{dest.name}: exists"
    t, material = fixture(task)
    label = dest.stem
    if arm in ("plain", "persona"):
        head = f"Act as an expert {FIELDS[task]}. " if arm == "persona" else ""
        prompt = f"{head}{t}\n\n{material}\n\n{FINAL}"
        answer = retry(claude, prompt, WRITER, label=label)
        body = f"## Prompt\n\n{prompt}\n\n## Answer\n\n{answer}\n"
    else:
        if arm == "felix":
            p1 = f"{FELIX}\n\nMy task: {t}\n\n{material}"
        else:
            p1 = (f"You are an AI assistant with this skill installed:\n\n<skill>\n{SKILL}\n</skill>\n\n"
                  f"The user typed:\n\n/deeper {t}\n\n{material}")
        r1 = retry(claude, p1, WRITER, label=label + " call1")
        rewritten, rule = extract(r1)
        p2 = f"{rewritten}\n\n{material}\n\n{FINAL}"
        answer = retry(claude, p2, WRITER, label=label + " call2")
        log(f"{label}: extraction rule = {rule}")
        body = (f"## Call 1 prompt\n\n{p1}\n\n## Call 1 reply\n\n{r1}\n\n## Extraction\n\n{rule}\n\n"
                f"## Call 2 prompt\n\n{p2}\n\n## Answer\n\n{answer}\n")
    dest.write_text(f"# {label}\n\nWriter: {WRITER}\n\n{body}")
    return f"{dest.name}: ok"


def answer_of(path):
    return path.read_text().split("## Answer\n\n", 1)[1].strip()


def checklist(task):
    sec = README.split(f"### {task}\n", 1)[1].split("\n### ", 1)[0].split("\n## ", 1)[0]
    return sec.strip()


def judge_one(job):
    judge, task = job
    dest = JUDGE / f"{judge}-{task}.json"
    if dest.exists():
        return f"{dest.name}: exists"
    key = json.loads((HERE / "key.json").read_text())[judge][task]
    t, material = fixture(task)
    answers = "\n\n".join(f"=== ANSWER {lab} ===\n{answer_of(RUNS / f'{key[lab]}.md')}" for lab in sorted(key))
    prompt = (
        "You are scoring answers to a task against a fixed checklist. Score only what each answer actually does. "
        "Naming a method, tool or expert earns nothing; an answer that only asks questions or only says what it "
        "would do scores 0 on items it did not carry out. Judge each answer on its own; length and style earn nothing.\n\n"
        f"=== TASK ===\n{t}\n\n=== MATERIAL GIVEN TO THE WRITER ===\n{material}\n\n=== CHECKLIST ===\n{checklist(task)}\n\n"
        f"{answers}\n\n=== OUTPUT ===\nReturn only JSON, no prose: an object keyed by answer label, each value an object "
        'keyed "1" to "6", each value [score, "one-sentence reason"] with score 1 or 0. Example: '
        '{"A": {"1": [1, "..."], "2": [0, "..."], ...}, ...}')
    fn = (lambda p: claude(p, CLAUDE_JUDGE)) if judge == "claude" else codex
    raw = retry(fn, prompt, label=dest.stem)
    data = json.loads(raw[raw.index("{"): raw.rindex("}") + 1])
    assert set(data) == set(key) and all(set(v) == {str(i) for i in range(1, 7)} for v in data.values()), "bad shape"
    dest.write_text(json.dumps(data, indent=1))
    return f"{dest.name}: ok"


def make_key():
    path = HERE / "key.json"
    if path.exists():
        return
    seed = random.SystemRandom().randrange(10**9)
    rng = random.Random(seed)
    names = {t: [f"{t}-{a}-{n}" for a in ARMS for n in (1, 2)] for t in TASKS}
    key = {"seed": seed}
    for judge in ("claude", "gpt"):
        key[judge] = {}
        for t in TASKS:
            order = names[t][:]
            rng.shuffle(order)
            key[judge][t] = dict(zip("ABCDEFGH", order))
    path.write_text(json.dumps(key, indent=1))


def leak_check():
    hits = []
    for p in sorted(RUNS.glob("*.md")):
        low = answer_of(p).lower()
        hits += [f"{p.stem}: {w}" for w in LEAKS if w in low]
    (JUDGE / "leaks.txt").write_text("\n".join(hits) + "\n" if hits else "none\n")
    return hits


if __name__ == "__main__":
    RUNS.mkdir(exist_ok=True)
    JUDGE.mkdir(exist_ok=True)
    if sys.argv[1] == "write":
        jobs = [(t, a, n) for t in TASKS for a in ARMS for n in (1, 2)]
        with cf.ThreadPoolExecutor(4) as ex:
            for line in ex.map(write_one, jobs):
                print(line, flush=True)
    elif sys.argv[1] == "judge":
        make_key()
        print("leaks:", leak_check() or "none")
        jobs = [(j, t) for j in ("claude", "gpt") for t in TASKS]
        with cf.ThreadPoolExecutor(4) as ex:
            for line in ex.map(judge_one, jobs):
                print(line, flush=True)
