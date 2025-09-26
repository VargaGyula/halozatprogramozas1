# Monogram generátor
nev = input("Kérem, adja meg a nevét: ")
nevek = nev.split()

if len(nevek) >= 2:
    # Vezetéknév első betű + keresztnév első két betű
    if len(nevek[1]) >= 2:
        monogram = nevek[0][0].upper() + nevek[1][0].upper() + nevek[1][1].upper()
    else:
        monogram = nevek[0][0].upper() + nevek[1][0].upper()
else:
    # Ha csak egy nevet adtak meg
    monogram = nevek[0][0].upper() if nevek else ""

print(f"{nev} monogramja: {monogram}")