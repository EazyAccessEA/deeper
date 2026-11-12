# downloads-plain-1

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

I can't see your Downloads folder directly; I only have the listing you pasted. So rather than claim I've moved anything, I've written a script you can review and run. It is deliberately cautious:

- **Nothing is permanently deleted.** Duplicates go to the Trash, so you can restore them.
- **Duplicates are only trashed if they are byte-for-byte identical.** Matching size and name isn't enough, so the script checks with `cmp`.
- **Nothing gets overwritten.** It uses `mv -n` and skips missing files.

## The plan

| Item | Action | Why |
|---|---|---|
| `Docker (1).dmg`, `Invoice-0412 (1).pdf`, `holiday-photos (1).zip`, `CV-2026 (1).docx` | Trash, **only if identical** to the original | Same size and date as the original, so almost certainly re-downloads |
| `Zoom.pkg`, `Docker.dmg`, `Figma-arm64.dmg` | → `Installers/` | Probably no longer needed once installed (see below) |
| Invoices, `P60-2025-26.pdf` | → `Documents/Finance/` | |
| `passport-scan.jpg` | → `Documents/Personal/` | Sensitive (see below) |
| `tenancy-agreement.pdf` | → `Documents/Housing/` | |
| `boarding-pass-LHR-LIS.pdf` | → `Documents/Travel/` | |
| `budget.xlsx`, `budget (1).xlsx` | → `Spreadsheets/`, **both kept** | Different sizes and dates, so `(1)` is a newer version, not a copy |
| Both `presentation-final*.key`, `CV-2026.docx` | → `Work/`, **both presentations kept** | v2 differs from the original |
| Screenshots | → `Screenshots/` | |
| `holiday-photos/` folder and `holiday-photos.zip` | → `Photos/` | Zip kept, since I can't confirm the folder holds everything |
| `tenancy-agreement.pdf.download` | **Left in place** | An unfinished Safari download (see below) |

## The script

Save it as `~/tidy-downloads.sh`, read it over, then run `zsh ~/tidy-downloads.sh`:

```zsh
#!/bin/zsh
set -u
cd ~/Downloads || { echo "No ~/Downloads"; exit 1; }

# Trash $1 only if it is byte-identical to $2
trash_if_dup() {
  if [[ -f "$1" && -f "$2" ]] && cmp -s "$1" "$2"; then
    if [[ -e ~/.Trash/"$1" ]]; then
      echo "KEPT (same name already in Trash): $1"
    else
      mv -n "$1" ~/.Trash/ && echo "Trashed duplicate: $1"
    fi
  else
    echo "KEPT (not identical, or missing): $1"
  fi
}

# Move each existing item into $1, never overwriting
move() {
  local dest="$1"; shift
  mkdir -p "$dest"
  for f in "$@"; do
    if [[ -e "$f" ]]; then
      if [[ -e "$dest/${f:t}" ]]; then
        echo "SKIPPED (already exists in $dest): $f"
      else
        mv -n "$f" "$dest/" && echo "Moved: $f -> $dest/"
      fi
    fi
  done
}

# 1. Exact duplicates -> Trash
trash_if_dup "Docker (1).dmg"         "Docker.dmg"
trash_if_dup "Invoice-0412 (1).pdf"   "Invoice-0412.pdf"
trash_if_dup "holiday-photos (1).zip" "holiday-photos.zip"
trash_if_dup "CV-2026 (1).docx"       "CV-2026.docx"

# 2. Sort into folders
move Installers          Zoom.pkg Docker.dmg "Docker (1).dmg" Figma-arm64.dmg
move Documents/Finance   Invoice-0412.pdf "Invoice-0412 (1).pdf" Invoice-0517.pdf P60-2025-26.pdf
move Documents/Personal  passport-scan.jpg
move Documents/Housing   tenancy-agreement.pdf
move Documents/Travel    boarding-pass-LHR-LIS.pdf
move Spreadsheets        budget.xlsx "budget (1).xlsx"
move Work                presentation-final.key presentation-final-v2.key CV-2026.docx "CV-2026 (1).docx"
move Screenshots         Screenshot\ *.png(N)
move Photos              holiday-photos holiday-photos.zip "holiday-photos (1).zip"

echo "\nLeft in place on purpose:"
ls -d *.download(N) 2>/dev/null
```

Any `(1)` file that turns out *not* to be identical won't be trashed. It gets filed next to its original instead, so nothing is lost.

## Assumptions and things to check yourself

1. **`tenancy-agreement.pdf.download`** is Safari's marker for an unfinished download. It's dated 20 Aug and is slightly bigger than the finished PDF from 11 Jul, so it may be a *different, newer* version that never finished downloading. Check whether you need a fresh copy before trashing it.
2. **Installers:** if Docker, Figma and Zoom are already in `/Applications`, you can trash the whole `Installers/` folder and free about 285 MB. Docker and Figma also go out of date quickly, so it's better to download fresh installers later anyway.
3. **`passport-scan.jpg`:** I've only filed it. Consider moving it into an encrypted location (for example an encrypted disk image or a password manager), not leaving it in Downloads.
4. **`holiday-photos.zip`:** once you've checked that the `holiday-photos/` folder contains everything, you can trash the zip.
5. **`budget (1).xlsx`** is newer than `budget.xlsx`. If it's the current version, consider renaming it (for example to `budget-2026-09.xlsx`) and archiving or trashing the older one.
6. **Boarding pass** (20 Sep) is likely for a past trip and could be trashed if you don't need it for expenses.
