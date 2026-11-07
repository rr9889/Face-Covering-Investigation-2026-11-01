# 08 — Subagent method, briefs and verification

Four subagents were used to cover the corpus in parallel. This file records:

- why they were used;
- the exact brief each received;
- how their output was checked;
- where they disagreed with each other.

Their **full returned reports** are in the `subagents/` folder, one file per agent.

| Agent ID | Label | File | Sources assigned |
|---|---|---|---|
| `88404c8c-59c0-4a92-8c99-5956e9370de7` | Greco-Roman veiling evidence | `subagents/A-greco-roman.md` | Smith 2014, Stafford 2024, Harris 2022, Edmondson & Keith 2015, Marlowe 2005, Oster 1988, Gill 1990, Massey 2015/2018 |
| `cea37b72-4a9a-4744-a14f-c31d32269a95` | Patristic veiling evidence | `subagents/B-patristic.md` | Upson-Saia 2011, Leone 2012, Radle 2019, Harmon (mislabelled), Burghartz 2015, Galter 2021, *Covered Glory*, Kovacs 2005, Bray & Oden 2006 |
| `f3c63761-eb17-4823-9d21-8ced4134a5fc` | Commentary and lexical sweep | `subagents/C-lexical-commentary.md` | BDAG; Barrett, Conzelmann, Fee ×2, Thiselton, Hays, Morris, Héring, Meyer, Godet, Edwards, Alford, Stanley, Hodge, Chadwick, Curtis, Massey 2018, Humann, Hoelke, Oster, Peters, Blomberg, Johnson, Oxford, Keener, Ciampa/Rosner, Reasoner |
| `364bda13-0c87-4232-b105-099eccbd2695` | Modern debate and reception | `subagents/D-modern-debate.md` | Nõmmik 2025, Wu 2020, Payne, Lakey, BeDuhn, Callon, Marshall, Leone, Calef & Simkins, Martin, *Pro-Veiling Sources*, *Anti Veiling Sources*, *Head Covering Bingo*, *Prostitutes Lie Orgins* |

---

## Why delegation

The corpus is ~720 MB and ~200 text files. A single reader cannot hold it in one context. The four assignments were made **disjoint** so that no source was read twice and no agent's conclusions were seeded by another's. Each was given the same output contract:

