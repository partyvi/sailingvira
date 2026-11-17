#!/usr/bin/env python3
"""Sailing log: Viktor's "Boat dates" Google Sheet -> data/sailing_log.json + sailing-log/index.html.

    python3 tools/sailing_log.py path/to/boat-dates.xlsx

The spreadsheet is the source. Download it as .xlsx (Google Drive), run this, commit the two outputs.
The .xlsx itself is NOT stored in the repo: it holds real crew names.

What the script does to the sheet:
- keeps every row that has a date and something in it (hours, miles, engine or notes);
- crew names are dropped: only the number of people aboard and Viktor's role (skipper / crew) stay;
  names inside the notes are replaced via SCRUB, and any crew name left over stops the run;
- fixes common typos (TYPOS), normalizes boats and waters, reads temperatures in F or C
  (a "c" after the number, or plain numbers from 12 Apr 2026 on, are Celsius);
- a wave cell that Sheets turned into a date (2-3 -> 3 Feb) is read back as "2–3".
Data mistakes (a wrong date, a wrong route) are best fixed in the sheet; `check` lists suspicious rows.

Needs openpyxl (pip install openpyxl). Not part of the site build, the page is not linked yet.
"""
import datetime as dt
import json
import os
import re
import sys

import openpyxl

B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_JSON = f"{B}/data/sailing_log.json"
OUT_HTML = f"{B}/sailing-log/index.html"
CELSIUS_FROM = dt.date(2026, 4, 12)

# columns of Sheet1 (0-based): A boat .. U total hours
COL = dict(boat=0, date=1, water=2, frm=3, to=4, hours=5, nm=6, avg=7, t24=8, wmin=9, wmax=10, gust=11,
           waves=12, temp=13, motor=14, motor_total=15, weather=16, crew=17, sail=18, problems=19)

# Phrases with names in the notes, replaced before the generic check.
SCRUB = [
    (r"\s*from Paul Coburn", ""),
    (r"\s*to Shawn Zernik", ""),
    (r"\bEugine tryed\b", "Our friend tried"),
    (r"\bEugine tried\b", "Our friend tried"),
]
# Words in the crew column that are not names.
NOT_NAMES = {"Me", "Crew", "Trainer", "Passanger", "Passangers", "SOLO", "Kid", "Baby", "Brother", "Wife",
             "Viktor", "Victor", "Vic", "Partyshev", "Partysheva", "Estonia", "David's", "Https"}

TYPOS = {
    "expereence": "experience", "squals": "squalls", "nocked": "knocked", "nockdown": "knockdown",
    "crusing": "cruising", "stady": "steady", "staty": "steady", "staddy": "steady", "suny": "sunny",
    "skys": "skies", "swel": "swell", "trafic": "traffic", "baot": "boat", "reffed": "reefed",
    "riffed": "reefed", "riffing": "reefing", "fron": "from", "windl": "wind", "dunny": "sunny",
    "ful": "full", "kat": "cat", "unplesent": "unpleasant", "trail": "trial", "hulling": "hauling",
    "ind": "and", "consistant": "consistent", "tryed": "tried", "benatau": "Beneteau",
    "tention": "tension", "bottim": "bottom", "rich": "reach", "ganoa": "genoa", "genua": "genoa",
    "genova": "genoa", "sale": "sail", "hout": "hour", "io": "to", "crasy": "crazy", "anuther": "another",
    "challange": "challenge", "quaters": "quarters", "parctice": "practice", "undocink": "undocking",
    "passangers": "passengers", "passanger": "passenger", "clowds": "clouds", "clousd": "clouds",
    "heawy": "heavy", "breese": "breeze", "cocpit": "cockpit", "suteable": "suitable",
    "oscilating": "oscillating", "foll": "full", "ruch": "rush", "bitting": "beating", "tine": "time",
    "earlyer": "earlier", "fo": "for", "dounwind": "downwind", "wownwind": "downwind", "0nly": "only",
    "doring": "during", "acked": "asked", "obgects": "objects", "onthe": "on the", "mororing": "motoring",
    "strout": "strut", "ancghor": "anchor", "becede": "besides", "probabpy": "probably",
    "moynted": "mounted", "barel": "barrel", "gree": "green", "appers": "appear", "nay": "may",
    "tagboat": "tugboat", "loosing": "losing", "shoppy": "choppy", "overcust": "overcast",
    "reverce": "reverse", "naviagation": "navigation", "frieand": "friend", "highter": "higher",
    "bassin": "basin", "mmain": "main", "ballanced": "balanced", "broducing": "producing",
    "usial": "usual", "comfortsable": "comfortable", "sailng": "sailing", "sailig": "sailing",
    "siling": "sailing", "walve": "valve", "appered": "appeared", "problens": "problems", "dask": "dusk",
    "slopy": "sloppy", "intertain": "entertain", "noce": "nice", "adn": "and", "exidents": "incidents",
    "excidents": "incidents", "avarage": "average", "stratched": "stretched", "dampher": "damper",
    "overcasted": "overcast", "chanel": "channel", "wit": "with", "surprisedly": "surprisingly",
    "mansfild": "Mansfield", "frend": "friend", "descent": "decent", "ley": "lay", "wing": "wind",
    "swimmed": "swam", "dickenson": "Dickinson", "hat": "had",
    "arraive": "arrive", "sailfrom": "sail from", "motorbotes": "motorboats", "bouys": "buoys",
}
TYPO_PHRASES = [
    (r"\bTaking([,.])", r"Tacking\1"), (r"\bdevil cove\b", "Devil's Cove"), (r"\bred ?fish island\b", "Redfish Island"),
    (r"\bgoat island\b", "Goat Island"), (r"\bBomb island\b", "Bomb Island"), (r"\bSometimes islands\b", "Sometimes Islands"),
    (r"\bmansfield dam\b", "Mansfield Dam"), (r"\bDreher park\b", "Dreher Park"), (r"\bopenplotter\b", "OpenPlotter"),
    (r"\bHo\.\.\.", "Ho…"), (r"\bJUst\b", "Just"), (r"\bGalveston bay\b", "Galveston Bay"), (r"[ \t]+\n", "\n"), (r"  +", " "),
]


