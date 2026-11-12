# downloads-felix-2

Writer: claude-opus-5-5

## Call 1 prompt

I want a deeper version of this task, not a bigger one. Before rewriting it: (1) say what a top professional in this field would do here that I'm not asking for; (2) name the rawest material they would start from instead of what has already been digested for me; (3) name the specific methods and tools they would use; (4) say what, other than you or me, would show the result is right. Then rewrite my prompt to ask for exactly that.

My task: Tidy my Downloads folder.

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

# Going deeper on "Tidy my Downloads folder"

## 1. What a top professional would do that you're not asking for

A records manager or a careful sysadmin wouldn't start by sorting files into folders. They would:

- **Prove duplicates instead of guessing them.** Equal size and a " (1)" suffix are hints, not proof. Your listing has four matching pairs: the Docker DMGs, Invoice-0412, holiday-photos.zip, and CV-2026. Each pair still needs a content check. Budget (1).xlsx is a different size and has a later date, so it's probably a newer version, not a duplicate.
- **Separate tidying from deleting.** Every removal should be reversible (Trash or a staging folder, never `rm`), and there should be a snapshot before anything moves.
- **Treat sensitive files as a security problem, not a filing problem.** `passport-scan.jpg`, `P60-2025-26.pdf`, the tenancy agreement, the invoices and the boarding pass contain personal data. They belong in encrypted storage with a retention decision. The P60 and invoices have tax-record retention periods. The boarding pass is probably disposable.
- **Resolve the anomalies.** `tenancy-agreement.pdf.download` is an incomplete Safari download, and it is dated about six weeks after the finished PDF. Was it a newer version that never arrived? Does `holiday-photos/` actually contain everything in the zip? Is "final" or "final-v2" the real final Keynote? Are the two screenshots taken 29 seconds apart near-duplicates?
- **Check whether installers are spent.** Zoom, Docker and Figma installers can go only if those apps are installed and working.
- **Fix the inflow, not just the stock.** That means setting a screenshot save location, a rule for installers, and an automated rule so the folder doesn't refill.

## 2. The rawest material to start from

`ls -l` is already digested, and its date is the *modification* time, not when you downloaded or last used the file. The raw sources are:

- **The file bytes**, for content hashes and byte comparison.
- **Spotlight and extended-attribute metadata**:
  - `kMDItemWhereFroms` gives the source URL for each download.
  - `kMDItemDateAdded` gives when the file arrived.
  - `kMDItemLastUsedDate` shows whether you ever opened it.
  - `com.apple.quarantine` records the downloading app.
- **Archive manifests** (the file list inside each zip), compared with the extracted folder.
- **Installed-app state**, from `/Applications` and the package receipts.
- **Your backup state**: whether Time Machine actually covers these files.

## 3. Methods and tools

| Question | Tool |
|---|---|
| Are "duplicates" identical? | `shasum -a 256`, `cmp` |
| Where and when did it come from? | `mdls -name kMDItemWhereFroms -name kMDItemDateAdded -name kMDItemLastUsedDate`, `xattr -l` |
| Is the zip already extracted in full? | `unzip -l` / `zipinfo` vs. `find holiday-photos -type f`, then `diff` of the lists |
| Is the `.download` salvageable? | `ls -la` inside the bundle, `file` |
| Are the apps installed? | `ls /Applications`, `pkgutil --pkgs \| grep -i zoom`, `mdfind "kMDItemCFBundleIdentifier == '…'"` |
| Rollback point | `tmutil localsnapshot`, or a full copy to an external disk |
| Sensitive storage | Encrypted disk image (`hdiutil create -encryption AES-256 -type SPARSEBUNDLE`) or an encrypted vault |
| Version decisions | Open both Keynote and xlsx versions; Quick Look the screenshots side by side |
| Ongoing hygiene | `defaults write com.apple.screencapture location …`, Hazel or Folder Actions rules, Finder tags, Smart Folders |

## 4. What would show the result is right (independent of us)

- **A before/after hash manifest.** Every unique SHA-256 from before still exists somewhere afterwards, so no unique content was lost. Only proven duplicates are gone.
- **A file-count and `du` reconciliation**: before = kept + moved + trashed, with the size of each.
- **A working rollback**: a Time Machine snapshot or copy taken *before* any change, which you can browse.
- **The apps launching**: Zoom, Docker and Figma open from `/Applications` before their installers are trashed.
- **External retention rules**: HMRC guidance for the P60 and invoices, and your tenancy terms, decide retention instead of gut feel.
- **Spotlight test**: `mdfind` still finds key documents in their new homes.

---

## Rewritten prompt

