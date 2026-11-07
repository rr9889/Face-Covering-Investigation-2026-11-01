# 11 — Independent audit of the DeepSeek dossier (7 November 2026)

**What this is:** a second-pass check of the dossier produced on 1 November 2026 by the DeepSeek Harness agent. Every load-bearing claim was traced back to the corpus or to a primary text. Where the original was wrong, it is corrected here and flagged in the original file with an `[Audit 2026-11-07]` note. The untouched originals are preserved in `archive/deepseek-original-2026-11-01/`.

**Auditor's posture:** no preferred answer. The audit asks only whether each conclusion follows from the evidence actually cited, and whether evidence pointing the other way was looked for with equal effort.

**Tools:** all 112 corpus PDFs were re-extracted (`scripts/extract_pdfs_audit.py`, PyMuPDF; 110 with usable text, the same 2 scanned Jervis files empty). Searches used a whitespace-normalised keyword-in-context tool (`scripts/kwic.py`), which finds matches that span PDF line breaks. Primary texts not in the corpus were checked online. The source of each check is given below.

---

## Summary

The dossier's broad picture survives: Paul names the head, never the face; face-covering is explicitly attested in Christian sources from Clement of Alexandria (c. 195) onward. But the dossier repeatedly **moved from "not stated" to "excluded"**, **used a mistaken lexical premise as its "strongest argument"**, **coded silent sources as supporting one side**, and **under-collected the evidence that pointed toward face-covering**. The net effect is a verdict stated with more confidence, and tilted further toward "face open", than its own evidence supports.

| # | Problem | Severity | Status |
|---|---|---|---|
| A1 | "Strongest argument" rests on a false premise: `κάλυμμα` is not a face-veil word | **High** | Verified against BDAG |
| A2 | LXX Gen 38:15 misquoted (`ἐκάλυψεν`); actual text uses Paul's own verb, middle voice, with "face" as object | **High** | Verified (LXX) |
| A3 | Claim that Isa 6:2 is "the one place" the verb takes "face" as object is false; no LXX concordance was done | **High** | Verified (full LXX list, `data/lxx-katakalypto-concordance.csv`) |
| A4 | Chrysostom and Theodoret coded "head only"; both are silent on the face, and Chrysostom stresses wrapping "on every side" | **High** | Verified (NPNF Hom. 26 on 1 Cor; Kovacs 2005) |
| A5 | Chrysostom and Theodoret called "the earliest" writers; they are c. 390–450, two centuries after Clement and Tertullian | Medium | Verified (dates) |
| A6 | Claim 8 ("head covering and face covering are not the same") contradicted by the dossier's own BDAG evidence | Medium | Verified against BDAG (Ps.-Dicaearchus) |
| A7 | Greek-East face-veil evidence under-reported: Llewellyn-Jones presented only through his critic; tegidion, Chalcedon and Thebes evidence omitted | Medium | Verified in corpus (Montier 2015; Calef & Simkins 2009); Plutarch verified in Greek, Llewellyn-Jones confirmed in his own words (follow-up) |
| A8 | Dio 33.48 (Tarsus) framed as an "extreme" exception without weighing that Tarsus is Paul's home city | Medium | Verified in corpus (Payne 2015; Marlowe 2005; Conzelmann 1975) |
| A9 | Portrait evidence used without noting its structural bias toward visible faces | Medium | Methodological |
| A10 | "First attested c. 190" treated as "arose c. 190–220" (absence of evidence from a near-empty period) | Medium | Methodological |
| A11 | The question was reframed so the headline verdict answers an easier question ("did Paul *require* it?") | Medium | Methodological |
| A12 | Pseudo-numeric confidence (≈95%+) with no stated basis | Low–medium | Methodological |
| A13 | Rhetorical framing in a document claiming neutrality ("loaded silence", "the single most weighty datum", "the two errors") | Low | Editorial |
| A14 | "Same letter collection" for 2 Cor 3 vs 1 Cor 11 | Low | Factual (different letters) |

---

## A1 — The "strongest argument" rests on a false premise

**Original claim** (`source-report.md` §1.3, `README.md`): *"Paul uses the face-veil word (`κάλυμμα`) explicitly in 2 Corinthians 3 but not here … That is the single most weighty datum in the whole debate."*

**What BDAG actually says** (BDAG 3rd ed., s.v. `κάλυμμα`, p. 447–448 in the corpus PDF):

