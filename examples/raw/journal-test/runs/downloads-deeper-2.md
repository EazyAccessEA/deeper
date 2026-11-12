# downloads-deeper-2

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

# /deeper: Tidy my Downloads folder

**Deliverable:** one tidy `~/Downloads`. Every file is kept and filed, or removed with a reason. Nothing else.

### 1. What would a top professional do that you haven't asked for?
**Field:** records management, with a Mac sysadmin's caution.
- **Prove duplicates by content, never by name.** The "(1)" files aren't all copies. `budget (1).xlsx` is a different size and a month newer than `budget.xlsx`, so it's likely the real current version.
- **Sort by sensitivity and reversibility before sorting by type.** `passport-scan.jpg`, `P60-2025-26.pdf` and `tenancy-agreement.pdf` are identity and financial documents. They need a deliberate home, not a "Documents" pile. Nothing gets deleted outright. Removals go to the Trash and are listed, so you can undo them.

### 2. What is the rawest material?
The listing is a summary. The raw material is the files themselves:
- **Their bytes:** hashes.
- **Their provenance:** the `kMDItemWhereFroms` source URL and download date in Spotlight metadata.
- **The zip contents** against the `holiday-photos` folder.
- **Which apps are actually installed** in `/Applications`.

I haven't read anything on your disk yet. The only material is the `ls` you pasted. Missing: whether a Time Machine backup exists, and where you want personal documents to live.

**Assumptions the material could disprove:**
- "`tenancy-agreement.pdf.download` is junk." It's an unfinished Safari download, but it's larger and newer (20 Aug) than the finished PDF. It may be a revised agreement you never got in full and need to download again.
- "The `holiday-photos` folder is the unzipped zip." The two must be compared before either zip goes.
- `Zoom.pkg` is only 240 KB. It's probably a downloader stub, not the app.

### 3. Which methods and tools would they use?
All of these ship with macOS:
- `shasum -a 256` and `cmp` to prove duplicates.
- `mdls -name kMDItemWhereFroms` and `xattr -l` for provenance.
- `zipinfo`/`unzip -l` with `diff -r` against the extracted folder.
- `ls /Applications` and `mdfind "kMDItemCFBundleIdentifier == '…'"` to confirm Docker, Figma and Zoom are installed before their installers go.
- `tmutil latestbackup` to confirm a backup exists first.
- Moving to the Trash rather than `rm`.
- Optionally, for `.docx` and `.xlsx` files that differ, unzip both and diff `docProps/core.xml` (last-modified-by, revision number).

**Skills and agents:** I haven't checked which skills are installed (`~/.claude/skills`, `.agents/skills`) or which subagent types are available. I can list them, and with your OK run `npx skills find file-organization`. That command downloads and runs the skills CLI from npm, so I'll only run it if you say yes. A general-purpose subagent isn't needed for 24 files.

### 4. What, other than us, would show the result is right?
- **A hash audit, run before and after.** Pass: every unique SHA-256 present before is still present afterwards, either in its new location or in the Trash with an approved reason. Every removed file is either a proven byte-identical duplicate or an installer for an app confirmed installed. Fail: any unique content removed without your explicit OK, or any file whose fate isn't explained.
- **Your own sign-off** on the judgment calls: `budget (1)`, the presentations, the tenancy `.download`.
- **A backup check.** `tmutil latestbackup` returns a backup from before the changes. If it doesn't, stop and tell you.

### Rewritten prompt