> I want to clean up `~/Downloads` on my Mac (macOS, zsh) **with zero loss of unique data and a full rollback path**. Don't run anything destructive. Work in phases and wait for my output between phases.
>
> **Phase 0: Safety.** Give me commands to (a) confirm Time Machine status and create a local snapshot (`tmutil localsnapshot`), and (b) write a manifest of every file in `~/Downloads` (recursively) with SHA-256, size, and path to a file outside Downloads.
>
> **Phase 1: Raw evidence.** Give me read-only commands that collect, for every item:
> - SHA-256 hashes, to prove or disprove these suspected duplicates: `Docker.dmg`/`Docker (1).dmg`, `Invoice-0412.pdf`/`(1)`, `holiday-photos.zip`/`(1)`, `CV-2026.docx`/`(1)`
> - `mdls` values for `kMDItemWhereFroms`, `kMDItemDateAdded` and `kMDItemLastUsedDate`, plus the `com.apple.quarantine` xattr
> - a comparison of `holiday-photos.zip`'s contents (`unzip -l`) against the `holiday-photos/` folder
> - the contents and state of `tenancy-agreement.pdf.download`, and whether its source URL differs from `tenancy-agreement.pdf`
> - whether Zoom, Docker and Figma are installed (`/Applications`, `pkgutil --pkgs`)
>
> **Phase 2: Decisions.** From my Phase 1 output, produce a table: file → evidence → action (keep / move to [destination] / move to Trash / needs my judgement) → reason. Rules:
> - Only call something a duplicate if hashes match.
> - Flag version pairs (`budget` vs `budget (1)`, `presentation-final` vs `-v2`, the two 10:02 screenshots) for me to decide, and tell me what to compare.
> - Treat `passport-scan.jpg`, `P60-2025-26.pdf`, the tenancy agreement, invoices and boarding pass as sensitive. Propose an encrypted destination (e.g. an AES-256 sparse bundle via `hdiutil`), and state a retention period for each, citing the external rule (e.g. HMRC record-keeping guidance) rather than guessing.
> - Installers can go only after I've confirmed the app launches.
>
> **Phase 3: Execute reversibly.** Give me a script that only uses `mv` (to destinations or `~/.Trash`), never `rm`. It should log every move to a file so the log can be replayed in reverse as an undo script.
>
> **Phase 4: Verify.** Give me commands that re-hash everything (Downloads, destinations, Trash). Prove every unique hash from the Phase 0 manifest still exists, and reconcile file counts and `du -sh` before and after. Confirm with `mdfind` that key documents are findable.
>
> **Phase 5: Prevent recurrence.** Suggest a screenshot save location (`defaults write com.apple.screencapture location`) and 2–3 Hazel or Folder Action rules (e.g. installers older than 14 days → Trash after app check; PDFs → review folder).
>
> Explain any command I might not recognise in one line.

## Extraction

whole reply

## Call 2 prompt

# Going deeper on "Tidy my Downloads folder"

## 1. What a top professional would do that you're not asking for

A records manager or a careful sysadmin wouldn't start by sorting files into folders. They would:

- **Prove duplicates instead of guessing them.** Equal size and a " (1)" suffix are hints, not proof. Your listing has four matching pairs: the Docker DMGs, Invoice-0412, holiday-photos.zip, and CV-2026. Each pair still needs a content check. Budget (1).xlsx is a different size and has a later date, so it's probably a newer version, not a duplicate.
- **Separate tidying from deleting.** Every removal should be reversible (Trash or a staging folder, never `rm`), and there should be a snapshot before anything moves.
- **Treat sensitive files as a security problem, not a filing problem.** `passport-scan.jpg`, `P60-2025-26.pdf`, the tenancy agreement, the invoices and the boarding pass contain personal data. They belong in encrypted storage with a retention decision. The P60 and invoices have tax-record retention periods. The boarding pass is probably disposable.
- **Resolve the anomalies.** `tenancy-agreement.pdf.download` is an incomplete Safari download, and it is dated about six weeks after the finished PDF. Was it a newer version that never arrived? Does `holiday-photos/` actually contain everything in the zip? Is "final" or "final-v2" the real final Keynote? Are the two screenshots taken 29 seconds apart near-duplicates?
- **Check whether installers are spent.** Zoom, Docker and Figma installers can go only if those apps are installed and working.
- **Fix the inflow, not just the stock.** That means setting a screenshot save location, a rule for installers, and an automated rule so the folder doesn't refill.

## 2. The rawest material to start from

`ls -l` is already digested, and its date is the *modification* time, not when you downloaded or last used the file. The raw sources are:

- **The file bytes**, for content hashes and byte comparison.
- **Spotlight and extended-attribute metadata**:
  - `kMDItemWhereFroms` gives the source URL for each download.
  - `kMDItemDateAdded` gives when the file arrived.
  - `kMDItemLastUsedDate` shows whether you ever opened it.
  - `com.apple.quarantine` records the downloading app.
- **Archive manifests** (the file list inside each zip), compared with the extracted folder.
- **Installed-app state**, from `/Applications` and the package receipts.
- **Your backup state**: whether Time Machine actually covers these files.

## 3. Methods and tools

| Question | Tool |
|---|---|
| Are "duplicates" identical? | `shasum -a 256`, `cmp` |
| Where and when did it come from? | `mdls -name kMDItemWhereFroms -name kMDItemDateAdded -name kMDItemLastUsedDate`, `xattr -l` |
| Is the zip already extracted in full? | `unzip -l` / `zipinfo` vs. `find holiday-photos -type f`, then `diff` of the lists |
| Is the `.download` salvageable? | `ls -la` inside the bundle, `file` |
| Are the apps installed? | `ls /Applications`, `pkgutil --pkgs \| grep -i zoom`, `mdfind "kMDItemCFBundleIdentifier == '…'"` |
| Rollback point | `tmutil localsnapshot`, or a full copy to an external disk |
| Sensitive storage | Encrypted disk image (`hdiutil create -encryption AES-256 -type SPARSEBUNDLE`) or an encrypted vault |
| Version decisions | Open both Keynote and xlsx versions; Quick Look the screenshots side by side |
| Ongoing hygiene | `defaults write com.apple.screencapture location …`, Hazel or Folder Actions rules, Finder tags, Smart Folders |

