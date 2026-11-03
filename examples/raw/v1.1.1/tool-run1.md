# Run with shell tools offered

Task: `/deeper111 Evaluate the typesetting of my book manuscript and improve it. The inner margins look exceedingly large.`

## Commands it ran

```
cd <test folder> && find . -not -path './.claude/*' -type f | head -50; which pdfinfo pdffonts qpdf mutool lualatex xelatex typst pandoc 2>/dev/null
```

```
pwd; ls -la; find . -maxdepth 3 -not -path '*/.claude/*' -type f | head -50
```

```
head -c 600 run1.jsonl; echo; grep -o '"[^"]*\.\(pdf\|tex\|typ\|docx\|indd\|idml\)"' run1.jsonl | sort -u | head
```

## Reply

[name], I couldn't find the manuscript. The only file in this folder is `run1.jsonl`, which is a session log. There's no PDF, `.tex`, `.typ`, `.docx` or InDesign file here. These typesetting tools are installed: `pdfinfo`, `pdffonts`, `typst`, `lualatex`, `xelatex` and `pandoc`.

**1. What a top book designer would do.** The field is book typography and prepress.
- **Judge the margins on the open two-page spread at print size, not one page at a time.** The classical page layouts put the inner margin at about half the outer margin. That way the two inner margins together equal one outer margin across the spread. Perfect binding then hides part of the gutter, and how much depends on page count. So an inner margin that looks huge on one page in a PDF viewer may be correct, too small, or not mirrored at all.
- **Design the text block first, then derive the margins from it.** Set line length (measure), leading and type size together, then fit the margins around that block. Nudging one margin on its own skews the line length.

**2. The rawest material.** None of it is here yet:
- the source file
- the exported print PDF
- the printer's spec: trim size, binding, final page count, paper
- the printer's own gutter table (KDP's minimum grows from 0.375 in at 24–150 pages to 0.875 in at 701–828 pages)

**This material could disprove that the inner margin is too large.** It may be exactly the printer's minimum gutter for your page count. Or the real fault may be margins that don't alternate between left and right pages.

**3. Methods and tools.**
- Poppler (`pdfinfo`, `pdffonts`, `pdftotext`) to measure page box sizes, check fonts are embedded and count characters per line. Installed.
- The source engine for the rebuild: LaTeX with the `geometry` and `microtype` packages, or Typst. Both are installed. If the source is InDesign or Word, the fix happens in that program, which I can't run here.
- The printer's preflight: KDP's print previewer or IngramSpark's file validation. Not here; it needs your account.
- Installed skills that fit: `anthropic-skills:pdf` and `anthropic-skills:docx`. `impeccable-reference` covers type scale but is web-oriented, so it's a weak fit.
- Subagents on offer: `general-purpose` and `Explore`.
- To look for on skills.sh: "book typesetting", "latex book design", "kdp print formatting".

**4. What would show the result is right, other than you or me.**
- The printer's preflight passes with no warnings.
- A bound proof copy, held open: no text lost in the gutter, and the spread looks balanced.
- Measured numbers:
  - inner margin at or above the printer's minimum for the page count
  - 45–75 characters per line, ideally around 60–70
  - every font embedded
  - margins alternate correctly on every page
  - zero widows and orphans
  - zero overfull lines in the LaTeX log

It fails if any one of these misses.

**Deliverables your task asks for:** (1) an evaluation of the typesetting, (2) an improved typeset manuscript.

```
Evaluate and improve the typesetting of my book manuscript. I think the inner margins look too large.

Inputs I'll supply: the source file (path: ___), the current print PDF (path: ___), the printer (KDP / IngramSpark / other: ___), trim size, binding type, paper, and final page count.

1. Evaluate (deliverable 1): Use the anthropic-skills:pdf skill and poppler (pdfinfo, pdffonts, pdftotext; render pages with pdftoppm). Measure from the PDF, don't eyeball it:
   - trim and page boxes
   - inner, outer, top and bottom margins on odd and even pages, to confirm they alternate correctly
   - inner margin against the printer's published minimum gutter for this page count
   - characters per line
   - leading against type size
   - fonts embedded or not
   - widows, orphans and overfull lines
   Judge the margins on the open two-page spread at print size, not on single pages. First say whether the inner margin really is too large, or only looks large because the page is viewed on its own, or is actually at the printer's minimum. Report every measurement as a number.
2. Improve (deliverable 2): Work in the original source (LaTeX with geometry and microtype, or Typst, or the native app if it's InDesign or Word, using anthropic-skills:docx for Word). Set the text block first: measure at 60–70 characters, leading and type size together. Then derive margins that alternate between left and right pages. Make the inner margin the printer's minimum gutter for this page count plus the binding loss, and keep the spread balanced. Don't move a margin on its own.
3. Verify against an external standard. It passes only if:
   - the printer's preflight passes with no warnings
   - the inner margin is at or above the printer's minimum for this page count
   - every line is 45–75 characters
   - every font is embedded
   - margins alternate correctly on every page
   - there are zero widows, orphans and overfull lines
   Any miss is a fail; fix it and re-measure. Show before and after numbers in a table. Finally, tell me to order a bound proof and check the gutter with the book held open, because no screen check replaces that.
```

Worth knowing, not in this task: a one-page house style sheet (type, measure, margins and spacing rules) would keep later editions and reprints consistent.

Shall I run it? If so, point me to the manuscript and tell me which printer you're using.
