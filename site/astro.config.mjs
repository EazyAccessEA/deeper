import { defineConfig } from "astro/config";

export default defineConfig({
  site: "https://deeper.tools",
  // Emit every script as a file so the CSP in public/_headers can forbid inline scripts.
  vite: { build: { assetsInlineLimit: 0 } },
});
