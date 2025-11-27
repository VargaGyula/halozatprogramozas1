import json

with open("loverseny.json", "r", encoding="utf-8") as fin:
    versenyek=json.load(fin)

#

#1. Olvasd be a json fájlt
#2. Hány verseny adatai vannak a fájlban?
verseny_db=[]
verseny_darab_nincs=[]
for verseny in versenyek:
    verseny_db.append(verseny["verseny_id"])


#3. A verseny gyözteseit válogasd ki egy listába
gyoztesek=[]
for gyoztes in versenyek:
    if gyoztes["helyezés"]==1:
            gyoztesek.append({"zsoké":gyoztes["zsoké"]})

print(f"A győztesek a következők: {gyoztesek}")

#4. Írasd ki gyoztesek.json fájlba a győzteseket

with open("gyoztesek.json", "w", encoding="utf-8") as fout:
    json.dump(gyoztesek, fout, ensure_ascii=False, indent=4)