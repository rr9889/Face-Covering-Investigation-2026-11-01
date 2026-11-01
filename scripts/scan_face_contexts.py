# NOTE: edit `src` and `ext` before running. `ext` is the output of extract_pdfs.py.
import os, re, glob, collections, json
src = r"C:\Users\Admin\Documents\Early Christianity\Head Coverings"
ext = r"C:\Users\Admin\Documents\deepseek-harness\default-workspace\hc_extract"
files = []
for root, dirs, fs in os.walk(src):
    dirs[:] = [d for d in dirs if d not in ("media", ".cache", ".obsidian", ".llm-wiki", "raw")]
    for f in fs:
        if f.lower().endswith((".txt", ".md")):
            files.append(os.path.join(root, f))
files += glob.glob(os.path.join(ext, "*.txt"))
seen=set(); uniq=[]
for p in files:
    try: t=open(p,encoding="utf-8",errors="replace").read()
    except Exception: continue
    k=(len(t)//500, t[:200])
    if k in seen: continue
    seen.add(k); uniq.append((p,t))

face = re.compile(r'(face|faces|facial|visage|πρόσωπ|prosōp|prosop|faciem|vultus|eyes?\b)', re.I)
veil = re.compile(r'(veil|cover|kalupt|καλυπτ|kalumm|καλυμμ|mantle|shawl|hood|wrap|προκαλυμ)', re.I)

out = collections.defaultdict(list)
for p,t in uniq:
    name = os.path.basename(p)
    if name.lower().startswith("headcover_raw_sources"): continue
    t2 = re.sub(r'\s+',' ',t)
    idxs=[]
    for m in face.finditer(t2):
        s=max(0,m.start()-300); e=min(len(t2),m.end()+300)
        ctx=t2[s:e]
        if veil.search(ctx):
            idxs.append((m.start(),ctx))
    # merge overlapping
    merged=[]
    for pos,ctx in idxs:
        if merged and pos - merged[-1][0] < 350:
            continue
        merged.append((pos,ctx))
    if merged:
        out[name]=merged

with open(r"C:\Users\Admin\Documents\deepseek-harness\default-workspace\face_digest.txt","w",encoding="utf-8") as fh:
    for name in sorted(out, key=lambda n:-len(out[n])):
        fh.write(f"\n\n################ {name}  [{len(out[name])}]\n")
        for pos,c in out[name]:
            fh.write("..."+c+"...\n\n")
print("files:", len(out), "contexts:", sum(len(v) for v in out.values()))
for n in sorted(out,key=lambda n:-len(out[n]))[:25]:
    print(len(out[n]), n[:100])
