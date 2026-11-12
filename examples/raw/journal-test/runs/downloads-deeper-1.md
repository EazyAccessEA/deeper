# downloads-deeper-1

Writer: claude-opus-5-5

## Call 1 prompt

You are an AI assistant with this skill installed:

<skill>
---
name: deeper
description: Rewrite a task into its deeper version (same scope, more expert) before doing it. Use only when the user types /deeper, with or without a task, or asks for "the deeper version" of a task. Do not use it on your own initiative.
license: Apache-2.0
metadata:
  version: "1.1.2"
  source: "Felix Rieseberg, How to be more ambitious: A tutorial for humans with models (13 October 2026), Depth section"
---

# /deeper: a deeper version of the task, not a bigger one

Adapted from the Depth section of Felix Rieseberg, "How to be more ambitious: A tutorial for
humans with models", 13 October 2026:
https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/

The task is whatever the user wrote with /deeper. If they wrote nothing, use the task currently
under discussion. If there is none, ask for the task in one line and stop.

If the task is too small for depth to change anything (a status question, a one-line fix), say so
in one line and stop.

Keep the scope the same size. Deeper means more expert, not more features. Don't start the work.
First answer these four, briefly and specifically for this task:

1. **What would a top professional in this field do here that I haven't asked for?** Name the
   field. Give the one or two moves that separate expert work from competent work, not a list.
2. **What is the rawest material they would start from?** Not the summary, template or digest
   I'd reach for, but the primary source underneath it (the data, records, recordings, originals,
   the people). If you can read files, check the workspace first. Say what's here, where it is,
   and what's missing. If you can't, ask me for it. Name one thing we take as true that this
   material could disprove.
3. **Which methods and tools would they use?** Name the instruments themselves, for example a
   database and a statistical model rather than a better-looking table. Models tend to change
   their vocabulary without changing their method. Say which of these tools are already here.
   Don't swap in a weaker tool just because it's to hand.
   Then the skills and agents for the field, if your environment has them. List the installed
   skills that fit (for example `.agents/skills`, `~/.claude/skills`, `~/.codex/skills`,
   `~/.cursor/skills`, enabled plugins) and the subagent types on offer. If you can run shell
   commands, offer to search the open skills ecosystem with `npx skills find <field>`, which
   downloads and runs the skills CLI from npm, and run it only if I say yes. Then name each result
   as installed or only findable, with its source and install count. If you can't run commands,
   say so rather than guessing. Ask before downloading or installing anything.
4. **What, other than you or me, would show the result is right?** A test, a measurement, a
   tool, a real audience, a domain expert. Prefer something that can be run straight away. A
   model grading its own work doesn't count. Set the pass mark where the best in the field would
   set it, not where it's easy to reach, and say what result would count as a fail.

Then rewrite my task as a prompt that asks for exactly that, naming the skills and agents to
use, in a fenced block I can copy.

**Same deliverables.** Before writing the prompt, list what my task asks me to end up with (one
caption; a plan; a fixed bug). The prompt asks for those and nothing else. Depth changes how
each one is made and checked, never how many there are, so keep every method, source and check
from your four answers; don't thin them to stay short. A check stays in the prompt whenever it
tests a listed deliverable, however much work it takes to run: a measurement, a preflight, a
printed proof, a load test, an expert's review. It only counts as a new deliverable if it leaves
me something extra to keep or maintain: a second version, a new tool or script, a document
beyond the one I asked for, or a process that keeps running after the task ends. Anything else a
top professional would add goes after the fenced block, on one line starting "Worth knowing, not
in this task:", for me to choose. Leave that line out if there's nothing to add.

End by asking whether to run it.

</skill>

The user typed:

/deeper Tidy my Downloads folder.

I'm on a Mac. Here is the output of `ls -l` in ~/Downloads (sizes in bytes):