## 4. What would show the result is right (independent of us)

- **A before/after hash manifest.** Every unique SHA-256 from before still exists somewhere afterwards, so no unique content was lost. Only proven duplicates are gone.
- **A file-count and `du` reconciliation**: before = kept + moved + trashed, with the size of each.
- **A working rollback**: a Time Machine snapshot or copy taken *before* any change, which you can browse.
- **The apps launching**: Zoom, Docker and Figma open from `/Applications` before their installers are trashed.
- **External retention rules**: HMRC guidance for the P60 and invoices, and your tenancy terms, decide retention instead of gut feel.
- **Spotlight test**: `mdfind` still finds key documents in their new homes.

---

## Rewritten prompt

> I want to clean up `~/Downloads` on my Mac (macOS, zsh) **with zero loss of unique data and a full rollback path**. Don't run anything destructive. Work in phases and wait for my output between phases.
>
> **Phase 0: Safety.** Give me commands to (a) confirm Time Machine status and create a local snapshot (`tmutil localsnapshot`), and (b) write a manifest of every file in `~/Downloads` (recursively) with SHA-256, size, and path to a file outside Downloads.
>
> **Phase 1: Raw evidence.** Give me read-only commands that collect, for every item:
> - SHA-256 hashes, to prove or disprove these suspected duplicates: `Docker.dmg`/`Docker (1).dmg`, `Invoice-0412.pdf`/`(1)`, `holiday-photos.zip`/`(1)`, `CV-2026.docx`/`(1)`
> - `mdls` values for `kMDItemWhereFroms`, `kMDItemDateAdded` and `kMDItemLastUsedDate`, plus the `com.apple.quarantine` xattr
> - a comparison of `holiday-photos.zip`'s contents (`unzip -l`) against the `holiday-photos/` folder
> - the contents and state of `tenancy-agreement.pdf.download`, and whether its source URL differs from `tenancy-agreement.pdf`
> - whether Zoom, Docker and Figma are installed (`/Applications`, `pkgutil --pkgs`)
>
> **Phase 2: Decisions.** From my Phase 1 output, produce a table: file → evidence → action (keep / move to [destination] / move to Trash / needs my judgement) → reason. Rules:
> - Only call something a duplicate if hashes match.
> - Flag version pairs (`budget` vs `budget (1)`, `presentation-final` vs `-v2`, the two 10:02 screenshots) for me to decide, and tell me what to compare.
> - Treat `passport-scan.jpg`, `P60-2025-26.pdf`, the tenancy agreement, invoices and boarding pass as sensitive. Propose an encrypted destination (e.g. an AES-256 sparse bundle via `hdiutil`), and state a retention period for each, citing the external rule (e.g. HMRC record-keeping guidance) rather than guessing.
> - Installers can go only after I've confirmed the app launches.
>
> **Phase 3: Execute reversibly.** Give me a script that only uses `mv` (to destinations or `~/.Trash`), never `rm`. It should log every move to a file so the log can be replayed in reverse as an undo script.
>
> **Phase 4: Verify.** Give me commands that re-hash everything (Downloads, destinations, Trash). Prove every unique hash from the Phase 0 manifest still exists, and reconcile file counts and `du -sh` before and after. Confirm with `mdfind` that key documents are findable.
>
> **Phase 5: Prevent recurrence.** Suggest a screenshot save location (`defaults write com.apple.screencapture location`) and 2–3 Hazel or Folder Action rules (e.g. installers older than 14 days → Trash after app check; PDFs → review folder).
>
> Explain any command I might not recognise in one line.

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

# Tidying ~/Downloads: complete runbook

You asked me to work in phases and wait for your output, but nobody can reply before I answer. So I've built the safety into the scripts instead:

- Phases 0–1 only read your files. They write reports to a separate folder.
- Phase 3 runs as a dry run by default.
- Phase 3 checks the evidence itself before moving anything. It only treats a "(1)" file as a duplicate if `cmp` proves it is byte-identical. It only stages an installer if you've listed that app as confirmed.
- Anything uncertain is parked in a review folder. Nothing is deleted.

## Assumptions

1. **You're in the UK (England & Wales).** The P60, HMRC and the LHR boarding pass suggest this, and it drives the retention periods.
2. **The `ls` dates are modification times**, not download dates. Invoice tax years below are based on these dates. Check the date printed on each invoice.
3. **Zoom's app is `/Applications/zoom.us.app`**, and Docker's and Figma's are `Docker.app` and `Figma.app`.
4. **Terminal can access Downloads.** If macOS asks, allow it. Without access, some commands fail with "Operation not permitted".
5. **You won't edit any of these files between Phase 0 and Phase 4.** Editing would change their hashes and make verification fail.
6. **Deliberate change: I stage files instead of moving them to `~/.Trash`.** Finder can empty the Trash automatically after 30 days, which would quietly make "reversible" irreversible. Everything goes to `~/Downloads-cleanup-20261112/`. You can trash it yourself after Phase 4 passes.

