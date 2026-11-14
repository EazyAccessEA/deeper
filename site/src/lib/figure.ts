// Journal images as HTML, for figures placed inside an article's Markdown with <!-- figure:<key> -->.
// The image files are licensed stock kept out of git (see .gitignore), so a checkout without them builds
// the page without the figure instead of failing.
import { getImage } from "astro:assets";

const images = import.meta.glob<{ default: ImageMetadata }>("../assets/journal/*.{jpg,jpeg,png,webp}", { eager: true });

export interface Fig { file: string; alt: string; caption?: string; credit?: string; creditUrl?: string; }

export const hasImage = (file: string) => Boolean(images[`../assets/journal/${file}`]);

const esc = (s = "") => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

export async function figureHtml(f: Fig, width = 612): Promise<string> {
  const img = images[`../assets/journal/${f.file}`]?.default;
  if (!img) return "";
  const widths = [Math.min(img.width, 400), Math.min(img.width, width), Math.min(img.width, width * 2)];
  const sizes = `(max-width: 899px) calc(100vw - 2.5rem), ${width}px`;
  const [avif, webp] = await Promise.all(["avif", "webp"].map((format) => getImage({ src: img, widths, sizes, format: format as "avif" | "webp" })));
  const h = Math.round((img.height / img.width) * width);
  const credit = !f.credit ? "" : f.creditUrl ? ` <a href="${esc(f.creditUrl)}">${esc(f.credit)}</a>` : ` ${esc(f.credit)}`;
  return `<figure class="jfig"><picture><source type="image/avif" srcset="${avif.srcSet.attribute}" sizes="${sizes}" />` +
    `<img src="${webp.src}" srcset="${webp.srcSet.attribute}" sizes="${sizes}" alt="${esc(f.alt)}" width="${width}" height="${h}" loading="lazy" decoding="async" /></picture>` +
    (f.caption || credit ? `<figcaption>${f.caption ? `<span class="cap">${esc(f.caption)}</span>` : ""}${credit}</figcaption>` : "") + `</figure>`;
}
