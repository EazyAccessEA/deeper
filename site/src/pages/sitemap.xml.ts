// Lists every public page at build time, so new pages appear without editing this file.
import type { APIRoute } from "astro";

const SKIP = new Set(["404", "subscribed"]);

export const GET: APIRoute = ({ site }) => {
  const pages = Object.keys(import.meta.glob("./*.astro"))
    .map((f) => f.replace("./", "").replace(".astro", ""))
    .filter((name) => !SKIP.has(name))
    .map((name) => new URL(name === "index" ? "/" : `/${name}/`, site).href)
    .sort();
  const body = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${pages
    .map((u) => `  <url><loc>${u}</loc></url>`)
    .join("\n")}\n</urlset>\n`;
  return new Response(body, { headers: { "Content-Type": "application/xml" } });
};