```
Tidy my ~/Downloads folder on macOS (listing below). Act as a records manager:
prove, then propose, then act, and keep everything reversible.

1. Preflight: run `tmutil latestbackup`. If there's no recent backup, stop and tell me.
2. Evidence: for every file, record its SHA-256 (`shasum -a 256`) and its source
   URL (`mdls -name kMDItemWhereFroms`). Compare holiday-photos.zip,
   holiday-photos (1).zip and the holiday-photos/ folder using zipinfo + diff -r.
   Check that Docker, Figma and Zoom are installed (/Applications, mdfind)
   before treating their installers as removable. Check whether Zoom.pkg is
   only a stub.
3. Classify each file:
   - Byte-identical duplicate (hash match only, never name).
   - Installer for an installed app.
   - Distinct version (e.g. budget vs budget (1), presentation-final vs -v2;
     for Office files, diff docProps/core.xml).
   - Incomplete download (tenancy-agreement.pdf.download: compare it with the
     PDF and its source URL, and tell me if it looks like a newer document I
     should download again).
   - Sensitive (passport-scan, P60, tenancy, CV).
   - Keep.
4. Show me one table: file, hash prefix, class, proposed action, destination,
   reason. Ask me where sensitive and personal documents should go. Don't
   assume a location. Make no changes until I approve.
5. Act: move approved files to the agreed destinations. Move removals to the
   Trash, never rm. Leave Downloads empty or holding only what I said to keep.
6. Verify: re-hash everything (new locations + Trash) and confirm every
   original unique hash is still present and every removal matches an
   approved reason. Report pass/fail. Fail if any unique content left without
   my explicit OK.

Listing:
[paste the ls -l output]
```

Worth knowing, not in this task: the passport scan and P60 might be better kept in an encrypted disk image or a password manager's document vault. Also, a Folder Action or Hazel rule could keep Downloads tidy from now on. Both would leave you something new to maintain.

Shall I run it? Running it starts with the read-only preflight and evidence steps, then the proposal table for you to approve. I can also check the installed skills first.

## Extraction

last fenced block

## Call 2 prompt

Tidy my ~/Downloads folder on macOS (listing below). Act as a records manager:
prove, then propose, then act, and keep everything reversible.

1. Preflight: run `tmutil latestbackup`. If there's no recent backup, stop and tell me.
2. Evidence: for every file, record its SHA-256 (`shasum -a 256`) and its source
   URL (`mdls -name kMDItemWhereFroms`). Compare holiday-photos.zip,
   holiday-photos (1).zip and the holiday-photos/ folder using zipinfo + diff -r.
   Check that Docker, Figma and Zoom are installed (/Applications, mdfind)
   before treating their installers as removable. Check whether Zoom.pkg is
   only a stub.
3. Classify each file:
   - Byte-identical duplicate (hash match only, never name).
   - Installer for an installed app.
   - Distinct version (e.g. budget vs budget (1), presentation-final vs -v2;
     for Office files, diff docProps/core.xml).
   - Incomplete download (tenancy-agreement.pdf.download: compare it with the
     PDF and its source URL, and tell me if it looks like a newer document I
     should download again).
   - Sensitive (passport-scan, P60, tenancy, CV).
   - Keep.
4. Show me one table: file, hash prefix, class, proposed action, destination,
   reason. Ask me where sensitive and personal documents should go. Don't
   assume a location. Make no changes until I approve.
5. Act: move approved files to the agreed destinations. Move removals to the
   Trash, never rm. Leave Downloads empty or holding only what I said to keep.
6. Verify: re-hash everything (new locations + Trash) and confirm every
   original unique hash is still present and every removal matches an
   approved reason. Report pass/fail. Fail if any unique content left without
   my explicit OK.

Listing:
[paste the ls -l output]

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

# Downloads tidy-up: evidence plan and provisional classification (no changes made)

**I could not run anything.** This session has no shell access, so I could not run `tmutil`, `shasum`, `mdls`, `zipinfo` or `diff`. Without those results I can't prove anything, and I won't invent hashes.

Below are:

1. The preflight and evidence script, ready for you to run.
2. A provisional table based only on your listing. Every row is marked as unproven.
3. The questions I need answered before anything moves.
4. The act and verify scripts. These only run after you approve.

Nothing in `~/Downloads` has been touched.

## Assumptions

- **Recent backup** means a completed Time Machine backup in the last 7 days. If there isn't one, the script stops.
- **Duplicates** are decided by matching SHA-256 only. Same size or a ` (1)` suffix is only a reason to check.
- **Removals go to the Trash through Finder**, so you can use **Put Back** to restore them. Nothing is ever deleted with `rm`. If your Trash auto-empties after 30 days (Finder › Settings › Advanced), files there can't be restored after that, so turn it off until you're satisfied.
- **Downloaded content is untrusted.** Zips are extracted only into new, empty scratch folders.

## Step 1–2: Preflight and evidence script

