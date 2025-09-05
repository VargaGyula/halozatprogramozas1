print("Szia", end=" ")
print("Tibi")
print("Szia", "Tóth", "Karcsi", "!", sep="")
print("Szia Tóth Kacsi!")
nev = "Tóth Karcsi"
print(f"Szia {nev}!")
print("Szia", "Peti", sep="\n", end="!")  #\t
#adattípusok 
# int()
# float()
# str()
# bool()
# list()
# set()
# tuple()
print()
print(int("5"))    
print(float(5))   
print(str(5.0))
print(type(str(5.0)))   
print(bool(-1))
print(["hétfő", "kedd",  "szerda"])
napok = ["hétfő", "kedd",  "szerda"]
print(f"Napok: {napok}")
nevek = ["Tibi", "Sanyi",  "Tibi"]
print(f"nevek: {set(nevek)}")
print(tuple([1,2,3]))



# HF: git parancsok:
# git init: adott mappa verziókövetésének inditása
# git add . : 