-rw-r--r--  245760  12 Jan 2026  Zoom.pkg
-rw-r--r-- 98304000  3 Feb 2026  Docker.dmg
-rw-r--r-- 98304000  3 Feb 2026  Docker (1).dmg
-rw-r--r-- 187000000 14 Mar 2026  Figma-arm64.dmg
-rw-r--r--   88412  2 Apr 2026  Invoice-0412.pdf
-rw-r--r--   88412  2 Apr 2026  Invoice-0412 (1).pdf
-rw-r--r--   91022  5 May 2026  Invoice-0517.pdf
-rw-r--r--  412337  6 Apr 2026  P60-2025-26.pdf
-rw-r--r--  1203344  18 Jun 2026  Screenshot 2026-06-18 at 10.02.11.png
-rw-r--r--  1198002  18 Jun 2026  Screenshot 2026-06-18 at 10.02.40.png
-rw-r--r--  2401120  2 Jul 2026  Screenshot 2026-07-02 at 16.45.03.png
-rw-r--r--  3311009  9 Jul 2026  passport-scan.jpg
-rw-r--r--   54210  11 Jul 2026  tenancy-agreement.pdf
-rw-r--r--   61733  20 Aug 2026  tenancy-agreement.pdf.download
-rw-r--r--  1520004  1 Aug 2026  holiday-photos.zip
-rw-r--r--  1520004  1 Aug 2026  holiday-photos (1).zip
drwxr-xr-x     -    1 Aug 2026  holiday-photos
-rw-r--r--   33120  15 Aug 2026  budget.xlsx
-rw-r--r--   35870  2 Sep 2026  budget (1).xlsx
-rw-r--r--   12001  20 Sep 2026  boarding-pass-LHR-LIS.pdf
-rw-r--r--  8800331  1 Oct 2026  presentation-final.key
-rw-r--r--  8812004  4 Oct 2026  presentation-final-v2.key
-rw-r--r--   22145  30 Oct 2026  CV-2026.docx
-rw-r--r--   22145  30 Oct 2026  CV-2026 (1).docx

## Call 1 reply

Deliverable: **a tidied ~/Downloads**. Nothing else. I've only used the listing you pasted and haven't touched the folder.

**1. What would a top professional do that you haven't asked for?**
Field: digital records management and Mac sysadmin. Two moves:
- **Decide by content, not by filename.** In this list, `budget (1).xlsx` is *not* a duplicate (different size, newer date). `presentation-final-v2.key` is newer than `-final`. `tenancy-agreement.pdf.download` is a later, larger, *incomplete* Safari download, possibly a revised agreement. A "delete everything with (1)" rule would lose real work.
- **Treat sensitive documents and installers as risks, not clutter.** `passport-scan.jpg`, `P60-2025-26.pdf`, the tenancy agreement, `CV-2026.docx` and the boarding pass are identity and tax records. They belong in an encrypted, backed-up place, not in Downloads. `Zoom.pkg` is 245 KB, which is far too small for a real Zoom installer, so check its signature before anything else.

**2. What is the rawest material?**
- `ls -l` gives names, sizes and modification dates. The raw material underneath is:
  - the bytes themselves (SHA-256 hashes)
  - each file's Spotlight metadata: `kMDItemWhereFroms` (the source URL), `kMDItemDateAdded` and the quarantine attribute
  - the package and disk-image signatures
  - the contents of the zips compared with the `holiday-photos/` folder
  - what is actually installed in `/Applications`
- None of this is in your listing. All of it can be read on your Mac.
- One assumption this material could disprove: "same name plus same size means the same file." `Docker`, `Invoice-0412`, `holiday-photos.zip` and `CV-2026` only *look* identical until they're hashed.

**3. Which methods and tools?**
- `shasum -a 256` to find exact duplicates.
- `mdls` and `xattr -l` for source URLs and date added.
- `pkgutil --check-signature` and `spctl -a -vv -t install` on `Zoom.pkg`.
- `hdiutil` plus `codesign -dv` for the dmgs, compared against installed app versions (`mdls -name kMDItemVersion /Applications/*.app`).
- `unzip -l` / `diff -r` to compare the zips with the extracted folder.
- Move files to the Trash (Finder via `osascript`), never `rm`, and log every move with old and new path so it can be undone.
- All of these ship with macOS, so there's nothing to install.
- Skills and agents: I haven't checked which skills are installed. I can list `~/.claude/skills` and `.agents/skills`, and, if you say yes, run `npx skills find file-organization`, which downloads the skills CLI from npm. No specialist subagent is needed for a folder this size.

