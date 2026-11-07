"""KWIC search over extracted PDFs + corpus txt/md. usage: kwic.py PATTERN [FILTER_REGEX] [WIDTH] [MAX]"""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
pat = re.compile(sys.argv[1], re.I)
flt = re.compile(sys.argv[2], re.I) if len(sys.argv) > 2 and sys.argv[2] else None
W = int(sys.argv[3]) if len(sys.argv) > 3 else 300
MX = int(sys.argv[4]) if len(sys.argv) > 4 else 40
roots = [r'C:/Users/Admin/hcwork/ext']
corpus = r'C:/Users/Admin/Documents/Early Christianity/Head Coverings'
files = [os.path.join(roots[0], f) for f in os.listdir(roots[0]) if f.endswith('.txt') and not f.startswith('headcover_raw')]
for f in os.listdir(corpus):
    if f.endswith(('.txt', '.md')): files.append(os.path.join(corpus, f))
for f in os.listdir(os.path.join(corpus, '18 and 19th Century')):
    if f.endswith('.txt'): files.append(os.path.join(corpus, '18 and 19th Century', f))
n = 0
for f in sorted(files):
    t = open(f, encoding='utf-8', errors='ignore').read()
    for m in pat.finditer(t):
        a, b = max(0, m.start() - W), m.end() + W
        win = re.sub(r'\s+', ' ', t[a:b])
        if flt and not flt.search(win): continue
        pg = re.findall(r'\[\[p\.(\d+)\]\]', t[:m.start()])
        print(f'--- {os.path.basename(f)[:70]} p.{pg[-1] if pg else "-"}\n{win}\n')
        n += 1
        if n >= MX: sys.exit()
