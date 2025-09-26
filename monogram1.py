def monogram(nev):
    if not nev.strip():  # Ellenőrzi, hogy a bemenet üres vagy csak szóközöket tartalmaz
        return ""
    
    digrafok = {'cs', 'dz', 'gy', 'ly', 'ny', 'sz', 'ty', 'zs'}  # Magyar digráfok
    trigraf = 'dzs'  # Az egyetlen trigraf
    
    szavak = nev.split()
    monogram = ""
    
    for szo in szavak:
        if not szo:  # Üres szó kihagyása
            continue
        
        # Kisbetűssé alakítás az ellenőrzéshez
        szo_lower = szo.lower()
        
        # Trigraf ellenőrzése (dzs)
        if len(szo_lower) >= 3 and szo_lower[0] + szo_lower[1] + szo_lower[2] == trigraf:
            monogram += (szo[0] + szo[1] + szo[2]).upper()
        
        # Digraf ellenőrzése (pl. gy, sz)
        elif len(szo_lower) >= 2 and (szo_lower[0] + szo_lower[1]) in digrafok:
            monogram += (szo[0] + szo[1]).upper()
        
        # Egyébként csak az első betű
        else:
            monogram += szo[0].upper()
            
    return monogram

# Név bekérése és monogram kiírása
nev = input("Kérem adja meg a nevet: ")
print("A monogram:", monogram(nev))