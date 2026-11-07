# 09 — Bibliography and corpus manifest

## 1. The corpus

**Location:** `C:\Users\Admin\Documents\Early Christianity\Head Coverings`
**Files:** 1,089 (including hidden files)
**Composition:**

| Extension | Count | Notes |
|---|---|---|
| .png | 582 | page images belonging to the PDFs (in `media/` folders) — not used for OCR |
| .txt | 200 | the working texts |
| .pdf | 112 | 110 with a text layer |
| .json | 105 | mostly `headcover/.llm-wiki/` session data — not used as evidence |
| .md | 83 | wiki summaries, mostly stubs |
| .docx | 3 | two Word documents plus a lock file |
| other | 4 | .webp, .com, .log, .ini |

**Structural map:**

- **Root:** ~150 named sources — commentaries, journal articles, theses, source compilations — as .txt and/or .pdf.
- **`18 and 19th Century/`:** six older commentaries (Alford, Edwards, Godet, Hodge, Meyer, Stanley).
- **`headcover/raw/sources/`:** 123 .txt files mirroring the root.
- **`headcover/wiki/`:** 74 .md summary files; the index and two concept pages are the only substantive ones.
- **`headcover/.llm-wiki/`:** 87 history JSON files, ingest queues, chat sessions. **Not used as evidence** — these are records of earlier AI sessions, and relying on them would be circular.
- **`media/`:** 582 page images.

---

## 2. Primary sources

### Biblical and Second Temple

| Source | Used for | Access |
|---|---|---|
| 1 Cor 11:2–16 (Greek) | The text itself | `Native Greek.txt` (in corpus) |
| 2 Cor 3:12–18 | Paul's own face-veil vocabulary | Standard text |
| LXX Gen 38:15 | `καλύπτω` + `πρόσωπον` | Cited in BDAG, s.v. `κατακαλύπτω` |
| LXX Exod 34:33–35 | Moses' `κάλυμμα` | Cited in BDAG, s.v. `κάλυμμα` |
| LXX Isa 6:2 | `κατακαλύπτω` with faces | Cited in BDAG, s.v. `κατακαλύπτω` |
| Mishnah *Ketubbot* 7:6 | Jewish head-covering custom | Cited in Barrett 1962: 249 |
| Mishnah *Shabbat* 6:6 | "Arabian" veiling | Cited in Edmondson & Keith 2015: 26 |

### Greco-Roman

| Source | Used for | Access |
|---|---|---|
| Horace, *Satires* 1.2.94–100 | The matron's face visible | Quoted in Smith 2014: 54 |
| Seneca the Elder, *Controversiae* 2.7.6 | Face-covering as a discrete act | Quoted in Smith 2014: 86 |
| Valerius Maximus 6.3.10 | Divorce for uncovered head | Cited in Smith 2014: 13–14 |
| Plutarch, *Quaest. Rom.* 14 | Roman head-covering at worship | Cited in Smith 2014: 13–14 |
| Plutarch, *Caesar* 66, *Brutus* 17 | Scipio / Caesar head-and-face covering | Cited in Nõmmik 2025, ch. 2 |
| Virgil, *Aeneid* 3.403–409 | `capite velato` and omens | Cited in Nõmmik 2025, ch. 2 |
| Dionysius of Halicarnassus 15.9.2 | "drew his cloak down over his head" | Cited in Massey 2018: n.13 |
| Josephus, *J.W.* 7.128 | Vespasian veiled before prayer | Cited in Massey 2018: n.14 |
| Dio Chrysostom, *Or.* 33.48 | Tarsian women's full covering | Cited in Chadwick 2022: 7–8 |
| Ps.-Dicaearchus (in BDAG) | Theban head-covering over the whole face | BDAG 458 |

### Christian

| Source | Date | Used for | Access |
|---|---|---|---|
| *Shepherd of Hermas*, Vis. 4.2.1 | 2nd c. | "veiled to the forehead" | Quoted in the article under review; Greek lemma in BDAG 458 |
| Irenaeus, *Haer.* 1.8.2 | c. 180 | `κάλυμμα` at 11:10 | Cited in Nõmmik 2025: 300–301 |
| Clement, *Paedagogus* 2.10; 3.11 | c. 190–200 | First clear requirement of the face | Quoted in Nõmmik 2025: 301–302; Leone 2012: 281 n.22 |
| Tertullian, *De virginibus velandis* 15, 17 | c. 200–213 | Arab face-covering; veil measured by hairline | Full text checked at New Advent (ANF vol. 4) |
| "Hippolytus," *Comm. Dan.* | 3rd c. | `κάλυμμα` at 11:10 | Cited in Nõmmik 2025: 300–301 |
| *Didascalia Apostolorum* 1.8–9 | c. 230 | Head with robe; face concealed | Gibson translation (external) |
| Cyprian, *De habitu virginum* | c. 250 | Silence on veils | Cited in Nõmmik 2025: 309 |
| John Chrysostom, *Hom. 1 Cor.* 26 | c. 390 | Head only | Kovacs 2005: 179 |
| Theodoret, on 11:10 | c. 400 | "Paul calls the veil authority" | Kovacs 2005: 183 |
| Jerome, *Ep.* 130.18 | 414 | Face veil except the eyes | Cited in Radle 2019: 1086 n.77 |
| Ambrose, *De poenitentia* 1.14 | c. 390 | `caput` and `vultus` | Cited in Radle 2019: 1086 n.77 |
| Psellos, *Chronographia* | 11th c. | Face veil, elite | Cited in Radle 2019: 1091–1092 |
| Vecellio, *De gli habiti antichi* | 1590s | Venetian `fazzuolo`, `cappa` | Cited in Burghartz 2015: 4–5 |