## Things I noticed in your listing

- **`tenancy-agreement.pdf.download` shows as a regular file (`-rw-`).** Modern Safari partial downloads are folders, so this is unusual. It is also **larger (61,733 vs 54,210 bytes) and newer (20 Aug vs 11 Jul)** than the finished PDF. It may be a revised agreement that never finished downloading. Treat it as important until proven otherwise.
- **Some installer sizes are suspiciously round**, if your figures are exact:
  - `Docker.dmg` is 98,304,000 bytes (exactly 93.75 MiB). Docker Desktop images are usually several hundred MB.
  - `Zoom.pkg` is 245,760 bytes (exactly 240 KiB), which is tiny for Zoom.
  - These may be truncated or stub files. Phase 1 runs `hdiutil verify` and `pkgutil --check-signature` to check.
  - Two identical truncated files are still duplicates of each other. It just means neither is a usable installer.
- **`budget (1).xlsx` is a newer version, not a duplicate.** It's 2,750 bytes bigger and 18 days later. The "(1)" means it was downloaded again, so it may contain someone else's edits.
- **The two screenshots taken at 10:02 are 29 seconds apart** and differ by about 5 KB. That's probably a retake, but you should look at both.

---

## Phase 0: Safety (run first)

```zsh
# 1. Backup state
tmutil destinationinfo          # is a Time Machine disk configured?
tmutil latestbackup             # when did it last complete? (may need Full Disk Access)
fdesetup status                 # is FileVault (full-disk encryption) on?
defaults read com.apple.finder FXRemoveOldTrashItems 2>/dev/null   # 1 = Trash auto-empties after 30 days

# 2. Local APFS snapshot (macOS deletes these after ~24h, so it is not your only rollback)
tmutil localsnapshot            # may ask for sudo
tmutil listlocalsnapshots /

# 3. The real rollback: a full copy, about 400 MB. ditto keeps extended attributes and source URLs.
ditto ~/Downloads ~/Downloads-BACKUP-20261112
```

## Phase 1: Evidence (read-only)

Save this as `~/cleanup-tools/audit.zsh` (keep it outside Downloads) and run `zsh ~/cleanup-tools/audit.zsh`. It writes only to a new `~/DownloadsAudit-<timestamp>/` folder.