Save this as `/private/tmp/claude-501/-private-var-folders-d0-zg5gq25n0x3cz1b6ndmxc3nc0000gn-T-tmpz-k0ec38/a394e1c1-4edc-4f2d-830a-09eb835455fc/scratchpad/evidence.zsh` and run `zsh <that path>`. It only reads `~/Downloads`. Everything it writes goes to the scratchpad.

```zsh
#!/bin/zsh
set -u
S=/private/tmp/claude-501/-private-var-folders-d0-zg5gq25n0x3cz1b6ndmxc3nc0000gn-T-tmpz-k0ec38/a394e1c1-4edc-4f2d-830a-09eb835455fc/scratchpad
D=$HOME/Downloads
OUT=$S/evidence.txt; MAN=$S/manifest.tsv
: > $OUT

# ---------- 1. PREFLIGHT ----------
B=$(tmutil latestbackup 2>&1)
echo "latestbackup: $B" | tee -a $OUT
TS=${${B:t}%.backup}
EPOCH=$(date -j -f "%Y-%m-%d-%H%M%S" "$TS" +%s 2>/dev/null)
if [[ -z "$EPOCH" ]] || (( $(date +%s) - EPOCH > 7*86400 )); then
  echo "STOP: no Time Machine backup in the last 7 days." | tee -a $OUT; exit 1
fi

# ---------- 2a. MANIFEST: hash + source URL for every file (incl. folder & bundle contents) ----------
print -r -- $'sha256\tbytes\tpath\twherefroms' > $MAN
find "$D" -type f -print0 | while IFS= read -r -d '' f; do
  h=$(shasum -a 256 "$f" | cut -d' ' -f1)
  s=$(stat -f %z "$f")
  w=$(mdls -raw -name kMDItemWhereFroms "$f" 2>/dev/null | tr -d '\n' | tr -s ' ')
  print -r -- "$h\t$s\t$f\t$w" >> $MAN
done
echo "== duplicate hashes ==" >> $OUT
cut -f1 $MAN | sort | uniq -d | while read h; do grep "^$h" $MAN; echo; done >> $OUT

# ---------- 2b. holiday-photos: zip vs zip vs folder ----------
for z in "holiday-photos.zip" "holiday-photos (1).zip"; do
  echo "== zipinfo $z ==" >> $OUT; zipinfo "$D/$z" >> $OUT 2>&1
done
mkdir -p $S/zipA $S/zipB   # fresh, isolated extraction dirs
unzip -q "$D/holiday-photos.zip"     -d $S/zipA
unzip -q "$D/holiday-photos (1).zip" -d $S/zipB
A=$S/zipA; [[ -d $S/zipA/holiday-photos ]] && A=$S/zipA/holiday-photos
echo "== diff -r zipA vs zipB ==" >> $OUT;   diff -r $S/zipA $S/zipB >> $OUT 2>&1 && echo IDENTICAL >> $OUT
echo "== diff -r zip vs folder ==" >> $OUT;  diff -r -x __MACOSX -x .DS_Store "$A" "$D/holiday-photos" >> $OUT 2>&1 && echo IDENTICAL >> $OUT

# ---------- 2c. Are the apps installed? ----------
for pair in "Docker:com.docker.docker" "Figma:com.figma.Desktop" "zoom.us:us.zoom.xos"; do
  app=${pair%%:*}; bid=${pair#*:}
  echo "== $app ==" >> $OUT
  ls -d "/Applications/$app.app" >> $OUT 2>&1
  mdfind "kMDItemCFBundleIdentifier == '$bid'" >> $OUT
  [[ -d "/Applications/$app.app" ]] && defaults read "/Applications/$app.app/Contents/Info" CFBundleShortVersionString >> $OUT 2>&1
done

# ---------- 2d. Is Zoom.pkg a stub? ----------
echo "== Zoom.pkg ==" >> $OUT
pkgutil --check-signature "$D/Zoom.pkg" >> $OUT 2>&1
pkgutil --payload-files "$D/Zoom.pkg" 2>/dev/null | wc -l | xargs echo "payload file count:" >> $OUT
mkdir -p $S/zoompkg && pkgutil --expand "$D/Zoom.pkg" $S/zoompkg/x >> $OUT 2>&1
du -sh $S/zoompkg/x >> $OUT; ls -R $S/zoompkg/x | head -50 >> $OUT

# ---------- 2e. Office/Keynote version metadata ----------
for f in "budget.xlsx" "budget (1).xlsx" "CV-2026.docx" "CV-2026 (1).docx"; do
  echo "== core.xml: $f ==" >> $OUT
  unzip -p "$D/$f" docProps/core.xml > "$S/core-${f//[ ()]/_}.xml" 2>>$OUT
  cat "$S/core-${f//[ ()]/_}.xml" >> $OUT; echo >> $OUT
done
diff $S/core-budget.xlsx.xml $S/core-budget__1_.xlsx.xml >> $OUT 2>&1
for k in presentation-final.key presentation-final-v2.key; do
  echo "== $k ==" >> $OUT; ls -ld "$D/$k" >> $OUT
  [[ -f "$D/$k" ]] && unzip -l "$D/$k" >> $OUT 2>&1    # single-file Keynote = zip
done

# ---------- 2f. Incomplete tenancy download ----------
T="$D/tenancy-agreement.pdf.download"
echo "== tenancy ==" >> $OUT
ls -ld "$T" "$D/tenancy-agreement.pdf" >> $OUT
mdls -name kMDItemWhereFroms -name kMDItemContentCreationDate "$D/tenancy-agreement.pdf" "$T" >> $OUT
if [[ -d "$T" ]]; then ls -la "$T" >> $OUT; plutil -p "$T/Info.plist" >> $OUT 2>&1
else head -c 8 "$T" | xxd >> $OUT; tail -c 64 "$T" | strings >> $OUT; fi   # %PDF header? %%EOF trailer?
echo "Done. Evidence: $OUT  Manifest: $MAN"
```

