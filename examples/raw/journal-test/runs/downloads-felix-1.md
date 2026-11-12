# downloads-felix-1

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

The difference between "tidy" and what a professional would do is that a professional doesn't sort by filename. They establish what each file *is*, where it came from, and whether it is safe to remove. They make every action reversible and checkable, and they fix whatever keeps refilling the folder.

## 1. What a top professional would do that you're not asking for

- **Prove duplicates instead of assuming them.** Matching size and a ` (1)` suffix are hints, not proof. `Docker.dmg` and `Docker (1).dmg` are probably identical. `budget.xlsx` and `budget (1).xlsx` differ in size, so they are two *versions*, and deleting one could lose work. The same applies to `presentation-final.key` vs `-v2.key`.
- **Treat installers as disposable only once their job is done.** Delete `Docker.dmg`, `Figma-arm64.dmg` and `Zoom.pkg` only after confirming each app is installed in `/Applications`, so the file can be re-downloaded if needed. (`Zoom.pkg` at 245 KB is a stub installer anyway.)
- **Resolve broken or half-finished states.**
  - `tenancy-agreement.pdf.download` is a Safari partial download, dated *after* the complete PDF. It is most likely a failed re-download.
  - `holiday-photos/` sits next to two copies of the zip it was extracted from. Verify the extraction is complete before deleting either zip.