```zsh
#!/bin/zsh
# audit.zsh: Phase 0 manifest + Phase 1 evidence. Read-only on ~/Downloads.
set -u
DL=$HOME/Downloads
OUT=$HOME/DownloadsAudit-$(date +%Y%m%d-%H%M%S)
mkdir -p "$OUT"; cd "$DL" || exit 1
print "Writing reports to $OUT"

# --- Phase 0: manifest (hash, size, count, disk use); .DS_Store excluded because Finder rewrites it
find . -type f ! -name .DS_Store -print0 | xargs -0 shasum -a 256 | sort > "$OUT/manifest-before.sha256"
find . -type f ! -name .DS_Store -print0 | xargs -0 stat -f '%z%t%N' > "$OUT/sizes-before.tsv"
wc -l < "$OUT/manifest-before.sha256" > "$OUT/count-before.txt"
du -sk "$DL" > "$OUT/du-before.txt"

# Check that the backup copy matches byte-for-byte
if [[ -d $HOME/Downloads-BACKUP-20261112 ]]; then
  (cd $HOME/Downloads-BACKUP-20261112 && find . -type f ! -name .DS_Store -print0 | xargs -0 shasum -a 256 | sort) \
    | diff -q - "$OUT/manifest-before.sha256" >/dev/null \
    && print "BACKUP OK" > "$OUT/01-backup-check.txt" || print "BACKUP MISMATCH" > "$OUT/01-backup-check.txt"
fi

# --- 1a. Suspected duplicates: cmp = byte-for-byte comparison (stronger than equal size)
for a b in "Docker.dmg" "Docker (1).dmg" "Invoice-0412.pdf" "Invoice-0412 (1).pdf" \
           "holiday-photos.zip" "holiday-photos (1).zip" "CV-2026.docx" "CV-2026 (1).docx" \
           "budget.xlsx" "budget (1).xlsx"; do
  cmp -s "$a" "$b" && print "IDENTICAL  $a == $b" || print "DIFFERENT  $a <> $b"
done > "$OUT/10-duplicates.txt"

# --- 1b. Provenance: source URL, date added, last opened, downloading app
for f in *(N); do
  print "=== $f"
  mdls -name kMDItemWhereFroms -name kMDItemDateAdded -name kMDItemLastUsedDate -name kMDItemUseCount "$f"
  xattr -p com.apple.quarantine "$f" 2>/dev/null || print "(no quarantine attribute)"
done > "$OUT/20-provenance.txt" 2>&1

# --- 1c. Is everything in the zip already in the folder, with identical content?
X="$OUT/zip-extract"; mkdir -p "$X"
ditto -x -k holiday-photos.zip "$X"                    # ditto -x -k = unzip
S=$X; [[ -d $X/holiday-photos ]] && S=$X/holiday-photos
{ print "Zip entries:";    zipinfo -1 holiday-photos.zip | grep -v '^__MACOSX/' | grep -v '/$' | wc -l
  print "Folder files:";   find holiday-photos -type f ! -name .DS_Store | wc -l
  print "Differences (empty = identical; 'Only in holiday-photos' = extra files in folder, harmless):"
  diff -rq -x .DS_Store -x __MACOSX "$S" holiday-photos
} > "$OUT/30-zip-vs-folder.txt" 2>&1

# --- 1d. The orphan .download
F=tenancy-agreement.pdf.download
{ ls -la@ "$F"; file "$F"
  [[ -d $F ]] && { print "-- bundle contents:"; ls -la@R "$F"; file "$F"/* }
  [[ -f $F ]] && { print "-- first bytes (PDFs start %PDF-):"; head -c 8 "$F" | xxd
                   print "-- end marker (%%EOF = probably complete):"; tail -c 2048 "$F" | strings | grep -E 'startxref|%%EOF' }
  print "-- source URLs, finished vs partial:"
  mdls -name kMDItemWhereFroms tenancy-agreement.pdf "$F"
} > "$OUT/40-tenancy-download.txt" 2>&1

# --- 1e. Are the apps installed? Are the installers intact?
{ for b in zoom.us Docker Figma; do
    [[ -d /Applications/$b.app ]] && print "INSTALLED /Applications/$b.app $(defaults read /Applications/$b.app/Contents/Info.plist CFBundleShortVersionString 2>/dev/null)" \
                                  || print "NOT FOUND /Applications/$b.app"
  done
  print "-- package receipts:"; pkgutil --pkgs | grep -iE 'zoom|docker|figma'
  print "-- installer integrity:"
  pkgutil --check-signature Zoom.pkg                  # verifies the developer signature
  hdiutil verify Docker.dmg; hdiutil verify Figma-arm64.dmg   # checks the disk image's internal checksum
} > "$OUT/50-apps.txt" 2>&1

# --- 1f. Version pairs: facts to help you decide
{ sips -g pixelWidth -g pixelHeight Screenshot*2026-06-18*.png  # image dimensions
  ls -l budget*.xlsx presentation-final*.key
} > "$OUT/60-versions.txt" 2>&1

print "Done. Read the files in $OUT. Then compare visually with:"
print "  qlmanage -p ~/Downloads/Screenshot*2026-06-18*.png      # Quick Look, side by side"
print "  open ~/Downloads/budget.xlsx ~/Downloads/'budget (1).xlsx'"
print "  open ~/Downloads/presentation-final.key ~/Downloads/presentation-final-v2.key   (close WITHOUT saving)"
```

**Encrypted vault for sensitive files.** Create this once. It asks for a password, so store that in your password manager.

```zsh
hdiutil create -size 1g -type SPARSEBUNDLE -fs APFS -encryption AES-256 -volname Vault ~/Documents/Vault.sparsebundle
hdiutil attach ~/Documents/Vault.sparsebundle      # mounts at /Volumes/Vault
```

A sparse bundle only takes up as much space as its contents, and Time Machine backs it up in encrypted form. Eject it when you're not using it.

---

## Phase 2: Decisions (provisional until you've read Phase 1)

| File | Evidence that decides it | Default action in tidy.zsh | Reason |
|---|---|---|---|
| `Docker (1).dmg`, `Invoice-0412 (1).pdf`, `holiday-photos (1).zip`, `CV-2026 (1).docx` | `cmp` IDENTICAL | → `cleanup/duplicates` | Proven byte-identical. If they DIFFER, both go to `review`. |
| `Zoom.pkg`, `Docker.dmg`, `Figma-arm64.dmg` | App in `/Applications` and you've launched it | → `cleanup/installers` only if listed in `APPS_CONFIRMED`; otherwise stays | Re-downloadable. Possibly truncated (see 50-apps.txt). |
| `holiday-photos.zip` | Every file in the zip matches a file in the folder | → `duplicates` if covered, else `review` | Redundant once the folder is complete. |
| `holiday-photos/` | n/a | → `~/Pictures/Holidays/2026-08/` | Photos belong in Pictures. Importing into Photos is your call. |
| `budget.xlsx` / `budget (1).xlsx` | Open both | `review` (set `BUDGET=new/old/both`) | Version pair, not a duplicate. |
| `presentation-final.key` / `-v2.key` | Open both | `review` (set `KEYNOTE=…`) | v2 is newer, but confirm it's the version you delivered. |
| Screenshots 10.02.11 / 10.02.40 | Quick Look both | `review` (set `SHOTS=…`) | Likely retake. |
| Screenshot 2026-07-02 | n/a | → `~/Pictures/Screenshots/` | Not a duplicate. |
| `CV-2026.docx` | n/a | → `~/Documents/Career/` | n/a |
| `passport-scan.jpg` | n/a | → `Vault/Identity` | Identity-theft risk. |
| `P60-2025-26.pdf` | n/a | → `Vault/Tax/2025-26` | Tax record. |
| `Invoice-0412.pdf` | Invoice date | → `Vault/Invoices/2025-26` | 2 Apr 2026 falls in tax year 2025-26, which ends 5 Apr. |
| `Invoice-0517.pdf` | Invoice date | → `Vault/Invoices/2026-27` | n/a |
| `tenancy-agreement.pdf` | n/a | → `Vault/Home` | Contract. |
| `tenancy-agreement.pdf.download` | 40-tenancy-download.txt | → `cleanup/review` always | Possibly a newer agreement. If it starts `%PDF-` and ends `%%EOF`, copy it to `salvaged.pdf` and open it. Otherwise re-download from the source URL. |
| `boarding-pass-LHR-LIS.pdf` | Any expense or delay claim? | → `cleanup/to-delete` (set `BOARDING=vault` if a claim is possible) | Low value after the flight. |