def fix_typos(s):
    def word(m):
        w = m.group(0)
        r = TYPOS.get(w.lower())
        if r is None:
            return w
        return r[0].upper() + r[1:] if w[0].isupper() and r[0].islower() else r
    s = re.sub(r"[A-Za-z0-9]+(?:'[a-z]+)?", word, s)
    for a, b in TYPO_PHRASES:
        s = re.sub(a, b, s, flags=0 if a.startswith(r"\bTaking") else re.I)
    return s.strip()


def text(v):
    if v is None:
        return ""
    return str(v).replace("\r", "").strip()


def num(v):
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        return round(float(v), 2)
    m = re.fullmatch(r"\s*(-?\d+(?:\.\d+)?)\s*", text(v))
    return round(float(m.group(1)), 2) if m else None


def parse_date(v):
    if isinstance(v, dt.datetime):
        return v.date()
    m = re.fullmatch(r"(\d{1,2})/(\d{1,2})/(\d{2,4})", text(v))
    if m:
        y = int(m.group(3))
        return dt.date(y + 2000 if y < 100 else y, int(m.group(1)), int(m.group(2)))
    return None


def boat_name(s):
    low = s.lower()
    if low.startswith("sea sun"):
        return "Sea Sun", "Hunter 19-2"
    if low.startswith("vira"):
        return "Vira", "Irwin Citation 34"
    if "beach cat" in low:
        return "Beach cat", "16' catamaran, main sail only"
    if low.startswith("first light"):
        return "First Light", "Hunter 28.5"
    if low.startswith("old school"):
        return "Old School", "a friend's boat"
    return s, ""


def water_name(s):
    low = s.lower()
    if "murray" in low:
        return "Lake Murray, SC"
    if "travis" in low:
        return "Lake Travis, TX"
    if "galveston" in low:
        return "Galveston Bay, TX"
    if "cozumel" in low:
        return "Cozumel, Mexico"
    return s.strip()


def place(s):
    s = text(s)
    if not s:
        return ""
    if "boat yard" in s.lower():
        return "Dickinson boatyard"
    return re.sub(r",\s*TX\.?$", "", s).strip()


def waves(v):
    if isinstance(v, dt.datetime):          # Sheets read "2-3" as a date
        return f"{v.month}–{v.day}"
    n = num(v)
    if n is not None:
        return f"{n:g}"
    return text(v)


def temperature(v, date):
    s = text(v)
    if not s or s == "-":
        return None, None
    m = re.fullmatch(r"(-?\d+(?:\.\d+)?)\s*([cCfF]?)", s)
    if not m:
        return None, None
    n = float(m.group(1))
    celsius = m.group(2).lower() == "c" or (not m.group(2) and date >= CELSIUS_FROM)
    if celsius:
        return round(n * 9 / 5 + 32), round(n)
    return round(n), round((n - 32) * 5 / 9)


def crew_count(s):
    """People aboard counted from the crew cell (Viktor included). Returns (count, role)."""
    s = text(s)
    if not s or s.lower().startswith("http"):
        return None, None
    role = "skipper"
    if re.search(r"trainer|skiper", s, re.I) or not re.match(r"\s*(me\b|viktor partyshev \(me\))", s, re.I):
        role = "crew"
    s = re.sub(r"\([^)]*\)|\[[^\]]*\]", lambda m: "" if "(" in m.group(0) else "PERSON", s)
    s = re.sub(r"(Trainer/skiper|crew|Crew|Passanger|Passangers)\s*:", ",", s)
    s = re.sub(r"\bSOLO\b", "", s)
    s = re.sub(r"\d+\s*gallon[^,]*", "", s)           # the famous empty barrel
    count = 0
    for m in re.finditer(r"(\d+)\s*kids?", s):
        count += int(m.group(1))
    s = re.sub(r"\+?\s*\d+\s*kids?\.?", "", s)
    s = re.sub(r"\b(?:and|amd|&)\b|&| - |\.\s+", ",", s)
    for part in s.split(","):
        part = part.strip(" .+'")
        if part:
            count += 1
    return count, ("solo" if count == 1 and role == "skipper" else role)


