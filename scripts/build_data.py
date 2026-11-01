# NOTE: edit `base` (this dossier's parent) and `src` (the corpus) before running.
import os, re, csv, json, glob

base = r"C:\Users\Admin\Documents\deepseek-harness\default-workspace"
dos  = os.path.join(base, "dossier")
data = os.path.join(dos, "data")
os.makedirs(data, exist_ok=True)

# ---------- 1. Parse the quote bank markdown into CSV/JSON ----------
md = open(os.path.join(dos, "05-quote-bank.md"), encoding="utf-8").read()
blocks = re.split(r"\n### ", md)[1:]
rows = []
for b in blocks:
    lines = b.strip().split("\n")
    head = lines[0].strip()
    m = re.match(r"(Q\d+)\s*[—-]\s*(.+)", head)
    if not m:
        continue
    qid, title = m.group(1), m.group(2).strip()
    quote = ""
    attr = corpus = typ = ver = ""
    for ln in lines[1:]:
        s = ln.strip()
        if s.startswith("> ") and not quote:
            quote = s[2:].strip()
        elif s.startswith("- **Attribution:**"):
            attr = s.split("**Attribution:**", 1)[1].strip()
        elif s.startswith("- **Corpus:**"):
            corpus = s.split("**Corpus:**", 1)[1].strip()
        elif s.startswith("- **Type:**"):
            rest = s.split("**Type:**", 1)[1]
            typ = rest.split("·")[0].strip()
            if "**Verified:**" in rest:
                ver = rest.split("**Verified:**", 1)[1].strip()
    rows.append(dict(id=qid, topic=title, quote=quote, attribution=attr,
                     corpus_file=corpus, evidence_type=typ, verified=ver))

with open(os.path.join(data, "quote-bank.csv"), "w", encoding="utf-8-sig", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["id","topic","quote","attribution","corpus_file","evidence_type","verified"])
    w.writeheader()
    w.writerows(rows)

json.dump(rows, open(os.path.join(data, "quote-bank.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("quote rows:", len(rows))

# ---------- 2. Corpus summary ----------
import collections
src = r"C:\Users\Admin\Documents\Early Christianity\Head Coverings"
ext = collections.Counter()
size = collections.Counter()
n = 0
for root, dirs, files in os.walk(src):
    for f in files:
        p = os.path.join(root, f)
        e = os.path.splitext(f)[1].lower() or "(none)"
        ext[e] += 1
        try: size[e] += os.path.getsize(p)
        except OSError: pass
        n += 1
with open(os.path.join(data, "corpus-summary.txt"), "w", encoding="utf-8") as fh:
    fh.write(f"CORPUS: {src}\nTOTAL FILES: {n}\nTOTAL MB: {sum(size.values())/1e6:.1f}\n\n")
    fh.write(f"{'ext':10}{'count':>8}{'MB':>10}\n")
    for e, c in ext.most_common():
        fh.write(f"{e:10}{c:>8}{size[e]/1e6:>10.1f}\n")
print("corpus summary written")

# ---------- 3. Face-context index (file -> count) from the digest ----------
dig = os.path.join(base, "face_digest.txt")
idx = []
if os.path.exists(dig):
    cur = None
    for ln in open(dig, encoding="utf-8", errors="replace"):
        if ln.startswith("################ "):
            m = re.match(r"################ (.+?)\s+\[(\d+)\]", ln)
            if m:
                idx.append((m.group(1), int(m.group(2))))
with open(os.path.join(data, "face-context-index.csv"), "w", encoding="utf-8-sig", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["file", "face_veil_contexts"])
    for name, c in sorted(idx, key=lambda x: -x[1]):
        w.writerow([name, c])
print("index rows:", len(idx))