**Retention periods.** These are external rules, not gut feel. Confirm them on gov.uk, because your circumstances matter.

| Document | Rule | Keep until |
|---|---|---|
| P60 2025-26 | HMRC "Keeping your pay and tax records": 22 months after the tax year ends if you file Self Assessment (gov.uk/keeping-your-pay-tax-records). Self-employed or landlords: 5 years after the 31 January filing deadline. | **31 Jan 2028** (employee) or **31 Jan 2032** (self-employed). Many people keep P60s longer as proof of income. |
| Invoices you **issued**, as a sole trader | HMRC "Business records if you're self-employed": 5 years after the 31 January submission deadline | 0412: **31 Jan 2032**. 0517: **31 Jan 2033**. If you trade through a limited company: 6 years from the end of the company's financial year. |
| Invoices you **received** (personal purchases) | Limitation Act 1980 s.5: 6 years for contract claims | Purchase date + 6 years, or the end of any warranty, whichever is later |
| Tenancy agreement | Limitation Act 1980: 6 years for contracts, 12 years if signed as a deed. Deposit disputes arise at the end of the tenancy. | **End of tenancy + 6 years** (+12 if a deed). In Scotland, prescription is 5 years. |
| Passport scan | No legal requirement to keep it | Only while you have a specific need. Otherwise delete it once Phase 4 passes. |
| Boarding pass | Only matters for claims. UK261 delay claims can be brought up to 6 years later in England & Wales. | Delete now unless the flight was delayed or cancelled, or you need it for expenses. |

---

## Phase 3: Execute reversibly

Save as `~/cleanup-tools/tidy.zsh`.

1. Edit the decisions block.
2. Run `zsh ~/cleanup-tools/tidy.zsh` and read the dry run.
3. Run `DRY_RUN=0 zsh ~/cleanup-tools/tidy.zsh`.

The script uses only `mkdir` and `mv`, never `rm`. It never overwrites anything, and it records every move so it can generate an undo script.