Then send me `evidence.txt` and `manifest.tsv` from that scratchpad folder.

## Step 3–4: Provisional classification

These rows are hypotheses from your listing, not proof. **Every hash prefix is pending.**

| File | Hash | Class (hypothesis) | Proposed action | Destination | Reason / what must be proven |
|---|---|---|---|---|---|
| Zoom.pkg | pending | Installer, likely **stub** | Trash | Trash | At 245,760 B it is far too small to be the full Zoom installer (which is typically more than 100 MB). Confirm with the payload count and the expanded size. Only trash it if zoom.us.app is installed. |
| Docker.dmg | pending | Installer for installed app | Trash | Trash | Only if Docker.app is present. |
| Docker (1).dmg | pending | Byte-identical dupe (same size) | Trash | Trash | Only if the hash matches Docker.dmg. If it differs, treat it as a different version. |
| Figma-arm64.dmg | pending | Installer for installed app | Trash | Trash | Only if Figma.app is present. |
| Invoice-0412.pdf | pending | Keep (financial) | Move | **ask you** | |
| Invoice-0412 (1).pdf | pending | Byte-identical dupe (same size) | Trash | Trash | Only if the hash matches. |
| Invoice-0517.pdf | pending | Keep (financial) | Move | **ask you** | |
| P60-2025-26.pdf | pending | **Sensitive** (tax) | Move | **ask you** | |
| Screenshot …10.02.11.png | pending | Keep | Move | **ask you** | Sizes differ, so these two are not duplicates. |
| Screenshot …10.02.40.png | pending | Keep | Move | **ask you** | |
| Screenshot …16.45.03.png | pending | Keep | Move | **ask you** | |
| passport-scan.jpg | pending | **Sensitive** (identity) | Move | **ask you** | |
| tenancy-agreement.pdf | pending | **Sensitive** | Move | **ask you** | |
| tenancy-agreement.pdf.download | pending | **Incomplete download** | Trash *after* re-download decision | Trash | See the note below the table. |
| holiday-photos/ | pending (per file) | Keep (personal) | Move | **ask you** | This is the canonical copy. |
| holiday-photos.zip | pending | Redundant archive | Trash | Trash | Only if `diff -r` between the zip contents and the folder is clean. |
| holiday-photos (1).zip | pending | Byte-identical dupe (same size) | Trash | Trash | Only if the hash matches holiday-photos.zip. |
| budget.xlsx | pending | Distinct version (older) | Keep both (default) | **ask you** | Sizes and dates differ. core.xml will show the author, modified date and revision. |
| budget (1).xlsx | pending | Distinct version (newer) | Keep, maybe rename to `budget-2026-09-02.xlsx` | **ask you** | |
| boarding-pass-LHR-LIS.pdf | pending | Personal (booking reference, barcode) | Move | **ask you** | |
| presentation-final.key | pending | Distinct version | Keep both (default) | **ask you** | -v2 is newer and larger, but I won't discard v1 without your OK. |
| presentation-final-v2.key | pending | Distinct version (newer) | Keep | **ask you** | |
| CV-2026.docx | pending | **Sensitive** (CV) | Move | **ask you** | |
| CV-2026 (1).docx | pending | Byte-identical dupe (same size) | Trash | Trash | Only if the hash matches. If not, use core.xml to tell the versions apart. |

