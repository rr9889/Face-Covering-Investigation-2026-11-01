# NOTE: edit `src` and `out` before running. `src` is the Head Coverings folder;
# `out` was the session working directory (hc_extract), not shipped with this dossier.
import fitz, os, sys, json, re
src = r"C:\Users\Admin\Documents\Early Christianity\Head Coverings"
out = r"C:\Users\Admin\Documents\deepseek-harness\default-workspace\hc_extract"
os.makedirs(out, exist_ok=True)
report = []
for root, dirs, files in os.walk(src):
    dirs[:] = [d for d in dirs if d not in ("media", ".cache", ".obsidian", ".llm-wiki")]
    for f in files:
        if not f.lower().endswith(".pdf"):
            continue
        path = os.path.join(root, f)
        rel = os.path.relpath(path, src)
        safe = re.sub(r'[^A-Za-z0-9._-]+', '_', rel)[:150] + ".txt"
        dest = os.path.join(out, safe)
        try:
            doc = fitz.open(path)
            n = doc.page_count
            chunks = []
            for i, page in enumerate(doc):
                chunks.append(f"\n[[p.{i+1}]]\n" + page.get_text("text"))
            text = "".join(chunks)
            with open(dest, "w", encoding="utf-8") as fh:
                fh.write(f"SOURCE: {rel}\nPAGES: {n}\n" + text)
            report.append({"file": rel, "pages": n, "chars": len(text), "out": safe})
            doc.close()
        except Exception as e:
            report.append({"file": rel, "error": str(e)})
with open(os.path.join(out, "_report.json"), "w", encoding="utf-8") as fh:
    json.dump(report, fh, indent=1)
print("done", len(report))
low = [r for r in report if r.get("chars", 0) < 2000]
print("low-text:", len(low))
for r in low[:40]:
    print(r.get("chars"), r["file"][:110])
