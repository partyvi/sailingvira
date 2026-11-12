import json, re, sys, collections
D=sys.argv[1]
posts=json.load(open(f"{D}/parsed.json"))
# ordered rules: (sub, regex on section title)
R=[
("small-electronics", r"khatka|controller|brightness|tri-?color|anchor light|power switch|dry bilge|small electronic|lpg solenoid|engine monitor|thermostat|wattcycle|battery monitor"),
("standing", r"chainplate|chain plate|forestay|backstay|shroud|standing rigging|dyneema|rope terminator"),
("sailing", r"^sailing|sailing\b|sail out|sunset sail|happy sailing|miles in|get out for"),
("deck-structure", r"hull to deck|deck to hull|rail removal"),
("beginning", r"welcome to my new old|known issues|problems found later|what i like|what i don.t like|wrong and good|beginning"),
("reports", r"report|things are done|what is done|improved vs|trello"),
("jailbreak", r"jailbreak|step-?down|a-frame|transport|boatyard|on the hard|splash|travel lift"),
("hull-bottom", r"blister|bottom|barrier|topside|hull|waterline|boat name|registration|\bname\b|antifoul|gelcoat peel|strut|cutless|propeller|no-drip|grounding|lightning|thru-?hull|through hull"),
("windlass", r"windlass|chain locker|chain|anchor|bow roller|pulpit|rode|shackle"),
("fuel", r"fuel"),
("steering", r"steering|rudder|quadrant|binacle|binnacle|pedestal|wheel|shaft|stuffing"),
("aircon", r"air ?con|a/c|hvac|vent|duct|webasto|koolair|raw water pump"),
("galley-fridge", r"galley|refrigerat|fridge|countertop|microwave|stove|propane|lpg|sink|faucet|evaporator|compressor|condenser"),
("head-shower", r"\bhead\b|toilet|shower|holding|sanitation"),
("water", r"water tank|fresh water|water heater|water pump|plumb|pressure|tank|gray water|water"),
("sole-cushions", r"cabin sole|sole|floor|cushion|pillow|cabin table|table|mattress"),
("navigation", r"navig|autopilot|plotter|openplotter|ais|radar|instrument|wind |windex|depth|nav ?pod|navpod|gps|imu|compass|vhf|display|screen|raspberr|rudder position|helm|speed sensor|antenna"),
("interior-wood", r"bulkhead"),
("electrical", r"electr|wiring|wire|batter|inverter|panel|elci|shore power|alternator|light|charger|solar|cable|breaker"),
("engine", r"engine|exhaust|oil|cooling|heat exchanger|starter|mount|transmission|telegraph|clutch|yanmar|generator|sump|bilge"),
("mast", r"mast|spreader|boom|nyalic|furler|top of"),
("standing", r"rigging|stay|shroud|chainplate|backstay|turnbuckle|dyneema"),
("sails", r"sail ?pack|sail|reef|outhaul|outhull|lazy ?jack|winch|running|bimini|dodger"),
("windows", r"window|port(s)?\b|plexi|lexan"),
("deck-paint", r"paint|priming|primer|no-?skid|fairing|sanding|hatch|companion"),
("deck-structure", r"deck|core|stanchion|lifeline|drain|toe ?rail|hull to deck|cleat|handle"),
("interior-wood", r"interior|cabin|headliner|ceiling|trim|varnish|bulkhead|wall|cabinet|drawer|door|teak|wood|v-?berth|liner|shelf|shelves|insulation"),
("sailing", r"sailing|sail out|happy|weather|lake|trip|birthday|wind puff|road|family|friends|girls|marina|dock|picture|fun|kemah|galveston"),
]
L={ # label fallback
"Engine":"engine","Engine monitor":"small-electronics","Electric":"electrical","Electrical":"electrical","Mast":"mast","chainplates":"standing","Deck":"deck-structure",
"Painting":"deck-paint","Windows":"windows","interior":"interior-wood","Galley":"galley-fridge","Refrigerator":"galley-fridge","Air conditioner":"aircon",
"Water tankage":"water","Head":"head-shower","shower":"head-shower","Sailing":"sailing","Navigation":"navigation","Instruments":"navigation","autopilot":"navigation",
"Windlass":"windlass","chain locker":"windlass","Fuel Tank":"fuel","Hull":"hull-bottom","Cushions":"sole-cushions","Sails":"sails","Sailpack":"sails",
"Report":"reports","Bilge Pump":"engine","Wood":"interior-wood","Stanchions":"deck-structure","Structural":"deck-structure","Garage":"engine","horor":"beginning","Headliner":"interior-wood",
}
PAGE={"Beginning...":"beginning","What's wrong and good in Irwin34 '78, My point of view":"beginning","What is improved vs original?":"reports","Fixed ports":"windows",
"Windlass & chain locker":"windlass","Engine - Fresh water cooling":"engine","Cabin sole rebuild story":"sole-cushions","Cabin table":"sole-cushions",
"Standing rigging":"standing","Rigid radar mount for $115":"navigation","Helm instrument console":"navigation","Recycling shower (CANCELLED)":"head-shower",
"Irwin 34, Photo Albums":None,"pictures":None}
def cls(p,s):
    if p["kind"]=="page":
        return PAGE.get(p["title"].strip(),"small-electronics")
    t=(s["title"] or "").lower()
    for sub,rx in R:
        if t and re.search(rx,t):
            if sub=="deck-structure" and t.strip(". ")=="deck" and "2024-02-2"<=p["date"]<="2024-06-30": return "deck-paint"
            return sub
    # untitled/unknown: use post title then labels
    pt=p["title"].lower()
    for sub,rx in R:
        if re.search(rx,pt): return sub
    for l in p["labels"]:
        if l in L: return L[l]
    return "sailing"
res=collections.defaultdict(list)
for p in posts:
    for i,s in enumerate(p["sections"]):
        sub=cls(p,s)
        if sub: res[sub].append((p["date"],p["title"][:40],i,s["title"]))
        s["sub"]=sub
json.dump(posts,open(f"{D}/classified.json","w"),ensure_ascii=False)
for k,v in sorted(res.items()): 
    print(f"\n## {k} ({len(v)})"); print("; ".join(f'{d[2:]}:{(t or "-")[:25]}' for d,pt,i,t in v))
