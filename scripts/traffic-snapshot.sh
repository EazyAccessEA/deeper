#!/usr/bin/env bash
# Appends today's GitHub traffic for a repo to a CSV. GitHub keeps only 14 days of traffic,
# so run this daily to keep the history. Needs `gh` signed in with push access to the repo.
# Usage: scripts/traffic-snapshot.sh [owner/repo] [csv]
set -euo pipefail

repo="${1:-EazyAccessEA/deeper}"
csv="${2:-$(dirname "$0")/../data/traffic.csv}"
today="$(date -u +%F)"

views="$(gh api "repos/$repo/traffic/views" --jq '[.count, .uniques] | @csv')"
clones="$(gh api "repos/$repo/traffic/clones" --jq '[.count, .uniques] | @csv')"
stars="$(gh api "repos/$repo" --jq '.stargazers_count')"
referrers="$(gh api "repos/$repo/traffic/popular/referrers" --jq '[.[] | "\(.referrer):\(.uniques)"] | join(" ")')"

mkdir -p "$(dirname "$csv")"
[ -s "$csv" ] || echo "date,views_14d,view_uniques_14d,clones_14d,clone_uniques_14d,stars,top_referrers" > "$csv"
echo "$today,$views,$clones,$stars,\"$referrers\"" >> "$csv"
tail -1 "$csv"
