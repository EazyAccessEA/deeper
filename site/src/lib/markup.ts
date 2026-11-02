// The red insertions on the home page. Each one is a verbatim phrase from the real /deeper
// prompt in examples/raw/deeper.md; the build fails if any phrase isn't found there.
import { pairs } from "./evidence";

const INSERTS: Record<string, string[]> = {
  T1: ["the label and its exact wording", "Put the hook in the first ~125 characters", "Every factual line traced to a document I gave you"],
  T2: ["the exported print PDF", "Measure margins, gutter and measure in mm", "Get a printed proof copy"],
  T3: ["full service history and MOT/inspection records", "Value the Polo from real sold prices", "an independent pre-purchase inspection"],
  T4: ["30 days of Vercel usage and logs", "the OpenNext Cloudflare adapter", "A load test at peak traffic"],
  T5: ["dates added, last-opened dates and file types", "Find duplicates by content hash", "no unique file is lost"],
};

export const markups = pairs.map((p) => {
  const inserts = INSERTS[p.id] ?? [];
  for (const phrase of inserts) {
    if (!p.deeper.includes(phrase)) throw new Error(`${p.id}: "${phrase}" is not in the real /deeper prompt`);
  }
  return { ...p, inserts };
});
