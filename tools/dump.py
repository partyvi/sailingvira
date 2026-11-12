import json, sys, os, collections
D=sys.argv[1]; posts=json.load(open(f"{D}/classified.json")); os.makedirs(f"{D}/dump",exist_ok=True)
by=collections.defaultdict(list); n=0; idx={}
for p in posts:
    for i,s in enumerate(p["sections"]):
        key=f"s{n}"; n+=1; s["key"]=key
        idx[key]={"date":p["date"],"ptitle":p["title"],"url":p["url"],"kind":p["kind"],"title":s["title"],"sub":s["sub"],
                  "imgs":[b["id"] for b in s["blocks"] if b["k"]=="img" and b.get("id")]}
        if s["sub"]: by[s["sub"]].append((p,s,key))
json.dump(idx,open(f"{D}/sections.json","w"),ensure_ascii=False)
for sub,items in by.items():
    items.sort(key=lambda x:(x[0]["kind"]!="page",x[0]["date"]))
    with open(f"{D}/dump/{sub}.txt","w") as f:
        for p,s,key in items:
            f.write(f"\n[{key}] {p['date']} {'PAGE ' if p['kind']=='page' else ''}«{p['title'][:70]}» § {s['title'] or '-'}\n")
            k=0
            for b in s["blocks"]:
                if b["k"]=="img": k+=1; f.write(f"<p{k}> ")
                else: f.write(b["t"]+"\n")
    print(sub, os.path.getsize(f"{D}/dump/{sub}.txt"))
