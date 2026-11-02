// Handles POST /api/subscribe; every other request goes straight to the static files in dist/.
// Stores the email with where the signup came from, so each channel (TikTok, X, the README) can be counted.
// Nothing is sent yet: the first email to anyone on this list must be a confirmation.

const EMAIL = /^[^\s@<>()",;:]+@[^\s@<>()",;:]+\.[^\s@<>()",;:]{2,}$/;
const PER_IP_PER_DAY = 5;

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname !== "/api/subscribe") return env.ASSETS.fetch(request);
    if (request.method !== "POST") return new Response("Method not allowed", { status: 405, headers: { Allow: "POST" } });
    if (!env.IP_SALT) return new Response("Signup is not configured", { status: 500 });

    const form = await request.formData().catch(() => null);
    const email = String(form?.get("email") ?? "").trim().toLowerCase();
    if (form?.get("company")) return back(url, "ok"); // honeypot: bots fill every field
    if (email.length > 254 || !EMAIL.test(email)) return back(url, "invalid");

    const referer = request.headers.get("Referer") ?? "";
    const source = sourceOf(referer, String(form.get("source") ?? ""));
    const ip = request.headers.get("CF-Connecting-IP") ?? "";
    const day = new Date().toISOString().slice(0, 10);
    const ipHash = ip ? await sha256(`${env.IP_SALT}|${day}|${ip}`) : null;

    if (ipHash) {
      const { n } = await env.DB.prepare("SELECT COUNT(*) AS n FROM signups WHERE ip_hash = ?").bind(ipHash).first();
      if (n >= PER_IP_PER_DAY) return back(url, "limit");
    }

    await env.DB.prepare(
      "INSERT INTO signups (email, created_at, source, referrer, country, ip_hash) VALUES (?, ?, ?, ?, ?, ?) ON CONFLICT(email) DO NOTHING",
    )
      .bind(email, new Date().toISOString(), source, referer.slice(0, 500) || null, request.cf?.country ?? null, ipHash)
      .run();
    return back(url, "ok");
  },

  // Daily, per the privacy notice: IP hashes go after a day, signups two years after the last email (or signup).
  async scheduled(_event, env) {
    await env.DB.batch([
      env.DB.prepare("UPDATE signups SET ip_hash = NULL WHERE ip_hash IS NOT NULL AND created_at < strftime('%Y-%m-%dT%H:%M:%fZ', 'now', '-1 day')"),
      env.DB.prepare("DELETE FROM signups WHERE COALESCE(last_emailed_at, created_at) < strftime('%Y-%m-%dT%H:%M:%fZ', 'now', '-2 years')"),
    ]);
  },
};

// The page the form sat on carries ?ref= or ?utm_source= from the link that brought the reader in.
function sourceOf(referer, fallback) {
  let s = fallback;
  try {
    const p = new URL(referer).searchParams;
    s = p.get("ref") || p.get("utm_source") || s;
  } catch {}
  return s.toLowerCase().replace(/[^a-z0-9._-]/g, "").slice(0, 40) || "direct";
}

// A plain form post, so every answer is a redirect to a page that explains it; X-Signup is for the tests.
function back(url, status) {
  return new Response(null, { status: 303, headers: { Location: new URL(`/subscribed/#${status}`, url).href, "X-Signup": status } });
}

async function sha256(text) {
  const buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(text));
  return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, "0")).join("");
}
