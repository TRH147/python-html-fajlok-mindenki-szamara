class Virag:
    def __init__(self, nev, ar, mennyiseg, szallitas_datum):
        self.nev = nev
        self.ar = ar
        self.mennyiseg = mennyiseg
        self.szallitas_datum = szallitas_datum

    def __str__(self):
        return f"{self.nev}, {self.ar} Ft, {self.mennyiseg} darab, Szállítás: {self.szallitas_datum}"

viragok = []
with open('viragok.txt', 'r', encoding='utf-8') as file:
    for sor in file:
        nev, ar, mennyiseg, szallitas_datum = sor.strip().split(", ")
        virag = Virag(nev, int(ar), int(mennyiseg), szallitas_datum)
        viragok.append(virag)


print("A fájl tartalma:")
for virag in viragok:
    print(virag)

legdragabb = viragok[0]
for virag in viragok[1:]:
    if virag.ar > legdragabb.ar:
        legdragabb = virag
print(f"\nA legdrágább virág: {legdragabb.nev} - {legdragabb.ar} Ft")

osszes_mennyiseg = sum(v.mennyiseg for v in viragok)
atlag = osszes_mennyiseg / len(viragok)
print(f"\nAz eladott virágok átlagos darabszáma: {atlag:.0f} darab")


rbetus_viragok = [v for v in viragok if v.nev.lower().startswith('r')]


print(f"\nA 'R'-rel kezdődő virágok száma: {len(rbetus_viragok)}\n")

print("A 'R'-rel kezdődő virágok:")
for virag in rbetus_viragok:
    print(virag)

with open('R_betus_viragok.txt', 'w', encoding='utf-8') as file:
    for virag in rbetus_viragok:
        file.write(str(virag) + "\n")