```zsh
#!/bin/zsh
# tidy.zsh: Phase 3. Dry run unless DRY_RUN=0. Only mkdir + mv -n; logs every move; writes an undo script.
set -u
setopt NULL_GLOB
DRY_RUN=${DRY_RUN:-1}
DL=$HOME/Downloads
STAGE=$HOME/Downloads-cleanup-20261112
VAULT=/Volumes/Vault
LOG=$STAGE/moves.tsv
UNDO=$STAGE/undo.zsh

# ================= YOUR DECISIONS (edit after reading Phase 1) =================
APPS_CONFIRMED=()      # add each app ONLY after it launches, e.g. (Zoom Docker Figma)
BUDGET=review          # new | old | both | review
KEYNOTE=review         # v2 | final | both | review
SHOTS=review           # first (10.02.11) | second (10.02.40) | both | review
BOARDING=stage         # stage (delete later) | vault | keep
# ===============================================================================

DONE=()
(( DRY_RUN )) && print "=== DRY RUN: nothing will move. Re-run with DRY_RUN=0 ===" || mkdir -p "$STAGE"

mvto() {  # mvto <name in Downloads> <destination dir> [new name]
  [[ -n ${1:-} && $1 != */* && $1 != . && $1 != .. ]] || { print -u2 "  skip (bad name): '${1:-}'"; return 1 }
  local src=$DL/$1 dir=$2 dest=$2/${3:-$1}
  (( ${DONE[(Ie)$1]} )) && { print -u2 "  skip (already handled): $1"; return 1 }
  [[ -e $src ]]  || { print -u2 "  skip (not found): $1"; return 1 }
  [[ -e $dest ]] && { print -u2 "  skip (destination exists): $dest"; return 1 }
  DONE+=("$1")
  if (( DRY_RUN )); then print "  would move: $1  ->  $dest"; return 0; fi
  mkdir -p "$dir" && mv -n "$src" "$dest" && [[ -e $dest && ! -e $src ]] || { print -u2 "  FAILED: $1"; return 1 }
  print -r -- "$src"$'\t'"$dest" >> "$LOG"
  print "  moved: $1  ->  $dest"
}

print "1) Exact duplicates (byte-for-byte, cmp)"
for a b in "Docker.dmg" "Docker (1).dmg" "Invoice-0412.pdf" "Invoice-0412 (1).pdf" \
           "holiday-photos.zip" "holiday-photos (1).zip" "CV-2026.docx" "CV-2026 (1).docx"; do
  if cmp -s "$DL/$a" "$DL/$b"; then mvto "$b" "$STAGE/duplicates"
  else print -u2 "  NOT identical, parking both: $a / $b"; mvto "$a" "$STAGE/review"; mvto "$b" "$STAGE/review"; fi
done

print "2) Installers (only apps in APPS_CONFIRMED that exist in /Applications)"
for app file bundle in Zoom Zoom.pkg zoom.us  Docker Docker.dmg Docker  Figma Figma-arm64.dmg Figma; do
  if (( ${APPS_CONFIRMED[(Ie)$app]} )) && [[ -d /Applications/$bundle.app ]]; then mvto "$file" "$STAGE/installers"
  else print "  keeping $file ($app not confirmed)"; fi
done

print "3) Holiday photos"
zip_covered() {  # true only if every file in the zip exists, byte-identical, in the folder
  local zip=$DL/holiday-photos.zip dir=$DL/holiday-photos x s f rel n=0 bad=0
  [[ -f $zip && -d $dir ]] || return 1
  x=$(mktemp -d) && ditto -x -k "$zip" "$x" || return 1
  s=$x; [[ -d $x/holiday-photos ]] && s=$x/holiday-photos
  for f in $s/**/*(.D); do
    [[ $f == */__MACOSX/* || ${f:t} == .DS_Store ]] && continue
    rel=${f#$s/}; n=$((n+1))
    cmp -s "$f" "$dir/$rel" || { print -u2 "  in zip, not identical in folder: $rel"; bad=1 }
  done
  print "  checked $n files from the zip"
  (( n > 0 && bad == 0 ))
}
if zip_covered; then mvto holiday-photos.zip "$STAGE/duplicates"; else mvto holiday-photos.zip "$STAGE/review"; fi
mvto holiday-photos "$HOME/Pictures/Holidays/2026-08"

print "4) Sensitive documents -> encrypted vault"
if [[ -d $VAULT && -w $VAULT ]]; then
  mvto passport-scan.jpg     "$VAULT/Identity"
  mvto P60-2025-26.pdf       "$VAULT/Tax/2025-26"
  mvto Invoice-0412.pdf      "$VAULT/Invoices/2025-26"
  mvto Invoice-0517.pdf      "$VAULT/Invoices/2026-27"
  mvto tenancy-agreement.pdf "$VAULT/Home"
  [[ $BOARDING == vault ]] && mvto boarding-pass-LHR-LIS.pdf "$VAULT/Travel"
else print -u2 "  Vault not mounted at $VAULT: sensitive files left in Downloads"; fi
[[ $BOARDING == stage ]] && mvto boarding-pass-LHR-LIS.pdf "$STAGE/to-delete"
mvto tenancy-agreement.pdf.download "$STAGE/review"

print "5) Versions"
FIN=$HOME/Documents/Finance; PRES=$HOME/Documents/Presentations; SHOTDIR=$HOME/Pictures/Screenshots
case $BUDGET in
  new)  mvto "budget (1).xlsx" "$FIN" budget.xlsx; mvto budget.xlsx "$STAGE/superseded" ;;
  old)  mvto budget.xlsx "$FIN";                   mvto "budget (1).xlsx" "$STAGE/superseded" ;;
  both) mvto budget.xlsx "$FIN" budget-2026-08-15.xlsx; mvto "budget (1).xlsx" "$FIN" budget-2026-09-02.xlsx ;;
  *)    mvto budget.xlsx "$STAGE/review"; mvto "budget (1).xlsx" "$STAGE/review" ;;
esac
case $KEYNOTE in
  v2)    mvto presentation-final-v2.key "$PRES"; mvto presentation-final.key "$STAGE/superseded" ;;
  final) mvto presentation-final.key "$PRES";    mvto presentation-final-v2.key "$STAGE/superseded" ;;
  both)  mvto presentation-final.key "$PRES";    mvto presentation-final-v2.key "$PRES" ;;
  *)     mvto presentation-final.key "$STAGE/review"; mvto presentation-final-v2.key "$STAGE/review" ;;
esac
s1=( $DL/Screenshot*2026-06-18*10.02.11*.png(N:t) )   # globs tolerate odd spaces in macOS screenshot names
s2=( $DL/Screenshot*2026-06-18*10.02.40*.png(N:t) )
s3=( $DL/Screenshot*2026-07-02*16.45.03*.png(N:t) )
mvto "${s3[1]:-}" "$SHOTDIR"
case $SHOTS in
  first)  mvto "${s1[1]:-}" "$SHOTDIR"; mvto "${s2[1]:-}" "$STAGE/superseded" ;;
  second) mvto "${s2[1]:-}" "$SHOTDIR"; mvto "${s1[1]:-}" "$STAGE/superseded" ;;
  both)   mvto "${s1[1]:-}" "$SHOTDIR"; mvto "${s2[1]:-}" "$SHOTDIR" ;;
  *)      mvto "${s1[1]:-}" "$STAGE/review"; mvto "${s2[1]:-}" "$STAGE/review" ;;
esac

print "6) Everything else"
mvto CV-2026.docx "$HOME/Documents/Career"

print "\nStill in Downloads:"; ls -A "$DL"

if (( ! DRY_RUN )) && [[ -s $LOG ]]; then
  { print '#!/bin/zsh'; print '# undo.zsh: reverses moves.tsv, newest first. Mount the Vault first.'
    tail -r "$LOG" | while IFS=$'\t' read -r src dest; do      # tail -r = print lines in reverse
      print -r -- "mkdir -p ${(q)${src:h}} && mv -n ${(q)dest} ${(q)src} || echo 'could not restore:' ${(q)src}"
    done } > "$UNDO"
  print "\nMove log: $LOG\nUndo:     zsh $UNDO"
fi
```

