# downloads-persona-1

Writer: claude-opus-5-5

## Prompt

Act as an expert IT support specialist. Tidy my Downloads folder.

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

# Tidying ~/Downloads

I can't see your Mac's files, only the listing you pasted. So below is a plan and a script that you run yourself. **The script defaults to a dry run**: it prints what it would do and changes nothing until you run it again with `DRY=0`. Nothing is permanently deleted. Removed files go to the Trash, so you can put them back.

## The plan

| Files | Action | Reason |
|---|---|---|
| `Docker (1).dmg`, `Invoice-0412 (1).pdf`, `CV-2026 (1).docx`, `holiday-photos (1).zip` | **Trash, only if byte-identical** to the original | Same size and date as the original, so probably duplicate downloads. The script checks with `cmp` first. |
| `Zoom.pkg`, `Docker.dmg`, `Figma-arm64.dmg` | **Trash if the app is already in /Applications**, otherwise move to `Downloads/Installers` | Installers are not needed once the app is installed. |
| `holiday-photos.zip` | **Trash only if** the extracted `holiday-photos` folder has the same number of files | The extracted folder already exists. |
| `holiday-photos/` folder | Move to `~/Pictures/` | |
| Invoices, `budget*.xlsx`, `P60-2025-26.pdf` | Move to `~/Documents/Finance/` | |
| `passport-scan.jpg` | Move to `~/Documents/Personal/ID/` and make it readable only by you | Sensitive |
| `tenancy-agreement.pdf` | Move to `~/Documents/Housing/` | |
| `boarding-pass-LHR-LIS.pdf` | Move to `~/Documents/Travel/` | |
| `CV-2026.docx`, `presentation-final*.key` | Move to `~/Documents/Work/` | |
| Screenshots | Move to `~/Pictures/Screenshots/` | |
| `tenancy-agreement.pdf.download` | **Left alone and flagged** | See below |

**Kept on purpose:**
- `budget (1).xlsx` is a different size and newer, so it is a different version. Both are kept.
- `presentation-final.key` and `-v2` are both kept.

**The tenancy file needs your judgement.** `tenancy-agreement.pdf.download` is an unfinished Safari download. It is newer (20 Aug) and larger than the finished PDF (11 Jul), so it may be a revised agreement that never finished downloading. Re-download it from the original source, then trash the `.download` file.

## The script

Save it as `~/tidy-downloads.sh`. Keep it outside Downloads.

```bash
#!/bin/bash
# Tidy ~/Downloads. Dry run by default; run with DRY=0 to apply.
set -uo pipefail
cd "$HOME/Downloads" || exit 1
DRY="${DRY:-1}"

run()   { if [ "$DRY" = 1 ]; then echo "[dry-run] $*"; else "$@"; fi; }
trashf() {
  if command -v trash >/dev/null 2>&1; then run trash "$1"
  else run osascript -e "tell application \"Finder\" to delete POSIX file \"$PWD/$1\"" >/dev/null; fi
}
movef() {  # movef <file> <destdir>   (-n = never overwrite)
  [ -e "$1" ] || { echo "missing, skipped: $1"; return; }
  run mkdir -p "$2"; run mv -n "$1" "$2/"
  [ "$DRY" = 1 ] || [ ! -e "$1" ] || echo "NOT MOVED (name already exists in $2): $1"
}
dedupe() { # dedupe <original> <copy>
  if [ -e "$1" ] && [ -e "$2" ] && cmp -s "$1" "$2"; then echo "identical -> trash: $2"; trashf "$2"
  else echo "KEPT (not identical or missing): $2"; fi
}
installer() { # installer <file> <App name>
  [ -e "$1" ] || return
  if [ -d "/Applications/$2" ]; then echo "$2 installed -> trash: $1"; trashf "$1"
  else movef "$1" "$HOME/Downloads/Installers"; fi
}

D="$HOME/Documents"; P="$HOME/Pictures"

# 1. Exact duplicates
dedupe "Docker.dmg"           "Docker (1).dmg"
dedupe "Invoice-0412.pdf"     "Invoice-0412 (1).pdf"
dedupe "CV-2026.docx"         "CV-2026 (1).docx"
dedupe "holiday-photos.zip"   "holiday-photos (1).zip"

# 2. Installers
installer "Zoom.pkg"          "zoom.us.app"
installer "Docker.dmg"        "Docker.app"
installer "Figma-arm64.dmg"   "Figma.app"

# 3. Holiday photos: drop the zip only if the extracted folder looks complete
if [ -f holiday-photos.zip ] && [ -d holiday-photos ]; then
  z=$(unzip -Z1 holiday-photos.zip | grep -v '/$' | grep -vc '__MACOSX')
  f=$(find holiday-photos -type f ! -name '.DS_Store' | wc -l | tr -d ' ')
  if [ "$z" = "$f" ]; then echo "zip ($z) matches folder ($f) -> trash zip"; trashf holiday-photos.zip
  else echo "KEPT holiday-photos.zip: zip has $z files, folder has $f"; fi
fi
movef "holiday-photos" "$P"

# 4. File documents
for f in Invoice-0412.pdf Invoice-0517.pdf P60-2025-26.pdf budget.xlsx "budget (1).xlsx"; do movef "$f" "$D/Finance"; done
movef "passport-scan.jpg"         "$D/Personal/ID"
movef "tenancy-agreement.pdf"     "$D/Housing"
movef "boarding-pass-LHR-LIS.pdf" "$D/Travel"
for f in CV-2026.docx presentation-final.key presentation-final-v2.key; do movef "$f" "$D/Work"; done
for f in Screenshot\ *.png; do [ -e "$f" ] && movef "$f" "$P/Screenshots"; done

# 5. Lock down sensitive files (owner-only access)
[ "$DRY" = 1 ] || chmod 600 "$D/Personal/ID/passport-scan.jpg" "$D/Finance/P60-2025-26.pdf" 2>/dev/null

echo; echo "Left in Downloads:"; ls -la
[ -e tenancy-agreement.pdf.download ] && echo "NOTE: tenancy-agreement.pdf.download is an unfinished download. Re-download it, then trash it."
```

## How to run it

```zsh
chmod +x ~/tidy-downloads.sh
~/tidy-downloads.sh            # dry run: review the output
DRY=0 ~/tidy-downloads.sh      # apply it
```

If your terminal shows "Operation not permitted", go to **System Settings → Privacy & Security → Full Disk Access** and enable your terminal app.

## Assumptions

1. Same name with "(1)", same size and same date means a likely duplicate. The script still checks the contents before trashing anything.
2. Installers are disposable once the app is in `/Applications`. If you keep installers on purpose, for example for offline installs, delete the `installer` lines.
3. Your personal files belong in `~/Documents` and `~/Pictures` under the folder names above. Change `D` and `P` in the script if you use a different layout.
4. The script never overwrites a file. If a destination already has a file with the same name, it tells you and leaves your file in Downloads.

## Expected result

- **Space freed:** about 98 MB from the duplicate Docker image, rising to about 384 MB if Docker, Figma and Zoom are all installed. Empty the Trash afterwards to actually free it.
- **Downloads afterwards:** only `tenancy-agreement.pdf.download`, plus `Installers/` for any apps you haven't installed.

## Security notes

- **Passport and P60:** if your Documents folder syncs to iCloud ("Desktop & Documents Folders" is turned on), these will be uploaded. For better protection, store them in an encrypted disk image (Disk Utility → File → New Image → Blank Image, with AES-256 encryption) or a password manager's secure file storage.
- **Old boarding pass:** the trip was in September, and boarding pass barcodes contain booking details. Consider deleting it rather than filing it.
