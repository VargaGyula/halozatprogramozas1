szamok = [1,1,2,2,4,5,2,1,3]

#egyes_darab = 0
#kettes_darab = 0
#harmas_darab = 0
#negyes_darab = 0
#otos_darab = 0

#for szam in szamok:
    #if szam==1:
        #egyes_darab+=1
    #elif szam==2:
        #kettes_darab+=1
    #elif szam==3:
        #harmas_darab+=1
   # elif szam==4:
        #negyes_darab+=1
    #elif szam==5:
      #  otos_darab+=1

#print(f"Az 1-es számból ennyi darab van: {egyes_darab}")
#print(f"Az 2-es számból ennyi darab van: {kettes_darab}")
#print(f"Az 3-es számból ennyi darab van: {harmas_darab}")
#print(f"Az 4-es számból ennyi darab van: {negyes_darab}")
#print(f"Az 5-es számból ennyi darab van: {otos_darab}")


# for i in range(1,6):
        # print(f"{i} bol van {szamok.count(i)}")


darab = [0,0,0,0,0]

for szam in szamok:
    darab[szam-1]+=1

print(darab)

for i in range(len(darab)):
    print(f"{i+1} bol van {darab[i]}")