**4. What would show the result is right, other than you or me?**
- A before/after hash check. Every SHA-256 from the "before" inventory must still exist afterwards, in a destination folder or the Trash. Nothing is permanently deleted.
- **Fail** if any unique hash is missing, if anything is removed with `rm`, if a non-duplicate is trashed as a duplicate, or if an ID, tax or tenancy document is left in Downloads.
- Spot-check: replay three entries from the move log in reverse and confirm the files come back.

```
Tidy my ~/Downloads folder on macOS. Work like a records manager: decide by content, never by filename.

1. Inventory first, change nothing. For every file record: SHA-256 (shasum -a 256), size, kMDItemWhereFroms and kMDItemDateAdded (mdls), and quarantine xattr. Save this "before" inventory in the scratchpad.
2. Safety checks before any move:
   - Zoom.pkg (only 245 KB): run pkgutil --check-signature and spctl -a -vv -t install. If it isn't signed by Zoom Video Communications, flag it and do not open it.
   - Docker*.dmg, Figma-arm64.dmg: compare with installed versions in /Applications (mdls kMDItemVersion). Installers for apps already installed at the same or newer version go to the Trash.
   - holiday-photos.zip, holiday-photos (1).zip vs holiday-photos/: compare with unzip -l and diff -r. Trash the zips only if the folder holds every file.
   - tenancy-agreement.pdf.download: inspect the bundle and its source URL. It is newer and larger than tenancy-agreement.pdf, so tell me whether it's a different version I need to re-download. Don't treat it as junk.
3. Duplicates: only files with identical SHA-256 are duplicates. Keep the one without "(1)". Pairs with different hashes (budget.xlsx / budget (1).xlsx, presentation-final / -v2) are versions: keep both and show me the dates and sizes.
4. Propose a plan as a table: file, evidence, action, destination. Sensitive documents (passport-scan.jpg, P60-2025-26.pdf, tenancy agreement, CV, boarding pass, invoices) go to a destination I choose; ask me for it. Screenshots: ask, don't assume. Wait for my approval.
5. Execute only the approved plan. Move to the Trash via Finder (osascript), never rm. Log every move (old path → new path) in the scratchpad.
6. Verify: hash everything again. Every "before" SHA-256 must exist in a destination or the Trash. Undo three logged moves and redo them to prove the log works. Report pass/fail. It is a fail if any unique hash is missing, anything was rm'd, a non-identical file was trashed as a duplicate, or a sensitive document is still in Downloads.
```

