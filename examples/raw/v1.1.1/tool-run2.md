# Run with shell tools offered

Task: `/deeper111 Evaluate the typesetting of my book manuscript and improve it. The inner margins look exceedingly large.`

## Commands it ran

```
cd <test folder> 2>/dev/null || cd <test folder>; pwd; find . -path ./.claude -prune -o -type f -print | head -50; which pdfinfo pdffonts qpdf xelatex lualatex pandoc typst 2>/dev/null
```

## Reply

[name], here's the deeper version before anything gets touched.

One thing first: there's no manuscript in this folder. The only files are `run1.jsonl` and `run2.jsonl`, which aren't a book. The machine does have `xelatex`/`lualatex` (TeX Live 2025 basic), `typst`, `pandoc`, `pdfinfo` and `pdffonts`.

**1. What a top book typographer would do that you didn't ask for**
The field is book typography and print production (prepress). Two things set the expert apart:
- **They judge margins on the two-page spread, at actual trim size, against the binding.** On a single page in a PDF viewer the inner margin can look huge. On a spread, the two inner margins together form the gutter, and the classical proportions (2:3:4:6 inner/top/outer/bottom) make the inner margin the smallest of the four. The gutter also has to grow with page count, because perfect binding swallows paper into the spine. So "too large" needs a diagnosis. The usual causes are a one-sided layout with a binding offset, margins that don't mirror between left and right pages, a trim size that doesn't match the page size, or a gutter allowance added twice.
- **They size the margins from the text block.** That means a line of about 60–75 characters at the chosen point size and leading, with the block sitting where the page proportions put it. While they're in there they also clear what spoils a text page: widows, orphans, rivers, and lines that overflow the margin or are stretched loose.

**2. The rawest material**
- The source files (LaTeX, Typst, InDesign or Word), especially the geometry and class settings. A PDF export is not enough.
- The printer's spec sheet: trim size, binding method, page count, paper thickness, and minimum gutter.
- A physical proof.
- What's missing here: all of it. I need the source and the PDF, and the name of the printer or the platform (KDP, IngramSpark, a local press).
- The assumption this could disprove: that the inner margins really are too large. They may be correct for a bound spread, or the size may be a symptom of a one-sided layout, in which case the fix is structural rather than a smaller number.

**3. Methods and tools**
- **Measure the PDF by machine, not by eye.** Read the page boxes (MediaBox, TrimBox, BleedBox) and the bounds of the text block on left and right pages separately, in millimetres.
- **Render spreads to images at 100% scale.**
- **Fix it in the source:** the layout settings in LaTeX or Typst, or InDesign's master pages. That beats patching the PDF.
- **Preflight** with the printer's own checker: the KDP or IngramSpark previewer, or Acrobat Preflight or callas pdfToolbox if you have them.

Here already: `pdfinfo`, `pdffonts`, `xelatex`/`lualatex`, `typst`, `pandoc`. Not here: a professional preflight tool. I haven't checked whether Poppler's `pdftoppm` is installed.

Installed skills that fit:
- `anthropic-skills:pdf` for measuring and rendering the PDF.
- `anthropic-skills:docx`, only if the source is Word.

Subagent: a general-purpose agent to re-measure the revised PDF independently. For more skills, try "book typesetting" or "LaTeX book typography" on https://skills.sh.

**4. What would show it's right, apart from you or me**
- **Measurements:** left and right pages mirror within ±0.5 mm. The inner margin is the smallest of the four and is at least the printer's minimum gutter for this page count. Lines average 60–75 characters.
- **LaTeX log, if the book is in LaTeX:** zero overfull boxes. Across the book: zero widows and orphans.
- **Fonts:** `pdffonts` shows every font embedded.
- **Printer:** the preflight or previewer passes with no warnings.
- **Physical proof:** a printed and folded spread at 100% shows no text lost in the spine and no gutter that looks too wide.

A fail is any of: a margin that doesn't mirror, a gutter under the printer's minimum, a preflight warning, or text running into the spine on the proof.

**Deliverables your task asks for:** an evaluation of the typesetting, and an improved typeset manuscript.

```
Evaluate and improve the typesetting of my book manuscript. Source and PDF: [PATH]. Printer/platform: [NAME], binding: [perfect/case], trim: [W×H], page count: [N]. My complaint: the inner margins look far too large.

Deliverable 1, the evaluation. Before judging anything, measure. Use the anthropic-skills:pdf skill with pdfinfo/pdffonts. Report:
- MediaBox, TrimBox and BleedBox against the stated trim size.
- The text-block bounds on left and right pages separately: inner, outer, top and bottom margins in mm.
- Whether the layout is one-sided or two-sided, and whether a binding offset is applied (read the source's layout settings).
- Average characters per line, point size and leading.
- Widows, orphans and overfull lines.
- Font embedding.
Render sample two-page spreads at 100% and judge the margins on the spread, against the classical proportions (inner smallest, about 2:3:4:6) and the printer's minimum gutter for this page count. Say whether the inner margins really are too large, or what actually causes the effect.

Deliverable 2, the improved manuscript. Fix the cause in the source, not by patching the PDF. Set the margins from the text block (60–75 characters per line) and the binding. Make left and right pages mirror. Clear widows, orphans and overfull boxes. Rebuild the PDF.

Verify before calling it done:
- Re-measure the new PDF, and have a general-purpose subagent repeat the measurement independently.
- Pass marks: left and right pages mirror within ±0.5 mm; inner margin is the smallest and at least the printer's minimum; 60–75 characters per line on average; zero overfull boxes, widows and orphans; all fonts embedded; the printer's preflight or previewer passes with no warnings.
- Give me one spread to print at 100% and fold as a physical proof.
Any failed mark means not done; report it with the numbers.
```

Worth knowing, not in this task: if the book will also be an ebook, the print margins and fixes don't carry over, so the EPUB needs its own pass.

Shall I run it once you've pointed me to the manuscript and the printer?
