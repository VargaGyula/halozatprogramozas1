import json

with open("loverseny.json", "r", encoding="utf-8") as fin:
    versenyek=json.load(fin)
#2
verseny_lista=[]
for verseny in versenyek:
    if verseny["verseny_id"] not in verseny_lista:
        verseny_lista.append(verseny["verseny_id"])

print(f"A versenyek száma a következő: {len(verseny_lista)}")