---

## 3. Secondary sources

### A. Lexica and grammars

| Work | Corpus file |
|---|---|
| Bauer, Danker, Arndt & Gingrich, *A Greek-English Lexicon of the NT*, 3rd ed. (2000) | `Bauer, W., Danker, F. W., ... (2000). A Greek-English lexicon ... .pdf` |
| *The Concise New International Dictionary of NT Theology and Exegesis* (2021) | quoted in `Pro-Veiling Sources.txt` |

### B. Commentaries

| Work | Corpus file | Relevance |
|---|---|---|
| Barrett (1968) | `Barret, C.K. A commentary ... pp. 246-258.txt` | Explicitly "not ... the face" |
| Conzelmann (1975) | `Conzelmann, H - 1 Corinthians (1975) pp. 181-191.txt` | "head or face" |
| Fee (1987) | `Fee, G. - First Epistle ... (1987) ... .txt` | External cloth; variant note |
| Fee (2014) | `Fee, G - The First Epistle ... Revised Edition pp. 581-585 (2014).txt` | `περίβολαιον` as wrap |
| Thiselton (2000) | `Thiselton, The First Epistle ... p.828-929, 833-835.txt` | Head covering; postpones the hair question |
| Hays (2011) | `Hays, R - First Corinthians ... (2011).txt` | "authority" ≠ "veil" |
| Morris (1983) | `Morris, L. - The first epistle ... (1983).txt` | "bare-faced" idiom |
| Héring (1962) | `Héring, J. - The first epistle ... (1962).txt` | Hair and part of the face |
| Johnson (2004) | `Johnson. A.F. Corinthians 1 ... (2004).txt` | The hair thesis stated fairly |
| Blomberg (1994) | `Blomberg, C - 1 Corinthians ... (1994).txt` | Shawl over hair and shoulders |
| Keener (2005) | `Keener, C - 1-2 Corinthians ... (2005).txt` | Face veils in the east |
| Ciampa & Rosner (2010) | `Ciampa, R. E. Rosner, B. S. (2010) ... .txt` | Head rather than face |
| Oxford Bible Commentary (2001) | `Barton, John; Muddiman, John (2001) ... .txt` | Face allowed |
| Reasoner (2025) | `Reasoner, Mark - 1 Cor (2025).txt` | "leaves open the question" |
| Bray & Oden (2006) | `Bray and Oden - 1-2 Corinthians ... .txt` | Patristic catena; no face |
| Kovacs (2005) | `Kovacs, J - 1 Corinthians Interpreted ... .txt` | Patristic catena; no face |

### C. Nineteenth-century commentaries

| Work | Corpus file |
|---|---|
| Alford (1863) | `18 and 19th Century\Alford, H - THE NEW TESTAMENT ... (1863).txt` |
| Edwards (1835) | `18 and 19th Century\Edwards T.C. - A Commentary ... (1835).txt` |
| Godet (1889) | `18 and 19th Century\Godet, F. - Commentary ... (1889).txt` |
| Hodge (1874) | `18 and 19th Century\Hodge, C - An exposition ... (1874).txt` |
| Meyer (1884) | `18 and 19th Century\Meyer, H. A. W. - Critical Exegetical Handbook ... (1884).txt` |
| Stanley (1882) | `18 and 19th Century\Stanley, A. P. - The epistles ... (1882).txt` |

### D. Monographs and dissertations

| Work | Corpus file | Relevance |
|---|---|---|
| Nõmmik, *Robes, Romans, and Rituals in First Corinthians* (2025) | `Robes Romans and Rituals in First Corinthians – Aldar Nõmmik – 2025.pdf` | **The key source** for the reception history |
| Wu, *The Veil in Classical Antiquity* (2020) | `Wu, R. (2020). The veil in classical antiquity ... .pdf` | Greek and Roman veil; definitional breadth |
| Smith, *Female Head Covering in the Early Imperial Period* (2014) | `Smith, E - Female Head Covering in Early Imperial Period (2014).pdf` | Roman terminology and gestures |
| Upson-Saia, *Early Christian Dress* (2011) | `Upson-Saia, K. (2011). Early Christian dress ... .pdf` | Tertullian; Carthaginian context |
| Lakey, *Image and Glory of God* (2010) | `Lakey, M. J. (2010). Image and glory of God ... .pdf` | Hermeneutics; no face discussion |
| Martin, *The Corinthian Body* (1995) | `Martin, D. - The Corinthian Body (1995) pp. 229 Chapter 2 Prophylactic Veils.txt` | Functional/prophylactic reading |
| Kim, *The Significance of Clothing Imagery in the Pauline Corpus* (1998) | `Kim, Jung Hoon (1998) ... .pdf` | Clothing symbolism |
| Canavan, *Clothing the Body of Christ at Colossae* (2011) | `Canavan, R, Clothing the Body of Christ at Colossae (PhD 2011).pdf` | Dress context |

