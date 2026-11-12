import json, re, os, sys, base64, io, collections
from PIL import Image
B=sys.argv[1]; D=f"{B}/data"; S=f"{B}/stories"; OUT=f"{B}/site"
os.makedirs(f"{OUT}/packs",exist_ok=True)
struct=json.load(open(f"{B}/tools/structure.json"))
sec=json.load(open(f"{D}/sections.json"))
def daynums(t):
    out=[]
    for m in re.finditer(r"Days?\s*#?\s*(\d{1,3})(?![\d/])((?:\s*[-,]\s*\d{1,3}(?![\d/]))*)",t):
        out.append(int(m.group(1)))
        out += [int(x) for x in re.findall(r"\d{1,3}",m.group(2))]
    return out
def parse(sub):
    fn=f"{S}/{sub}.md"
    if not os.path.exists(fn): return None
    lines=open(fn).read().split("\n"); intro=[]; chaps=[]; cover=None
    cur=None
    for ln in lines:
        ln=ln.rstrip()
        if not ln: continue
        if ln.startswith("cover:"): cover=ln.split(":",1)[1].strip(); continue
        if ln.startswith("skip:"):
            for tok in ln[5:].split():
                k,_,rng=tok.partition(":"); imgs=sec[k]["imgs"]
                idx=[]
                for part in (rng.split(",") if rng else []):
                    a,_,b=part.partition("-"); idx+=list(range(int(a),int(b or a)+1))
                if not rng: idx=list(range(1,len(imgs)+1))
                SKIPPED.update(imgs[i-1] for i in idx if 0<i<=len(imgs)); SKIPKEYS.add(k)
            continue
        if ln.startswith("## "): cur={"h":ln[3:].strip(),"blocks":[],"keys":[]}; chaps.append(cur); continue
        tgt = cur["blocks"] if cur else intro
        if ln.startswith("@"):
            g=[]
            for tok in ln[1:].split():
                k,_,rng=tok.partition(":"); imgs=sec[k]["imgs"]
                if rng:
                    idx=[]
                    for part in rng.split(","):
                        a,_,b=part.partition("-"); idx+=list(range(int(a),int(b or a)+1))
                else: idx=list(range(1,len(imgs)+1))
                g.append((k,[imgs[i-1] for i in idx if 0<i<=len(imgs)]))
                if cur is not None: cur["keys"].append(k)
            tgt.append({"g":g})
        elif ln.startswith("- "):
            if tgt and "ul" in tgt[-1]: tgt[-1]["ul"].append(ln[2:])
            else: tgt.append({"ul":[ln[2:]]})
        else: tgt.append({"p":ln})
    return intro,chaps,cover
SKIPPED=set(); SKIPKEYS=set()
GPLACED=set()
for g_ in struct:
    for sid_,_,_ in g_["subs"]:
        r_=parse(sid_)
        if r_:
            for c_ in r_[1]:
                for b_ in c_["blocks"]:
                    if "g" in b_:
                        for k_,ids_ in b_["g"]: GPLACED.update(ids_)
GPLACED|=SKIPPED
data={"structure":struct,"subs":{},"sources":{}}
used_keys=set(); report=[]; seen_by={}
for grp in struct:
    for sid,title,blurb in grp["subs"]:
        r=parse(sid); entry={"title":title,"blurb":blurb,"group":grp["title"]}
        if r:
            intro,chaps,cover=r
            # append unplaced photos of referenced sections after their last reference
            placed=collections.defaultdict(set); last={}
            for ci,c in enumerate(chaps):
                for bi,b in enumerate(c["blocks"]):
                    if "g" in b:
                        for k,ids in b["g"]: placed[k].update(ids); last[k]=(ci,bi)
            for k,(ci,bi) in last.items():
                rest=[i for i in sec[k]["imgs"] if i not in placed[k] and i not in GPLACED]
                if rest:
                    g=chaps[ci]["blocks"][bi]["g"]
                    for j,(kk,ids) in enumerate(g):
                        if kk==k: g[j]=(kk,ids+rest)
            out=[]; allimgs=[]
            for c in chaps:
                keys=list(dict.fromkeys(c["keys"])); dates=sorted(sec[k]["date"] for k in keys)
                days=sorted(set(d for k in keys if sec[k]["kind"]=="post" for d in daynums(sec[k]["ptitle"])))
                blocks=[]
                for b in c["blocks"]:
                    if "g" in b:
                        items=[]
                        for k,ids in b["g"]:
                            if k in seen_by and seen_by[k]!=sid: print('DUP',k,seen_by[k],sid)
                            seen_by[k]=sid; used_keys.add(k); data["sources"][k]={"d":sec[k]["date"],"u":sec[k]["url"],"t":sec[k]["ptitle"],"page":sec[k]["kind"]=="page"}
                            for i in ids: items.append([i,k]); allimgs.append(i)
                        blocks.append({"g":items})
                    else: blocks.append(b)
                out.append({"h":c["h"],"from":dates[0] if dates else None,"to":dates[-1] if dates else None,"days":[days[0],days[-1]] if days else None,"blocks":blocks})
            entry.update(intro=intro,chapters=out,n=len(set(allimgs)))
            # pack
            pack={i:base64.b64encode(open(f"{D}/img/{i}.webp","rb").read()).decode() for i in set(allimgs)}
            json.dump(pack,open(f"{OUT}/packs/{sid}.json","w"))
            cv = cover and sec[cover.split(":")[0]]["imgs"][int(cover.split(":")[1])-1] if cover else (allimgs[-1] if allimgs else None)
        else:
            keys=[k for k,v in sec.items() if v["sub"]==sid]; ims=[i for k in keys for i in sec[k]["imgs"]]
            entry.update(chapters=None,n=len(ims)); cv=ims[-1] if ims else None
        if cv:
            im=Image.open(f"{D}/img/{cv}.webp"); im.thumbnail((480,480)); bio=io.BytesIO(); im.save(bio,"WEBP",quality=55)
            entry["cover"]=base64.b64encode(bio.getvalue()).decode()
        data["subs"][sid]=entry
# stats
posts=set((v["date"],v["ptitle"]) for v in sec.values() if v["kind"]=="post")
data["stats"]={"posts":len(posts),"photos":len(os.listdir(f"{D}/img")),"first":min(p[0] for p in posts),"last":max(p[0] for p in posts),
  "days":max(d for p in posts for d in (daynums(p[1]) or [0]))}
tpl=open(f"{B}/tools/template.html").read()
open(f"{OUT}/index.html","w").write(tpl.replace("/*__DATA__*/null",json.dumps(data,ensure_ascii=False).replace("</","<\\/")))
written=[s for s in data["subs"] if data["subs"][s]["chapters"]]
for s in written:
    miss=[k for k,v in sec.items() if v["sub"]==s and k not in used_keys and k not in SKIPKEYS and (v["imgs"])]
    if miss: print("UNUSED in",s,miss)
print("index",os.path.getsize(f"{OUT}/index.html"),"packs",sum(os.path.getsize(f"{OUT}/packs/"+f) for f in os.listdir(f"{OUT}/packs")))
