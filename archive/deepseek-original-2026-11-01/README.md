# Face Covering Investigation — Research Dossier

**Question:** Did the "head covering" of 1 Corinthians 11:2–16 include covering the face?

**Date of investigation:** 1 November 2026
**Corpus:** `C:\Users\Admin\Documents\Early Christianity\Head Coverings` — 1,089 files (200 .txt, 112 .pdf, 83 .md, 105 .json, 582 .png, 3 .docx, plus misc; ≈720 MB as Windows reports it).
**Investigator:** AI research agent (DeepSeek Harness), working from the local corpus plus external checks of primary texts.
**Starting posture:** deliberately agnostic. No position was assumed; the verdicts below are where the evidence landed.

---

## Verdict in one paragraph

Paul commands a covering **on the head** and never mentions the face; the strongest single argument is that he uses the face-veil word (`κάλυμμα`) explicitly in 2 Corinthians 3 but not here. The Greek word he does use (`κατακαλύπτω`) is generic, so it does not *exclude* the face — it simply does not require it. Surrounding Greco-Roman practice normally left the face visible; face-covering was a marked, regional, or situational gesture. From about 190–200 CE some Christian writers (Clement of Alexandria first, then the Didascalia, Tertullian in a limited way, later Jerome and Ambrose) extended the practice to the face, and the reading was reinforced by a secondary textual variant at 11:10 (`κάλυμμα` for `ἐξουσία`). Face covering is therefore **not required, not forbidden, historically Christian, and not the default.**

---

## File map

| File | Contents |
|---|---|
| `README.md` | This index and the verdict summary |
| `01-method-and-steps.md` | Full chronological research log: inventory, PDF extraction, scanning, targeted reading, subagent delegation, verification, known errors |
| `02-text-and-lexis.md` | The Greek text, lemma-by-lemma lexical evidence, grammar, the 11:10 variant, LXX and 2 Cor 3 comparisons |
| `03-greco-roman-background.md` | Roman, Greek, Corinthian, Jewish and "eastern" evidence; art and iconography |
| `04-patristic-and-later-practice.md` | What Christian writers and churches actually did, with a dated timeline |
| `05-quote-bank.md` | **The selected scholarly quotes**, organised by topic, each with attribution and locator |
| `06-quote-bank.csv` | The same quote bank as a spreadsheet (sortable/filterable) |
| `07-claim-verdicts.md` | Ten discrete claims tested, with verdicts, confidence levels and reasoning |
| `08-subagent-method.md` | Why subagents were used, the exact briefs they received, how their output was verified, and where they disagreed |
| `subagents/` | The four full subagent reports, verbatim: `A-greco-roman.md`, `B-patristic.md`, `C-lexical-commentary.md`, `D-modern-debate.md` |
| `09-bibliography-and-corpus-manifest.md` | Bibliography of everything used, mapped to corpus filenames; corpus composition and gaps |
| `10-open-questions.md` | What remains unknown, what would overturn the verdicts, suggested next steps |
| `source-report.md` | The finished report as delivered to the user |
| `scripts/` | `extract_pdfs.py` (PDF text extraction), `scan_face_contexts.py` (face-and-veil context scan), `build_data.py` (CSV/JSON generation) — the work can be reproduced |
| `data/` | `quote-bank.csv` / `.json`, `face-context-index.csv`, `pdf-extraction-report.json`, `corpus-summary.txt` |

---

## A note on `hc_extract`

The PDFs were extracted to a working directory (`hc_extract/`) in the research session, with `[[p.N]]` page markers. That directory is **not** shipped here (it is ~30 MB of derived text). To rebuild it, run `scripts/extract_pdfs.py` after editing its two path variables. Page numbers in this dossier map to the `[[p.N]]` markers in those extracted files.

## How to use this dossier

- If you want **the argument**, read `source-report.md` then `07-claim-verdicts.md`.
- If you want **the evidence**, read `02`–`04`, then `05-quote-bank.md` for the quotations with page numbers.
- If you want **to check the work**, read `01-method-and-steps.md` and `08-subagent-method.md` (with the full reports in `subagents/`), then follow the corpus filenames in `09`.
- If you want **to push back**, read `10-open-questions.md` first.

## Confidence key

| Label | Meaning |
|---|---|
| **Very high** | ≈95%+ — the evidence is close to decisive |
| **High** | ≈80–95% — strong, with room for a dissent |
| **Probable** | ≈60–80% — the balance of evidence, not certainty |
| **Contested** | ≈40–60% — genuinely unresolved |

## One-line findings

1. `πρόσωπον` ("face") never occurs in 1 Cor 11:2–16. — *very high*
2. Paul's expressed object is `τὴν κεφαλήν`, the head. — *very high*
3. Paul uses `κάλυμμα` for a face-veil in 2 Cor 3:13–18 but not in 1 Cor 11. — *very high*
4. `κατακαλύπτω` does not exclude the face. — *very high*
5. The culture's default head-covering left the face open. — *high (Rome/Corinth), probable (Greek East)*
6. No first-century Corinthian evidence for Christian face-veils. — *high*
7. Face covering is first clearly required by Clement of Alexandria, c. 190–200. — *high*
8. The `κάλυμμα` reading at 11:10 is not in any early Greek manuscript. — *very high*
9. Face covering was never the universal Christian practice. — *high*
10. Face covering is not a later Islamic import; it has independent Christian attestation. — *high*
