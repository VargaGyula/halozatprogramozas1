# feladat: négyzet/téglalap kerületének számítása
def beker(alakzat, oldal):
    """Bekéri az 'alakzat' 'oldal' oldalának hosszát"""
    oldalhossz= int(input(f"Kérem a {alakzat} {oldal} oldalának hosszát [cm]:"))    
    return oldalhossz

def teglalapKerulete(a,b):
    """ Kiszámolja az 'a' és 'b' oldal ismeretében a téglalap kerületét. k= 2*(a+b)"""
    kerulet = 2* (a+b)
    return kerulet


def kiir(alakzat, kerulet):
    """Kiírja az 'alakzat' 'kerulet'-ét"""
    print(f"A {alakzat} kerülete: {kerulet}cm")

# input 
mit = input("[T]églalap vagy [N]égyzet kerületét számoljam? [T|N]")
if mit.upper() == "N":
    alap = beker("négyzet", "a")
    # calculation
    kerulet = teglalapKerulete(alap, alap)
    # output
    print(f"A négyzet kerülete: {kerulet} cm.")
elif mit.upper() == "T":
    a_oldal = beker("téglalap", "a")
    b_oldal = beker("téglalap", "b")
    # calculation
    kerulet = teglalapKerulete(a_oldal, b_oldal)
    # output
    kiir("téglalap", kerulet)
else:
    print("Hibás választás. Kilépek!")