def name_tokens(cells):
    toks = {"Paul", "Coburn", "Shawn", "Zernik"}
    for c in cells:
        if c.lower().startswith("http"):
            continue
        for w in re.findall(r"[A-Z][a-z']+", c):
            if w not in NOT_NAMES and len(w) > 2:
                toks.add(w.rstrip("'"))
    return toks


def scrub(s):
    for a, b in SCRUB:
        s = re.sub(a, b, s)
    return s


def read(path):
    wb = openpyxl.load_workbook(path, data_only=True)
    ws = wb["Sheet1"]
    rows = [r for r in ws.iter_rows(min_row=4, values_only=True)]
    names = name_tokens([text(r[COL["crew"]]) for r in rows if r[COL["crew"]]])
    out, leaks = [], []
    for i, r in enumerate(rows, 4):
        r = list(r) + [None] * 21
        date = parse_date(r[COL["date"]])
        if not date:
            continue
        hours, nm, motor = num(r[COL["hours"]]), num(r[COL["nm"]]), num(r[COL["motor"]])
        notes = {k: fix_typos(scrub(text(r[COL[k]]))) for k in ("weather", "sail", "problems")}
        if not (hours or nm or motor or any(notes.values())):
            continue
        for k, v in notes.items():
            for t in names:
                if re.search(rf"\b{re.escape(t)}\b", v):
                    leaks.append((i, k, t))
        if not (hours or nm or motor) and notes["weather"] and not notes["sail"]:
            notes["sail"], notes["weather"] = notes["weather"], ""      # an event: boat bought, sold
        boat, model = boat_name(text(r[COL["boat"]]))
        tf, tc = temperature(r[COL["temp"]], date)
        aboard, role = crew_count(r[COL["crew"]])
        frm, to = place(r[COL["frm"]]), place(r[COL["to"]])
        e = dict(row=i, date=date.isoformat(), boat=boat, model=model, water=water_name(text(r[COL["water"]])),
                 frm=frm, to=to, hours=hours, nm=nm, avg=num(r[COL["avg"]]), t24=num(r[COL["t24"]]),
                 wind_min=num(r[COL["wmin"]]), wind_max=num(r[COL["wmax"]]), gust=num(r[COL["gust"]]),
                 waves=waves(r[COL["waves"]]), temp_f=tf, temp_c=tc, motor=motor, aboard=aboard, role=role,
                 **notes)
        out.append({k: v for k, v in e.items() if v not in (None, "")})
    return out, leaks


def check(entries):
    """Rows that look wrong in the sheet (for Viktor to fix there)."""
    issues = []
    for a, b in zip(entries, entries[1:]):
        if b["date"] < a["date"]:
            issues.append(f"row {b['row']}: date {b['date']} comes after {a['date']} (row {a['row']})")
    for e in entries:
        if e.get("frm") and "Galveston" not in e["water"]:
            issues.append(f"row {e['row']}: route {e['frm']} → {e.get('to')} but water is {e['water']}")
        if e.get("hours") and e.get("nm") and e.get("avg") and abs(e["nm"] / e["hours"] - e["avg"]) > 0.3:
            issues.append(f"row {e['row']}: avg {e['avg']} kn but {e['nm']} NM / {e['hours']} h = {e['nm'] / e['hours']:.2f}")
    return issues


def html(entries):
    tpl = open(f"{B}/tools/sailing_log.html", encoding="utf-8").read()
    data = json.dumps(entries, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return tpl.replace("/*DATA*/[]", data).replace("{{updated}}", dt.date.today().strftime("%-d %b %Y"))


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    entries, leaks = read(sys.argv[1])
    if leaks:
        for i, k, t in leaks:
            print(f"row {i} {k}: crew name '{t}' left in the notes; add it to SCRUB", file=sys.stderr)
        sys.exit(1)
    issues = check(entries)
    os.makedirs(os.path.dirname(OUT_HTML), exist_ok=True)
    clean = [{k: v for k, v in e.items() if k != "row"} for e in entries]
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(clean, f, ensure_ascii=False, indent=1)
        f.write("\n")
    with open(OUT_HTML, "w", encoding="utf-8") as f:
        f.write(html(clean))
    h = sum(e.get("hours", 0) for e in entries)
    nm = sum(e.get("nm", 0) for e in entries)
    print(f"{len(entries)} entries, {h:g} h, {nm:g} NM -> {os.path.relpath(OUT_JSON, B)}, {os.path.relpath(OUT_HTML, B)}")
    for s in issues:
        print("check:", s)


if __name__ == "__main__":
    main()
