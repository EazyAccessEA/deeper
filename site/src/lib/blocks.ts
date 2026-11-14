// Visual blocks for journal articles, placed in the Markdown with <!-- block:<key> -->.
// Every number is read from examples/raw at build time (except quoted figures from cited sources), like the rest of the site, so a block can't drift
// from its study. Design: Paper, "deeper.tools — elevate", page "Journal — feature article".
import fs from "node:fs";
import path from "node:path";

const RAW = path.resolve(process.cwd(), "../examples/raw");
const read = (f: string) => JSON.parse(fs.readFileSync(path.join(RAW, f), "utf8"));
const esc = (s = "") => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
const pct = (n: number) => `${Math.round(n)}%`;
const fmt = (n: number) => n.toLocaleString("en-GB");
// Two decimals, rounding an exact half to even as Python does, so the page prints what score.py prints (5.625 -> 5.62).
const r2 = (x: number) => { const v = x * 100, f = Math.floor(v + 1e-9), d = v - f; return ((d > 0.5 + 1e-9 || (Math.abs(d - 0.5) < 1e-9 && f % 2)) ? f + 1 : f) / 100; };
const two = (x: number) => r2(x).toFixed(2);

// ---- Three shapes, shared by every article (Paper: "Journal — feature article"). ----
type Bar = { label: string; value: number; shown: string; cls?: string; tag?: string };
const barChart = (caption: string, rows: Bar[], max: number, note: string) =>
  `<figure class="jblock jchart"><figcaption class="jlabel">${esc(caption)}</figcaption><ol>` +
  rows.map((r) => `<li class="${r.cls ?? ""}"><span class="lab">${esc(r.label)}${r.tag ? ` <span class="tag">${esc(r.tag)}</span>` : ""}</span>` +
    `<span class="val">${r.shown}</span><span class="bar" style="--w:${((r.value / max) * 100).toFixed(1)}%"></span></li>`).join("") +
  `</ol><p class="jnote">${esc(note)}</p></figure>`;
const statBand = (label: string, n: string, of: string, say: string) =>
  `<aside class="jblock jstat" aria-label="${esc(label)}"><p class="jlabel">${esc(label)}</p>` +
  `<p class="big"><span class="n">${n}</span> <span class="of">${esc(of)}</span></p><p class="say">${esc(say)}</p></aside>`;
type Col = { title: string; cls: string; rows: [string, string][] };
const splitBand = (head: string, cols: Col[], note: string) =>
  `<aside class="jblock jgap" aria-label="${esc(head)}"><p class="head">${esc(head)}</p><div class="cols">` +
  cols.map((c) => `<div class="${c.cls}"><p class="jlabel">${esc(c.title)}</p><ul>${c.rows.map(([l, v]) => `<li><span>${esc(l)}</span><b>${v}</b></li>`).join("")}</ul></div>`).join("") +
  `</div><p class="jnote">${esc(note)}</p></aside>`;

// ---- journal-complaints: What bugs people about AI assistants ----
function complaints() {
  const r = read("journal-complaints/results.json").complaint;
  const book = read("journal-complaints/codebook.json").complaint;
  const top = Math.max(...Object.values(r.shares).map((s: any) => s.pct));
  // Red: the joint first place the article names. Outlined: categories that hold what researchers warn about.
  const red = new Set(["C1", "C5"]), outline = new Set(["C3", "C8"]);
  const rows = Object.entries(r.shares).filter(([c]) => c !== "C10").map(([c, s]: [string, any]) => ({
    label: book[c].split(":")[0], value: s.pct, shown: `${s.pct.toFixed(1)}%`,
    cls: red.has(c) ? "loud" : outline.has(c) ? "warned" : "", tag: outline.has(c) ? "Expert worry" : undefined }));
  return barChart(`${r.n} one- and two-star reviews, by main subject`, rows, top,
    `Red: joint first, their margins of error overlap. Outlined: what researchers warn about. Not shown: ${r.shares.C10.pct.toFixed(1)}% with no clear subject.`);
}

function chats() {
  const k = read("journal-complaints/keywords.json").all;
  return statBand("Training on your chats", fmt(k["training on chats"]), `of ${fmt(k.reviews)} reviews`,
    "mention it. All six big US developers studied appear to train on chats by default.");
}

function gap() {
  const s = read("journal-complaints/results.json").complaint.shares;
  const k = read("journal-complaints/keywords.json").all;
  return splitBand("The buzzer and the crash", [
    { title: "What users name", cls: "users", rows: [["Limits and money", pct(s.C1.pct)], ["App broken", pct(s.C5.pct)], ["Got worse after an update", pct(s.C6.pct)]] },
    { title: "What experts warn about", cls: "experts", rows: [["Tone complaints, where flattery would go", pct(s.C8.pct)], ["Made-up answers", pct(s.C3.pct)], ["Training on your chats", `${k["training on chats"]} of ${fmt(k.reviews)}`]] },
  ], "Share of 1- and 2-star complaints, except the last line, which counts all reviews.");
}

