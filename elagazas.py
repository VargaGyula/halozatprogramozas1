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

#Készíts függvényt előjel néven, mely átvesz egy egész számot és az előjelét adja vissza

def elojel(szam):
    if szam >= 0:
        return "+"
    else:
        return "-"

szam = int(input("Kérek egy számot előjellel: "))

print(f"A {szam} elojele: {elojel(szam)}.")

print(f"A {szam} elojele: {'+' if szam>=0 else '-'}.")

def tesztesetek():
    teszt(5,"+");
    teszt(-3,"-")
    teszt(-1,"-")
    teszt(0,"+")
    teszt(1,"+")
    #...


def teszt(szam, elvart_elojel):
    if elojel(szam) == elvart_elojel:
        print(f"elojel({szam})=={elvart_elojel} true")
    else:
        print(f"elojel({szam})=={elvart_elojel} false")

tesztesetek()