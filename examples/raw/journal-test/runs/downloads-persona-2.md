# downloads-persona-2

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

I don't have access to your Mac from here, so I've written the cleanup as a script you can run. It does a **dry run by default**, moves files to the **Trash** instead of deleting them, and checks that two files are byte-for-byte identical before trashing either one.

## The plan

| Action | Files | Why |
|---|---|---|
| **Trash, if identical** | `Docker (1).dmg`, `Invoice-0412 (1).pdf`, `holiday-photos (1).zip`, `CV-2026 (1).docx` | Same size and date as the original. `cmp` confirms they match first. |
| **Trash, if the app is installed** | `Docker.dmg`, `Figma-arm64.dmg`, `Zoom.pkg` | You don't need installers once the app is in `/Applications`. If the app isn't there, they go to an `Installers` folder. |
| **Keep both** | `budget.xlsx` / `budget (1).xlsx` | Different sizes and dates, so they're probably different versions. |
| **Keep both** | `presentation-final.key` / `presentation-final-v2.key` | Different versions. |
| **Leave in place and flag** | `tenancy-agreement.pdf.download` | An unfinished Safari download. It's newer and larger than the complete PDF, so it may be a revised agreement. |
| **Keep** | `holiday-photos.zip` plus the `holiday-photos` folder | I can't confirm the folder holds everything in the zip, and it only saves 1.5 MB. |
| **File into folders** | everything else | See the layout below. |

**Folder layout**, created in `~/Documents` (you can change this with `BASE`):
```
Finance/     Invoice-0412.pdf, Invoice-0517.pdf, P60-2025-26.pdf, budget*.xlsx
Personal/    passport-scan.jpg, tenancy-agreement.pdf   ← sensitive
Travel/      boarding-pass-LHR-LIS.pdf
Work/        presentation-final*.key, CV-2026.docx
Screenshots/ Screenshot *.png
Photos/      holiday-photos/, holiday-photos.zip
Installers/  only for installers whose app isn't installed
```

**Space recovered:** about 100 MB from duplicates, plus about 285 MB more if Docker, Figma and Zoom are installed. That's up to **about 385 MB**, freed once you empty the Trash.

## The script

Save it as `~/tidy-downloads.zsh`:

```zsh
#!/bin/zsh
# Tidy ~/Downloads. Dry run by default: DRY_RUN=0 zsh ~/tidy-downloads.zsh to apply.
set -euo pipefail
DRY_RUN=${DRY_RUN:-1}
BASE=${BASE:-$HOME/Documents}
cd ~/Downloads

run() { if (( DRY_RUN )); then print -r -- "[dry-run] ${(q)@}"; else "$@"; fi }

to_trash() {
  local f=$1
  [[ -e $f ]] || { print -r -- "skip (missing): $f"; return 0; }
  local dest="$HOME/.Trash/${f:t}"
  [[ -e $dest ]] && dest="$HOME/.Trash/${f:t:r} $(date +%s)${f:e:+.${f:e}}"
  run mv -n -- "$f" "$dest"
  print -r -- "→ Trash: $f"
}

trash_if_identical() {   # $1 = original to keep, $2 = suspected duplicate
  if [[ -f $1 && -f $2 ]] && cmp -s -- "$1" "$2"; then
    to_trash "$2"
  else
    print -r -- "KEEPING (not identical or missing): $2"
  fi
}

trash_installer_if_installed() {  # $1 = installer, $2 = app name
  [[ -e $1 ]] || return 0
  if [[ -d "/Applications/$2" ]]; then
    to_trash "$1"
  else
    file_into Installers "$1"
  fi
}

file_into() {
  local dir="$BASE/$1"; shift
  run mkdir -p -- "$dir"
  local f
  for f in "$@"; do
    if [[ -e $f ]]; then
      if [[ -e "$dir/${f:t}" ]]; then
        print -r -- "CONFLICT, left in Downloads: $f (already exists in $dir)"
      else
        run mv -n -- "$f" "$dir/"
        print -r -- "→ $1/: $f"
      fi
    else
      print -r -- "skip (missing): $f"
    fi
  done
}

print "== 1. Exact duplicates =="
trash_if_identical "Docker.dmg"           "Docker (1).dmg"
trash_if_identical "Invoice-0412.pdf"     "Invoice-0412 (1).pdf"
trash_if_identical "holiday-photos.zip"   "holiday-photos (1).zip"
trash_if_identical "CV-2026.docx"         "CV-2026 (1).docx"

print "\n== 2. Installers =="
trash_installer_if_installed "Docker.dmg"      "Docker.app"
trash_installer_if_installed "Figma-arm64.dmg" "Figma.app"
trash_installer_if_installed "Zoom.pkg"        "zoom.us.app"

print "\n== 3. Filing =="
file_into Finance     "Invoice-0412.pdf" "Invoice-0517.pdf" "P60-2025-26.pdf" "budget.xlsx" "budget (1).xlsx"
file_into Personal    "passport-scan.jpg" "tenancy-agreement.pdf"
file_into Travel      "boarding-pass-LHR-LIS.pdf"
file_into Work        "presentation-final.key" "presentation-final-v2.key" "CV-2026.docx"
file_into Screenshots Screenshot\ *.png(N)
file_into Photos      "holiday-photos" "holiday-photos.zip"

print "\n== Needs your attention =="
[[ -e "tenancy-agreement.pdf.download" ]] && print -r -- \
  "• tenancy-agreement.pdf.download is an unfinished download (20 Aug, newer than the PDF). Re-download it if it's a revised agreement, then trash it."
print "• budget.xlsx and budget (1).xlsx differ. Check which is current and consider renaming."
(( DRY_RUN )) && print "\nDry run only. Nothing changed. Re-run with DRY_RUN=0 to apply."
```

**To run it:**
```zsh
zsh ~/tidy-downloads.zsh             # preview
DRY_RUN=0 zsh ~/tidy-downloads.zsh   # apply
```
Everything goes to the Trash, so you can undo anything until you empty it. If Terminal is blocked from reading Downloads, go to System Settings → Privacy & Security → Files and Folders and allow it.

## Assumptions
1. **Same size and date means a likely duplicate**, but nothing is trashed unless `cmp` confirms the files are identical.
2. **The newer, larger budget and presentation files are different versions**, not duplicates, so both are kept.
3. **Installers aren't needed** once the matching app is in `/Applications`. You can download them again anytime.
4. **The `.download` file is an interrupted Safari download.** It can't be opened as-is, so it's flagged rather than trashed.
5. **Files go into `~/Documents`.** If "Desktop & Documents" iCloud syncing is on, they'll sync to iCloud, including your passport scan. Use `BASE=~/SomewhereElse` if you'd prefer not to.

## Recommendations
- **Sensitive files:** `passport-scan.jpg` and `P60-2025-26.pdf` (which includes your National Insurance number) are stored unencrypted. Consider moving them into an encrypted disk image (Disk Utility → File → New Image → Blank Image, with 256-bit AES encryption) or a password manager's secure storage. Empty the Trash afterwards.
- **Old items:** the boarding pass is from a September trip and the June/July screenshots are probably no longer needed. Review and delete them.
- **Stop screenshots landing in Downloads:** press ⌘⇧5 → Options → Save to, or run:
  ```zsh
  mkdir -p ~/Pictures/Screenshots && defaults write com.apple.screencapture location ~/Pictures/Screenshots && killall SystemUIServer
  ```
