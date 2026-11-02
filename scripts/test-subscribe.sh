#!/usr/bin/env bash
# Tests the signup Worker against a local D1 (nothing touches Cloudflare). Run from anywhere after `npm run build` in site/.
set -euo pipefail
cd "$(dirname "$0")/../site"
port=8799
db() { npx --no-install wrangler d1 execute deeper-list --local --json --command "$1" 2>/dev/null | python3 -c 'import json,sys;print(json.dumps(json.load(sys.stdin)[0]["results"]))'; }
post() { curl -s -o /dev/null -D - -X POST "http://localhost:$port/api/subscribe" -H "CF-Connecting-IP: $1" -H "Referer: $2" --data-urlencode "email=$3" ${4:+--data-urlencode "$4"} | tr -d '\r' | awk -F': ' 'tolower($1)=="x-signup"{print $2}'; }
fail=0
check() { if [ "$2" = "$3" ]; then echo "pass  $1"; else echo "FAIL  $1: expected [$3], got [$2]"; fail=1; fi; }

if lsof -ti tcp:$port >/dev/null; then echo "port $port is in use; stop that server first"; exit 2; fi
rm -rf .wrangler/state
npx --no-install wrangler d1 execute deeper-list --local --file=schema.sql >/dev/null 2>&1
npx --no-install wrangler dev --local --port $port >/tmp/deeper-wrangler.log 2>&1 &
pid=$!; trap 'kill $pid 2>/dev/null; lsof -ti tcp:$port | xargs kill 2>/dev/null || true' EXIT
for _ in $(seq 60); do curl -s -o /dev/null "http://localhost:$port/" && break; sleep 0.5; done

check "home page still served"         "$(curl -s -o /dev/null -w '%{http_code}' http://localhost:$port/)" 200
check "subscribed page served"         "$(curl -s -o /dev/null -w '%{http_code}' http://localhost:$port/subscribed/)" 200
check "GET on the API refused"         "$(curl -s -o /dev/null -w '%{http_code}' http://localhost:$port/api/subscribe)" 405
check "malformed email refused"        "$(post 10.0.0.1 https://deeper.tools/ 'not-an-email')" invalid
check "overlong email refused"         "$(post 10.0.0.1 https://deeper.tools/ "$(printf 'a%.0s' $(seq 250))@x.io")" invalid
check "nothing saved for bad emails"   "$(db 'SELECT COUNT(*) AS n FROM signups')" '[{"n": 0}]'
check "valid signup accepted"          "$(post 10.0.0.2 'https://deeper.tools/?ref=TikTok-03' 'Reader@Example.com')" ok
check "source taken from ?ref="        "$(db "SELECT source FROM signups WHERE email='reader@example.com'")" '[{"source": "tiktok-03"}]'
check "utm_source also counts"         "$(post 10.0.0.3 'https://deeper.tools/?utm_source=x' 'b@example.com')" ok
check "utm source saved"               "$(db "SELECT source FROM signups WHERE email='b@example.com'")" '[{"source": "x"}]'
check "no ref means direct"            "$(post 10.0.0.3 'https://deeper.tools/' 'c@example.com'; db "SELECT source FROM signups WHERE email='c@example.com'")" "ok
[{\"source\": \"direct\"}]"
check "duplicate keeps one row"        "$(post 10.0.0.4 https://deeper.tools/ 'reader@example.com'; db "SELECT COUNT(*) AS n FROM signups WHERE email='reader@example.com'")" "ok
[{\"n\": 1}]"
check "raw IP never stored"            "$(db "SELECT COUNT(*) AS n FROM signups WHERE ip_hash LIKE '%10.0.0%' OR referrer LIKE '%10.0.0%'")" '[{"n": 0}]'
check "IP hash stored"                 "$(db "SELECT length(ip_hash) AS n FROM signups WHERE email='reader@example.com'")" '[{"n": 64}]'
check "honeypot saves nothing"         "$(post 10.0.0.5 https://deeper.tools/ 'bot@example.com' 'company=Acme'; db "SELECT COUNT(*) AS n FROM signups WHERE email='bot@example.com'")" "ok
[{\"n\": 0}]"
for i in 1 2 3 4 5; do post 10.0.0.9 https://deeper.tools/ "flood$i@example.com" >/dev/null; done
check "sixth signup from one IP capped" "$(post 10.0.0.9 https://deeper.tools/ 'flood6@example.com')" limit
check "capped signup not saved"        "$(db "SELECT COUNT(*) AS n FROM signups WHERE email='flood6@example.com'")" '[{"n": 0}]'

# Retention, as the privacy notice promises: IP hashes cleared after a day, rows deleted two years after last contact.
db "INSERT INTO signups (email, created_at, source, ip_hash) VALUES
  ('old@example.com', strftime('%Y-%m-%dT%H:%M:%fZ','now','-25 months'), 'direct', 'x'),
  ('emailed@example.com', strftime('%Y-%m-%dT%H:%M:%fZ','now','-25 months'), 'direct', NULL),
  ('yesterday@example.com', strftime('%Y-%m-%dT%H:%M:%fZ','now','-2 days'), 'direct', 'y')" >/dev/null
db "UPDATE signups SET last_emailed_at = strftime('%Y-%m-%dT%H:%M:%fZ','now','-3 months') WHERE email='emailed@example.com'" >/dev/null
curl -s -o /dev/null "http://localhost:$port/cdn-cgi/handler/scheduled?cron=17+3+*+*+*"
check "two-year-old signup deleted"     "$(db "SELECT COUNT(*) AS n FROM signups WHERE email='old@example.com'")" '[{"n": 0}]'
check "recently emailed signup kept"    "$(db "SELECT COUNT(*) AS n FROM signups WHERE email='emailed@example.com'")" '[{"n": 1}]'
check "day-old IP hash cleared"         "$(db "SELECT ip_hash FROM signups WHERE email='yesterday@example.com'")" '[{"ip_hash": null}]'
check "today's IP hash kept"            "$(db "SELECT length(ip_hash) AS n FROM signups WHERE email='reader@example.com'")" '[{"n": 64}]'
exit $fail
