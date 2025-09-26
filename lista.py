gyumolcsok = ["eper", "dinnye",]
jegyek = [2,5,4]

jegyek.append(1)
gyumolcsok.append("alma")
print(jegyek)
print(gyumolcsok)
jegyek.sort()
print(jegyek)
# print(sorted(jegyek))
gyumolcsok.remove("dinnye")
print(gyumolcsok)
gyumolcsok.insert(1, "banan")
print(gyumolcsok)
# gyumolcsok = []
jegyek.reverse()
print(jegyek)
print(gyumolcsok.index("banan"))
print(jegyek.count(5))
print(sum(jegyek))
print(min(jegyek))
print(max(jegyek))
print(len(jegyek))
# stringeket tartalmazó lista kiírása
print(f"{', '.join(gyumolcsok)}")
# inteket tartalmazo  lista kiirasa
print(f"{', '.join(map(str,jegyek))}")
# lista bejárása elemenkent
for jegy in jegyek:
    print(jegy)
# lista bejarasa index szerint
for i in range(len(gyumolcsok)):
    print(gyumolcsok[i])

mx = [
        [1,2,3],
        [4,5,6]
]
for sor in mx:
    # for oszlop in sor:
       # print(oszlop,end=", ")
       print(",".join(map(str,sor)))
    # print()

    