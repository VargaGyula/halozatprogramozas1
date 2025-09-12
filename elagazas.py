import random

gondolt_szam = random.randint(1,3)


#print(f"A gondolt szám: {gondolt_szam}")
bekert_szam = int(input("Kérem a tippet: "))

if gondolt_szam == bekert_szam:
    print("Gratulálok, eltaláltad!")
elif gondolt_szam > bekert_szam:
    print("Nagyobbra gondoltam!")
else:
    print("Kisebbre gondoltam!")