> "**head-covering, veil** lit., of the veil w. which Moses covered his face (Ex 34:33–35) 2 Cor 3:13 … κ. ἐπὶ τὴν καρδίαν κεῖται a veil lies on the mind vs. 15"

So:

1. BDAG's first gloss for `κάλυμμα` is **"head-covering"**. It is not a face-specific word. In 2 Cor 3:15 the same word lies "on the heart".
2. Paul's wording in 2 Cor 3 comes from LXX Exod 34:33–35, which he is expounding. His choice there is driven by the source text, not by a preference between face and head words.
3. The corpus already contains a source making exactly this point: *Covered Glory* (p. 10) says the 2 Cor 3 term "is fairly general and its definition does not specify that the face is covered (**and so Paul specifies 'face'** in the passage)."

**What survives:** a weaker, legitimate form of the argument. When Paul means the face he **names** `πρόσωπον` (2 Cor 3:7, 13, 18). In 1 Cor 11 he names `κεφαλή`. This shows that **the head is the body part his rule is about**. It does **not** show that the covering he had in mind stopped at the hairline, which is what the dossier used it to establish.

**Also wrong:** "in the same letter collection" (§1.3). 1 and 2 Corinthians are separate letters written at different times. Minor, but it inflates the parallel.

---

## A2 — LXX Gen 38:15 misquoted

**Original** (`02-text-and-lexis.md` §5.2): *"Tamar: `ἐκάλυψεν γὰρ τὸ πρόσωπον αὐτῆς`"*, and the method log admits "the LXX text itself was not separately collated".

**Actual LXX text** (Rahlfs, via Blue Letter Bible LXX):

> Gen 38:15 `καὶ ἰδὼν αὐτὴν Ιουδας ἔδοξεν αὐτὴν πόρνην εἶναι· κατεκαλύψατο γὰρ τὸ πρόσωπον αὐτῆς`

The verb is **`κατακαλύπτω` in the middle voice**. That is Paul's verb, in the voice BDAG suggests for 1 Cor 11:6 ("cover oneself"), with **"face"** as its object. BDAG cites Gen 38:15 *at 1 Cor 11:7* as its grammatical parallel. This is the single closest lexical parallel to Paul's usage, and the dossier misquoted it in a way that hid the match.

**Interpretive caution:** Tamar is disguising herself and is taken for a prostitute. The parallel is lexical, not social. Notably, v. 14 says she put on a `θέριστρον`, the same garment Rebekah puts on in Gen 24:65.

---

## A3 — No concordance; "the one place" claim is false

**Original** (`02` §5.4): Isa 6:2 is *"the one place where the verb itself takes 'face' as its object."*

**Full LXX check** (all 23 occurrences in 22 verses; table in `data/lxx-katakalypto-concordance.csv`):

| Object of `κατακαλύπτω` | Occurrences |
|---|---|
| Human or angelic **face** (`πρόσωπον`) | **3**: Gen 38:15, Isa 6:2, Jer 28:51 (MT 51:51) |
| Feet | 1: Isa 6:2 |
| **Head** (`κεφαλή`) | **0** |
| Reflexive, no object ("disguise oneself") | 1: 2 Chr 18:29 |
| Objects, animals, landscape, cities | 17 |

Every LXX occurrence with a human or angelic body part as object is the face (or, once, feet). It never takes "head". Outside the LXX, BDAG records the verb with the head as the covered part in Hermas (*Vis.* 4.2.1, "veiled to the forehead") and in Paul himself (11:7).

**Reading:** the verb is generic ("cover over") and is used readily for faces. It does not lean toward the head. It cannot carry the weight the dossier put on Paul's word choice in either direction. The decisive lexical fact is the one Paul supplies: at 11:7 the object is `τὴν κεφαλήν`.