**About the tenancy download.** The partial file is dated 20 Aug, which is later than the PDF (11 Jul). It is also larger than the complete PDF (61,733 B vs 54,210 B). A partial download that is already bigger than the finished file is very unlikely to be the same document. **It probably is a newer or amended agreement, and I'd recommend downloading it again** from its `kMDItemWhereFroms` URL, or from the `DownloadEntryURL` if it is a Safari bundle. The evidence script checks whether the URL matches the PDF's URL, and whether the file has a `%PDF` header or an `%%EOF` trailer. Please don't open the partial file as if it were the agreement. I'll trash it only after you've downloaded the new copy or told me it isn't needed.

## Questions I need answered before acting

1. **Sensitive files** (passport, P60, tenancy, CV): where should they go? For example, an encrypted disk image, a specific folder, or a password manager. Should they be kept out of iCloud sync?
2. **Financial files** (invoices, budgets): where should they go?
3. **Personal files** (holiday-photos, screenshots, boarding pass): where should they go? Is the boarding pass for a past trip that can be trashed?
4. **Version pairs** (budget and presentation): keep both, or trash the older one of each?
5. **Tenancy agreement**: will you download it again?
6. **Anything that should stay** in Downloads?

## Step 5: Act script (template, only after approval)

I'll fill in `MOVES` and `TRASH` from your answers and the proven evidence. Moves never overwrite an existing file. Removals go through Finder so **Put Back** works.

```zsh
#!/bin/zsh
set -eu
D=$HOME/Downloads
typeset -A MOVES=(  # "source" "destination dir" — filled after approval
)
TRASH=(             # filled after approval, each tied to a proven reason
)
for src dst in ${(kv)MOVES}; do mkdir -p "$dst"; mv -n "$D/$src" "$dst/"; [[ -e "$D/$src" ]] && echo "NOT MOVED (name clash): $src"; done
for f in $TRASH; do osascript -e "tell application \"Finder\" to delete (POSIX file \"$D/$f\" as alias)" >/dev/null; done
ls -la "$D"
```

## Step 6: Verify script

This checks that every unique hash in the original manifest is still present, either in its new location or in the Trash.

```zsh
#!/bin/zsh
S=/private/tmp/claude-501/-private-var-folders-d0-zg5gq25n0x3cz1b6ndmxc3nc0000gn-T-tmpz-k0ec38/a394e1c1-4edc-4f2d-830a-09eb835455fc/scratchpad
DESTS=( "$HOME/.Trash" "$HOME/Downloads" )   # + approved destination dirs
find $DESTS -type f -print0 | xargs -0 shasum -a 256 | cut -d' ' -f1 | sort -u > $S/after.txt
tail -n +2 $S/manifest.tsv | cut -f1 | sort -u > $S/before.txt
MISSING=$(comm -23 $S/before.txt $S/after.txt)
if [[ -z "$MISSING" ]]; then echo "PASS: all $(wc -l < $S/before.txt | xargs) unique hashes present"
else echo "FAIL: missing hashes:"; for h in ${(f)MISSING}; do grep "^$h" $S/manifest.tsv; done; fi
```

The verify step will also compare each item in the Trash with the approved reason for removing it. It fails if any unique content was removed without your explicit OK.

Next step: run the evidence script, send me `evidence.txt` and `manifest.tsv`, and answer the six questions. I'll then replace the "pending" rows with proven hashes and classes and hand you the final act list to approve.
