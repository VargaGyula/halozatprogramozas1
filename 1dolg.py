#B csoport 

lista = [2,4,1,8,3]


#B.1


def osszegez(lista):
    osszeg = 0
    for elem in lista:
        osszeg += elem
    return osszeg

def szamok_darabszama(lista):
    db = 0
    for szam in lista:
         if szam:
            db+=1
    return db


print(f"A számok  darabszáma: {szamok_darabszama(lista)}")


#B.2
def paros_szamok_darabszama(lista):
    db = 0
    for szam in lista:
         if szam%2 == 0:
            db+=1
    return db


print(f"Páros számok darabszáma: {paros_szamok_darabszama(lista)}")


#AB

print("2:"*1)

for i in  range(2):
    print("*",end=" ")

print("4:"*1)

for i in  range(4):
    print("*",end=" ")

print("1:"*1)

for i in  range(1):
    print("*",end=" ")

print("8:"*1)

for i in  range(8):
    print("*",end=" ")

print("3:"*1)

for i in  range(3):
    print("*",end=" ")


