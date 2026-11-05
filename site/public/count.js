// Counts page views and clicks on the Copy buttons, for the A/B baseline (research/ab/preregistration.md).
// Sends only the page path and the event. Nothing is stored on the device. Skipped when the browser sends Global Privacy Control.
(() => {
  if (navigator.globalPrivacyControl) return;
  const send = (k) => {
    try {
      navigator.sendBeacon("/api/e", new Blob([JSON.stringify({ p: location.pathname, k })], { type: "text/plain" }));
    } catch {}
  };
  send("pv");
  document.addEventListener("click", (e) => {
    if (e.target instanceof Element && e.target.closest("[data-copy], .copy-skill")) send("copy");
  }, true);
})();