Worth knowing, not in this task: an encrypted home for ID documents (e.g. an encrypted APFS disk image or a password manager's file vault), a Folder Action or Hazel rule to keep Downloads tidy, and changing your browser's download location.

Shall I run it? And should I first list the installed skills and search with `npx skills find`?

## Extraction

last fenced block

## Call 2 prompt

Tidy my ~/Downloads folder on macOS. Work like a records manager: decide by content, never by filename.

1. Inventory first, change nothing. For every file record: SHA-256 (shasum -a 256), size, kMDItemWhereFroms and kMDItemDateAdded (mdls), and quarantine xattr. Save this "before" inventory in the scratchpad.
2. Safety checks before any move:
   - Zoom.pkg (only 245 KB): run pkgutil --check-signature and spctl -a -vv -t install. If it isn't signed by Zoom Video Communications, flag it and do not open it.
   - Docker*.dmg, Figma-arm64.dmg: compare with installed versions in /Applications (mdls kMDItemVersion). Installers for apps already installed at the same or newer version go to the Trash.
   - holiday-photos.zip, holiday-photos (1).zip vs holiday-photos/: compare with unzip -l and diff -r. Trash the zips only if the folder holds every file.
   - tenancy-agreement.pdf.download: inspect the bundle and its source URL. It is newer and larger than tenancy-agreement.pdf, so tell me whether it's a different version I need to re-download. Don't treat it as junk.
3. Duplicates: only files with identical SHA-256 are duplicates. Keep the one without "(1)". Pairs with different hashes (budget.xlsx / budget (1).xlsx, presentation-final / -v2) are versions: keep both and show me the dates and sizes.
4. Propose a plan as a table: file, evidence, action, destination. Sensitive documents (passport-scan.jpg, P60-2025-26.pdf, tenancy agreement, CV, boarding pass, invoices) go to a destination I choose; ask me for it. Screenshots: ask, don't assume. Wait for my approval.
5. Execute only the approved plan. Move to the Trash via Finder (osascript), never rm. Log every move (old path → new path) in the scratchpad.
6. Verify: hash everything again. Every "before" SHA-256 must exist in a destination or the Trash. Undo three logged moves and redo them to prove the log works. Report pass/fail. It is a fail if any unique hash is missing, anything was rm'd, a non-identical file was trashed as a duplicate, or a sensitive document is still in Downloads.

I'm on a Mac. Here is the output of `ls -l` in ~/Downloads (sizes in bytes):

-rw-r--r--  245760  12 Jan 2026  Zoom.pkg
-rw-r--r-- 98304000  3 Feb 2026  Docker.dmg
-rw-r--r-- 98304000  3 Feb 2026  Docker (1).dmg
-rw-r--r-- 187000000 14 Mar 2026  Figma-arm64.dmg
-rw-r--r--   88412  2 Apr 2026  Invoice-0412.pdf
-rw-r--r--   88412  2 Apr 2026  Invoice-0412 (1).pdf
-rw-r--r--   91022  5 May 2026  Invoice-0517.pdf
-rw-r--r--  412337  6 Apr 2026  P60-2025-26.pdf
-rw-r--r--  1203344  18 Jun 2026  Screenshot 2026-06-18 at 10.02.11.png
-rw-r--r--  1198002  18 Jun 2026  Screenshot 2026-06-18 at 10.02.40.png
-rw-r--r--  2401120  2 Jul 2026  Screenshot 2026-07-02 at 16.45.03.png
-rw-r--r--  3311009  9 Jul 2026  passport-scan.jpg
-rw-r--r--   54210  11 Jul 2026  tenancy-agreement.pdf
-rw-r--r--   61733  20 Aug 2026  tenancy-agreement.pdf.download
-rw-r--r--  1520004  1 Aug 2026  holiday-photos.zip
-rw-r--r--  1520004  1 Aug 2026  holiday-photos (1).zip
drwxr-xr-x     -    1 Aug 2026  holiday-photos
-rw-r--r--   33120  15 Aug 2026  budget.xlsx
-rw-r--r--   35870  2 Sep 2026  budget (1).xlsx
-rw-r--r--   12001  20 Sep 2026  boarding-pass-LHR-LIS.pdf
-rw-r--r--  8800331  1 Oct 2026  presentation-final.key
-rw-r--r--  8812004  4 Oct 2026  presentation-final-v2.key
-rw-r--r--   22145  30 Oct 2026  CV-2026.docx
-rw-r--r--   22145  30 Oct 2026  CV-2026 (1).docx

Nobody can answer questions before you reply. Do the task now with what's provided, and state any assumptions you make.

## Answer

# Downloads tidy-up: Phase 1 (inventory, safety checks and proposed plan)

**I could not run any commands in this session.** No shell was available, so I have no SHA-256 hashes, `mdls`, `xattr` or signature results. I won't invent them. This reply gives you:

- what the `ls -l` output already shows,
- a **read-only** script that builds the inventory and runs the safety checks,
- a plan that depends on that evidence,
- the two answers I need from you.

Nothing has been moved. Steps 5–6 (execute and verify) wait for your approval anyway, and the scripts for them are at the end.

## What the `ls -l` output already shows

| Finding | Why it matters |
|---|---|
| **Zoom.pkg is 245,760 bytes.** | A full Zoom installer is tens of MB. A tiny `.pkg` is consistent with a script-only package, which is a common malware pattern. **Treat it as suspect until the signature checks pass. Do not double-click it.** |
| **`tenancy-agreement.pdf.download` is a regular file (`-rw-r--r--`), not a directory.** | Safari's `.download` items are bundles (directories with an `Info.plist`). So this was probably not made by Safari, and there may be no bundle or source URL inside it. The `kMDItemWhereFroms` xattr may still hold the URL. |
| **The `.download` file (61,733 B, 20 Aug) is larger than `tenancy-agreement.pdf` (54,210 B, 11 Jul).** | An interrupted download can't be larger than the finished file it copies. So it is **not** a partial copy of the PDF you already have. It is a different document or version. Whether it is complete, or needs re-downloading, depends on the header and `%%EOF` checks below. |
| **budget pair: 33,120 vs 35,870 B. presentation pair: 8,800,331 vs 8,812,004 B.** | Different sizes guarantee different hashes. These are **versions, so keep both.** |
| **Same-size pairs:** Docker / Docker (1), Invoice-0412 / (1), CV-2026 / (1), holiday-photos zip / (1). | These are only *candidate* duplicates. Same size proves nothing. Only `cmp`/SHA-256 decides. |
| **Docker.dmg is exactly 98,304,000 B (96,000 KiB).** | Recent Docker Desktop DMGs are usually much larger, and a perfectly round size is unusual. Check the app's code signature before trusting it. |
| **The `ls` dates are modification dates, not "date added".** | The versions table below uses mtime for now. `kMDItemDateAdded` will be filled in from the inventory. |

### Versions (keep both)

| File | Size | Modified |
|---|---|---|
| budget.xlsx | 33,120 B | 15 Aug 2026 |
| budget (1).xlsx | 35,870 B | 2 Sep 2026 (newer, despite the "(1)") |
| presentation-final.key | 8,800,331 B | 1 Oct 2026 |
| presentation-final-v2.key | 8,812,004 B | 4 Oct 2026 |

## Step 1–2: read-only inventory and safety-check script

**What it does and doesn't do:**
- It moves nothing and deletes nothing.
- It never opens or installs Zoom.pkg.
- DMGs are mounted read-only, without opening or auto-running anything, in empty scratch directories.
- Zips are extracted into empty scratch directories.

Save it as `/private/tmp/claude-501/-private-var-folders-d0-zg5gq25n0x3cz1b6ndmxc3nc0000gn-T-tmp3690k0ha/ebe3a97b-f368-49a6-ad39-e2015e7399bf/scratchpad/phase1.zsh` and run it with `zsh <that path>`. Run it from your home folder, not from inside Downloads.

```zsh
#!/bin/zsh
set -u
SP=/private/tmp/claude-501/-private-var-folders-d0-zg5gq25n0x3cz1b6ndmxc3nc0000gn-T-tmp3690k0ha/ebe3a97b-f368-49a6-ad39-e2015e7399bf/scratchpad
DL=$HOME/Downloads
INV=$SP/inventory-before.tsv
REP=$SP/safety-report.txt
: > $REP

# ---------- 1. Inventory (every file, including inside folders/bundles) ----------
print -r -- $'path\tsha256\tbytes\tdate_added\twhere_froms\tquarantine' > $INV
find $DL -type f -print0 | sort -z | while IFS= read -r -d '' f; do
  h=$(shasum -a 256 "$f" | awk '{print $1}')
  s=$(stat -f %z "$f")
  d=$(mdls -raw -name kMDItemDateAdded "$f" 2>/dev/null)
  w=$(mdls -raw -name kMDItemWhereFroms "$f" 2>/dev/null | tr '\n' ' ' | tr -s ' ')
  q=$(xattr -p com.apple.quarantine "$f" 2>/dev/null || print none)
  print -r -- "$f\t$h\t$s\t$d\t$w\t$q" >> $INV
done

# ---------- 2a. Zoom.pkg: signature only, never install ----------
{ print "== Zoom.pkg"
  pkgutil --check-signature "$DL/Zoom.pkg"
  spctl -a -vv -t install "$DL/Zoom.pkg"
  mdls -name kMDItemWhereFroms "$DL/Zoom.pkg"
} >> $REP 2>&1

# ---------- 2b. DMGs vs /Applications ----------
check_dmg() {  # $1=dmg  $2=app name
  local mnt=$(mktemp -d $SP/mnt.XXXX)
  print "== $1:t" >> $REP
  if hdiutil attach -readonly -nobrowse -noautoopen -mountpoint $mnt "$1" >/dev/null 2>>$REP; then
    local app=$mnt/$2.app
    print "dmg version:  $(plutil -extract CFBundleShortVersionString raw "$app/Contents/Info.plist" 2>&1)" >> $REP
    codesign -dv --verbose=2 "$app" 2>&1 | grep -E 'Authority|TeamIdentifier' >> $REP
    hdiutil detach $mnt -quiet
  fi
  print "installed:    $(mdls -raw -name kMDItemVersion "/Applications/$2.app" 2>&1)" >> $REP
}
check_dmg "$DL/Docker.dmg"      Docker
check_dmg "$DL/Docker (1).dmg"  Docker
check_dmg "$DL/Figma-arm64.dmg" Figma

# ---------- 2c. holiday-photos: content comparison, not just names ----------
for z in "$DL/holiday-photos.zip" "$DL/holiday-photos (1).zip"; do
  x=$(mktemp -d $SP/unzip.XXXX)
  { print "== $z:t"; unzip -l "$z"
    unzip -q "$z" -d $x -x '__MACOSX/*' '*.DS_Store'
    root=$x; [[ -d $x/holiday-photos ]] && root=$x/holiday-photos
    print "-- diff (lines 'Only in $DL/...' are fine; 'Only in $SP' or 'differ' = folder is missing data):"
    diff -rq $root "$DL/holiday-photos"
  } >> $REP 2>&1
done

# ---------- 2d. tenancy-agreement.pdf.download ----------
T="$DL/tenancy-agreement.pdf.download"
{ print "== tenancy"
  ls -ld@ "$T"; file "$T"; xattr -l "$T"
  mdls -name kMDItemWhereFroms "$T" "$DL/tenancy-agreement.pdf"
  if [[ -d $T ]]; then
    ls -la "$T"; plutil -p "$T/Info.plist"     # Safari: DownloadEntryURL, BytesSoFar, TotalToLoad
  else
    print -n "header: "; head -c 8 "$T" | xxd | head -1
    print -n "%%EOF in last 1 KB: "; tail -c 1024 "$T" | grep -ac '%%EOF'
    print -n "old PDF is byte-prefix of new? "; cmp -n 54210 "$T" "$DL/tenancy-agreement.pdf" && print yes
  fi
} >> $REP 2>&1

# ---------- 3. Candidate duplicates ----------
for a b in "Docker.dmg" "Docker (1).dmg" "Invoice-0412.pdf" "Invoice-0412 (1).pdf" \
           "CV-2026.docx" "CV-2026 (1).docx" "holiday-photos.zip" "holiday-photos (1).zip"; do
  cmp -s "$DL/$a" "$DL/$b" && print "IDENTICAL: $a == $b" >> $REP || print "DIFFERENT: $a vs $b" >> $REP
done
print "Done. See $INV and $REP"
```

## Decision rules I'll apply to the results

**Zoom.pkg**
- **Passes** only if `pkgutil` reports `Developer ID Installer: Zoom Video Communications, Inc.` and `spctl` reports `accepted … Notarized Developer ID`.
- **Anything else** (unsigned, other signer, rejected): flag it, don't open it, and Trash it after you confirm.
- **Even if it passes,** I suggest not using a 245 KB stub. Re-download from zoom.us when you need Zoom.

**Docker and Figma DMGs**
- Trash only if the installed version is **the same or newer** than the version inside the DMG.
- Keep the DMG if the app isn't in /Applications, if the DMG is newer, or if the codesign authority isn't Docker Inc / Figma Inc.

**Holiday zips**
- Trash a zip only if `diff` shows no "Only in <scratch>" lines and no "differ" lines for it.

**`tenancy-agreement.pdf.download`**
- **Starts with `%PDF` and has `%%EOF`:** it is a complete newer version. Rename it to a `.pdf` name, with your approval, and keep both.
- **Missing `%%EOF`, or the bundle shows BytesSoFar < TotalToLoad:** it is an incomplete newer version. Re-download it from the `WhereFroms`/`DownloadEntryURL` address.
- **In both cases** it is a separate version. It is never junk.

## Step 4: proposed plan (subject to the checks above)

`<SECURE>` means the destination you choose for sensitive documents.

| File | Evidence | Action | Destination |
|---|---|---|---|
| Zoom.pkg | 245 KB, signature pending | Flag, don't open. Trash only after you confirm. | Trash (pending) |
| Docker.dmg | Version vs /Applications pending | Trash if installed ≥ DMG, otherwise keep | Trash or keep |
| Docker (1).dmg | Same size as Docker.dmg, hash pending | If identical: Trash as duplicate. If different: treat like Docker.dmg. | Trash |
| Figma-arm64.dmg | Version pending | Trash if installed ≥ DMG | Trash or keep |
| Invoice-0412.pdf | Sensitive | Move | `<SECURE>`/Invoices |
| Invoice-0412 (1).pdf | Same size, hash pending | Trash only if identical, otherwise move as a version | Trash or `<SECURE>` |
| Invoice-0517.pdf | Sensitive | Move | `<SECURE>`/Invoices |
| P60-2025-26.pdf | Sensitive | Move | `<SECURE>`/Tax |
| passport-scan.jpg | Sensitive | Move | `<SECURE>`/ID |
| tenancy-agreement.pdf | Sensitive, older version | Move | `<SECURE>`/Housing |
| tenancy-agreement.pdf.download | Newer, larger version; completeness pending | Move (renamed, with your approval). Re-download if incomplete. | `<SECURE>`/Housing |
| boarding-pass-LHR-LIS.pdf | Sensitive | Move | `<SECURE>`/Travel |
| CV-2026.docx | Sensitive | Move | `<SECURE>`/CV |
| CV-2026 (1).docx | Same size, hash pending | Trash only if identical | Trash or `<SECURE>` |
| holiday-photos/ | Folder | Move (proposed) | ~/Pictures/holiday-photos |
| holiday-photos.zip | diff pending | Trash only if the folder holds every file | Trash or keep |
| holiday-photos (1).zip | Same size as the zip, hash pending | Same rule | Trash or keep |
| budget.xlsx, budget (1).xlsx | Different sizes, so versions | Keep both | ~/Documents/Finance (proposed) |
| presentation-final.key, -v2.key | Different sizes, so versions | Keep both | ~/Documents/Work (proposed) |
| 3 × Screenshot*.png | Not inspected | **Your call** | ? |

## I need from you

1. **Where should sensitive documents go?** For example, an encrypted APFS volume or disk image, or a specific folder.
2. **Screenshots:** keep (where?), Trash, or review each one?
3. **Are the proposed destinations OK?** These are the Finance/Work/Pictures folders for budget, presentation and holiday-photos.
4. **Run `phase1.zsh` and paste the two files back:**
   - `/private/tmp/claude-501/-private-var-folders-d0-zg5gq25n0x3cz1b6ndmxc3nc0000gn-T-tmp3690k0ha/ebe3a97b-f368-49a6-ad39-e2015e7399bf/scratchpad/inventory-before.tsv`
   - `/private/tmp/claude-501/-private-var-folders-d0-zg5gq25n0x3cz1b6ndmxc3nc0000gn-T-tmp3690k0ha/ebe3a97b-f368-49a6-ad39-e2015e7399bf/scratchpad/safety-report.txt`

   I'll then fill the evidence into the table.

## Steps 5–6: execution and verification helpers (do not run until the plan is approved)

How these keep to your rules:
- There is no `rm` anywhere.
- `mv -n` never overwrites an existing file.
- Trashing goes through Finder and records the actual path in the Trash.
- `trash_dup` refuses to Trash anything that isn't byte-identical to the file being kept.

```zsh
SP=/private/tmp/claude-501/-private-var-folders-d0-zg5gq25n0x3cz1b6ndmxc3nc0000gn-T-tmp3690k0ha/ebe3a97b-f368-49a6-ad39-e2015e7399bf/scratchpad
LOG=$SP/move-log.tsv      # ts  op  sha256  old  new
hsh() { [[ -d $1 ]] && print dir || shasum -a 256 "$1" | awk '{print $1}' }

move() {  # src destdir
  local h=$(hsh "$1") new="$2/${1:t}"
  mkdir -p "$2"; [[ -e $new ]] && { print -u2 "EXISTS $new"; return 1 }
  mv -n "$1" "$new" && [[ -e $new && ! -e $1 ]] &&
    print -r -- "$(date -u +%FT%TZ)\tMOVE\t$h\t$1\t$new" >> $LOG
}
trash() {  # src  (Finder, never rm)
  local h=$(hsh "$1") new
  new=$(osascript -e 'on run {p}' -e 'tell application "Finder" to set t to delete (POSIX file p as alias)' \
                  -e 'return POSIX path of (t as alias)' -e 'end run' "$1") || return 1
  print -r -- "$(date -u +%FT%TZ)\tTRASH\t$h\t$1\t${new%/}" >> $LOG
}
trash_dup() {  # dup keeper — refuses unless byte-identical
  cmp -s "$1" "$2" || { print -u2 "NOT IDENTICAL, refusing: $1"; return 1 }
  print -r -- "$(date -u +%FT%TZ)\tDUPCHECK\t$(hsh "$1")\t$1\t$2" >> $LOG; trash "$1"
}
undo_redo_last3() {
  grep -E $'\t(MOVE|TRASH)\t' $LOG | tail -n 3 > $SP/undo-set.tsv
  while IFS=$'\t' read -r ts op h old new; do
    mv -n "$new" "$old" && [[ $(hsh "$old") == $h ]] &&
      print -r -- "$(date -u +%FT%TZ)\tUNDO\t$h\t$new\t$old" >> $LOG || print -u2 "UNDO FAIL $old"
  done < $SP/undo-set.tsv
  while IFS=$'\t' read -r ts op h old new; do
    [[ $op == MOVE ]] && move "$old" "${new:h}" || trash "$old"
  done < $SP/undo-set.tsv
}
```

**Verification.** Terminal needs Full Disk Access to read `~/.Trash`.

```zsh
tail -n +2 $SP/inventory-before.tsv | cut -f2 | sort -u > $SP/before.h
find ~/Downloads ~/.Trash <SECURE> ~/Pictures/holiday-photos ~/Documents/Finance ~/Documents/Work \
     -type f -print0 | xargs -0 shasum -a 256 | awk '{print $1}' | sort -u > $SP/after.h
comm -23 $SP/before.h $SP/after.h            # must print nothing → PASS
ls ~/Downloads | grep -Ei 'passport|P60|tenancy|CV-|boarding|invoice'   # must print nothing → PASS
```

**Pass/fail criteria:**
- `comm` prints nothing.
- The sensitive-file `ls` prints nothing.
- Every `DUPCHECK` line has a matching identical keeper.
- The three `UNDO` lines restore the original hashes and are followed by successful redos.
- No `rm` appears anywhere in the shell history for the session.

## Assumptions

- **Nothing has been run.** All results above come only from your `ls -l` output.
- **The `ls` dates are modification times,** not date added.
- **Proposed destinations:** ~/Documents/Finance, ~/Documents/Work and ~/Pictures are suggestions until you approve them.
- **Zoom team ID:** if Zoom passes the signature check, I'll still confirm its Developer ID team identifier against Zoom's published one before treating it as genuine.
