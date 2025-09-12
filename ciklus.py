# ciklusok

lista = [1, 2, 3, 4, 5]

def osszegez(lista):
    osszeg = 0
    for elem in lista:
        osszeg += elem
    return osszeg

def paros_szamok_darabszama(lista):
    db = 0
    for szam in lista:
         if szam%2 == 0:
            db+=1
    return db


print(f"A lista elemeinek összege:{osszegez(lista)}")
print(f"A lista páros elemeinek darabszáma: {paros_szamok_darabszama(lista)}")