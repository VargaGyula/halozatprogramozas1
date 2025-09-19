#kérjünk be 0 végjelű számokat,és írjuk ki az összegüket.
# ossz=0
# while True:
#     beszam = int(input("Kérek egy számot: "))
#     if beszam!=0:
#         ossz=ossz+beszam
#     else:
#         break

# print(f"A bekért számok összege: {ossz}")

#Enter végjelig kérjünk be számokat,és írjuk ki az összegüket.

#ossz=0
#while True:
 #    bestring = (input("Kérek egy számot: "))
  #   if bestring!="":
   #      ossz=ossz+int(bestring)
    # else:
       #  break
     
#print(f"A bekért számok összege: {ossz}")


#Kerjel be egy szamot es 0 tol eddig a paros szamokat irasd ki

hatar = int(input("Kerek a határszámot: "))
szam1 = 0
while szam1 != hatar+1:
    if szam1%2 == 0:
     print(szam1)
    szam1 += 1

