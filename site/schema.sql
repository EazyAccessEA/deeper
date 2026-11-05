-- The email list. Apply with: npx wrangler d1 execute deeper-list --file=schema.sql (add --remote for production).
-- ip_hash is SHA-256 of a secret salt, the day and the IP: it caps repeat signups and can't be turned back into an IP.
CREATE TABLE IF NOT EXISTS signups (
  email TEXT PRIMARY KEY,
  created_at TEXT NOT NULL,
  source TEXT NOT NULL,
  referrer TEXT,
  country TEXT,
  ip_hash TEXT,
  confirmed_at TEXT,
  last_emailed_at TEXT
);
CREATE INDEX IF NOT EXISTS signups_ip_hash ON signups (ip_hash);

-- Copy-click counting for the A/B baseline (research/ab/preregistration.md).
-- Counters only: one row per day, page, event, country and variant, never one per person. Nothing identifies a visitor.
CREATE TABLE IF NOT EXISTS events (
  day TEXT NOT NULL,
  page TEXT NOT NULL,
  kind TEXT NOT NULL,          -- 'pv' (page view) or 'copy' (a Copy button was clicked)
  country TEXT NOT NULL,
  variant TEXT NOT NULL DEFAULT 'live',
  n INTEGER NOT NULL DEFAULT 0,
  PRIMARY KEY (day, page, kind, country, variant)
);