- neutral reporting, including evidence against the position the source itself argues;
- verbatim quotations of **25 words maximum**, with a locator (page, chapter or section);
- explicit separation of **EVIDENCE** (primary data) from **INTERPRETATION** (the scholar's argument);
- explicit reporting of scholarly disagreement;
- a maximum length, to force selection rather than dumping.

---

## Brief A — Greco-Roman and Corinthian practice

> You are doing neutral historical research for a report on 1 Corinthians 11:2-16. Core question: in the Greek, Roman and Corinthian world of the first century, when a woman "covered her head," did the covering also cover her FACE? Was face-covering normal, optional, rare, or a distinct gesture?
>
> You have a local corpus of extracted texts in this folder (use glob/read, they are .txt): `C:\Users\Admin\Documents\deepseek-harness\default-workspace\hc_extract\`
>
> Read these files in it (use glob with author surname to find exact names):
> - Smith_E_ (Female Head Covering in Early Imperial Period, 2014)
> - Stafford_G_ (Veiling and Head-Covering in Late Antiquity, 2024)
> - Harris_S_ (Textiles in Ancient Mediterranean Iconography, 2022)
> - Edmondson_J_ (Dressing Judeans and Christians in Antiquity, 2015)
> - Marlowe_M_-_Headcovering_Customs_of_the_Ancient_World
> - Oster (txt at `C:\Users\Admin\Documents\Early Christianity\Head Coverings\Oster, R. E. (1988)....txt`)
> - Gill, D - Importance of Roman Portraiture (glob *Gill*)
> - Massey 2015 and 2018 (glob *Massey*)
>
> Rules:
> 1. NEUTRAL. Report what the evidence says, including evidence that cuts against the majority view and against whatever the author is arguing.
> 2. Never invent a quotation. Quote verbatim, 25 words max, with a locator (page number like p.53, or section heading).
> 3. Separate EVIDENCE (primary data: ancient text, inscription, image, artifact) from INTERPRETATION (the modern scholar's argument).
> 4. Note explicitly when a scholar disagrees with another scholar, and who.
> 5. Pay special attention to: whether faces were visible under head coverings; regional/cultural variation (Greek vs Roman vs "eastern"/Arabian/Jewish); what specific garments did (palla, amictus, ricinium, flammeum, kredemnon, kalumma, mitra, theristron); the capite velato of men; evidence from art (statues, coins, sarcophagi, vase painting, Pompeii, Dura-Europos).
>
> Return a compact evidence log, max ~1200 words: For each source: 3-6 bullets of form "[EVIDENCE|INTERPRETATION] quote/locator — what it establishes". End with: "Where sources disagree" (3-5 bullets) and "What remains unknown" (2-4 bullets).

---

## Brief B — Patristic and later Christian practice

> You are doing neutral historical research for a report on 1 Corinthians 11:2-16. Core question: did early Christian teaching and practice require women to cover the FACE as well as the head, and when/where did face-covering appear?
>
> You have a local corpus of extracted texts in this folder (use glob/read, they are .txt): `C:\Users\Admin\Documents\deepseek-harness\default-workspace\hc_extract\` plus .txt files under `C:\Users\Admin\Documents\Early Christianity\Head Coverings\`
>
> Read these (glob by surname): Upson-Saia_K_ (Early Christian Dress, 2011) — two files, read both; Leone_M_ (Cultures of Invisibility, 2012); Radle_G_ (Veiling of Women in Byzantium, 2019); Harmon_S_ (2003); Burghartz_S_ (Covered Women, 2015); Galter_H._D._ (Veil and headscarf, 2021); Covered_Glory; Kovacs, J - 1 Corinthians Interpreted by Early Christian Medieval Commentators; Bray and Oden - 1-2 Corinthians.
>
> Also grep the whole corpus for: Clement of Alexandria Paedagogus, Tertullian De virginibus velandis / De oratione, Didascalia, Apostolic Tradition, Chrysostom Homily 26, Cyprian, Irenaeus, Augustine, and for the words "face", "prosopon", "kalumma".
>
> Rules:
> 1. NEUTRAL. Include evidence on both sides, including cases where Christians did NOT cover faces and where they explicitly distinguished head from face.
> 2. Never invent a quotation. Quote verbatim, 25 words max, with locator (page, chapter, or section).
> 3. Separate EVIDENCE (what a primary text actually says) from INTERPRETATION (modern scholar's argument).
> 4. Where a modern scholar gives a date/region for the spread of face-covering, report it with the citation.
> 5. Flag anything about the textual variant at 1 Cor 11:10 (ἐξουσίαν vs κάλυμμα / "velamen").
>
> Return a compact evidence log, max ~1200 words: For each source: 3-6 bullets "[EVIDENCE|INTERPRETATION] quote/locator — what it establishes". End with: "Timeline of face-covering in Christian sources" (bullet list with dates and places), "Where sources disagree", "What remains unknown".

---

## Brief C — Lexica and commentaries

> You are doing neutral exegetical research for a report on 1 Corinthians 11:2-16. Core question: does the Greek text require, permit, or say nothing about covering the FACE? What do standard lexica and commentaries say about κατακαλύπτω, ἀκατακάλυπτος, κατὰ κεφαλῆς ἔχων, and περίβολαιον, and about the object covered?
>
> Local corpus: `...\hc_extract\`; `C:\Users\Admin\Documents\Early Christianity\Head Coverings\`; `...\18 and 19th Century\`
>
> Read at minimum (glob by surname):
> 1. BDAG: glob *Bauer* — find the entries κατακαλύπτω, ἀκατακάλυπτος, κάλυμμα, περίβολαιον, ἐξουσία, κεφαλή. Report exact glosses and any note on what is covered.
> 2. Commentaries: Barret, Conzelmann, Fee (two files), Morris, Héring, Hays, Johnson, Thiselton, Ciampa, Barton/Oxford, Keener, Blomberg.
> 3. 18 and 19th Century: Meyer, Godet, Edwards, Alford, Stanley, Hodge.
> 4. hc_extract: Chadwick_C, LET_HER_BE_SHORN...Curtis, Peters_J, Massey 2018, Humann_R, Hoelke.
> 5. Main folder: Oster 1988 .txt; Massey 2015 pdf.
>
> Rules:
> 1. NEUTRAL: report agreement and disagreement; note where a commentator says the covering definitely did NOT cover the face and where one says it did or might.
> 2. Never invent a quotation. Verbatim quotes, 25 words max, with locator (page number).
> 3. Tag each item [EVIDENCE] (lexical/textual data) or [INTERPRETATION] (exegetical judgment) or [DISPUTED].
> 4. Track: (a) what the verb's object is; (b) whether any ancient usage of κατακαλύπτω with πρόσωπον/face exists; (c) the 11:10 textual variant ἐξουσίαν/κάλυμμα; (d) how "head" is used for whole person vs body part; (e) the hair-vs-cloth debate and whether it bears on face.
>
> Return max ~1200 words: bullet log per source (2-5 bullets), then "Lexical summary" (5 bullets), "Commentator split" (who says what, minimal), "Unresolved".

---

## Brief D — Modern debate and reception history

> You are doing neutral research for a report on 1 Corinthians 11:2-16. Core question: how did the idea that the covering includes the FACE enter the tradition, and what do modern scholars make of it?
>
> Local corpus: `...\hc_extract\`; `C:\Users\Admin\Documents\Early Christianity\Head Coverings\`
>
> Read (glob by surname): Robes_Romans (Nõmmik 2025) — especially 1 Cor 11:10, κάλυμμα, Clement, Tertullian, and his conclusions; Wu_R_2020 — especially any section on face-covering and the conclusion; Payne (two .txt files); Lakey_M; BeDuhn; Callon_C; Marshall_J; Leone; Calef_and_Simkins; Martin, D. - The Corinthian Body; Pro-Veiling Sources.txt; Anti Veiling Sources.txt; Head Covering Bingo.md; Prostitutes Lie Orgins.txt.
>
> Rules:
> 1. NEUTRAL. Report the strongest version of each position, and note where a scholar's claim is asserted without evidence.
> 2. Never invent a quotation. Verbatim, 25 words max, with locator (page).
> 3. Tag [EVIDENCE] / [INTERPRETATION] / [ASSERTION-NO-EVIDENCE].
> 4. Specifically answer: (a) Is there any ancient evidence that Paul's Corinthian women wore face-veils? (b) Do any scholars argue the covering WAS a face veil, and on what grounds? (c) What does Nõmmik conclude about when and why the "facial veil" reading arose? (d) Does any source give art-historical evidence of Christian women with covered faces?
>
> Return max ~1200 words: bullet log per source, then "Three positions" (short), "Weakest links on each side", "Unresolved".

---

## How the output was verified

The subagent reports were treated as leads, not conclusions. Each report was read against the question, and every quotation that ended up carrying weight was checked back to the source file or the external text (the full verification table is in `01-method-and-steps.md`, Step 7).

**Checks that changed or sharpened the result:**

1. **Agent A** reported that Marlowe calls the flammeum "without covering her face," while Smith infers from Lucan that it covered the face. This was kept as a genuine disagreement rather than resolved — it is a good example of how unstable the evidence is.
2. **Agent A** found Massey's footnote reporting that **Goulder argues the opposite** of Massey — that the veil is drawn down over the face for both sexes. This was added to the report specifically to prevent the dossier from becoming one-sided.
3. **Agent B** discovered that the file labelled "Harmon" is actually Curtis Montier's *Let Her Be Shorn*. Nothing was attributed to Harmon.
4. **Agent B** supplied the single most important patristic datum: Clement of Alexandria, c. 190–200, is the first Christian text to require the face. This shifted the historical verdict from "face-covering is marginal" to "face-covering is early, real, and regional."
5. **Agent C** supplied Conzelmann's "head or face" and the BDAG Theban parallel — both of which cut against a simple "head only" conclusion, and both were verified directly.
6. **Agent D** supplied the Nõmmik reconstruction of the `κάλυμμα` variant, which became the spine of the reception-history section.

**Checks that were not possible:**

- Oster 1988 exists only as an abstract in the corpus; his argument is reported via Gill and Massey.
- Clement's *Paedagogus* text was not independently fetched in full; the quotations are from Nõmmik and Leone, both of whom print the Greek.
- The Mishnah and the LXX were not independently collated.

---

## Where the four agents disagreed with each other

| Question | Agent A / C | Agent B / D | Resolution |
|---|---|---|---|
| Did Roman women's veils cover the face? | Usually not (Smith, Gill, Marlowe) | Oxford/Keener: often yes | Recorded as a genuine split; verdict = "probable, not certain" |
| Did Tertullian require the face? | — | Radle: no; Leone/Upson-Saia: implies yes | Weighted to Radle on the basis of *Virg.* 17.3 |
| Is the Greek word a face-veil? | No (BDAG, Massey) | No, but it can cover the face (BDAG Theban) | Both true; the word is generic |
| Is the referent even a cloth? | Commentators split (hair vs cloth) | Payne: hair | Noted as a separate dispute that makes the face question moot on one view |