### E. Journal articles and chapters

| Work | Corpus file | Relevance |
|---|---|---|
| Gill, "Roman Portraiture ..." *TynBul* 41 (1990) | `Gill, D - Importance of Roman Portraiture ... (1990).pdf` | Corinthian portraits |
| Massey, "Veiling among Men ..." *JBL* 137 (2018) | `Massey, P. T. (2018). ... .pdf` | Lexical; Goulder footnote |
| Massey, "Dress codes at Roman Corinth ..." *JGRChJ* 11 (2015) | `Massey, P. T. (2015). ... .pdf` | Andania inscription |
| Stafford, "Veiling and Head-Covering in Late Antiquity," *P&P* 263 (2024) | `Stafford, G - Veiling and Head-Covering in Late Antiquity (2024).pdf` | Visual corpus |
| Radle, "The Veiling of Women in Byzantium," *Speculum* 94 (2019) | `Radle, G. (2019). ... .pdf` | Byzantine practice |
| Leone, "Cultures of Invisibility" (2012) | `Leone, M. (2012). ... .pdf` | Clement; semiotics |
| Chadwick, *Headdress or Hairstyle* (2022) | `Chadwick, C - Headdress or Hairstyle ... (2022).pdf` | Dio Chrysostom; Tarsus |
| Burghartz, "Covered Women" (2015) | `Burghartz, S - Covered women ... (2015).pdf` | Early modern Europe |
| Galter, "Veil and Headscarf" (2021) | `Galter, H. D. (2021). Veil and headscarf.pdf` | Ancient Near East |
| Oster, "When Men Wore Veils to Worship," *NTS* 34 (1988) | `Oster, R. E. (1988). ... .txt` (abstract only) | `capite velato` |
| Marshall, "Uncovering Traditions ..." *NovT* 61 (2019) | `Marshall, J - Uncovering Traditions ... (2019).pdf` | The referent is unclear |
| Callon, "Authority Over Whose Head?" *HTR* 117 (2024) | `Callon, C. (2024). ... .pdf` | Wives, not all women |
| Payne, *Man and Woman, One in Christ* (2015) | `Payne, P.B. - Man and Woman ... (2015).txt` | Hair thesis |
| BeDuhn, "Because of the Angels," *JBL* 118 (1999) | `BeDuhn, J. D. (1999). ... .pdf` | Veil as marital marker |
| Martin / Harris / Edmondson & Keith (eds) | see corpus | Dress and iconography |

### F. Reference and popular works (used with caution)

| Work | Corpus file | Note |
|---|---|---|
| *Covered Glory* | `Covered Glory.pdf` | Popular tract; not peer-reviewed |
| *Pro-Veiling Sources.txt* | root | Compilation; useful as a lead, not an authority |
| *Anti Veiling Sources.txt* | root | Compilation; same |
| *Head Covering Bingo.docx* | root | Empty placeholder |
| *Prostitutes Lie Orgins.txt* | root | Source-genealogy of a claim; useful historiographically |

---

## 4. Works consulted but not used

- **Harnack, *Mission and Expansion*** — background only.
- **Various studies on hairstyles, headship, gender semantics** (Payne, Lakey, BeDuhn, Callon, Townsley, Jervis, Mount, Watson) — read for the face question, but they either do not address it or treat it only in passing. They are relevant to the *other* debates in 1 Cor 11 (headship, hair, silence), not to this one.
- **Modern African and Asian contextual studies** (Kügler et al.; Telhalia et al.; Odafe) — modern application, not historical evidence.
- **Hallmann (ed.) 2025; Harris et al. 2022** — dress and iconography generally; only a few passages bear on veils.

---

## 5. Gaps in the corpus

| Gap | Consequence |
|---|---|
| No full text of Oster 1988 | His argument is known only via Gill and Massey |
| No full text of Clement's *Paedagogus* | The Clement quotations are via Nõmmik and Leone |
| No Mishnah or LXX critical text | Jewish and LXX data are second-hand |
| No systematic art-historical database coded for face visibility | The art argument rests on Stafford, Gill and Marlowe |
| Almost no first-century Corinthian material culture | The Corinthian question cannot be settled from this corpus |
| The `wiki/` layer is mostly stubs | The `raw/` and root files were used instead |

---

## 6. How to find a source in the corpus

1. Use the **corpus file** column in `05-quote-bank.md` or `06-quote-bank.csv`.
2. For PDFs, the extracted text is at `hc_extract/<sanitised name>.txt` with `[[p.N]]` page markers, so a page number in this dossier maps directly to a `[[p.N]]` block.
3. For the root .txt files, page numbers come from the printed edition and are usually embedded in the text.
4. To reproduce the extraction, run `scripts/extract_pdfs.py`; to reproduce the scan, run `scripts/scan_face_contexts.py`.
