// Reads the blind test straight from examples/raw so the site can't drift from the evidence.
import fs from "node:fs";
import path from "node:path";

const RAW = path.resolve(process.cwd(), "../examples/raw");
const read = (f: string) => fs.readFileSync(path.join(RAW, f), "utf8");

function sections(md: string): Record<string, string> {
  const out: Record<string, string> = {};
  for (const m of md.matchAll(/## (T\d)\s*\n([\s\S]*?)(?=\n## T\d|$)/g)) {
    out[m[1]] = m[2].trim().replace(/^```text\n/, "").replace(/\n```$/, "").trim();
  }
  return out;
}

const tasks = Object.fromEntries(
  read("tasks.md").trim().split("\n").map((l) => l.split(": ", 2) as [string, string]),
);
const baseline = sections(read("baseline.md"));
const deeper = sections(read("deeper.md"));
const key: Record<string, { A: string; B: string }> = JSON.parse(read("key.json"));
const judge: Record<string, any> = JSON.parse(read("judge.json"));

export const MEASURES = [
  ["expert_method", "Expert method"],
  ["raw_material", "Starts from raw material"],
  ["external_check", "Check outside the model, with a pass mark"],
  ["scope_kept", "Kept to the original scope"],
] as const;

export const SHORT: Record<string, string> = {
  T1: "Honey caption",
  T2: "Book typesetting",
  T3: "Selling a car",
  T4: "Leaving Vercel",
  T5: "Tidy Downloads",
};

export const pairs = Object.keys(tasks).sort().map((id) => {
  const side = (arm: string) => (key[id].A === arm ? "A" : "B");
  const verdict = judge[id].verdict;
  return {
    id,
    short: SHORT[id],
    task: tasks[id],
    plain: baseline[id],
    deeper: deeper[id],
    winner: verdict === "tie" ? "tie" : key[id][verdict as "A" | "B"],
    // The judge wrote "A" and "B"; swap in the real labels, leaving "A/B test" alone.
    reason: (judge[id].reason as string)
      .replace(/A\/B/g, "\u0000")
      .replace(/\b(A|B)('s)?\b/g, (_: string, l: "A" | "B", s = "") =>
        (key[id][l] === "deeper" ? "/deeper" : "the plain rewrite") + s)
      .replace(/\u0000/g, "A/B")
      .replace(/^the/, "The"),
    scores: { plain: judge[id][side("baseline")], deeper: judge[id][side("deeper")] },
  };
});

const avg = (arm: "plain" | "deeper", m: string) =>
  (pairs.reduce((s, p) => s + p.scores[arm][m], 0) / pairs.length).toFixed(1);

export const averages = MEASURES.map(([k, label]) => ({ label, plain: avg("plain", k), deeper: avg("deeper", k) }));
export const wins = pairs.filter((p) => p.winner === "deeper").length;
