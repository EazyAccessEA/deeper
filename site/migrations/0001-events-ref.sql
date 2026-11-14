-- 14 Nov 2026: add ref to events and to its key, so views and copies can be counted per channel.
-- Existing rows get ref '' (no ref). Run once: npx wrangler d1 execute deeper-list --remote --file=migrations/0001-events-ref.sql
CREATE TABLE events_new (
  day TEXT NOT NULL,
  page TEXT NOT NULL,
  kind TEXT NOT NULL,
  country TEXT NOT NULL,
  variant TEXT NOT NULL DEFAULT 'live',
  ref TEXT NOT NULL DEFAULT '',
  n INTEGER NOT NULL DEFAULT 0,
  PRIMARY KEY (day, page, kind, country, variant, ref)
);
INSERT INTO events_new (day, page, kind, country, variant, ref, n) SELECT day, page, kind, country, variant, '', n FROM events;
DROP TABLE events;
ALTER TABLE events_new RENAME TO events;
