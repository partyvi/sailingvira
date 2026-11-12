import json, re, sys, os, hashlib, urllib.request, concurrent.futures as cf, io
from PIL import Image, ImageOps
D=sys.argv[1]; O=f"{D}/img"; os.makedirs(O,exist_ok=True)
posts=json.load(open(f"{D}/classified.json"))
urls={}
for p in posts:
    for s in p["sections"]:
        for b in s["blocks"]:
            if b["k"]=="img" and "googleusercontent" in b["src"]:
                u=re.sub(r"/(?:[swh]\d+[^/]*)/([^/]+)$",r"/w1000/\1",b["src"])
                iid=hashlib.md5(b["src"].encode()).hexdigest()[:10]; b["id"]=iid; urls[iid]=u
json.dump(posts,open(f"{D}/classified.json","w"),ensure_ascii=False)
print(len(urls))
def get(item):
    iid,u=item; fn=f"{O}/{iid}.webp"
    if os.path.exists(fn): return 0
    for a in range(3):
        try:
            data=urllib.request.urlopen(u,timeout=60).read()
            im=Image.open(io.BytesIO(data)); im=ImageOps.exif_transpose(im).convert("RGB")
            im.thumbnail((720,720)); im.save(fn,"WEBP",quality=62,method=5); return 1
        except Exception as e: err=e
    print("FAIL",iid,u,err); return 0
with cf.ThreadPoolExecutor(16) as ex: print(sum(ex.map(get,urls.items())))
