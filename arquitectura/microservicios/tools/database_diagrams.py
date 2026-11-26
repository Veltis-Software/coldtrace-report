import re,sys,pathlib,subprocess,html
root=pathlib.Path(sys.argv[1]); out=pathlib.Path(sys.argv[2])
svcs={'identity-service':'Identity','asset-service':'Asset','monitoring-service':'Monitoring','alert-service':'Alert','report-service':'Report','subscription-service':'Subscription','maintenance-service':'Maintenance'}
def split_top(s):
    parts,depth,cur=[],0,''
    for ch in s:
        if ch=='(':depth+=1
        if ch==')':depth-=1
        if ch==',' and depth==0: parts.append(cur);cur=''
        else: cur+=ch
    parts.append(cur); return [p.strip() for p in parts if p.strip()]
def tag(t,c,pk,fk):
    k=("PK " if c in pk else "")+("FK " if (t,c) in fk else "")
    return f'<FONT POINT-SIZE="8" COLOR="#1F4E79"><B>{k}</B></FONT>' if k else ''
for repo,label in svcs.items():
    sql='\n'.join(p.read_text(encoding='utf-8',errors='ignore') for p in sorted((root/f'coldtrace-{repo}/src/main/resources').rglob('V*.sql'),key=lambda p:[int(x) if x.isdigit() else x for x in re.split(r'(\d+)',p.name)]))
    sql=re.sub(r'--[^\n]*','',sql)
    tables={};fks=[]
    for m in re.finditer(r'create\s+table\s+(?:if\s+not\s+exists\s+)?`?(\w+)`?\s*\((.*?)\)\s*(?:engine[^;]*)?;',sql,re.I|re.S):
        t=m.group(1).lower(); cols=[];pk=set()
        for item in split_top(m.group(2)):
            low=item.lower()
            if low.startswith('primary key'): pk|={c.strip(' `').lower() for c in re.search(r'\((.*?)\)',item).group(1).split(',')}
            elif low.startswith(('constraint','foreign key','unique','key ','index','check')):
                f=re.search(r'foreign\s+key\s*\((.*?)\)\s*references\s+`?(\w+)`?',item,re.I)
                if f: fks.append((t,f.group(1).strip(' `').lower(),f.group(2).lower()))
            else:
                p=item.split(); name=p[0].strip('`').lower(); typ=p[1].lower() if len(p)>1 else ''
                typ=re.sub(r'\(.*','',typ) if 'varchar' not in typ and 'decimal' not in typ else typ
                cols.append([name,typ,' not null' in ' '+low]);
                if 'primary key' in low: pk.add(name)
                r=re.search(r'references\s+`?(\w+)`?',item,re.I)
                if r: fks.append((t,name,r.group(1).lower()))
        tables[t]=[cols,pk]
    for m in re.finditer(r'alter\s+table\s+`?(\w+)`?(.*?);',sql,re.I|re.S):
        t=m.group(1).lower()
        if t not in tables: continue
        for a in re.finditer(r'add\s+(?:column\s+)?`?(\w+)`?\s+(\w+(?:\(\d+(?:,\d+)?\))?)',m.group(2),re.I):
            if a.group(1).lower() in ('constraint','index','key','unique','primary','foreign'): continue
            if a.group(1).lower() not in [c[0] for c in tables[t][0]]: tables[t][0].append([a.group(1).lower(),a.group(2).lower(),False])
        for f in re.finditer(r'foreign\s+key\s*\((.*?)\)\s*references\s+`?(\w+)`?',m.group(2),re.I): fks.append((t,f.group(1).strip(' `').lower(),f.group(2).lower()))
    fkcols={(a,b) for a,b,c in fks}
    dot=['digraph G {','graph [rankdir=TB, splines=true, nodesep=0.35, ranksep=0.45, fontname="Arial", bgcolor="white", pad=0.15, newrank=true];','node [shape=plaintext, fontname="Arial", fontsize=10];','edge [color="#1F4E79", arrowhead=crow, arrowtail=tee, dir=both, penwidth=1.1];']
    names=list(tables)
    TECH=('outbox','processed_events','webhook_events')
    for t,(cols,pk) in tables.items():
        if any(k in t for k in TECH):
            keep=[c for c in cols if c[0] in pk or c[0] in ('event_id','event_type','aggregate_id','published_at','status')][:4]
            rows=''.join(f'<TR><TD ALIGN="LEFT" BGCOLOR="{"#EAF1FB" if c[0] in pk else "white"}">{tag(t,c[0],pk,fkcols)}{html.escape(c[0])}</TD><TD ALIGN="LEFT"><FONT COLOR="#555555">{html.escape(c[1])}</FONT></TD></TR>' for c in keep)+f'<TR><TD COLSPAN="2" ALIGN="LEFT"><FONT COLOR="#777777" POINT-SIZE="8"><I>tabla técnica: {len(cols)} columnas</I></FONT></TD></TR>'
            dot.append(f'"{t}" [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="3" COLOR="#A6A6A6"><TR><TD COLSPAN="2" BGCOLOR="#7F7F7F"><FONT COLOR="white"><B>{t}</B></FONT></TD></TR>{rows}</TABLE>>];')
            continue
        rows=''.join(f'<TR><TD ALIGN="LEFT" BGCOLOR="{"#EAF1FB" if c[0] in pk else "white"}">{tag(t,c[0],pk,fkcols)}{html.escape(c[0])}</TD><TD ALIGN="LEFT"><FONT COLOR="#555555">{html.escape(c[1])}{" NN" if c[2] and c[0] not in pk else ""}</FONT></TD></TR>' for c in cols)
        dot.append(f'"{t}" [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="3" COLOR="#7F7F7F"><TR><TD COLSPAN="2" BGCOLOR="#1F4E79"><FONT COLOR="white"><B>{t}</B></FONT></TD></TR>{rows}</TABLE>>];')
    per=4 if len(names)>8 else (3 if len(names)>4 else len(names))
    rows=[names[i:i+per] for i in range(0,len(names),per)]
    for r in rows: dot.append('{rank=same; '+' '.join(f'"{n}";' for n in r)+'}')
    for a,b in zip(rows,rows[1:]): dot.append(f'"{a[0]}" -> "{b[0]}" [style=invis];')
    for r in rows:
        for a,b in zip(r,r[1:]): dot.append(f'"{a}" -> "{b}" [style=invis];')
    seen=set()
    for a,col,b in fks:
        if b in tables: dot.append(f'"{b}" -> "{a}" [constraint=false];'); seen.add((a,col))
    target={'asset_id':'assets','gateway_id':'gateways','location_id':'locations','device_id':'iot_devices','iot_device_id':'iot_devices','incident_id':'incidents','user_id':'users','role_id':'roles','organization_id':'organizations','plan_id':'subscription_plans','report_id':'reports','asset_settings_id':'asset_settings','schedule_id':'maintenance_schedules'}
    for t,(cols,pk) in tables.items():
        for c in cols:
            b=target.get(c[0])
            if b and b in tables and b!=t and (t,c[0]) not in seen:
                dot.append(f'"{b}" -> "{t}" [constraint=false, style=dashed, color="#8FA9C8", arrowhead=crow, arrowtail=none];')
    dot.append(f'labelloc="t"; label=<<B>ct_{repo.split("-")[0]}</B> (MySQL 8.4) - {label} Service>; fontsize=13;}}')
    name=f'db-{repo.split("-")[0]}'; (out/f'{name}.dot').write_text('\n'.join(dot),encoding='utf-8')
    subprocess.run(['dot','-Tpng','-Gdpi=170',str(out/f'{name}.dot'),'-o',str(out/f'{name}.png')],check=True)
    print(label,len(tables),'tables',len(fks),'fks')
