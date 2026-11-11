// The SHA-256 of the SKILL.md this build ships, in `shasum -a 256 -c` format. Served from Cloudflare, not GitHub,
// so a GitHub account takeover can't change the file and its hash together (SECURITY.md).
import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";

export function GET() {
  const skill = fs.readFileSync(path.resolve(process.cwd(), "../skills/deeper/SKILL.md"));
  const version = /version: "([^"]+)"/.exec(skill.toString())?.[1] ?? "unknown";
  const hash = createHash("sha256").update(skill).digest("hex");
  return new Response(`# deeper ${version}\n${hash}  SKILL.md\n`, { headers: { "Content-Type": "text/plain; charset=utf-8" } });
}
