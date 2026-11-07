# 01 — Method and steps

A complete, chronological record of how the investigation was actually done: what was inspected, in what order, with which tools, and what went wrong.

---

## Step 0 — Framing

The question was set as three separable questions, because most of the confusion in the literature comes from merging them:

1. **Exegetical:** did Paul require, permit, or say nothing about the face?
2. **Historical:** did Christians in fact cover the face as part of this practice?
3. **Normative:** ought face covering to be included in "the head covering"?

The working rule was that a claim only counts if it can be tied to a text, an image, an artefact, or a named scholar's argument — and that "the text does not mention X" is evidence about what is *required*, not about what is *permitted*.

---

## Step 1 — Corpus inventory

**Command used:** PowerShell `Get-ChildItem -Recurse` over `C:\Users\Admin\Documents\Early Christianity\Head Coverings`, grouped by extension. (The `glob` and `read` tools were used for files thereafter.)

**Result at the top level:**

| Extension | Count | Size |
|---|---|---|
| .png | 582 | 256.8 MB |
| .txt | 200 | 26.4 MB |
| .pdf | 112 | 434.3 MB |
| .json | 105 | 0.8 MB |
| .md | 83 | 0.4 MB |
| .docx | 2 | 0.1 MB |
| other | 3 | 0.9 MB |
| **Total** | **1,087** | **719.6 MB** |

**Structural findings:**

