# Design System: deeper

## 1. Visual Theme & Atmosphere

An editor's desk under cool daylight. Bright white page, black type, and one red pencil that only ever adds. The page is quiet and confident, with lots of white space and large, plain type; the only colour on it is what deeper inserts. Density: airy (3). Variance: offset (6), left-aligned, never centred heroes. Motion: restrained (3); one moment on load where the red insertions write in, and nothing loops.

The idea in one line: deeper marks up your request the way an expert editor would, inserting what's missing and leaving your scope alone.

## 2. Color Palette & Roles

- **Page White** (#FFFFFF): background of every section. Cool, never cream.
- **Margin Grey** (#F4F5F6): the one quiet surface, for code blocks and the demo's plain column.
- **Press Black** (#141414): all body text, headlines and the wordmark.
- **Graphite** (#5B5F66): secondary text and captions. 6.5:1 on white.
- **Rule Grey** (#E3E5E8): the few dividers that carry structure.
- **Proof Red** (#D0241B): the single accent. Used only for what deeper inserts: the caret, inserted words, the primary action and focus rings. 5.3:1 on white.

Dark mode: Night Page (#121212), Night Surface (#1C1C1C), Paper Ink (#EDEDED), Graphite (#A3A3A3), Proof Red Light (#FF5A4E).

## 3. Typography Rules

- **Everything:** Schibsted Grotesk. Headlines 600, tight tracking (-0.03em), large but calm (clamp 2.6rem to 4.5rem). Body 400 at 1.0625rem, line height 1.6, measure 36em.
- **Insertions:** Schibsted Grotesk italic 500 in Proof Red. This is how the page shows what deeper adds. No other italics.
- **Code:** JetBrains Mono, only inside real commands and prompts. Never for labels, nav or numbers in prose.
- **Banned:** Inter, Geist (the last version), any serif, any handwriting or marker font, all-caps labels, eyebrows above headings.

## 4. The mark

A filled caret (^) with a sharp mitred apex and flat, horizontal feet. On a 16 px grid it's 12 wide and 9 tall, with legs 3 px thick measured across the leg. In the wordmark it sits below the baseline, apex pointing up into the gap between "d" and "e", in Proof Red. The wordmark itself is lowercase "deeper" in Schibsted Grotesk 700, Press Black.

## 5. Component Stylings

- **Primary action:** the install command, in Press Black on Margin Grey, with a Proof Red "Copy" button. 4 px corners. Press: 1 px down.
- **Secondary action:** a plain text link with an underline, no box.
- **Demo:** your request in Press Black. deeper's insertions appear inline in red italic with a small red caret before each. Below, the full rewritten prompt in a Margin Grey block.
- **Cards:** none. Group with white space and the occasional Rule Grey line.
- **Tables:** numbers in tabular figures of Schibsted Grotesk, not mono.

## 6. Layout Principles

Left-aligned 12-column grid, max 72rem. Hero: headline and install on the left 7 columns, the hero image (a red pencil tip on white) on the right 5. Sections alternate width, never two identical layouts in a row. Collapses to one column below 768 px. Section gaps clamp(4rem, 9vw, 8rem).

## 7. Imagery

Photographs only, generated and kept in brand/plates: a red pencil on bright white paper, no text in frame, cool light. At most one image per section. Never paper texture as a background, never handwriting.

**Journal exception (13 Nov 2026):** journal pages may also use archival public-domain photographs and licensed stock, still at most one per section, never showing a face or an animal, each with a caption that tells the reader something. Licence records and the image files are kept outside this repo. Some stock licences forbid showing the files to an AI model, so those pages are checked by eye. Journal photos are shown in a three-tone map of the palette: ink, Proof Red, white.

## 8. Motion & Interaction

On load, the red insertions in the hero demo appear one by one (opacity and a 4 px rise, 120 ms apart). Hover: underline thickens. Everything collapses to static under prefers-reduced-motion.

## 9. Anti-Patterns (Banned)

- Strike-throughs, deletion marks, X shapes, erasers: deeper only inserts.
- Monospace labels, hairline grids, telemetry readouts, depth gauges, version stamps.
- Purple or blue gradients, glows, three equal feature cards.
- Cream or beige backgrounds, serif display type, terracotta.
- Invented numbers, logos of companies that don't use it, testimonials we don't have.
- Em dashes, eyebrow labels, "scroll to explore".
