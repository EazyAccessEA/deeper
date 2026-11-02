// The red insertions on the home page. Each one is a verbatim phrase from the real deeper 1.1
// prompt in examples/raw/v1.1/final.md; the build fails if any phrase isn't found there.
import { pairs, finals, round2 } from "./evidence";

// Developer task first: most visitors come from coding agents.
const ORDER = ["T4", "T2", "T5", "T3", "T1"];

const INSERTS: Record<string, string[]> = {
  T4: ["Start from the primary material: the repository", "Prove it rather than reason about it", "A route-by-route comparison of the preview against Vercel production"],
  T2: ["the print PDF and the source layout file", "Judge margins on two-page spreads, never single pages", "A printed proof at 100% on the actual trim size"],
  T5: ["Find exact duplicates by content hash", "Use Finder and the Trash, never `rm`", "Any file unaccounted for is a fail"],
  T3: ["Keep the two deals separate", "an independent pre-purchase inspection", "Selling below the best binding offer is a fail"],
  T1: ["the pollen analysis (melissopalynology) certificate", "Put the hook and the reason to care inside the first 125 characters", "List every factual claim next to the document that backs it"],
};

export const markups = ORDER.map((id) => {
  const p = pairs.find((x) => x.id === id)!;
  const prompt = finals[id];
  const inserts = INSERTS[id];
  for (const phrase of inserts) {
    if (!prompt.includes(phrase)) throw new Error(`${id}: "${phrase}" is not in the real deeper 1.1 prompt`);
  }
  return { id, short: p.short, task: p.task, plain: p.plain, deeper: prompt, inserts, reason: round2.find((r) => r.id === id)!.reason };
});
