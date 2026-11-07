import fitz, os, re, sys, json
root = r'C:/Users/Admin/Documents/Early Christianity/Head Coverings'
out = r'C:/Users/Admin/hcwork/ext'
rep = {}
for dp, dn, fn in os.walk(root):
    dn[:] = [d for d in dn if d not in ('media', '.cache', '.obsidian', '.llm-wiki', 'Face Covering Investigation (2026-11-01)')]
    for f in fn:
        if not f.lower().endswith('.pdf'): continue
        p = os.path.join(dp, f)
        name = re.sub(r'[^\w.-]+', '_', os.path.relpath(p, root))[:150] + '.txt'
        try:
            d = fitz.open(p)
            parts = [f'[[p.{i+1}]]\n' + pg.get_text() for i, pg in enumerate(d)]
            t = '\n'.join(parts).replace('\x00', '')
            open(os.path.join(out, name), 'w', encoding='utf-8').write(t)
            rep[os.path.relpath(p, root)] = {'pages': len(d), 'chars': len(t)}
        except Exception as e:
            rep[os.path.relpath(p, root)] = {'error': str(e)}
json.dump(rep, open(os.path.join(out, '_report.json'), 'w'), indent=1)
print(len(rep), sum(1 for v in rep.values() if v.get('chars', 0) < 2000), 'near-empty')
