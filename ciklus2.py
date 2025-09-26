#Kérjünk be számokat és adjuk meg az összegüket.
#1 0 végjelig
#2 enter végjelig HF ez a 2
osszeg=0
be_n=1
while be_n !=0:

    be_n=int(input("Kérek egy számot: "))
    osszeg=+be_n

print(osszeg)


# 0 végjelig

osszeg = 0

while True:
    szam = int(input("Adj meg egy számot (0 = vége): "))
    if szam == 0:
        break
    osszeg += szam

print(f"A megadott számok összege: {osszeg}")



# enter végjelig

osszeg = 0

while True:
    user_input = input("Adj meg egy számot (Enter = vége): ")
    if user_input == "":
        break
    osszeg += int(user_input)

print(f"A megadott számok összege: {osszeg}")

    
