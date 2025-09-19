#dolgazatok javitasa

lista = [2,4,1,8,3]

#A1 lista elemeinek összege

osszeg = 0
for szam in lista:
    osszeg += szam

print(f"A1 számok összege:{osszeg}")
print(f"A1 számok összege:{sum(lista)}")


#B1 Lista elemeinek darabszáma

darab = 0
for _ in lista:
    darab += 1

print(f"B1 Lista elemeinek darabszáma:{darab}")
print(f"B1 Lista elemeinek darabszáma:{len(lista)}")


#A2 Páros számok átlaga

paros_osszeg = 0
paros_darab = 0

for szam in lista:
    if szam % 2 == 0:
        paros_osszeg += szam
        paros_darab += 1
print(f"A2 Páros számok átlaga{paros_osszeg / paros_darab: .3}:")




#B2 Páros számok darabszáma

print(f"B2 Páros számok darabszáma: {paros_darab}")

parosok_lista = [szam for szam in lista if szam % 2 == 0]
#parosok lista = [2,4,8]

print(f"A2 Páros számok átlaga: {sum(parosok_lista) / len(parosok_lista)}")
print(f"B2 Páros számok darabszáma: {len(parosok_lista)}")


#A2 és B2 sávdiagram

for szam in lista:
    print(szam, "*" * szam)
