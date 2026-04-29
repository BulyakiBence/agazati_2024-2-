class Diafilm():
    def __init__(self, cim_, megjelenesi_ev, filmkockak_szama, szines_e_):
            self.cim = cim_
            self.megjelenesi_ev = megjelenesi_ev
            self.filmkockak_szama = filmkockak_szama
            self.szines_e = szines_e_
            




diafilmek = []
with open('02_feladat/filmek.txt', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        cim =adatok[0]
        diafilm = Diafilm(cim, int(adatok[1]), int(adatok[2]), int(adatok[3]))
        diafilmek.append(diafilm)

# print(f'{diafilmek=}')
for diafilm in diafilmek:
    print(diafilm.cim)
    
    