// ---- journal-test: four ways of asking, two judges (scored as in examples/raw/journal-test/score.py) ----
const ARMS: [string, string][] = [["plain", "Just asking"], ["persona", "\"Act as an expert\""], ["felix", "Felix's prompt"], ["deeper", "deeper"]];
function journalTest() {
  const key = read("journal-test/key.json");
  const scores: { judge: string; arm: string; n: number }[] = [];
  const items = new Map<string, number[]>();
  for (const judge of ["claude", "gpt"]) for (const task of ["cv", "rent", "complaint", "downloads"]) {
    const data = read(`journal-test/judgements/${judge}-${task}.json`);
    for (const [lab, name] of Object.entries(key[judge][task]) as [string, string][]) {
      const marks = Object.entries(data[lab]).map(([i, v]: [string, any]) => {
        const id = `${task}-${i}`; items.set(id, [...(items.get(id) ?? []), +v[0]]); return +v[0];
      });
      scores.push({ judge, arm: name.split("-")[1], n: marks.reduce((a, b) => a + b, 0) });
    }
  }
  const mean = (f: (x: (typeof scores)[0]) => boolean) => { const v = scores.filter(f).map((x) => x.n); return v.reduce((a, b) => a + b, 0) / v.length; };
  const all = [...items.values()];
  return { mean, total: all.length, everyone: all.filter((v) => v.every(Boolean)).length };
}

function arms() {
  const t = journalTest();
  const rows: Bar[] = ARMS.map(([a, label]) => ({ label, value: t.mean((x) => x.arm === a), shown: two(t.mean((x) => x.arm === a)) }));
  const best = Math.max(...rows.map((r) => r.value));
  rows.forEach((r) => (r.cls = r.value === best ? "loud" : ""));
  return barChart("Actions done, out of 6. Four tasks, two runs, two blind judges", rows, 6,
    "Gaps under 1.0 count as no difference, a rule set before the test. All four are level.");
}

function ceiling() {
  const t = journalTest();
  return statBand("The ceiling", String(t.everyone), `of ${t.total} actions`,
    "were done by every single answer, under both judges, however the question was asked.");
}

function judges() {
  const t = journalTest();
  const col = (judge: string, title: string, cls: string): Col =>
    ({ title, cls, rows: ARMS.map(([a, label]) => [label, two(t.mean((x) => x.arm === a && x.judge === judge))]) });
  return splitBand("Two judges, two companies", [col("claude", "Claude judge", "users"), col("gpt", "GPT judge", "experts")],
    "Actions done out of 6, each judge scoring all 32 answers blind.");
}

// ---- v1.1 and v1.1.1: the scope tests behind "Ask for depth, get size" ----
function v11(dir: string, round: string) {
  const judge = read(`${dir}/${round}-judge.json`), key = read(`${dir}/${round}-key.json`);
  const by: Record<string, { scope: number[]; added: number[] }> = {};
  for (const [task, labels] of Object.entries(key) as [string, Record<string, string>][])
    for (const [lab, arm] of Object.entries(labels)) {
      const j = judge[task][lab]; if (!j) continue;
      (by[arm] ??= { scope: [], added: [] }).scope.push(j.scope_kept); by[arm].added.push(j.added.length);
    }
  const avg = (v: number[]) => v.reduce((a, b) => a + b, 0) / v.length;
  return (arm: string) => ({ scope: avg(by[arm].scope), added: avg(by[arm].added) });
}

function extras() {
  const r = v11("v1.1", "round2");
  const rows: Bar[] = [["plain", "No skill"], ["v1.0", "deeper's first version"], ["v1.1a", "First 1.1 draft"], ["v1.1b", "Final 1.1"]]
    .map(([a, label]) => ({ label, value: r(a).added, shown: r(a).added.toFixed(1), cls: a === "v1.0" ? "loud" : "" }));
  return barChart("Extra things added per task, by the judge's count", rows, Math.max(...rows.map((x) => x.value)),
    "One judging pass, five tasks. Red: the tool built to go deeper.");
}

function twopasses() {
  const a = v11("v1.1", "round2")("v1.1b"), b = v11("v1.1.1", "round2")("pub-1.1");
  return splitBand("Same words, judged twice", [
    { title: "First pass", cls: "users", rows: [["Kept to scope, out of 5", a.scope.toFixed(1)], ["Extras per task", a.added.toFixed(1)]] },
    { title: "Second pass", cls: "experts", rows: [["Kept to scope, out of 5", b.scope.toFixed(1)], ["Extras per task", b.added.toFixed(1)]] },
  ], "The final 1.1 text, letter for letter, in two separate judging passes.");
}

const BLOCKS: Record<string, () => string> = { complaints, chats, gap, arms, ceiling, judges, extras, twopasses };

export function blockHtml(key: string): string {
  const fn = BLOCKS[key];
  if (!fn) throw new Error(`journal block "${key}" doesn't exist`);
  return fn();
}

// "Copilot, 1 star, 30 October 2026" captions become App Store review cards: stars, app and date.
export function reviewCards(body: string): string {
  return body.replace(/<figure class="run">\s*<figcaption>([A-Za-z]+), (\d) stars?, (\d{1,2} \w+ \d{4})<\/figcaption>/g, (_m, app, n, date) => {
    const stars = Array.from({ length: 5 }, (_, i) => `<span class="${i < +n ? "on" : ""}"></span>`).join("");
    return `<figure class="run review"><figcaption><span class="app" aria-hidden="true">${app[0]}</span><span class="who"><b>${app}</b> <span>${date}</span>` +
      `<span class="stars" role="img" aria-label="${n} out of 5 stars">${stars}</span></span></figcaption>`;
  });
}
