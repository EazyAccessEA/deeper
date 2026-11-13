"""Label every sampled review twice (Claude, GPT), then settle disagreements with a third Claude call."""
import concurrent.futures as cf, json, os, pathlib, random, re, subprocess, sys, tempfile, time

HERE = pathlib.Path(__file__).parent
CODER_A, SETTLER = "claude-sonnet-5-5", "claude-opus-5-5"
BOOK = json.loads((HERE / "codebook.json").read_text())
SAMPLES = json.loads((HERE / "data/samples.json").read_text())
BATCH = 30


def claude(prompt, model):
    env = {**os.environ, "CLAUDE_CODE_DISABLE_CLAUDE_MDS": "1"}
    with tempfile.TemporaryDirectory() as tmp:
        r = subprocess.run(["claude", "-p", prompt, "--model", model, "--setting-sources", "project",
                            "--strict-mcp-config", "--tools", "", "--system-prompt", "You are a careful research assistant."],
                           cwd=tmp, env=env, capture_output=True, text=True, timeout=900, stdin=subprocess.DEVNULL)
    if r.returncode or not r.stdout.strip():
        raise RuntimeError(r.stderr[-500:])
    return r.stdout.strip()


def codex(prompt):
    with tempfile.TemporaryDirectory() as tmp:
        out = pathlib.Path(tmp) / "reply.md"
        subprocess.run(["codex", "exec", "--skip-git-repo-check", "--ephemeral", "-s", "read-only", "-C", tmp,
                        "-o", str(out), prompt], check=True, capture_output=True, timeout=900, stdin=subprocess.DEVNULL)
        text = out.read_text().strip()
    if not text:
        raise RuntimeError("empty")
    return text


def log(line):
    with open(HERE / "codes/log.txt", "a") as f:
        f.write(time.strftime("%H:%M:%S ") + line + "\n")


def parse(reply, ids, codes):
    found = dict(re.findall(r'"id"\s*:\s*"([^"]+)"\s*,\s*"code"\s*:\s*"([A-Z]\d+)"', reply))
    missing = [i for i in ids if found.get(i) not in codes]
    if missing:
        raise RuntimeError(f"missing or bad codes for {missing[:3]}")
    return {i: found[i] for i in ids}


def retry(fn, *a, label=""):
    for n in range(3):
        try:
            return fn(*a)
        except Exception as e:  # logged, never retried because of content
            log(f"{label}: attempt {n + 1} failed: {str(e)[:200]}")
            time.sleep(10)
    raise RuntimeError(f"{label}: failed 3 times")


def item(r):
    return json.dumps({"id": r["id"], "stars": r["rating"], "title": r["title"], "text": r["text"]}, ensure_ascii=False)


def prompt_for(pool, batch):
    book = "\n".join(f"{k}: {v}" for k, v in BOOK[pool].items())
    return f"""Label each app review below with exactly one code from this codebook: its main subject.
Where a review names two things, the one it spends most words on wins; on a tie, the first one named.

{book}

Reply with one JSON object per line and nothing else, in this form:
{{"id": "<id>", "code": "<code>"}}

Reviews:
""" + "\n".join(item(r) for r in batch)


def label(coder, pool):
    out = HERE / f"codes/{coder}-{pool}.json"
    if out.exists():
        return json.loads(out.read_text())
    rows = list(SAMPLES[pool])
    random.Random(f"{coder}-{pool}").shuffle(rows)  # each coder gets its own order
    batches = [rows[i:i + BATCH] for i in range(0, len(rows), BATCH)]
    fn = codex if coder == "gpt" else (lambda p: claude(p, CODER_A))

    def one(n_b):
        n, b = n_b
        ids = [r["id"] for r in b]
        return retry(lambda: parse(fn(prompt_for(pool, b)), ids, BOOK[pool]), label=f"{coder}-{pool}-{n}")

    labels = {}
    with cf.ThreadPoolExecutor(4) as ex:
        for part in ex.map(one, enumerate(batches)):
            labels.update(part)
    out.write_text(json.dumps(labels, indent=1, sort_keys=True))
    return labels


def settle(pool, a, b):
    out = HERE / f"codes/settled-{pool}.json"
    if out.exists():
        return
    by_id = {r["id"]: r for r in SAMPLES[pool]}
    book = "\n".join(f"{k}: {v}" for k, v in BOOK[pool].items())
    final = {i: a[i] for i in a if a[i] == b[i]}

    def one(i):
        two = sorted({a[i], b[i]})
        p = f"""Two coders labelled this app review differently. Using the codebook and its rule (the subject the review spends most words on wins; on a tie, the first one named), pick one of {two[0]} or {two[1]}. Reply with the code only.

{book}

Review: {item(by_id[i])}"""
        def ask():
            m = re.search(r"\b([A-Z]\d+)\b", claude(p, SETTLER))
            if not m or m.group(1) not in two:
                raise RuntimeError("not one of the two")
            return m.group(1)
        return i, retry(ask, label=f"settle-{pool}-{i}")

    with cf.ThreadPoolExecutor(6) as ex:
        final.update(ex.map(one, [i for i in a if a[i] != b[i]]))
    out.write_text(json.dumps(final, indent=1, sort_keys=True))


if __name__ == "__main__":
    for pool in ("complaint", "praise"):
        with cf.ThreadPoolExecutor(2) as ex:
            a, b = ex.map(lambda c: label(c, pool), ["claude", "gpt"])
        assert set(a) == set(b) == {r["id"] for r in SAMPLES[pool]}, "coder id sets differ"  # Gate C
        settle(pool, a, b)
        print(pool, "done")