**Undo:** run `zsh ~/Downloads-cleanup-20261112/undo.zsh`. After undoing, rename `moves.tsv` so a later run starts a fresh log. You can re-run `tidy.zsh` after changing decisions. Items already moved are reported as "not found" and skipped.

---

## Phase 4: Verify

Save as `~/cleanup-tools/verify.zsh` and run `zsh ~/cleanup-tools/verify.zsh ~/DownloadsAudit-<timestamp>`. Mount the Vault first.

```zsh
#!/bin/zsh
# verify.zsh: proves no unique content was lost. Hashes Downloads + every moved item (from the log).
set -u
AUD=${1:?usage: zsh verify.zsh ~/DownloadsAudit-YYYYMMDD-HHMMSS}
DL=$HOME/Downloads; LOG=$HOME/Downloads-cleanup-20261112/moves.tsv

{ print -r -- "$DL"; [[ -f $LOG ]] && cut -f2 "$LOG" } |
  while IFS= read -r p; do [[ -e $p ]] && find "$p" -type f ! -name .DS_Store -print0; done |
  xargs -0 shasum -a 256 | sort > "$AUD/manifest-after.sha256"

cut -c1-64 "$AUD/manifest-before.sha256" | sort -u > "$AUD/h-before"
cut -c1-64 "$AUD/manifest-after.sha256"  | sort -u > "$AUD/h-after"
missing=$(comm -23 "$AUD/h-before" "$AUD/h-after")      # comm -23 = lines only in the first file
if [[ -z $missing ]]; then print "PASS: every unique file content from before still exists"
else print "FAIL: content missing after cleanup:"
     print -r -- "$missing" | while read -r h; do grep "^$h" "$AUD/manifest-before.sha256"; done; fi
extra=$(comm -13 "$AUD/h-before" "$AUD/h-after")
[[ -n $extra ]] && print "NOTE: $(print -r -- "$extra" | wc -l | tr -d ' ') new contents appeared (new downloads or edited files?)"

b=$(wc -l < "$AUD/manifest-before.sha256" | tr -d ' '); a=$(wc -l < "$AUD/manifest-after.sha256" | tr -d ' ')
print "File count: before $b, after $a (Downloads + moved items). These should be EQUAL: only moves happened."
print "Disk use before: $(cut -f1 "$AUD/du-before.txt") KB"
print "Disk use after:  $(du -skc "$DL" ${(f)"$( [[ -f $LOG ]] && cut -f2 "$LOG")"} 2>/dev/null | tail -1 | cut -f1) KB (block rounding causes small differences)"

print "\nSpotlight can still find:"
for n in CV-2026 budget presentation-final Screenshot holiday-photos; do
  print "== $n"; mdfind -name "$n" | grep -v -e Downloads-BACKUP -e DownloadsAudit
done
[[ -d /Volumes/Vault ]] && mdutil -s /Volumes/Vault     # indexing status; enable with: sudo mdutil -i on /Volumes/Vault
```

**After Phase 4 passes:**

1. Launch Zoom, Docker and Figma once more.
2. Wait a cooling-off period, for example two weeks.
3. Drag `duplicates/`, `installers/`, `superseded/` and `to-delete/` from `~/Downloads-cleanup-20261112/` to the Trash.
4. Work through `review/` by hand.
5. Delete `~/Downloads-BACKUP-20261112` last.

---

## Phase 5: Stop it refilling

```zsh
mkdir -p ~/Pictures/Screenshots
defaults write com.apple.screencapture location ~/Pictures/Screenshots   # where screenshots are saved
killall SystemUIServer                                                    # applies the setting
```

You can also set this in the Cmd-Shift-5 toolbar under Options → Save to.

Then set up two or three rules in **Hazel**, or in **Folder Actions** (Finder → right-click Downloads → Services → Folder Actions Setup):

1. **Installers:** extension is `dmg` or `pkg`, and date added is more than 14 days ago → tag "Installer – check app". Trash after you've confirmed the app runs. Don't auto-delete outright, because an app check can't be automated reliably.
2. **PDFs:** kind is PDF and date added is more than 3 days ago → move to `~/Documents/Inbox-Review`. Do a weekly sweep, and move anything sensitive to the Vault.
3. **Re-downloads:** name matches `* (1).*` → colour-tag red so duplicates are visible immediately. Optionally run a Hazel shell-script condition with `cmp -s "$1" "${1/ (1)/}"` to flag proven duplicates.

Finally, add calendar reminders for the retention end dates in the table above, such as **31 Jan 2028** for the P60. That way deletion happens on schedule rather than never.