**Josephus (verified in the follow-up check; see "Follow-up verification" below):** BDAG cites *Ant.* 7.254 for the *middle absolute* sense ("cover oneself"), the construction BDAG suggests for 1 Cor 11:6. The Greek (Niese, via Perseus) reads `κατακαλυψαμένου δὲ τοῦ βασιλέως καὶ στένοντος τὸν υἱόν` ("when the king had covered himself and was lamenting his son"). Josephus is paraphrasing 2 Sam 19:5, where both the LXX (`ἔκρυψεν τὸ πρόσωπον αὐτοῦ`, "hid his face") and the Hebrew (Strong's H3813 "muffle/cover" + H6440 "face") specify the **face**. So the absolute middle of Paul's verb is used by a 1st-century Jewish Greek writer for an act his source describes as covering the face. **Limits:** Josephus himself names no body part; mourners also covered the *head* (2 Sam 15:30), so he may have had the whole mantle-over-head-and-face gesture in mind. What the passage shows is that the absolute middle **does not restrict the covering to the head**. It cannot show what Paul meant, since Paul supplies `τὴν κεφαλήν` at 11:7.

---

## A4 — Silence coded as "head only"

**Original** (`04` §7–8 and timeline): Chrysostom and Theodoret = **"head only"**.

**What Chrysostom says** (*Hom. 26 in 1 Cor.*, NPNF 1.12, New Advent):

> "For he said not merely covered, but **covered over**, meaning that she be carefully wrapped up **on every side**." … "the woman he commands to be **at all times** covered."

**What Theodoret says** (on 11:10, Kovacs 2005: 183): "Paul calls the veil authority. This means: let her show her subjection, making herself humble…"

Neither mentions the face. Chrysostom's comment on the `κατα-` prefix stresses **completeness of wrapping**, which, if it points anywhere, points away from a minimal head-only covering. The correct code for both is **"silent on the face"**. The dossier's own assessment line ("the greatest Greek commentator on Paul says nothing about the face") is accurate. The timeline label "head only" and the inference drawn from it are not.

---

## A5 — "The earliest" writers misidentified

**Original** (`04`, table at the end): *"Face-covering was required by the earliest Christian writers | False — the earliest (Chrysostom, Theodoret) say head only."*

Chrysostom wrote c. 390–407 and Theodoret c. 430–450. The earliest Christian writers on the covering's form are **Hermas** (Rome, early-to-mid 2nd c.), **Clement of Alexandria** (c. 195) and **Tertullian** (Carthage, c. 200–210). Of these:

| Writer | Face? |
|---|---|
| Hermas, *Vis.* 4.2.1 | Head covered "to the forehead" with a `μίτρα`: **face visible** (allegorical figure of the Church) |
| Clement, *Paed.* 3.11 | **Face covered.** "Let her be entirely covered … nor will she invite another to fall into sin by uncovering her face … it is becoming for her to pray veiled" (ANF, New Advent; verified) |
| Tertullian, *Virg. vel.* 17 | Christian women **not** covering the face; he holds up Arab women who cover "not only the head but the face" as exceeding them (verified by DeepSeek; accepted) |

So the earliest evidence is **split by region**: face visible in the Latin West (Rome, Carthage), face covered in Alexandria. It is not "head only".

---

## A6 — Claim 8 contradicted by the dossier's own source

**Original** (`07`, Claim 8): *"'Head covering' and 'face covering' are the same thing — **False**, high."*

BDAG, quoted by the dossier itself, cites Ps.-Dicaearchus on the women of Thebes: **`τὸ τῶν ἱματίων ἐπὶ τῆς κεφαλῆς κάλυμμα`** ("the covering of the garments *on the head*") is "of such a kind that the whole face seems to be covered as with a mask." A Greek writer calls a face-concealing garment **"the covering on the head"**. Plutarch's Chalcedonian women (below) veil half the face with the same mantle.

The ancient sources did **not** keep a sharp lexical line between head covering and face covering. One garment, drawn further or less far, could be either. The modern categories are the analyst's. Revised verdict: **misframed**. The right question is not whether the two things are identical, but where along a continuum a given garment usually sat.

---

## A7 — Greek-East evidence under-reported

The dossier presents Llewellyn-Jones (*Aphrodite's Tortoise*, 2003) in one line, immediately followed by his critic Smith. Corpus sources that relay his face-veil evidence were not used:

- **Montier 2015** (*Let Her Be Shorn*; the file mislabelled "Harmon 2003", pp. 14–15 of the extraction): the **tegidion** "was a rectangular cloth worn **over the face with holes cut out for eyes**. In private the tegidion could be pulled back over the head … The women of **Thebes**, in particular, were noted for covering their whole face". Examples are reproduced "from various Greek cities such as **Alexandria and Pergamon**". Plutarch, *Greek Questions* 49: women of **Chalcedon** veiled **half the face** before strange men.
  - *Follow-up check:* Llewellyn-Jones's own statement (podcast interview, below) confirms the tegidion as "a full face veil" with eye holes, evidenced "from Alexandria and the Greek-speaking cities of North Africa", appearing from the end of the 4th c. BCE and common in Hellenistic terracottas. He adds: "I'm not sure how far-flung the tegidion went." **Pergamon is not confirmed** by his statement. The Theban evidence is **one text**, Heraclides Criticus, the same passage BDAG cites as Ps.-Dicaearchus (A6), and must not be counted twice.
  - *Follow-up check:* Plutarch *Greek Questions* 49 verified in Greek (below). Montier's paraphrase is accurate in substance.
- **Calef & Simkins 2009** (p. 7): "from the archaic era through the Roman period, women of varying social strata in the ancient Greek world were habitually veiled".
- **Payne 2015** (n. 31): Galt (*AJA* 1931, "Veiled Ladies") argued *for* Greek face-veiling against the consensus; de Vaux (1935) for himation-over-head-not-face at Tanagra and Myrina.

**Weighting caution:** much of this is Classical or Hellenistic (5th–2nd c. BCE), and Thebes, Chalcedon and Alexandria are not Corinth. It shows that face-veiling was a **real, regionally varied Greek practice**, not an exotic or merely "eastern" one. It does not show what Corinthian Christian women did in the 50s CE. The original's error is not its conclusion about Corinth but its omission of this material from the scales.

**Verification status:** Llewellyn-Jones's book is not in the corpus and could not be obtained; the tegidion claims are now confirmed in his own words (interview), not from the book's catalogue. Plutarch is verified in Greek.

---

## A8 — Tarsus framed as an "extreme" exception

Dio Chrysostom, *Or.* 33.48 (c. 100 CE, Tarsus): women "so arrayed … that nobody could see any part of them, **neither of the face** nor of the rest of the body" (Loeb, quoted in Payne 2015 n. 45 and Marlowe 2005: 17). Marlowe reads Dio as describing a covering drawn diagonally across the face, leaving one eye.

The dossier calls this an "extreme local custom". That is defensible: the Loeb editors attribute it to "the oriental element at Tarsus", and Nõmmik (2025: 40) doubts it was universal. But two facts that belong on the scales were not weighed:

1. **Tarsus is Paul's home city.** Conzelmann (1975, in the corpus excerpt pp. 181–191; exact page not recoverable from the text file): "From Tarsus Paul is familiar with veiling as a universal custom." If Paul's own mental picture of a covered woman matters (cf. 11:16 "we have no such custom"), Tarsus is the most relevant single data point outside Corinth.
2. ~~**Dio describes the custom as decaying** (Conzelmann: "Dio Chrysostomus laments its decay"). So it was on the way out c. 100, which implies it was stronger in Paul's lifetime.~~ **Withdrawn after checking the Greek (follow-up below).** Dio lists the women's dress among customs **still in force** (`τῶν νῦν ἔτι μενόντων`) as a survival of the city's older strictness. What he laments is moral decay *despite* the veil ("faces covered, but souls uncovered"). The custom was current c. 100 CE; nothing in the passage says whether it was stronger or weaker in Paul's day. Conzelmann's paraphrase, which this audit repeated, misstates Dio.

None of this shows Corinthian women veiled their faces. It shows that "face open" cannot be treated as the unmarked default for every setting Paul knew.

---

## A9 — Portrait evidence has a built-in bias

Claim 4 leans on portraiture: Roman matrons and the Corinthian portraits (Gill 1990), and *capite velato* male sacrificants. Honorific and funerary portraits exist **to show the face**. A face-veiled portrait would defeat its own purpose. So "the portraits show faces" is weak evidence about street or worship dress. It was presented without that caveat. Figurines and genre scenes (e.g. Tanagra-type statuettes, where mantles cover the lower face) are the less-biased visual class, and the dossier did not code them.

This does not reverse Claim 4. It lowers how much the visual evidence should move the verdict.

---

## A10 — "First attested" is not "arose"

Claim 9 dates the rise of the face reading to c. 190–220 (confidence "high"). But the 2nd-century Christian record says almost nothing about the covering's form: one allegorical vision (Hermas) and nothing else before Clement and Tertullian. In a period that thin, the absence of earlier face evidence is weak evidence of absence. The defensible statement is: **"the first explicit Christian evidence for face-covering is Clement, c. 195; there is too little earlier evidence to say whether the practice is older."** The causal story (practice ⇄ textual variant) remains open, as the dossier itself conceded.

Also, the 11:10 variant reads `κάλυμμα`, which BDAG glosses first as "head-covering" (A1). So the variant is evidence for reading "authority" as a **covering**, not specifically as a **face**-covering. The dossier's account of the variant "reinforcing" the face reading needs that qualification.

---

## A11 — The question was quietly narrowed

The user's question was whether the head covering of 1 Cor 11 **included** the face. The dossier's headline verdict ("Paul requires a face covering — **False, very high**") answers whether the text *requires* it. That is close to trivial, since the text never mentions the face, so it is easy to answer with very high confidence. The genuinely uncertain question is **historical**: what did the covering Paul presupposed usually look like in Corinth? That question got a lower-confidence "Probable" (Claim 4). The README's one-paragraph verdict leads with the easy answer and so reads as more settled than the evidence allows.

---

## A12–A14 — Confidence and tone

- **Pseudo-numeric confidence** ("≈95%+") is attached to judgments with no stated likelihood model. Numbers imply a precision that was never computed. The revised method (`12-revised-method.md`) replaces them with labels tied to explicit reasons.
- **Advocacy language** in a dossier that claims neutrality: "a *loaded* silence", "the single most weighty datum", "The two errors", "The one thing the evidence will not support…". These pre-empt the reader's judgment. They are flagged, not deleted, in the original files.
- **"Same letter collection"**: see A1.

---

## What the audit confirms (no change needed)

| Original finding | Audit check |
|---|---|
| `πρόσωπον` does not occur in 1 Cor 11:2–16 | Confirmed (`Native Greek.txt`) |
| Paul's expressed object is `τὴν κεφαλήν` (11:7) and the covering is "on the head" (11:10) | Confirmed |
| Clement of Alexandria explicitly requires the face covered | Confirmed against ANF text (*Paed.* 3.11) |
| Tertullian contrasts Christian practice with Arab face-veiling | Accepted (checked by DeepSeek against ANF) |
| No early Greek MS reads `κάλυμμα` at 11:10 | Accepted (Nõmmik; BDAG lists it only as v.l.) |
| Face-covering has Christian attestation independent of Islam | Confirmed (Clement, Didascalia, Jerome) |
| The "Harmon 2003" files actually contain Montier 2015 | Confirmed |

---

## Follow-up verification (7 November 2026, second pass)

All fetched source documents are saved in `collections/` (index: `collections/INDEX.md`).

The four items left open by the first pass of this audit were checked against primary texts.

| Item | Source checked | Text | Result | What it does and does not show |
|---|---|---|---|---|
| **Josephus, *Ant.* 7.254** | Niese Greek text via Perseus (`1999.01.0145`, bk 7 §254); Whiston English (Lexundria) | `κατακαλυψαμένου δὲ τοῦ βασιλέως καὶ στένοντος τὸν υἱόν` | **Verified.** Middle, absolute, no object | Josephus uses Paul's verb in the absolute middle for David's mourning, which 2 Sam 19:5 describes as covering/hiding the **face** (LXX `ἔκρυψεν τὸ πρόσωπον αὐτοῦ`; Hebrew "covered his face", Strong's H3813 + H6440). Shows the absolute middle does not restrict the covering to the head. Does not show Paul's meaning: Paul names the head (11:7) |
| **Plutarch, *Greek Questions* 49** (*Mor.* 302E–F) | Babbitt Greek text; Babbitt and Goodwin English (PerseusDL `canonical-greekLit`, tlg0007.tlg084b) | `διὰ τί ταῖς Χαλκηδονίαις ἔθος ἐστίν, ὅταν ἀνδράσιν ἀλλοτρίοις ἐντύχωσι, μάλιστα δʼ ἄρχουσι, τὴν ἑτέραν παρακαλύπτεσθαι παρειάν;` … `ἀπάγουσαι θάτερον μέρος τοῦ προσώπου τῆς καλύπτρας` | **Verified.** Babbitt: "to veil one cheek"; the founding women did business before judges "drawing aside one part of the veil that covered their faces" | A living custom in Plutarch's day (`ἔθος ἐστίν`, c. 100 CE) at Chalcedon (Bithynia, on the Bosporus): respectable women half-veil the face before strange men and officials. The aetiology implies the `καλύπτρα` could cover the whole face. **But** Plutarch treats it as a local oddity needing explanation, which is evidence that half-face veiling was *not* the general Greek norm in his world |
| **Susanna 32 (Theodotion)** | Rahlfs-based text, sacred-texts.com "Susanna Th" (Theodotion; consistent with the Th wording of vv. 28 and 31) | `οἱ δὲ παράνομοι ἐκέλευσαν ἀποκαλυφθῆναι αὐτήν· ἦν γὰρ κατακεκαλυμμένη· ὅπως ἐμπλησθῶσιν τοῦ κάλλους αὐτῆς` | **Verified** | A respectable married Jewish woman, in a public assembly, is `κατακεκαλυμμένη`; unveiling her lets the elders "feast on her beauty". **No body part is named.** It fits a covering that hid the face, but does not state it. (In v. 34 the elders then lay hands "on her head".) Weak evidence that the participle of Paul's verb could describe a covering that concealed a woman's looks |
| **Llewellyn-Jones** (*Aphrodite's Tortoise*, 2003) | Book not obtainable (JSTOR / paywall). The reviews by Dillon, *Classical Review* 55.2 (2005) 682–4, and Rose, *Cloelia* 37.1 (2007) 26–7, could not be opened. Checked instead: his own statements in the podcast *Women Who Went Before*, S2E3 "Veiled But Not Hidden" | "So this is actually a full face veil"; "We have lots of evidence of it from Alexandria and the Greek-speaking cities of North Africa"; "doesn't really appear until the end of the 4th century and then it becomes very popular"; "We see it quite a lot in the terracottas of the Hellenistic Period"; "I'm not sure how far-flung the tegidion went" | **Partly verified**: the claims, in the author's own words; not the book's evidence catalogue | Confirms a real Greek face-veil (tegidion), Hellenistic, best attested in Alexandria and North Africa. Does **not** confirm Montier's "Pergamon", or any 1st-c. CE or Corinthian use. Llewellyn-Jones gives no estimate of how common face-veiling was |

### Effect on the assessment

- **Josephus** strengthens audit A3: the lexical evidence gives Paul's verb no head-only bias, including in the absolute middle. Q1 (what the text requires) is unchanged, because Paul states the object.
- **Plutarch** adds a **verified c. 100 CE** case of respectable Greek women half-veiling the face (Chalcedon). Plutarch's framing also cuts the other way: he treats it as a local peculiarity.
- **Llewellyn-Jones** narrows the tegidion evidence to Hellenistic Alexandria and North Africa. It is weaker as background for Roman Corinth than the first pass of this audit implied.
- **Theban evidence** is a single text (Heraclides Criticus = BDAG's Ps.-Dicaearchus) and is counted once (E6).
- **Net:** the Q2 leaning (head-drape with face visible, more likely than not at Corinth; *probable, not high*) is **unchanged**. The supporting evidence is now verified, and two over-statements in this audit (Pergamon; double-counted Thebes) are removed.

### Additional check: Dio Chrysostom, *Or.* 33.48–49

Not on the list, but the only other face-veil text in the matrix that was known only second-hand. Checked against the Greek (PerseusDL `canonical-greekLit`, tlg0612.tlg001 perseus-grc2):

> `πολλὰ τῶν νῦν ἔτι μενόντων … ὧν ἐστι τὸ περὶ τὴν ἐσθῆτα τῶν γυναικῶν, τὸ τοῦτον τὸν τρόπον κατεστάλθαι καὶ βαδίζειν ὥστε μηδένα μηδὲ ἓν αὐτῶν μέρος ἰδεῖν μήτε τοῦ προσώπου μήτε τοῦ λοιποῦ σώματος` … `ὥστε τὰ μὲν πρόσωπα κεκαλυμμέναι βαδίζουσι, τῇ ψυχῇ δὲ ἀκαλύπτῳ`

"Among the customs *still remaining* … is the women's dress: that they are so arrayed and walk so that no one could see any part of them, neither of the face nor of the rest of the body … so that they walk with their faces covered, but with the soul uncovered" (and they "see more sharply with one of their eyes").

**Result:** the face-covering is **verified** as a current Tarsian custom c. 100 CE, presented as a relic of the city's old strictness. The "decaying custom" reading (Conzelmann, repeated in A8) is **withdrawn**. The Loeb editors' suggestion that the custom reflects "the oriental element at Tarsus" is their inference, not Dio's.

## What remains unverified

1. The NA28/ECM apparatus at 11:10.
2. Gill 1990's portrait counts (reported second-hand by the dossier).
3. Llewellyn-Jones's catalogue of face-veiled figures (book not obtained).
4. A full concordance of `κατακαλύπτω` outside the LXX (Philo, Josephus, Plutarch, Apostolic Fathers).