- **Handle sensitive documents differently.** These are identity, tax, legal and financial records that shouldn't live in Downloads:
  - `passport-scan.jpg`
  - `P60-2025-26.pdf`
  - `tenancy-agreement.pdf`
  - invoices
  - boarding pass
  - CV

  Each needs a deliberate home, a retention decision (a P60 is worth keeping; a used boarding pass usually isn't), and possibly encryption.
- **Fix the root causes, not just the symptoms.**
  - macOS saves screenshots to the Desktop by default, so someone changed that setting to Downloads.
  - The ` (1)` files come from re-downloading things you already had.
- **Make it reversible.** Move files to the Trash rather than `rm`, after confirming a Time Machine backup exists, and keep a written manifest of every action.

## 2. The rawest material to start from

`ls -l` is already digested: it shows names, sizes and dates, which are the least reliable signals. The raw material is:

- **File contents**: cryptographic hashes of every file.
- **Origin metadata** macOS records on each download:
  - `kMDItemWhereFroms` (source URL and referrer)
  - the `com.apple.quarantine` extended attribute (which app downloaded it, and when)
- **Usage metadata**: `kMDItemLastUsedDate` and `kMDItemUseCount`, which show whether you ever opened a file.
- **Archive manifests**: the zip's internal file list and CRCs, compared against the extracted folder's actual contents.
- **The installed apps**: each app's `Info.plist` version in `/Applications`, compared with the installer's version.
- **The document internals**: the two budget spreadsheets' actual cell differences and the two Keynote decks' modification history, not their filenames.
- **Your existing filing system**: the real folder structure in `~/Documents` (or iCloud Drive), so files go where you'd actually look for them.

## 3. Methods and tools

| Purpose | Tool |
|---|---|
| Content identity | `shasum -a 256` on every file; group by hash |
| Origin and usage | `mdls -name kMDItemWhereFroms -name kMDItemLastUsedDate`, `xattr -l` |
| Archive vs folder | `unzip -l`, `unzip -t` (integrity), then extract to a temp dir and `diff -r` against `holiday-photos/` |
| Installer vs installed app | `hdiutil attach -nobrowse -readonly` plus `defaults read …/Info.plist CFBundleShortVersionString`; `pkgutil --payload-files`/`--pkg-info` for `.pkg` |
| Version comparison | Export both budgets to CSV and diff them; compare Keynote modification dates and slide counts |
| Dry run | Generate a manifest (CSV: path, hash, origin, proposed action, destination, reason) and review it *before* anything moves |
| Safe execution | Move to `~/.Trash` (or `trash` via Homebrew), never `rm`; confirm `tmutil latestbackup` first |
| Sensitive files | Move to a dedicated folder or an encrypted APFS disk image (`hdiutil create -encryption AES-256`); check whether Downloads is included in iCloud/Time Machine |
| Prevention | `defaults write com.apple.screencapture location ~/Pictures/Screenshots`; browser "ask where to save"; a Folder Action, Hazel rule or `launchd` job that flags Downloads items older than N days |

## 4. What, other than you or me, would show the result is right

- **A hash ledger.** Every file's SHA-256 before the cleanup must appear afterwards either at its new destination with the same hash, or in the Trash. Every hash group marked "duplicate" must have exactly one surviving copy. This is mechanical, not a judgment.
- **A count reconciliation.** 24 entries in must equal kept + moved + trashed, with zero unaccounted for.
- **The apps themselves.** Docker, Figma and Zoom launch and report the same or newer versions than the installers being deleted.
- **The archive tool.** `unzip -t` passes, and `diff -r` between a fresh extraction and `holiday-photos/` prints nothing.
- **The files open.** `pdfinfo` or `qlmanage -p` succeeds on every kept PDF and image, which catches corrupt or partial files.
- **The OS.** Spotlight (`mdfind`) still finds each moved document. A new screenshot lands in the new location. Downloads stays clean a month later, which shows the root cause was fixed.
- **Time Machine.** A backup completed before the run, so any mistake is recoverable.

---

## Rewritten prompt

> I'm on macOS. Help me clean up `~/Downloads` (listing below) **rigorously and reversibly**, and stop it from getting messy again. Don't rely on filenames, sizes or dates to decide anything. Base decisions on file contents and macOS metadata.
>
> **Phase 1: Investigate (read-only; change nothing).** Give me a single zsh script that writes its output to a report file and:
> 1. Computes `shasum -a 256` for every file and groups identical content.
> 2. Records `kMDItemWhereFroms`, `kMDItemLastUsedDate`, `kMDItemUseCount` (via `mdls`) and the `com.apple.quarantine` attribute for each file.
> 3. For each `.dmg`/`.pkg`, reads the installer's version (mount with `hdiutil attach -nobrowse -readonly`, or use `pkgutil`) and compares it with the installed app's `CFBundleShortVersionString` in `/Applications`.
> 4. Runs `unzip -t` on both holiday-photos zips and compares a fresh extraction against the existing `holiday-photos/` folder with `diff -r`.
> 5. Inspects `tenancy-agreement.pdf.download` and says whether it's an incomplete Safari download and how it relates to the complete PDF.
> 6. Shows what actually differs between `budget.xlsx` and `budget (1).xlsx`, and between the two Keynote files, so I can decide whether they're versions worth keeping.
> 7. Checks `tmutil latestbackup` and whether Downloads is covered by Time Machine or iCloud.
>
> **Phase 2: Proposed plan (still no changes).** From that report, produce a manifest table with these columns: file, SHA-256, origin, proposed action (keep / move / trash / ask me), destination, and reason. Rules for the plan:
> - Only call something a duplicate if hashes match.
> - Only trash an installer if the installed app is the same or a newer version.
> - Never trash a differing version without asking me.
> - Treat `passport-scan.jpg`, `P60-2025-26.pdf`, the tenancy agreement, invoices, boarding pass and CV as sensitive. Propose where each should live and how long to keep it (e.g. tax records vs a used boarding pass), and offer an encrypted APFS disk image as an option.
> - Propose destinations that fit a sensible `~/Documents` structure, and ask me about my existing folders if needed.
>
> **Phase 3: Execute.** Once I approve the manifest, give me a script that refuses to run unless a recent Time Machine backup exists. It must move files to the Trash rather than `rm` them, and it must log every action.
>
> **Phase 4: Verify independently.** Give me a verification script that:
> - re-hashes everything and confirms every original hash is either at its destination or in the Trash
> - checks that the counts reconcile (24 in = kept + moved + trashed)
> - confirms each surviving duplicate group has exactly one copy
> - runs `pdfinfo` / `qlmanage` on each kept document
> - confirms `mdfind` locates each moved file
>
> **Phase 5: Prevent recurrence.**
> - Move screenshots out of Downloads (`defaults write com.apple.screencapture location …`) and explain how this setting likely got changed.
> - Suggest browser settings that stop ` (1)` re-downloads.
> - Set up a lightweight rule (Folder Action, `launchd` job or Hazel) that flags anything in Downloads older than 30 days.
>
> Use only built-in macOS tools unless you say why something else is worth installing. Explain any judgment call in one line.
>
> *[paste `ls -l` output here]*

## Extraction

whole reply

## Call 2 prompt

The difference between "tidy" and what a professional would do is that a professional doesn't sort by filename. They establish what each file *is*, where it came from, and whether it is safe to remove. They make every action reversible and checkable, and they fix whatever keeps refilling the folder.

## 1. What a top professional would do that you're not asking for

- **Prove duplicates instead of assuming them.** Matching size and a ` (1)` suffix are hints, not proof. `Docker.dmg` and `Docker (1).dmg` are probably identical. `budget.xlsx` and `budget (1).xlsx` differ in size, so they are two *versions*, and deleting one could lose work. The same applies to `presentation-final.key` vs `-v2.key`.
- **Treat installers as disposable only once their job is done.** Delete `Docker.dmg`, `Figma-arm64.dmg` and `Zoom.pkg` only after confirming each app is installed in `/Applications`, so the file can be re-downloaded if needed. (`Zoom.pkg` at 245 KB is a stub installer anyway.)
- **Resolve broken or half-finished states.**
  - `tenancy-agreement.pdf.download` is a Safari partial download, dated *after* the complete PDF. It is most likely a failed re-download.
  - `holiday-photos/` sits next to two copies of the zip it was extracted from. Verify the extraction is complete before deleting either zip.
- **Handle sensitive documents differently.** These are identity, tax, legal and financial records that shouldn't live in Downloads:
  - `passport-scan.jpg`
  - `P60-2025-26.pdf`
  - `tenancy-agreement.pdf`
  - invoices
  - boarding pass
  - CV

  Each needs a deliberate home, a retention decision (a P60 is worth keeping; a used boarding pass usually isn't), and possibly encryption.
- **Fix the root causes, not just the symptoms.**
  - macOS saves screenshots to the Desktop by default, so someone changed that setting to Downloads.
  - The ` (1)` files come from re-downloading things you already had.
- **Make it reversible.** Move files to the Trash rather than `rm`, after confirming a Time Machine backup exists, and keep a written manifest of every action.

## 2. The rawest material to start from

`ls -l` is already digested: it shows names, sizes and dates, which are the least reliable signals. The raw material is:

- **File contents**: cryptographic hashes of every file.
- **Origin metadata** macOS records on each download:
  - `kMDItemWhereFroms` (source URL and referrer)
  - the `com.apple.quarantine` extended attribute (which app downloaded it, and when)
- **Usage metadata**: `kMDItemLastUsedDate` and `kMDItemUseCount`, which show whether you ever opened a file.
- **Archive manifests**: the zip's internal file list and CRCs, compared against the extracted folder's actual contents.
- **The installed apps**: each app's `Info.plist` version in `/Applications`, compared with the installer's version.
- **The document internals**: the two budget spreadsheets' actual cell differences and the two Keynote decks' modification history, not their filenames.
- **Your existing filing system**: the real folder structure in `~/Documents` (or iCloud Drive), so files go where you'd actually look for them.

## 3. Methods and tools

| Purpose | Tool |
|---|---|
| Content identity | `shasum -a 256` on every file; group by hash |
| Origin and usage | `mdls -name kMDItemWhereFroms -name kMDItemLastUsedDate`, `xattr -l` |
| Archive vs folder | `unzip -l`, `unzip -t` (integrity), then extract to a temp dir and `diff -r` against `holiday-photos/` |
| Installer vs installed app | `hdiutil attach -nobrowse -readonly` plus `defaults read …/Info.plist CFBundleShortVersionString`; `pkgutil --payload-files`/`--pkg-info` for `.pkg` |
| Version comparison | Export both budgets to CSV and diff them; compare Keynote modification dates and slide counts |
| Dry run | Generate a manifest (CSV: path, hash, origin, proposed action, destination, reason) and review it *before* anything moves |
| Safe execution | Move to `~/.Trash` (or `trash` via Homebrew), never `rm`; confirm `tmutil latestbackup` first |
| Sensitive files | Move to a dedicated folder or an encrypted APFS disk image (`hdiutil create -encryption AES-256`); check whether Downloads is included in iCloud/Time Machine |
| Prevention | `defaults write com.apple.screencapture location ~/Pictures/Screenshots`; browser "ask where to save"; a Folder Action, Hazel rule or `launchd` job that flags Downloads items older than N days |

## 4. What, other than you or me, would show the result is right

- **A hash ledger.** Every file's SHA-256 before the cleanup must appear afterwards either at its new destination with the same hash, or in the Trash. Every hash group marked "duplicate" must have exactly one surviving copy. This is mechanical, not a judgment.
- **A count reconciliation.** 24 entries in must equal kept + moved + trashed, with zero unaccounted for.
- **The apps themselves.** Docker, Figma and Zoom launch and report the same or newer versions than the installers being deleted.
- **The archive tool.** `unzip -t` passes, and `diff -r` between a fresh extraction and `holiday-photos/` prints nothing.
- **The files open.** `pdfinfo` or `qlmanage -p` succeeds on every kept PDF and image, which catches corrupt or partial files.
- **The OS.** Spotlight (`mdfind`) still finds each moved document. A new screenshot lands in the new location. Downloads stays clean a month later, which shows the root cause was fixed.
- **Time Machine.** A backup completed before the run, so any mistake is recoverable.

---

## Rewritten prompt

> I'm on macOS. Help me clean up `~/Downloads` (listing below) **rigorously and reversibly**, and stop it from getting messy again. Don't rely on filenames, sizes or dates to decide anything. Base decisions on file contents and macOS metadata.
>
> **Phase 1: Investigate (read-only; change nothing).** Give me a single zsh script that writes its output to a report file and:
> 1. Computes `shasum -a 256` for every file and groups identical content.
> 2. Records `kMDItemWhereFroms`, `kMDItemLastUsedDate`, `kMDItemUseCount` (via `mdls`) and the `com.apple.quarantine` attribute for each file.
> 3. For each `.dmg`/`.pkg`, reads the installer's version (mount with `hdiutil attach -nobrowse -readonly`, or use `pkgutil`) and compares it with the installed app's `CFBundleShortVersionString` in `/Applications`.
> 4. Runs `unzip -t` on both holiday-photos zips and compares a fresh extraction against the existing `holiday-photos/` folder with `diff -r`.
> 5. Inspects `tenancy-agreement.pdf.download` and says whether it's an incomplete Safari download and how it relates to the complete PDF.
> 6. Shows what actually differs between `budget.xlsx` and `budget (1).xlsx`, and between the two Keynote files, so I can decide whether they're versions worth keeping.
> 7. Checks `tmutil latestbackup` and whether Downloads is covered by Time Machine or iCloud.
>
> **Phase 2: Proposed plan (still no changes).** From that report, produce a manifest table with these columns: file, SHA-256, origin, proposed action (keep / move / trash / ask me), destination, and reason. Rules for the plan:
> - Only call something a duplicate if hashes match.
> - Only trash an installer if the installed app is the same or a newer version.
> - Never trash a differing version without asking me.
> - Treat `passport-scan.jpg`, `P60-2025-26.pdf`, the tenancy agreement, invoices, boarding pass and CV as sensitive. Propose where each should live and how long to keep it (e.g. tax records vs a used boarding pass), and offer an encrypted APFS disk image as an option.
> - Propose destinations that fit a sensible `~/Documents` structure, and ask me about my existing folders if needed.
>
> **Phase 3: Execute.** Once I approve the manifest, give me a script that refuses to run unless a recent Time Machine backup exists. It must move files to the Trash rather than `rm` them, and it must log every action.
>
> **Phase 4: Verify independently.** Give me a verification script that:
> - re-hashes everything and confirms every original hash is either at its destination or in the Trash
> - checks that the counts reconcile (24 in = kept + moved + trashed)
> - confirms each surviving duplicate group has exactly one copy
> - runs `pdfinfo` / `qlmanage` on each kept document
> - confirms `mdfind` locates each moved file
>
> **Phase 5: Prevent recurrence.**
> - Move screenshots out of Downloads (`defaults write com.apple.screencapture location …`) and explain how this setting likely got changed.
> - Suggest browser settings that stop ` (1)` re-downloads.
> - Set up a lightweight rule (Folder Action, `launchd` job or Hazel) that flags anything in Downloads older than 30 days.
>
> Use only built-in macOS tools unless you say why something else is worth installing. Explain any judgment call in one line.
>
> *[paste `ls -l` output here]*

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

# Downloads clean-up: investigation, plan, execution, verification and prevention

I haven't run anything on your Mac. Below are five scripts and a manifest, written for stock macOS 26 tools and not tested against your files. Phase 1 is read-only, so it is safe to run first. If any command fails there, the error goes into the report, and nothing gets touched.

## Assumptions

1. **You're in the UK** (P60, LHR), so retention advice follows HMRC and English law.
2. **The invoices are ones you received personally**, not ones your business issued. If they are business records, keep them for 6 years.
3. **The apps are installed as** `/Applications/Docker.app`, `Figma.app` and `zoom.us.app`.
4. **I don't know your `~/Documents` structure.** I've proposed one; edit the destination column to match yours.
5. **The LHR→LIS trip is over.** Boarding passes are issued no more than about 48 hours before departure, and this one arrived on 20 Sep. You don't need it for an expense claim.
6. **Terminal permissions:**
   - Terminal has **Full Disk Access** (System Settings › Privacy & Security). This is needed for `tmutil` and `~/.Trash`.
   - You'll allow **Automation › Finder** when prompted. Files go to the Trash through Finder, so **Put Back** works.
7. **`pdfinfo` isn't built in**, so I use PDFKit via `osascript -l JavaScript` instead. This needs no installs.

## What the listing already suggests (each point needs proof)

- **Four pairs are probably byte-identical** (same size): Docker, Invoice-0412, holiday-photos zip, CV. Only their hashes can confirm this.
- **Three pairs are different versions:** budget, the Keynote decks, and the tenancy agreement.
- **`tenancy-agreement.pdf.download` is odd.** Safari normally creates `.download` as a *bundle directory*, but `ls` shows a regular file. It is also **larger and five weeks newer** than the PDF, so it could be a newer copy, such as a countersigned one, that never got renamed. I'm not assuming it's a failed download; it's marked "ask".
- **Two browsers may be involved.** The ` (1)` naming is Chrome/Edge-style, while `.download` is Safari's format. The quarantine "agent" field in the report will confirm this.
- **The two screenshots taken 29 s apart are probably a retake.**

## How to run

```zsh
mkdir -p ~/DownloadsCleanup/bin        # scripts live here, never in Downloads
# save each script below into ~/DownloadsCleanup/bin/, then:
zsh ~/DownloadsCleanup/bin/phase1-investigate.zsh      # read-only → ~/DownloadsCleanup/latest/report.txt
# read the report, edit ~/DownloadsCleanup/manifest.txt
zsh ~/DownloadsCleanup/bin/phase3-execute.zsh
zsh ~/DownloadsCleanup/bin/phase4-verify.zsh
zsh ~/DownloadsCleanup/bin/phase5-prevent.zsh
```

---

## Phase 1: Investigate (read-only)

`~/DownloadsCleanup/bin/phase1-investigate.zsh`

```zsh
#!/bin/zsh
# READ-ONLY. Never writes inside ~/Downloads. Output: ~/DownloadsCleanup/run-<ts>/ (symlinked as "latest")
emulate zsh
setopt pipe_fail extended_glob
autoload -Uz is-at-least

DL=${${1:-$HOME/Downloads}:A}
RUN=$HOME/DownloadsCleanup/run-$(date +%Y%m%d-%H%M%S)
mkdir -p $RUN/previews && ln -sfn $RUN $HOME/DownloadsCleanup/latest
print -r -- $DL > $RUN/downloads-root.txt
WORK=$(mktemp -d "${TMPDIR:-/tmp}/dlclean.XXXXXX")     # scratch for mounts/extractions (untrusted data)
typeset -a MOUNTS
cleanup() {
  local m; for m in $MOUNTS; do hdiutil detach -quiet "$m" 2>/dev/null || hdiutil detach -force -quiet "$m"; done
  mount | grep -qF "$WORK" || rm -rf -- "$WORK"
}
trap cleanup EXIT
exec > >(tee $RUN/report.txt) 2>&1

sec()    { print "\n==================== $* ====================" }
hashof() { awk -F'\t' -v p="$1" '$3==p {print $1}' $RUN/ledger.tsv }
pdf_js='function run(a){ObjC.import("PDFKit");var d=$.PDFDocument.alloc.initWithURL($.NSURL.fileURLWithPath(a[0]));if(d.isNil())return "UNREADABLE";return a[1]=="text"?(ObjC.unwrap(d.string)||""):"pages="+d.pageCount}'
pdfpages() { osascript -l JavaScript -e $pdf_js "$1" pages </dev/null 2>&1 }
pdftext()  { osascript -l JavaScript -e $pdf_js "$1" text  </dev/null 2>/dev/null }

sec "0. Environment & safety net"
sw_vers; date; print "Downloads: $DL"
print -n "Latest Time Machine backup: "; tmutil latestbackup 2>&1 || print "(none, or Terminal lacks Full Disk Access)"
print -n "Downloads in Time Machine? "; tmutil isexcluded "$DL" 2>&1
print -n "Screenshot location setting: "; defaults read com.apple.screencapture location 2>/dev/null || print "(unset = Desktop, the macOS default)"
if [[ -d "$HOME/Library/Mobile Documents/com~apple~CloudDocs/Documents" ]]; then
  print "iCloud Desktop & Documents: probably ON (heuristic)"; else print "iCloud Desktop & Documents: probably OFF (heuristic)"; fi
print "Note: ~/Downloads is never synced by iCloud Desktop & Documents."

sec "1. Inventory"
TOP=( $DL/^(.DS_Store|.localized)(DN) )
print -rl -- ${TOP:t} > $RUN/toplevel.txt
print "Top-level entries: ${#TOP}  (your listing: 24)"
ls -la@ "$DL"

sec "2. Content hashes  → ledger.tsv (sha256, bytes, path)"
: > $RUN/ledger.tsv
find "$DL" -type f ! -name .DS_Store ! -path "$DL/.localized" -print0 |
while IFS= read -r -d '' f; do
  print -r -- "$(shasum -a 256 "$f" | cut -d' ' -f1)"$'\t'"$(stat -f %z "$f")"$'\t'"${f#$DL/}" >> $RUN/ledger.tsv
done
print "$(wc -l < $RUN/ledger.tsv | tr -d ' ') files hashed."
print "\nSuspected pairs:"
for a b in "Docker.dmg" "Docker (1).dmg"  "Invoice-0412.pdf" "Invoice-0412 (1).pdf" \
           "holiday-photos.zip" "holiday-photos (1).zip"  "CV-2026.docx" "CV-2026 (1).docx" \
           "budget.xlsx" "budget (1).xlsx"  "presentation-final.key" "presentation-final-v2.key" \
           "tenancy-agreement.pdf" "tenancy-agreement.pdf.download"; do
  ha=$(hashof $a); hb=$(hashof $b)
  if [[ -z $ha || -z $hb ]]; then print "  NOT COMPARABLE (one is a folder/package or missing): $a | $b"
  elif [[ $ha == $hb ]];     then print "  IDENTICAL  $a == $b   (${ha[1,16]}…)"
  else                            print "  DIFFERENT  $a != $b"; fi
done
print "\nAll identical-content groups:"
awk -F'\t' '{n[$1]++; p[$1]=p[$1] "\n    " $3} END {for (h in n) if (n[h]>1) print "  " substr(h,1,16) "… ×" n[h] p[h]}' $RUN/ledger.tsv

sec "3. Origin & usage metadata"
for f in $TOP; do
  print "\n--- ${f:t}\n  type: $(file -b "$f")"
  mdls -name kMDItemWhereFroms -name kMDItemDateAdded -name kMDItemLastUsedDate -name kMDItemUseCount \
       -name kMDItemContentType -name kMDItemIsScreenCapture "$f" 2>&1 | sed 's/^/  /'
  q=$(xattr -p com.apple.quarantine "$f" 2>/dev/null)
  if [[ -n $q ]]; then qp=( "${(@s:;:)q}" )
    print "  quarantine: agent=${qp[3]:-?}  when=$(date -r $(( 16#${qp[2]:-0} )) '+%F %T' 2>/dev/null)  flags=${qp[1]}"
  else print "  quarantine: (none)"; fi
done

sec "4. Installers vs installed apps  → installers.tsv"
print -r $'file\tinstaller_ver\tinstaller_team\tapp\tinstalled_ver\tinstalled_team\tverdict' > $RUN/installers.tsv
appver()  { /usr/libexec/PlistBuddy -c 'Print :CFBundleShortVersionString' "$1/Contents/Info.plist" 2>/dev/null }
appteam() { codesign -dv "$1" 2>&1 | sed -n 's/^TeamIdentifier=//p' }
verdict() {   # installer_ver installer_team installed_ver installed_team
  if   [[ -z $3 ]]; then print "NO: app not installed in /Applications"
  elif [[ -z $1 ]]; then print "NO: could not read installer version"
  elif [[ -n $2 && $2 != $4 ]]; then print "NO: different signer ($2 vs $4)"
  elif is-at-least "$1" "$3"; then print "OK"
  else print "NO: installer $1 is newer than installed $3; update the app first"; fi }
record() { print "  $1: installer=${2:-?} [$3]  installed $4=${5:-none} [$6]\n    → $7"
           print -r -- "$1"$'\t'"$2"$'\t'"$3"$'\t'"$4"$'\t'"$5"$'\t'"$6"$'\t'"$7" >> $RUN/installers.tsv }
check_dmg() {
  local name=$1 app=/Applications/$2 f=$DL/$1 mnt iv= it= av= at=; local -a a
  [[ -f $f ]] || return
  mnt=$(mktemp -d $WORK/mnt.XXXX)
  if hdiutil attach -nobrowse -readonly -noautoopen -mountpoint $mnt "$f" </dev/null >/dev/null 2>&1; then
    MOUNTS+=$mnt
    a=( $mnt/*.app(N) ); (( $#a )) && { iv=$(appver $a[1]); it=$(appteam $a[1]) }
    hdiutil detach -quiet $mnt && MOUNTS=( ${MOUNTS:#$mnt} )
  else print "  $name: could not mount (corrupt, or licence prompt)"; fi
  [[ -d $app ]] && { av=$(appver $app); at=$(appteam $app) }
  record "$name" "$iv" "$it" "${app:t}" "$av" "$at" "$(verdict "$iv" "$it" "$av" "$at")"
}
check_pkg() {
  local name=$1 app=/Applications/$2 f=$DL/$1 sig it= iv= av= at= v x=$WORK/pkg.$RANDOM
  [[ -f $f ]] || return
  sig=$(pkgutil --check-signature "$f" 2>&1); print -r -- "$sig" | sed 's/^/    /'
  it=$(print -r -- "$sig" | sed -n 's/.*Developer ID Installer:.*(\([A-Z0-9]\{10\}\)).*/\1/p' | head -1)
  pkgutil --expand "$f" $x >/dev/null 2>&1 &&
    iv=$(grep -rhoE '<pkg-info[^>]*' $x | head -1 | sed -nE 's/.*[[:space:]]version="([^"]+)".*/\1/p')
  [[ -d $app ]] && { av=$(appver $app); at=$(appteam $app) }
  if (( $(stat -f %z "$f") < 5000000 )) && [[ -n $av ]]; then
    # Judgment call: a stub installer downloads the latest build, so its version isn't comparable. Require same signer instead.
    [[ -n $it && $it == $at ]] && v="OK: stub installer, app present, same signer" || v="NO: stub, signer mismatch/unknown ($it vs $at)"
  else v=$(verdict "$iv" "$it" "$av" "$at"); fi
  record "$name" "$iv" "$it" "${app:t}" "$av" "$at" "$v"
}
check_dmg "Docker.dmg"      Docker.app
check_dmg "Docker (1).dmg"  Docker.app
check_dmg "Figma-arm64.dmg" Figma.app
check_pkg "Zoom.pkg"        zoom.us.app

sec "5. holiday-photos zips vs extracted folder  → archives.tsv"
print -r $'archive\tfolder\tverdict' > $RUN/archives.tsv
FOLDER=$DL/holiday-photos
print "Folder holds $(find "$FOLDER" -type f ! -name .DS_Store | wc -l | tr -d ' ') files"
for z in "holiday-photos.zip" "holiday-photos (1).zip"; do
  f=$DL/$z; [[ -f $f ]] || continue
  print "--- $z"; unzip -l "$f" | tail -1
  unzip -tq "$f" && t=ok || t=FAIL
  x=$(mktemp -d $WORK/unz.XXXX); unzip -qq "$f" -d $x -x '__MACOSX/*' '*.DS_Store'
  src=$x; inner=( $x/*(DN) ); (( $#inner == 1 )) && [[ -d $inner[1] ]] && src=$inner[1]
  d=$(diff -rq -x .DS_Store "$src" "$FOLDER" 2>&1)
  print -r -- "$d" | sed 's/^/    /' | head -40
  bad=$(print -r -- "$d" | grep -vF "Only in $FOLDER" | grep -v '^$')   # extra files in the folder are fine
  if [[ $t == ok && -z $bad ]]; then v="OK: every file in the zip is byte-identical in the folder"
  else v="NO: zip test=$t; zip content missing/different in folder"; fi
  print "  → $v"; print -r -- "$z"$'\t'"holiday-photos"$'\t'"$v" >> $RUN/archives.tsv
done

sec "6. tenancy-agreement.pdf.download"
T=$DL/tenancy-agreement.pdf.download; P=$DL/tenancy-agreement.pdf; typeset -a cand
if   [[ -d $T ]]; then print "Bundle directory (Safari's normal interrupted-download format):"
  ls -la@ "$T"; [[ -f $T/Info.plist ]] && plutil -p "$T/Info.plist"; cand=( $T/^Info.plist(.N) )
elif [[ -f $T ]]; then print "REGULAR FILE, not Safari's usual bundle. Don't assume it's partial."; cand=( $T ); fi
for c in $cand; do
  print "--- ${c:t}: $(file -b "$c")"
  tail -c 2048 "$c" | LC_ALL=C grep -aq '%%EOF' && print "  has %%EOF trailer → structurally complete" || print "  no %%EOF trailer → truncated"
  print "  this: $(pdfpages "$c")    tenancy-agreement.pdf: $(pdfpages "$P")"
  print "  text diff ('<' only in .download, '>' only in .pdf):"; diff <(pdftext "$c") <(pdftext "$P") | head -80
done

sec "7. Version pairs: what actually differs"
xlsx_dump() { local f=$1 out=$2 part; mkdir -p $out
  unzip -Z1 "$f" 2>/dev/null | grep -E '^(xl/worksheets/sheet[0-9]+\.xml|xl/sharedStrings\.xml|xl/workbook\.xml|docProps/core\.xml)$' |
  while IFS= read -r part; do mkdir -p $out/${part:h}; unzip -p "$f" "$part" | xmllint --nonet --format - > $out/$part 2>/dev/null; done }
xlsx_dump "$DL/budget.xlsx" $WORK/budget-A; xlsx_dump "$DL/budget (1).xlsx" $WORK/budget-B
for s in A B; do print "budget-$s: $(grep -hoE '<(dcterms:modified|cp:lastModifiedBy)[^<]*' $WORK/budget-$s/docProps/core.xml 2>/dev/null | tr '\n' ' ')"; done
print "(A = budget.xlsx, B = budget (1).xlsx; sharedStrings index shifts can add noise)"
( cd $WORK && diff -ru budget-A budget-B ) | head -200
for k in presentation-final.key presentation-final-v2.key; do f=$DL/$k
  print "--- $k  ($(file -b "$f"))"
  mdls -name kMDItemContentModificationDate -name kMDItemLastUsedDate -name kMDItemAuthors "$f" | sed 's/^/  /'
  if [[ -d $f ]]; then ( cd "$f" && find . -type f | sed 's|^\./||' | sort ) > $WORK/$k.list
  else unzip -Z1 "$f" 2>/dev/null | sort > $WORK/$k.list; fi
  print "  slide parts: $(grep -c '^Index/Slide' $WORK/$k.list)"
done
print "Parts only in final (<) / only in v2 (>):"; diff $WORK/presentation-final.key.list $WORK/presentation-final-v2.key.list
[[ $(hashof CV-2026.docx) != $(hashof "CV-2026 (1).docx") ]] && { print "CV text diff:"
  diff <(textutil -convert txt -stdout "$DL/CV-2026.docx") <(textutil -convert txt -stdout "$DL/CV-2026 (1).docx") }
[[ $(hashof Invoice-0412.pdf) != $(hashof "Invoice-0412 (1).pdf") ]] && { print "Invoice-0412 text diff:"
  diff <(pdftext "$DL/Invoice-0412.pdf") <(pdftext "$DL/Invoice-0412 (1).pdf") }

sec "8. Previews for eyeballing → $RUN/previews"
qlmanage -t -s 900 -o $RUN/previews "$DL"/Screenshot*.png(N) "$DL"/budget*.xlsx(N) "$DL"/presentation*.key(N) >/dev/null 2>&1
ls $RUN/previews
print "\nReport: $RUN/report.txt"
```

---

## Phase 2: Proposed plan (provisional until the report confirms it)

The report supplies the SHA-256 and origin for each row. Phase 3 also writes the hash into its action log. The **conditions** are not advisory: Phase 3 enforces them and refuses any action that fails one.

| # | Item | Action | Destination | Reason / enforced condition |
|---|---|---|---|---|
| 1 | Docker (1).dmg | trash-dup | – | Only if its hash equals Docker.dmg's |
| 2 | Docker.dmg | trash-installer | – | Installed Docker.app is the same or newer, with the same signer |
| 3 | Figma-arm64.dmg | trash-installer | – | Same rule |
| 4 | Zoom.pkg | trash-installer | – | 245 KB stub: zoom.us.app is present with the same signer (stub versions aren't comparable) |
| 5 | Invoice-0412 (1).pdf | trash-dup | – | Hash must match; if different → **ask** |
| 6–7 | Invoice-0412.pdf, Invoice-0517.pdf | move | ~/Documents/Finance/Invoices/2026/ | |
| 8 | P60-2025-26.pdf | **vault** | Vault/Tax/2025-26/ | NI number plus income: high identity-theft value |
| 9–11 | 3 screenshots | move | ~/Pictures/Screenshots/ | Check the previews; the 10.02 pair is probably a retake |
| 12 | passport-scan.jpg | **vault** | Vault/Identity/ | Identity document |
| 13 | tenancy-agreement.pdf | move | ~/Documents/Housing/Tenancy/ | FileVault protects it; the vault is optional |
| 14 | tenancy-agreement.pdf.download | **ask** | – | Possibly a *newer* copy; decide from report §6 |
| 15 | holiday-photos (1).zip | trash-dup | – | Hash must match holiday-photos.zip |
| 16 | holiday-photos.zip | trash-archive | – | Only if `unzip -t` passes and every file in it is byte-identical in the folder |
| 17 | holiday-photos/ | move | ~/Pictures/Holidays/2026-08 holiday-photos | Or import into Photos afterwards |
| 18–19 | budget.xlsx / budget (1).xlsx | move both, date-labelled | ~/Documents/Finance/Budget/ | Different versions: **ask** before deleting either |
| 20 | boarding-pass-LHR-LIS.pdf | trash | – | Trip over; keep only for an expense or compensation claim |
| 21–22 | presentation-final.key / -v2.key | move both | ~/Documents/Work/Presentations/ | Different versions: **ask** which is the real final |
| 23 | CV-2026 (1).docx | trash-dup | – | Hash must match |
| 24 | CV-2026.docx | move | ~/Documents/Career/CV/ | |

**Retention guidance (my suggestions, UK):**

| Document | Suggested retention |
|---|---|
| P60 | At least 22 months after the tax year ends (to 31 Jan 2028). I suggest about 6 years, because lenders ask for P60s. If you're self-employed, keep tax records 5 years after the 31 January filing deadline. |
| Tenancy agreement | For the tenancy, until the deposit is back, then ideally 6 years (the limitation period for contract claims). |
| Invoices | Personal purchases: for the warranty period, or up to 6 years for big items. Business expenses: 6 years. |
| Passport scan | Only while you actually need it; delete when the passport is renewed. |
| Boarding pass | Discard. |
| CV | Keep the latest. |

**Encrypted vault** (one-off setup before Phase 3):

```zsh
mkdir -p ~/Vault      # outside ~/Documents so iCloud never tries to sync a sparse bundle
hdiutil create -size 2g -type SPARSEBUNDLE -fs APFS -encryption AES-256 -volname Vault ~/Vault/Vault.sparsebundle
# prompts for a password: store it in your password manager, NOT the login keychain
hdiutil attach ~/Vault/Vault.sparsebundle      # mounts at /Volumes/Vault
```

One caveat: Time Machine already holds unencrypted copies of the passport and P60 from before the move. Emptying the Trash doesn't remove those. An SSD also can't guarantee a secure delete. Your protection here is FileVault plus an encrypted backup disk.

**Manifest:** save this as `~/DownloadsCleanup/manifest.txt`. It is pipe-separated, so copy-paste can't break it. If a row isn't needed, its argument is `-`. Keep the order: duplicates first, then the archive before the folder moves.

```text
# action        | item in ~/Downloads                    | argument                                            | reason
trash-dup       | Docker (1).dmg                         | Docker.dmg                                          | identical re-download
trash-dup       | Invoice-0412 (1).pdf                   | Invoice-0412.pdf                                    | identical re-download
trash-dup       | holiday-photos (1).zip                 | holiday-photos.zip                                  | identical re-download
trash-dup       | CV-2026 (1).docx                       | CV-2026.docx                                        | identical re-download
trash-installer | Docker.dmg                             | Docker.app                                          | installed same/newer
trash-installer | Figma-arm64.dmg                        | Figma.app                                           | installed same/newer
trash-installer | Zoom.pkg                               | zoom.us.app                                         | stub; app installed
trash-archive   | holiday-photos.zip                     | holiday-photos                                      | contents verified in folder
vault           | passport-scan.jpg                      | Identity/                                           | identity document
vault           | P60-2025-26.pdf                        | Tax/2025-26/                                        | NI number + income
move            | Invoice-0412.pdf                       | ~/Documents/Finance/Invoices/2026/                  | keep 6y if business
move            | Invoice-0517.pdf                       | ~/Documents/Finance/Invoices/2026/                  |
move            | tenancy-agreement.pdf                  | ~/Documents/Housing/Tenancy/                        |
move            | CV-2026.docx                           | ~/Documents/Career/CV/                              |
move            | budget.xlsx                            | ~/Documents/Finance/Budget/budget (2026-08-15).xlsx | older version, ask before deleting
move            | budget (1).xlsx                        | ~/Documents/Finance/Budget/budget (2026-09-02).xlsx | newer version
move            | presentation-final.key                 | ~/Documents/Work/Presentations/                     | ask which is final
move            | presentation-final-v2.key              | ~/Documents/Work/Presentations/                     |
move            | holiday-photos                         | ~/Pictures/Holidays/2026-08 holiday-photos          |
move            | Screenshot 2026-06-18 at 10.02.11.png  | ~/Pictures/Screenshots/                             |
move            | Screenshot 2026-06-18 at 10.02.40.png  | ~/Pictures/Screenshots/                             |
move            | Screenshot 2026-07-02 at 16.45.03.png  | ~/Pictures/Screenshots/                             |
trash           | boarding-pass-LHR-LIS.pdf              | -                                                   | trip over
ask             | tenancy-agreement.pdf.download         | -                                                   | decide from report §6
```

If the report shows a pair is *different*, change its `trash-dup` row to `ask` or `move`; Phase 3 would refuse it anyway. If a screenshot name is reported "not found", copy the exact name from `toplevel.txt`. macOS sometimes uses invisible narrow spaces in screenshot names.

---

## Phase 3: Execute

`~/DownloadsCleanup/bin/phase3-execute.zsh`

```zsh
#!/bin/zsh
# Runs an APPROVED manifest. Refuses without a recent Time Machine backup. Never uses rm; trash goes via Finder (Put Back works).
emulate zsh
setopt pipe_fail extended_glob
MANIFEST=${1:-$HOME/DownloadsCleanup/manifest.txt}
RUN=${${2:-$HOME/DownloadsCleanup/latest}:A}
DL=$(<$RUN/downloads-root.txt); LOG=$RUN/actions.tsv
VAULT=/Volumes/Vault; VAULT_IMAGE=$HOME/Vault/Vault.sparsebundle; MAX_BACKUP_AGE_HOURS=24

die()  { print -u2 "ABORT: $*"; exit 1 }
trim() { local s=$1; s=${s##[[:space:]]#}; REPLY=${s%%[[:space:]]#} }
sha()  { shasum -a 256 "$1" | cut -d' ' -f1 }
ledger_tree() { awk -F'\t' -v n="$1" '$3==n {print $1 "\t"} index($3, n "/")==1 {print $1 "\t" substr($3, length(n)+2)}' $RUN/ledger.tsv | sort }
disk_tree() { if [[ -f $1 ]]; then print -r -- "$(sha "$1")"$'\t'
  else ( cd -- "$1" && find . -type f ! -name .DS_Store -print0 | while IFS= read -r -d '' f; do print -r -- "$(sha "$f")"$'\t'"${f#./}"; done ) | sort; fi }
unchanged()   { local l=$(ledger_tree "$1"); [[ -n $l && $l == "$(disk_tree "$2")" ]] }
tsv_verdict() { awk -F'\t' -v f="$2" '$1==f {print $NF}' "$1" }
to_trash()    { osascript -e 'on run argv' -e 'tell application "Finder" to delete (POSIX file (item 1 of argv) as alias)' -e 'end run' "$1" </dev/null >/dev/null 2>&1; [[ ! -e $1 ]] }

[[ -r $MANIFEST ]] || die "no manifest at $MANIFEST"
[[ -e $LOG ]] && die "this run was already executed ($LOG). Re-run Phase 1 for a fresh run."

# Gate 1: recent backup that includes Downloads
b=$(tmutil latestbackup 2>/dev/null); [[ -n $b ]] || die "no Time Machine backup visible (or Terminal lacks Full Disk Access)"
stamp=${${b:t}%.backup}
bt=$(date -j -f %Y-%m-%d-%H%M%S "$stamp" +%s 2>/dev/null) || die "can't parse backup time from $b"
age=$(( ($(date +%s) - bt) / 3600 ))
(( age <= MAX_BACKUP_AGE_HOURS )) || die "latest backup is ${age}h old; run: tmutil startbackup --block"
tmutil isexcluded "$DL" | grep -q '^\[Included\]' || die "Downloads is excluded from Time Machine"
print "✓ backup $stamp (${age}h old) covers Downloads"

# Gate 2: manifest covers every top-level entry exactly once
typeset -a ACT NAME ARG WHY; typeset -A seen
while IFS= read -r line || [[ -n $line ]]; do
  [[ $line == [[:space:]]#(\#*|) ]] && continue
  f=( "${(@s:|:)line}" ); (( $#f >= 2 )) || die "bad line: $line"
  trim "$f[1]"; a=$REPLY; trim "$f[2]"; n=$REPLY; trim "${f[3]:-}"; g=$REPLY; trim "${f[4]:-}"; w=$REPLY
  [[ $g == - ]] && g=
  [[ $a == (keep|ask|move|vault|trash|trash-dup|trash-installer|trash-archive) ]] || die "unknown action '$a'"
  [[ -e $DL/$n ]] || die "not found in Downloads: '$n'"
  (( ${+seen[$n]} )) && die "listed twice: $n"
  seen[$n]=1; ACT+=("$a"); NAME+=("$n"); ARG+=("$g"); WHY+=("$w")
done < $MANIFEST
for n in ${(f)"$(<$RUN/toplevel.txt)"}; do (( ${+seen[$n]} )) || die "manifest doesn't cover: $n"; done
print "✓ manifest covers all ${#NAME} entries exactly once"

# Gate 3: nothing changed since Phase 1
for n in $NAME; do unchanged "$n" "$DL/$n" || die "'$n' changed since Phase 1; re-run Phase 1"; done
print "✓ every item matches the Phase 1 hash ledger"

# Gate 4: vault is the encrypted image, mounted
if (( ${ACT[(I)vault]} )); then
  [[ -d $VAULT ]] || die "mount the vault first: hdiutil attach '$VAULT_IMAGE'"
  hdiutil isencrypted "$VAULT_IMAGE" 2>/dev/null | grep -q 'encrypted: YES' || die "$VAULT_IMAGE isn't encrypted"
  hdiutil info | awk -v img="$VAULT_IMAGE" -v mp="$VAULT" '/^image-path/ {sub(/^image-path *: */,""); cur=($0==img)} cur && index($0,mp) {ok=1} END {exit !ok}' \
    || die "$VAULT isn't mounted from $VAULT_IMAGE"
  print "✓ encrypted vault mounted"
fi

print "\nPlanned actions:"; for i in {1..$#ACT}; do printf '  %-16s %s%s\n' "$ACT[i]" "$NAME[i]" "${ARG[i]:+  →  $ARG[i]}"; done
read -r "?Type YES to proceed: " ok; [[ $ok == YES ]] || die "not confirmed"

print -r $'time\taction\titem\tsha256\tdestination\tstatus\tnote' > $LOG
log() { print -r -- "$(date '+%F %T')"$'\t'"$1"$'\t'"$2"$'\t'"${3:--}"$'\t'"${4:--}"$'\t'"$5"$'\t'"${6:--}" >> $LOG
        print "  [$5] $1  $2${4:+  →  $4}${6:+   ($6)}" }
fails=0
for i in {1..$#ACT}; do
  a=$ACT[i] n=$NAME[i] g=$ARG[i] src=$DL/$NAME[i] dest= st=FAILED note=$WHY[i]
  h=$(awk -F'\t' -v p="$n" '$3==p {print $1}' $RUN/ledger.tsv); [[ -z $h ]] && h="(folder/package)"
  case $a in
    keep|ask) st=KEPT ;;
    trash)    to_trash "$src" && st=TRASHED ;;
    trash-dup)
      if   [[ ! -e $DL/$g ]];                                  then st=REFUSED note="keeper '$g' not in Downloads"
      elif [[ "$(ledger_tree "$n")" != "$(ledger_tree "$g")" ]]; then st=REFUSED note="NOT byte-identical to '$g'"
      elif ! unchanged "$g" "$DL/$g";                          then st=REFUSED note="keeper changed"
      else to_trash "$src" && st=TRASHED; fi ;;
    trash-installer)
      v=$(tsv_verdict $RUN/installers.tsv "$n")
      if   [[ $v != OK* ]];             then st=REFUSED note="installer check: ${v:-not run}"
      elif [[ ! -d /Applications/$g ]]; then st=REFUSED note="/Applications/$g missing"
      else to_trash "$src" && st=TRASHED; fi ;;
    trash-archive)
      v=$(tsv_verdict $RUN/archives.tsv "$n")
      if   [[ $v != OK* ]]; then st=REFUSED note="archive check: ${v:-not run}"
      elif [[ ! -d $DL/$g ]] || ! unchanged "$g" "$DL/$g"; then st=REFUSED note="folder '$g' moved/changed; trash archives first"
      else to_trash "$src" && st=TRASHED; fi ;;
    move)
      dest=${g/#\~/$HOME}; [[ $dest == */ ]] && dest+=$n
      if   [[ -z $g ]];     then note="no destination"
      elif [[ -e $dest ]];  then st=REFUSED note="destination already exists"
      else mkdir -p "${dest:h}" && mv -n "$src" "$dest" && [[ ! -e $src ]] && unchanged "$n" "$dest" && st=MOVED; fi ;;
    vault)
      dest=$VAULT/${g#/}; [[ $dest == */ ]] && dest+=$n
      if [[ -e $dest ]]; then st=REFUSED note="already in vault"
      else mkdir -p "${dest:h}" && ditto "$src" "$dest" && unchanged "$n" "$dest" && to_trash "$src" && st=VAULTED; fi ;;
  esac
  [[ $st == (FAILED|REFUSED) ]] && (( fails++ ))
  log "$a" "$n" "$h" "$dest" "$st" "$note"
done
print "\n$fails action(s) refused/failed (those items are untouched). Log: $LOG"
print "Nothing was permanently deleted. Next: zsh ~/DownloadsCleanup/bin/phase4-verify.zsh"
exit $(( fails > 0 ))
```

---

## Phase 4: Verify independently

`~/DownloadsCleanup/bin/phase4-verify.zsh`

```zsh
#!/bin/zsh
emulate zsh
setopt pipe_fail extended_glob
RUN=${${1:-$HOME/DownloadsCleanup/latest}:A}
DL=$(<$RUN/downloads-root.txt); LOG=$RUN/actions.tsv; VAULT=/Volumes/Vault
[[ -r $LOG ]] || { print "No actions log; run Phase 3 first."; exit 1 }
pass=0 fail=0 warn=0
ok()  { (( pass++ )); [[ -n ${1:-} ]] && print "  PASS  $1" }
bad() { (( fail++ )); print "  FAIL  $1" }
meh() { (( warn++ )); print "  WARN  $1" }
sha() { shasum -a 256 "$1" | cut -d' ' -f1 }
pdf_js='function run(a){ObjC.import("PDFKit");var d=$.PDFDocument.alloc.initWithURL($.NSURL.fileURLWithPath(a[0]));if(d.isNil())return "UNREADABLE";return "pages="+d.pageCount}'

typeset -A ST DEST ACTN
while IFS=$'\t' read -r t a n h d s note; do [[ $t == time ]] && continue
  ST[$n]=$s; ACTN[$n]=$a; [[ $d != - ]] && DEST[$n]=$d; done < $LOG
TOPS=( ${(f)"$(<$RUN/toplevel.txt)"} )

print "1. Count reconciliation"
typeset -A C
for n in $TOPS; do
  case ${ST[$n]:-} in KEPT|FAILED|REFUSED) c=kept;; MOVED) c=moved;; VAULTED) c=vaulted;; TRASHED) c=trashed;; *) c=unaccounted;; esac
  (( C[$c]++ ))
  case $c in
    kept)          [[ -e $DL/$n ]] || bad "$n should still be in Downloads" ;;
    moved|vaulted) [[ -e ${DEST[$n]:-/nonexistent} && ! -e $DL/$n ]] || bad "$n not at its destination" ;;
    trashed)       [[ ! -e $DL/$n ]] || bad "$n still in Downloads" ;;
    unaccounted)   bad "$n has no logged action" ;;
  esac
done
sum=$(( ${C[kept]:-0} + ${C[moved]:-0} + ${C[vaulted]:-0} + ${C[trashed]:-0} ))
print "  in=${#TOPS}  kept=${C[kept]:-0}  moved=${C[moved]:-0}  vaulted=${C[vaulted]:-0}  trashed=${C[trashed]:-0}  unaccounted=${C[unaccounted]:-0}"
(( sum == ${#TOPS} && ${C[unaccounted]:-0} == 0 )) && ok "counts reconcile" || bad "counts don't reconcile"

print "2. Hash ledger: every original byte-stream is at its destination or in the Trash"
typeset -A TRASH
for f in ${(0)"$(find ~/.Trash -type f -cnewer $RUN/ledger.tsv -print0 2>/dev/null)"}; do [[ -f $f ]] && TRASH[$(sha "$f")]=1; done
before=$fail
while IFS=$'\t' read -r h size p; do
  top=${p%%/*}; rest=${p#$top}; rest=${rest#/}
  [[ -n ${ST[$top]:-} ]] || continue
  case $ST[$top] in
    TRASHED)       (( ${+TRASH[$h]} )) || bad "$p (${h[1,12]}…) not found in Trash"; continue ;;
    MOVED|VAULTED) loc=${DEST[$top]}${rest:+/$rest} ;;
    *)             loc=$DL/$p ;;
  esac
  [[ -f $loc && $(sha "$loc") == $h ]] || bad "$p: expected at $loc with hash ${h[1,12]}…"
done < $RUN/ledger.tsv
(( fail == before )) && ok "all $(wc -l < $RUN/ledger.tsv | tr -d ' ') ledger hashes accounted for"

print "3. Duplicate groups: exactly one survivor (or zero, if removed by design)"
for line in ${(f)"$(awk -F'\t' '$3 !~ /\// {c[$1]++; m[$1]=m[$1] "|" $3} END {for (h in c) if (c[h]>1) print h m[h]}' $RUN/ledger.tsv)"}; do
  parts=( "${(@s:|:)line}" ); members=( $parts[2,-1] ); surv=0 byDesign=0
  for m in $members; do
    if [[ ${ST[$m]:-} == TRASHED ]]; then [[ ${ACTN[$m]} != trash-dup ]] && byDesign=1; else (( surv++ )); fi
  done
  if   (( surv == 1 ));              then ok "one copy kept: ${(j:, :)members}"
  elif (( surv == 0 && byDesign )); then ok "removed entirely by design: ${(j:, :)members}"
  else bad "$surv survivors: ${(j:, :)members}"; fi
done

print "4. Surviving files open"
typeset -a SURV
for n in $TOPS; do
  case ${ST[$n]:-} in TRASHED) continue;; MOVED|VAULTED) base=${DEST[$n]};; *) base=$DL/$n;; esac
  if [[ -d $base ]]; then SURV+=( $base/**/^.DS_Store(.ND) ); else SURV+=("$base"); fi
done
tmp=$(mktemp -d)
for f in $SURV; do
  case ${f:e:l} in
    pdf)  r=$(osascript -l JavaScript -e $pdf_js "$f" </dev/null 2>&1); [[ $r == pages=<1-> ]] && ok "${f:t} ($r)" || bad "PDF won't open: $f ($r)" ;;
    jpg|jpeg|png|heic|gif|tif|tiff) sips -g pixelWidth "$f" 2>/dev/null | grep -q 'pixelWidth: [1-9]' && ok || bad "image won't decode: $f" ;;
    docx|doc|rtf|txt) textutil -convert txt -stdout "$f" >/dev/null 2>&1 && ok "${f:t}" || bad "won't open: $f" ;;
    xlsx|key|pptx|numbers|pages|zip) [[ -d $f ]] && ok "${f:t} (package)" || { unzip -tqq "$f" >/dev/null 2>&1 && ok "${f:t} intact" || bad "corrupt container: $f" } ;;
    download|dmg|pkg) meh "not content-checked: ${f:t}" ;;
    *) qlmanage -t -o $tmp "$f" 2>&1 | grep -q 'produced one thumbnail' && ok "${f:t}" || meh "Quick Look can't preview: $f" ;;
  esac
done; rm -rf -- $tmp

print "5. Spotlight finds moved items"
for n in ${(k)ST}; do [[ $ST[$n] == (MOVED|VAULTED) ]] || continue; d=$DEST[$n]
  found() { mdfind -onlyin "${d:h}" -name "${d:t}" 2>/dev/null | grep -qxF -- "$d" }
  if found; then ok "$d"
  else mdimport "$d" 2>/dev/null; sleep 5
    if found; then ok "$d (after reindex)"
    elif [[ $d == $VAULT/* ]]; then meh "vault not indexed ($(mdutil -s $VAULT 2>&1 | tail -1)); normal for an encrypted image"
    else bad "Spotlight can't find $d (re-run in a few minutes)"; fi
  fi
done

print "6. Root-cause fixes"
loc=$(defaults read com.apple.screencapture location 2>/dev/null)
[[ ${loc:A} == ${DL} ]] && bad "screenshots still save to Downloads" || ok "screenshots save to: ${loc:-Desktop (default)}"
launchctl print gui/$(id -u)/local.downloads-stale >/dev/null 2>&1 && ok "stale-Downloads job loaded" || meh "stale-Downloads job not loaded (run Phase 5)"
print "\nLeft in Downloads:"; print -l -- "  "${^${:-$DL/*(DN:t)}}
print "\nPASS=$pass  WARN=$warn  FAIL=$fail"
(( fail == 0 )) && print "Safe to empty the Trash (it holds unencrypted copies of anything vaulted)." || print "Do NOT empty the Trash; use Put Back on anything listed above."
exit $(( fail > 0 ))
```

Re-run this in a month. The "Left in Downloads" list then shows whether the fixes held.

---

## Phase 5: Prevent recurrence

`~/DownloadsCleanup/bin/phase5-prevent.zsh`

```zsh
#!/bin/zsh
emulate zsh
SHOTS=$HOME/Pictures/Screenshots
print "Screenshot location was: $(defaults read com.apple.screencapture location 2>/dev/null || print 'unset (Desktop)')"
mkdir -p $SHOTS
defaults write com.apple.screencapture location -string "$SHOTS"
killall SystemUIServer 2>/dev/null
print "Now: $(defaults read com.apple.screencapture location). Press ⌘⇧3 to confirm."
print "(⌘⇧5 › Options › Save to also writes this setting; if you change it there later, this is undone.)"

# Daily notifier for items that have sat in Downloads > 30 days (by DATE ADDED, not modification date)
mkdir -p $HOME/bin $HOME/Library/LaunchAgents $HOME/DownloadsCleanup
cat > $HOME/bin/downloads-stale.zsh <<'EOF'
#!/bin/zsh
out=$HOME/DownloadsCleanup/stale.txt
mdfind -onlyin $HOME/Downloads 'kMDItemDateAdded < $time.today(-30)' |
  awk -v d="$HOME/Downloads/" 'index($0,d)==1 && substr($0,length(d)+1) !~ /\//' > $out
n=$(wc -l < $out | tr -d ' ')
(( n > 0 )) && osascript -e "display notification \"$n item(s) in Downloads are over 30 days old. See ~/DownloadsCleanup/stale.txt\" with title \"Downloads\""
EOF
chmod +x $HOME/bin/downloads-stale.zsh
PLIST=$HOME/Library/LaunchAgents/local.downloads-stale.plist
cat > $PLIST <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>local.downloads-stale</string>
  <key>ProgramArguments</key><array><string>/bin/zsh</string><string>$HOME/bin/downloads-stale.zsh</string></array>
  <key>StartCalendarInterval</key><dict><key>Hour</key><integer>10</integer><key>Minute</key><integer>0</integer></dict>
  <key>StandardErrorPath</key><string>$HOME/DownloadsCleanup/stale.err</string>
</dict></plist>
EOF
plutil -lint $PLIST
launchctl bootout gui/$(id -u)/local.downloads-stale 2>/dev/null
launchctl bootstrap gui/$(id -u) $PLIST && launchctl kickstart gui/$(id -u)/local.downloads-stale
print "Job loaded and run once. Check ~/DownloadsCleanup/stale.txt."
```

If no notification ever appears:

- Check `~/DownloadsCleanup/stale.err`.
- macOS privacy controls may block a background job from reading Downloads. Give `/bin/zsh` Full Disk Access, or use Hazel instead.
- Notifications may also need allowing under System Settings › Notifications › Script Editor.

### Root causes and how they were likely introduced

- **Screenshots:** the macOS default is the Desktop. The setting only points at Downloads if someone changed it, and the usual way is **⌘⇧5 › Options › Save to**, which persists silently. Report §0 shows the current value. If it's *unset*, these PNGs arrived some other way, for example by dragging the floating thumbnail into a browser or chat app. The where-from and quarantine data in §3 will tell you which.
- **` (1)` copies:** the same file was downloaded twice. For Docker, that was the same day, probably a double click. The invoice and CV were probably opened twice from webmail.
  - **Chrome/Edge:** Settings › Downloads › turn on **"Ask where to save each file before downloading"**. The save dialog then shows the existing file and asks before duplicating.
  - **Safari:** Settings › General › File download location › **"Ask for each download"**.
  - **Habit:** reopen files from the browser's download list ("Show in Finder") instead of downloading again.

## What needs your decision after Phase 1

1. **`tenancy-agreement.pdf.download`:** report §6 tells you whether it's a truncated partial (trash it) or a complete, newer agreement (keep it and rename it).
2. **budget, two versions:** §7 shows which cells changed. Then delete the old one or keep both.
3. **Keynote decks:** §7 slide-part diff plus the previews tell you which is really final.
4. **Duplicate pairs that turn out to differ:** change their rows to `ask`. Phase 3 would refuse them anyway.
