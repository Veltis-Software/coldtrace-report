import re,sys,pathlib,subprocess,html
root=pathlib.Path(sys.argv[1]); out=pathlib.Path(sys.argv[2])
CFG={'identity':['**/iam/domain/model/aggregates','**/iam/domain/model/entities','**/iam/domain/model/valueobjects'],
 'asset':['**/assetmanagement/domain/model/aggregates','**/assetmanagement/domain/model/valueobjects'],
 'alert':['**/alerts','**/alerts/application','**/alerts/domain','**/platform/alerts/domain/model/aggregates','**/platform/alerts/domain/model/valueobjects'],
 'report':['**/reports/domain','**/reports/application'],
 'subscription':['**/billing/domain/model/aggregates','**/billing/domain/model/entities','**/billing/domain/model/valueobjects'],
 'maintenance':['**/maintenancemanagement/domain/model/aggregates'],
 'monitoring':['**/monitoring/domain','**/monitoring/domain/*']}
SKIP=re.compile(r'(Test|Exception|Repository|Controller|Config|Properties|Mapper|Assembler|Resource|Application|Push|Message)$')
NEST={}
def parse(p):
    src=p.read_text(encoding='utf-8',errors='ignore'); src=re.sub(r'/\*.*?\*/|//[^\n]*','',src,flags=re.S)
    res=[]
    for m in re.finditer(r'(?:public\s+)?(?:abstract\s+)?(class|record|enum|interface)\s+(\w+)(?:\s*\((.*?)\))?[^{]*\{',src,re.S):
        kind,name,comps=m.group(1),m.group(2),m.group(3)
        if SKIP.search(name): continue
        body=src[m.end():]
        depth=1;i=0
        while depth and i<len(body):
            depth+= body[i]=='{'; depth-= body[i]=='}'; i+=1
        body=body[:i]
        fields=[]
        if kind=='record' and comps:
            for c in re.split(r',(?![^<]*>)',comps):
                c=re.sub(r'@\w+(\([^)]*\))?','',c).split()
                if len(c)>=2: fields.append((c[-1],' '.join(c[:-1])))
        elif kind=='enum':
            head=re.split(r'[;}]',body,1)[0]
            head=re.sub(r'\([^)]*\)','',head)
            fields=[(v.strip(),'') for v in head.split(',') if re.fullmatch(r'[A-Z][A-Z0-9_]*',v.strip())][:8]
        else:
            top=re.sub(r'\{[^{}]*\}','',re.sub(r'\{[^{}]*\{[^{}]*\}[^{}]*\}','',body))
            for f in re.finditer(r'(?:private|protected)\s+(?:final\s+)?([\w<>,\s\[\]]+?)\s+(\w+)\s*(?:=[^;]*)?;',top):
                if 'static' in f.group(0): continue
                fields.append((f.group(2),' '.join(f.group(1).split())))
        nested=set(re.findall(r'(?:record|class|enum|interface)\s+(\w+)',body))
        if kind=='interface':
            methods=sorted({x for x in re.findall(r'^\s*(?:default\s+)?[\w<>\[\],.?\s]+?\s+(\w+)\s*\([^;{]*\)\s*[;{]',body,re.M) if x not in nested})[:6]
        elif kind in ('enum','record'): methods=[]
        else:
            methods=sorted({x for x in re.findall(r'public\s+(?:[\w<>\[\],\s]+\s+)?(\w+)\s*\(',body) if x!=name and x not in nested and x not in ('record','class','enum','interface') and not re.match(r'(get|set|is|equals|hashCode|toString)[A-Z]?',x)})[:6]
        NEST[name]=nested
        res.append((name,kind,fields,methods))
    return res
for svc,globs in CFG.items():
    base=root/f'coldtrace-{svc}-service/src/main/java'; classes={}
    for g in globs:
        for d in base.glob(g):
            for p in sorted(d.glob('*.java')):
                for c in parse(p): classes.setdefault(c[0],c)
    names=set(classes)
    dot=['digraph G {','graph [rankdir=TB, splines=true, newrank=true, nodesep=0.35, ranksep=0.5, fontname="Arial", pad=0.15];','node [shape=plaintext, fontname="Arial", fontsize=10];','edge [arrowhead=vee, color="#1F4E79", fontname="Arial", fontsize=8];']
    for n,(name,kind,fields,methods) in sorted(classes.items()):
        st={'record':'«record»','enum':'«enumeration»','interface':'«interface»'}.get(kind,'«aggregate»' if '/aggregates/' in '' else '')
        hdr=('#1F4E79' if kind=='class' else '#2E75B6' if kind=='record' else '#7F7F7F')
        fr=''.join(f'<TR><TD ALIGN="LEFT">{"- " if kind=="class" else ("+ " if kind=="record" else "")}{html.escape(f[0])}{(": "+html.escape(re.sub(r"java\.\w+\.","",f[1]))) if f[1] else ""}</TD></TR>' for f in fields[:14]) or '<TR><TD> </TD></TR>'
        if len(fields)>14: fr+=f'<TR><TD ALIGN="LEFT"><I>… {len(fields)-14} atributos más</I></TD></TR>'
        mr=''.join(f'<TR><TD ALIGN="LEFT">+ {html.escape(m)}()</TD></TR>' for m in methods)
        lbl=f'<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0" CELLPADDING="2" COLOR="#7F7F7F"><TR><TD BGCOLOR="{hdr}"><FONT COLOR="white"><B>{(st+"<BR/>") if st else ""}{name}</B></FONT></TD></TR><HR/>{fr}' + (f'<HR/>{mr}' if mr else '') + '</TABLE>'
        dot.append(f'"{name}" [label=<{lbl}>];')
    for o,ns in NEST.items():
        for n2 in ns:
            if o in names and n2 in names and n2!=o: dot.append(f'"{o}" -> "{n2}" [arrowhead=odot, color="#7F7F7F", constraint=false];')
    order=sorted(classes,key=lambda n:(classes[n][1]!='class',-len(classes[n][2])))
    per=4 if len(order)>9 else 3
    rows=[order[i:i+per] for i in range(0,len(order),per)]
    for r in rows: dot.append('{rank=same; '+' '.join(f'"{n}";' for n in r)+'}')
    for a,b in zip(rows,rows[1:]): dot.append(f'"{a[0]}" -> "{b[0]}" [style=invis];')
    for r in rows:
        for a,b in zip(r,r[1:]): dot.append(f'"{a}" -> "{b}" [style=invis];')
    for n,(name,kind,fields,_) in classes.items():
        for fname,ftype in fields:
            for t in re.findall(r'\w+',ftype or ''):
                if t in names and t!=name:
                    many=bool(re.search(r'(List|Set|Collection)<',ftype))
                    dot.append(f'"{name}" -> "{t}" [{"headlabel=\"0..*\", " if many else ""}arrowtail=diamond, dir=both, arrowhead=vee, constraint=false];' if kind=='class' and classes[t][1]!='enum' else f'"{name}" -> "{t}" [style=dashed, constraint=false];')
    dot.append(f'labelloc="t"; label=<<B>{svc.capitalize()} Service</B> - modelo de dominio>; fontsize=13;}}')
    (out/f'class-{svc}.dot').write_text('\n'.join(dot),encoding='utf-8')
    r=subprocess.run(['dot','-Tpng','-Gdpi=170',str(out/f'class-{svc}.dot'),'-o',str(out/f'class-{svc}.png')],capture_output=True,text=True)
    print(svc,len(classes),'classes',r.returncode,r.stderr[:200])
