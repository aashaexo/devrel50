import json, html, re
D={d["handle"].lower():d for d in json.load(open("data.json"))}
# (handle, display name, short line, optional note)
L=[("mattyp","Matt Palmer","Cursor"),("skeptrune","Nick Khami","Inference at Morph"),("max_kelly","Max Kelly","FDE at Firecrawl"),("fromsinaimportx","Sina Matian","NYU, scout at Y Combinator"),("yoimnotkesku","kesku","Exa, ex Perplexity"),
("asakohayase","Asako Hayase","Growth at Dimensional"),("AJs_AI","AJ's AI","President, The AI Collective"),("0xJuliechen","Julie Chen","CMO at Photon"),
("waynesutton","Wayne Sutton","Community at Convex"),("MarkVillacampa","Mark Villacampa","Product, code and design"),("paulostergaard","Paul Ostergaard","CEO at Norwood Systems"),
("kevinwhinnery","Kevin Whinnery","DX at OpenAI"),("dkundel","Dominik Kundel","DevX at OpenAI"),("ojusave","Ojus Save","Developers at Render"),
("jayrodge15","Jay Rodge","Developer Advocacy at NVIDIA"),("roangws","Roan Weigert","DevRel at GMI Cloud"),("Charles_Y_Wu","Yingcheng Charles Wu","Cofounder at PhAI Labs"),
("blaire_pang","Blaire Pang","Founder, ex Citadel and Coinbase"),("DhruvDiddi","Dhruv Diddi","Physical AI at Nebius"),("alexkaplan0","Alex Kaplan","Growth at Cognition"),
("ParasMadan9","Paras Madan","GTM Engineering at Varnan Labs"),("ryanzhuuuu","Ryan Zhu","Cofounder at Photon"),("contextconor","Conor Brennan-Burke","Founder at Hyperspell"),
("MrAhmadAwais","Ahmad Awais","CEO at Command Code"),("AleeeM1","Alex Marin","YouTuber, Melbourne"),("ivanleomk","Ivan Leo","DX at Google DeepMind"),
("yuqih","Yuqi Hou","Community at GMI Cloud"),("Coffee_and_NLP","Sonam Gupta","DevRel at Telnyx"),("IvyLeanIn","IvyLeanIn","Intern at Anyway, podcaster"),
("sammakesthings","Sam Stowers","AI Engineer"),("celesteanglm","Celeste Ang","Builder, ex Virtuals"),("iHarnoorSingh","Harnoor Singh","DevRel at AssemblyAI"),
("danizeres","Dani Bauer","Developers at OpenAI"),
("not_simantak","Simantak","Product and DevRel at TinyFish"),("helloLizZhang","Liz Zhang","DevRel AI Lead at FalkorDB"),
("yuaanlin","Yuanlin Lin","CEO at Zeabur"),("louszbd","Lou","Z.ai"),("LLMJunky","am.will","DevX"),
]
def put(lst,i,x): lst.insert(i,x)
put(L,0,("dabit3","Nader Dabit","Growth at Cognition"));
put(L,2,("0xyoussea","Youssef","DevRel at Base")); L.append(("juampitech","Juampi","Growth at Firecrawl"))
put(L,5,("aashatwt","aasha","DevRel, ex Eigen Labs"))
import os
put(L,10,("samclaassen","Sam Claassen","AI at Type"))
MUSKAN=os.environ.get("MUSKAN")
if MUSKAN: put(L,10,(MUSKAN,"Muskan Kalra",os.environ.get("MUSKAN_LINE","")))
L.append(("georgepickett","George Pickett","DevRel at p0"))
ORIG=list(L)
PIN={"mattyp":0,"dabit3":1,"0xyoussea":2,"0xJuliechen":3,"georgepickett":4,"aashatwt":5,"skeptrune":6,"samclaassen":10}
rest=[x for x in L if x[0] not in PIN]; L=[None]*len(L)
for x in [y for y in sum([[z] for z in rest],[])]: pass
byh={x[0]:x for x in L if x}
import itertools
src={x[0]:x for x in rest}
allx=rest[:]
L=[None]*(len(rest)+len(PIN)); 
for h,i in PIN.items(): L[i]=next(x for x in ORIG if x[0]==h)
it=iter(rest)
L=[x if x else next(it) for x in L]
cards=[]
for i,(h,n,line) in enumerate(L):
    has=h.lower() in D and "error" not in D[h.lower()]
    img=f'<img src="avatars/{h}.jpg" alt="{html.escape(n)}" loading="lazy">' if has else f'<div class="ph">{n[0]}</div>'
    cards.append(f'''<a class="card" href="https://x.com/{h}" target="_blank" rel="noopener" style="--i:{i}">
<div class="media">{img}</div>
<div class="meta"><h2>{html.escape(n)}</h2>{f'<p>{html.escape(line)}</p>' if line else ''}</div></a>''')
open("index.html","w").write(open("template.html").read().replace("{{CARDS}}","\n".join(cards)).replace("{{COUNT}}",str(len(L))))
