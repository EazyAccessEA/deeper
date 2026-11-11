// The Claude Code plugin marketplace: `/plugin marketplace add https://deeper.tools/marketplace.json`.
// It points at skills/ in the public repo, pinned to the latest release tag and its commit, so a plugin install
// fetches that one folder (git-subdir is a sparse fetch) instead of cloning the whole repo. Built on every deploy.
import { execFileSync } from "node:child_process";
import fs from "node:fs";

const git = (...args: string[]) => execFileSync("git", args, { encoding: "utf8" }).trim();

export function GET() {
  const tag = git("describe", "--tags", "--abbrev=0", "--match", "v*");
  const sha = git("rev-list", "-n", "1", tag);
  // skill-sha256.txt publishes the working-tree SKILL.md as the latest release; the plugin installs the tag.
  // If they differ, an unreleased edit would be served as released, so the build stops here.
  if (git("show", `${tag}:skills/deeper/SKILL.md`) !== fs.readFileSync("../skills/deeper/SKILL.md", "utf8").trim()) {
    throw new Error(`skills/deeper/SKILL.md differs from ${tag}. Tag a release before deploying, or revert the edit.`);
  }
  const plugin = JSON.parse(fs.readFileSync("../.claude-plugin/plugin.json", "utf8"));
  const marketplace = {
    name: "deeper",
    owner: { name: "EazyAccessEA" },
    plugins: [
      {
        name: "deeper",
        description: plugin.description,
        version: tag.slice(1),
        source: { source: "git-subdir", url: "https://github.com/EazyAccessEA/deeper.git", path: "skills", ref: tag, sha },
        strict: false,
        skills: ["./deeper"],
        license: plugin.license,
        homepage: "https://deeper.tools",
      },
    ],
  };
  return new Response(JSON.stringify(marketplace, null, 2) + "\n", { headers: { "Content-Type": "application/json" } });
}
