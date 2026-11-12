# downloads-plain-2

Writer: claude-opus-5-5

## Prompt

Tidy my Downloads folder.

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

# Plan for tidying ~/Downloads

I can't see or change your files directly, so below is a script you can run. **It only moves files. Nothing is permanently deleted.** Anything removed goes to the Trash, and you can restore it with Finder's "Put Back". By default it only prints what it would do. It makes no changes until you add `--apply`.

## Assumptions

1. **Duplicates.** Files named "X (1)" with the same size as "X" are probably duplicates. The script checks that the contents really match (`cmp`) before trashing the "(1)" copy. If they differ, it leaves both.
2. **Different sizes mean different versions.** `budget.xlsx`/`budget (1).xlsx` and the two `presentation-final` files are kept. The script renames the budget files to show which is newer.
3. **Installers** (`.dmg`/`.pkg`) are trashed only if the app is already in `/Applications`. Otherwise they move to `Installers/`.
4. **`tenancy-agreement.pdf.download`** is an unfinished Safari download. It's newer and larger than the finished PDF, so it may be an updated version that never completed. **I left it alone.** You should check it or download it again.
5. **`holiday-photos.zip`** sits next to an extracted `holiday-photos` folder. I kept the zip in `Archives/` rather than assume the extraction is complete. Only the identical "(1)" copy is trashed.
6. **Sensitive files** (`passport-scan.jpg`, `P60-2025-26.pdf`) go to `Personal-Sensitive/`. Downloads is not a good long-term home for them. See the notes at the end.

## Resulting layout

```
~/Downloads/
├── Installers/            (only those whose app isn't installed)
├── Finance/               Invoice-0412.pdf, Invoice-0517.pdf, P60 → see Sensitive, budget-2026-08-15.xlsx, budget-2026-09-02.xlsx
├── Personal-Sensitive/    passport-scan.jpg, P60-2025-26.pdf
├── Housing/               tenancy-agreement.pdf
├── Travel/                boarding-pass-LHR-LIS.pdf
├── Work/                  presentation-final.key, presentation-final-v2.key, CV-2026.docx
├── Screenshots/           3 screenshots
├── Archives/              holiday-photos.zip, holiday-photos/
└── tenancy-agreement.pdf.download   (left for you to check)
```

## Script

Save it as `tidy-downloads.sh`, then run:
- `zsh tidy-downloads.sh` to preview the changes
- `zsh tidy-downloads.sh --apply` to make them

```zsh
#!/bin/zsh
set -u
cd ~/Downloads || exit 1
APPLY=0; [[ "${1:-}" == "--apply" ]] && APPLY=1

run() { if (( APPLY )); then "$@"; else echo "[dry-run] $*"; fi }

# Move to Trash via Finder (supports "Put Back")
to_trash() {
  [[ -e "$1" ]] || return
  if (( APPLY )); then
    osascript -e "tell application \"Finder\" to delete POSIX file \"$PWD/$1\"" >/dev/null
    echo "Trashed: $1"
  else echo "[dry-run] trash: $1"; fi
}

# Move, refusing to overwrite anything
mv_safe() { [[ -e "$1" ]] || return; run mkdir -p "$2"; run mv -n "$1" "$2/"; }

# Trash "(1)" copy only if byte-identical to the original
dedupe() {
  if [[ -e "$1" && -e "$2" ]]; then
    if cmp -s "$1" "$2"; then to_trash "$2"
    else echo "KEPT (contents differ): $1 vs $2"; fi
  fi
}

# --- 1. Exact duplicates ---
dedupe "Docker.dmg"           "Docker (1).dmg"
dedupe "Invoice-0412.pdf"     "Invoice-0412 (1).pdf"
dedupe "holiday-photos.zip"   "holiday-photos (1).zip"
dedupe "CV-2026.docx"         "CV-2026 (1).docx"

# --- 2. Installers: trash if app installed, else file away ---
installer() {  # $1 = file, $2 = app name
  if [[ -d "/Applications/$2.app" ]]; then to_trash "$1"
  else mv_safe "$1" Installers; fi
}
installer "Zoom.pkg"         "zoom.us"
installer "Docker.dmg"       "Docker"
installer "Figma-arm64.dmg"  "Figma"

# --- 3. Rename budget versions by date, then file ---
[[ -e "budget.xlsx" ]]     && run mv -n "budget.xlsx"     "budget-2026-08-15.xlsx"
[[ -e "budget (1).xlsx" ]] && run mv -n "budget (1).xlsx" "budget-2026-09-02.xlsx"

# --- 4. File everything ---
for f in Invoice-0412.pdf Invoice-0517.pdf budget-2026-08-15.xlsx budget-2026-09-02.xlsx; do mv_safe "$f" Finance; done
for f in passport-scan.jpg P60-2025-26.pdf; do mv_safe "$f" Personal-Sensitive; done
mv_safe tenancy-agreement.pdf Housing
mv_safe boarding-pass-LHR-LIS.pdf Travel
for f in presentation-final.key presentation-final-v2.key CV-2026.docx; do mv_safe "$f" Work; done
for f in Screenshot*.png(N); do mv_safe "$f" Screenshots; done
mv_safe holiday-photos.zip Archives
mv_safe holiday-photos Archives

# Restrict the sensitive folder to your user only
[[ -d Personal-Sensitive ]] && run chmod 700 Personal-Sensitive

echo "Left in place for review: tenancy-agreement.pdf.download"
(( APPLY )) || echo "\nDry run only. Re-run with --apply to make changes."
```

## Space recovered (approximate)

| Item | Size |
|---|---|
| Docker (1).dmg | 98 MB |
| Docker.dmg + Figma + Zoom (if installed) | ~285 MB |
| holiday-photos (1).zip, Invoice/CV dupes | ~1.6 MB |
| **Total** | **up to ~385 MB** |

You only get this space back once you empty the Trash.

## Worth doing by hand

- **Passport scan and P60:** consider moving these into an encrypted location, such as an encrypted disk image made with Disk Utility or a password manager's secure file storage, rather than leaving them in Downloads.
- **`tenancy-agreement.pdf.download`:** right-click it, choose Show Package Contents, and check whether it's a newer version. If it is, download it again. Otherwise trash it.
- **`holiday-photos.zip`:** once you've confirmed the folder has all the photos, you can trash the zip too.
- **Old versions:** the boarding pass from 20 Sep is probably no longer needed. `presentation-final.key` may also be superseded by `-v2`, and so may the older budget file. I kept all of them to be safe.
