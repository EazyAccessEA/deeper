// Counts page views and clicks on the Copy buttons, for the A/B baseline (research/ab/preregistration.md),
// and which channel's link brought the reader in (?ref=, marketing/social/README.md "The goal").
// Sends only the page path, the event and that ref. Nothing is stored on the device: the ref rides along on
// internal links instead. Skipped when the browser sends Global Privacy Control.
(() => {
  if (navigator.globalPrivacyControl) return;
  const ref = new URLSearchParams(location.search).get("ref") || "";
  const send = (k) => {
    try {
      navigator.sendBeacon("/api/e", new Blob([JSON.stringify({ p: location.pathname, k, r: ref })], { type: "text/plain" }));
    } catch {}
  };
  send("pv");
  document.addEventListener("click", (e) => {
    if (!(e.target instanceof Element)) return;
    if (e.target.closest("[data-copy], .copy-skill")) send("copy");
    const a = ref && e.target.closest("a[href]");
    const u = a && new URL(a.href);
    if (u && u.origin === location.origin && !u.searchParams.has("ref")) { u.searchParams.set("ref", ref); a.href = u.href; }
  }, true);
})();