- The root holds ~150 named sources (commentaries, journal articles, theses, source compilations) as .txt and/or .pdf.
- `18 and 19th Century\` holds six older commentaries (Alford, Edwards, Godet, Hodge, Meyer, Stanley) as .txt.
- `headcover\` is a separate Obsidian-style wiki with three layers: `raw/sources/` (123 .txt), `wiki/sources/` (74 .md summaries), and `.llm-wiki/` (87 history JSON files, ingest queues, chat sessions). The `wiki/` layer was mostly stubs — only the index and a couple of concept pages had content — so the `raw/` and root .txt files were the real evidence base.
- `media/` holds 582 PNG page-images belonging to the PDFs. These were **not** used for OCR: 110 of the 112 PDFs already carried a text layer.
- Some pre-built research aids existed in the root and were used as leads, not as authorities: `Scholarly Remarks.txt` (a curated quote sheet), `Pro-Veiling Sources.txt` (~1,000 lines of pro-practice quotations), `Anti Veiling Sources.txt`, `NT LEXICON HEAD COVERINGS.txt` (a BDAG placement table), `NT CROSS REFERENCES HEAD COVERINGS.txt`, `Native Greek.txt` (the Greek text of 1 Cor 11:1–16), `Prostitutes Lie Orgins.txt` (a source-genealogy of the "only prostitutes went unveiled" claim), and `Evidence ledger — Why Christian Hea.txt` (the output of the preceding turn's work).

**Deliberate exclusions:** the `.llm-wiki/history` and `chats` JSON were not mined for arguments. They record earlier AI sessions, not evidence, and using them would have introduced circularity.

---

## Step 2 — PDF text extraction

**Tool:** Python 3.12 with PyMuPDF (`fitz`) 1.28. Script saved at `scripts/extract_pdfs.py`.

**Method:** walk the corpus, skip `media/`, `.cache/`, `.obsidian/`, `.llm-wiki/`; for every .pdf, extract per-page text with a `[[p.N]]` marker before each page; write to a flat directory of sanitised filenames; record pages/chars/errors in `_report.json`.

**Result:** 112 PDFs processed.

- **110** produced usable text.
- **2** produced almost none (both copies of the 1993 Jervis article — a scanned image PDF; its argument was recoverable from the .txt twin in the root, so this did not affect the findings).
- The BDAG PDF extracted as a 9.8 MB text file (126,815 lines), which made direct lexical checking possible.

**Output directory:** `hc_extract/`, with `_report.json` (copied here as `data/pdf-extraction-report.json`).

**Known artefact:** two Massey PDFs contained NUL bytes and needed null-stripping before grep; a cleaned copy was used for those checks.

---

## Step 3 — Systematic scan for face-and-veil co-occurrence

**Purpose:** reduce 272 unique text files to the passages where "face" and "covering/veil" actually occur near each other, so that the reading could be targeted rather than exhaustive.

**Tool:** Python regex scan. Script saved at `scripts/scan_face_contexts.py`.

**Method:**

1. Collect all `.txt` and `.md` files, skipping duplicates (`raw/` mirrors the root) and de-duplicating by size + first 200 characters → **272 unique files**.
2. Normalise whitespace.
3. Find every occurrence of the face-family terms — `face|faces|facial|visage|countenance|πρόσωπ|prosōp|prosop|faciem|vultus` — and keep a ±300-character window only where a covering-family term also appears in that window: `veil|cover|kalupt|καλυπτ|kalumm|καλυμμ|mantle|shawl|hood|wrap`.
4. Merge overlapping windows.

**Result:** **944 raw contexts**, reduced to **498 merged contexts across 76 files**.

**Distribution (top files):**

| Contexts | File |
|---|---|
| 46 | Nõmmik 2025, *Robes, Romans, and Rituals* |
| 30 | Wu 2020, *The Veil in Classical Antiquity* |
| 29 | Smith 2014, *Female Head Covering in the Early Imperial Period* |
| 20 | Hallmann (ed.) 2025, *Outward Appearance vs Inward Significance* |
| 19 | Burghartz 2015, *Covered Women* |
| 18 | Harris, Brøns & Żuchowska (eds) 2022, *Textiles in Ancient Mediterranean Iconography* |
| 15 | BDAG; *Covered Glory*; Edmondson & Keith 2015; Galter 2021 |
| 14 | Marlowe 2005, *Headcovering Customs of the Ancient World* |
| 12 | Calef & Simkins 2009; Curtis (Montier), *Let Her Be Shorn*; Massey 2018; Upson-Saia 2011 |
| 11 | Payne 2015; Leone 2012; Radle 2019; Stafford 2024 |

**Limitation:** a keyword scan finds *discussions* of the face, not every implicit assumption. Commentaries that simply assume a head-cloth and never say "face" (Barrett, Fee, Thiselton) barely register. That gap was filled by the targeted commentary sweep (subagent C).

---

## Step 4 — Targeted deep reading

The scan output was read selectively, then the highest-value sources were read directly at the relevant sections:

| Source | What was read | Why |
|---|---|---|
| Nõmmik 2025 (997 KB) | Introduction (§1.2–1.6), the 11:10 discussion (pp. 300–303), the Clement section (pp. 301–305), the Conclusions (pp. 317–320) | The only source in the corpus that reconstructs *how the face reading arose* |
| Wu 2020 (584 KB) | Introduction and ch. 1 (Greek veils), ch. 2 (Roman dress), ch. 5 (exegesis) | Definitional breadth and the Greek evidence |
| Smith 2014 (283 KB) | Terminology chapter (pp. 19–21), Roman matron section (pp. 54–69), the *flammeum* (p. 66) | The best treatment of what "veil" means in the Roman world |
| Stafford 2024 | The visual-corpus sections (pp. 14–18, 37) | The largest art-historical survey in the corpus |
| Upson-Saia 2011 (536 KB) | Ch. 3 on Tertullian and the Carthaginian virgins | The social context of the Tertullian evidence |
| Kovacs 2005 | The 1 Cor 11 catena (pp. 177–183) | What the Greek Fathers actually said |
| Marlowe 2005 | pp. 3–11 (Greek and Roman customs; the Jeremias material; the argument from silence) | The most direct treatment in the corpus |
| BDAG | The entries for `κατακαλύπτω`, `κάλυμμα`, `περίβολον`, `ἐξουσία`, `κεφαλή`, `περίβολαιον` | Lexical control |
| Oxford Bible Commentary | pp. 1125–1126 | A mainstream commentary that *allows* face covering |

---

## Step 5 — External checks of primary texts

The corpus contains many quotations of primary texts but few full texts. The following were checked externally:

| Text | Check | Result |
|---|---|---|
| Tertullian, *De virginibus velandis* 17 | Full English text at New Advent (ANF vol. 4) | Confirmed: the Arab women "cover not only the head, but the face also ... with one eye free"; confirmed that Tertullian defines the veil's extent by the hairline, and that he is arguing against Christian women who were *not* covering as he wished |
| Didascalia Apostolorum 1.8–9 | Gibson's English translation (Syriac Didascalia, online) | Confirmed: "cover thy head with thy robe ... And adorn not thy natural face; but walk with downcast looks, being veiled"; "if thou coverest thy face from strange men with a veil of modesty" |
| Clement of Alexandria, *Paedagogus* | Gutenberg/ANF text attempted; the relevant books were not in the fetched volume | Not independently collated; relied on the quotations in Nõmmik (pp. 301–302) and Leone (p. 281 n.22), both of which quote the Greek and give the reference |
| 1 Cor 11:10 variant | Nõmmik's manuscript discussion (pp. 300–301); BDAG s.v. `κάλυμμα`; Héring (p. 108); Fee (p. 518 n.27) | Confirmed: no early Greek MS reads `κάλυμμα`; the reading is in later Latin and Bohairic witnesses and in patristic citations (Irenaeus, "Hippolytus") |
| BDAG entries | Direct extraction from the 9.8 MB BDAG text file | Verified verbatim (see `02-text-and-lexis.md`) |
| LXX Gen 38:15 | BDAG cites it at 11:7 as an accusative-of-specification parallel | Confirmed as cited; the LXX text itself was not separately collated |
| Mishnah *Shabbat* 6:6 | Via Edmondson & Keith 2015, p. 26 | Secondary; not independently checked against a Mishnah edition |

**Failed or abandoned checks:** the Clement Gutenberg fetch returned only Book I; the *Stromata* and *Paedagogus* III sections needed were not retrieved. The LXX book of Genesis was not fetched in a usable form (the interlinear pages render via JavaScript). Both gaps are marked in the bibliography.

---

## Step 6 — Delegation to four subagents

Because the corpus is larger than one context window, four parallel subagents were given disjoint reading assignments with a common output contract: neutral reporting, verbatim quotes of ≤25 words with page locators, explicit separation of **evidence** from **interpretation**, and explicit reporting of disagreement.

| Agent | Assignment | Files |
|---|---|---|
| A | Greco-Roman and Corinthian practice, art and archaeology | Smith 2014, Stafford 2024, Harris 2022, Edmondson & Keith 2015, Marlowe 2005, Oster 1988, Gill 1990, Massey 2015/2018 |
| B | Patristic and later Christian practice | Upson-Saia 2011, Leone 2012, Radle 2019, Harmon (mislabelled — see below), Burghartz 2015, Galter 2021, *Covered Glory*, Kovacs 2005, Bray & Oden 2006 |
| C | Lexica and commentaries | BDAG, Barrett, Conzelmann, Fee (1987 and 2014), Thiselton, Hays, Morris, Héring, Meyer, Godet, Edwards, Alford, Stanley, Hodge, Chadwick, Curtis, Massey 2018, Humann, Hoelke, Oster, Peters, Blomberg, Johnson, Oxford, Keener, Ciampa/Rosner, Reasoner |
| D | Modern debate and reception history | Nõmmik 2025, Wu 2020, Payne, Lakey, BeDuhn, Callon, Marshall, Leone, Calef & Simkins, Martin, *Pro-Veiling Sources*, *Anti Veiling Sources*, *Head Covering Bingo*, *Prostitutes Lie Orgins* |

The exact briefs and the full returned reports are reproduced in `08-subagent-briefs-and-reports.md`. Their findings were **not** taken on trust: the load-bearing quotations were re-checked against the source files (Step 7).

---

## Step 7 — Verification pass

Every quotation that carried weight in the final report was checked back against the corpus file or the external text:

| Quote / claim | Verified against | Result |
|---|---|---|
| BDAG: Theban women, "whole face ... as with a mask"; "veiled to the forehead" | BDAG text file, entry `κατακαλύπτω` (lines 67014–67027 of the extraction) | ✅ verbatim |
| BDAG: `κάλυμμα` as variant at 11:10 | BDAG entry | ✅ |
| Nõmmik: no early Greek MS reads `κάλυμμα`; the c. 190–220 shift | Nõmmik pp. 300–301 | ✅ |
| Massey n.12: Goulder argues the veil covers the face | Massey 2018, footnote 12 | ✅ |
| Stafford: three covering styles; no east/west difference | Stafford pp. 14, 18 | ✅ |
| Smith: Horace, "In a matron one can see only her face" | Smith p. 54 | ✅ |
| Oxford: himation "over the face as well"; women covered "heads and even their faces" | Oxford pp. 1125–1126 | ✅ |
| Conzelmann: "the head, and more particularly the face" | Conzelmann p. 187 | ✅ |
| Barrett: "not as a covering for the face" | Barrett p. 249 | ✅ |
| Keener: face veils "far to the east and in Arabia" | Keener pp. 90–94 | ✅ |
| Marlowe: "We would expect him to use a word ... for the face-covering ... but that is not the case here" | Marlowe p. 10 | ✅ |
| Marlowe: Jeremias' two-veil reconstruction | Marlowe p. 8 | ✅ (as reported by Marlowe) |
| Tertullian 17: Arab face-covering; veil measured by the hairline | New Advent ANF text | ✅ |
| Didascalia: head covered with the robe; face concealed | Gibson translation | ✅ |
| Radle: face references "quite rare"; Tertullian "does not advocate facial veils" | Radle pp. 1085 n.71, 1092 | ✅ |
| Héring: veil "conceal the hair and part of the face" | Héring p. 106 | ✅ |
| Fee 1987: `κατὰ κεφαλῆς ἔχων` = external cloth covering | Fee p. 506 | ✅ |
| Hays: "authority" does not mean "veil" | Hays p. 187 | ✅ (as reported) |
| Gill: Corinthian women's portraits mostly bare-headed | Gill p. 251 | ✅ (as reported) |

**Not re-verified (flagged):** a small number of subagent quotations from sources that were not independently opened in this pass — marked in the quote bank with `[secondary]`. None of them changes a verdict.

---

## Step 8 — Synthesis and writing

1. Claims were split into ten discrete, testable propositions (`07-claim-verdicts.md`).
2. Each was assigned a verdict and a confidence level, with the strongest opposing evidence recorded alongside it.
3. The report was written to state the verdict first, then the evidence, then the strongest counter-case, then the answer to the normative question.
4. This dossier was then assembled from the working files, the subagent reports, and the verification log.

---

## Errors, artefacts and limitations

1. **Mislabelled file.** The text named *"Harmon, S. — A Note on the Critical Use of Instrumenta for the Retrieval of Patristic Biblical Exegesis (2003)"* — in the root, in `raw/`, and in `hc_extract/` — actually contains **Curtis Montier, *Let Her Be Shorn* (2015)**. Harmon's article is not in the corpus. No finding is attributed to Harmon.
2. **Oster 1988 is abstract-only.** The file is the publisher's abstract, not the article. Oster's argument is reported here only through Gill and Massey.
3. **Two scanned PDFs** (Jervis 1993) had no text layer; the .txt twin was used instead.
4. **`raw/` duplicates the root.** 123 files in `raw/sources` mirror root .txt files; de-duplication was necessary before any frequency judgement.
5. **The keyword scan is biased toward explicit discussion.** Sources that assume a head-cloth without arguing about the face are under-represented in `data/face-context-index.csv`; the commentary sweep compensates.
6. **`Head Covering Bingo.md` is empty** (a placeholder with "Analysis not available"), and `Prostitutes Lie Orgins.txt` is a claim-genealogy, not a source of primary evidence.
7. **No first-century Corinthian evidence exists either way.** The negative result is itself a finding, not a gap that further reading of the same corpus could close.
