// Visual blocks for journal articles, placed in the Markdown with <!-- block:<key> -->.
// Every number is read from examples/raw at build time, like the rest of the site, so a block can't drift
// from its study. Design: Paper, "deeper.tools — elevate", page "Journal — feature article".
import fs from "node:fs";
import path from "node:path";

const RAW = path.resolve(process.cwd(), "../examples/raw");
const read = (f: string) => JSON.parse(fs.readFileSync(path.join(RAW, f), "utf8"));
const esc = (s = "") => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
const pct = (n: number) => `${Math.round(n)}%`;
const fmt = (n: number) => n.toLocaleString("en-GB");

function complaints() {
  const r = read("journal-complaints/results.json").complaint;
  const book = read("journal-complaints/codebook.json").complaint;
  const name = (c: string) => book[c].split(":")[0];
  const top = Object.values(r.shares).reduce((m: number, s: any) => Math.max(m, s.pct), 0) as number;
  // Red: the joint first place the article names. Outlined: categories that hold what researchers warn about.
  const red = new Set(["C1", "C5"]), outline = new Set(["C3", "C8"]);
  const rows = Object.entries(r.shares).filter(([c]) => c !== "C10").map(([c, s]: [string, any]) =>
    `<li class="${red.has(c) ? "loud" : outline.has(c) ? "warned" : ""}"><span class="lab">${esc(name(c))}${outline.has(c) ? ' <span class="tag">Expert worry</span>' : ""}</span>` +
    `<span class="val">${s.pct.toFixed(1)}%</span><span class="bar" style="--w:${((s.pct / top) * 100).toFixed(1)}%"></span></li>`).join("");
  const other = r.shares.C10.pct.toFixed(1);
  return `<figure class="jblock jchart"><figcaption class="jlabel">${r.n} one- and two-star reviews, by main subject</figcaption><ol>${rows}</ol>` +
    `<p class="jnote">Red: joint first, their margins of error overlap. Outlined: what researchers warn about. Not shown: ${other}% with no clear subject.</p></figure>`;
}

function chats() {
  const k = read("journal-complaints/keywords.json").all;
  return `<aside class="jblock jstat" aria-label="Training on your chats"><p class="jlabel">Training on your chats</p>` +
    `<p class="big"><span class="n">${fmt(k["training on chats"])}</span> <span class="of">of ${fmt(k.reviews)} reviews</span></p>` +
    `<p class="say">mention it. All six big US developers studied appear to train on chats by default.</p></aside>`;
}

function gap() {
  const s = read("journal-complaints/results.json").complaint.shares;
  const k = read("journal-complaints/keywords.json").all;
  const col = (cls: string, title: string, rows: [string, string][]) =>
    `<div class="${cls}"><p class="jlabel">${title}</p><ul>${rows.map(([l, v]) => `<li><span>${esc(l)}</span><b>${v}</b></li>`).join("")}</ul></div>`;
  return `<aside class="jblock jgap" aria-label="What users name, and what experts warn about"><p class="head">The buzzer and the crash</p><div class="cols">` +
    col("users", "What users name", [["Limits and money", pct(s.C1.pct)], ["App broken", pct(s.C5.pct)], ["Got worse after an update", pct(s.C6.pct)]]) +
    col("experts", "What experts warn about", [["Tone complaints, where flattery would go", pct(s.C8.pct)], ["Made-up answers", pct(s.C3.pct)], ["Training on your chats", `${k["training on chats"]} of ${fmt(k.reviews)}`]]) +
    `</div><p class="jnote">Share of 1- and 2-star complaints, except the last line, which counts all reviews.</p></aside>`;
}

const BLOCKS: Record<string, () => string> = { complaints, chats, gap };

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
