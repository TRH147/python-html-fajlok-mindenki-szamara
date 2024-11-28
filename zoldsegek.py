class Zoldseg:
    def __init__(self, nev, mennyiseg, ar, termesztes_ev):
        self.nev = nev
        self.mennyiseg = mennyiseg
        self.ar = float(ar)
        self.termesztes_ev = int(termesztes_ev)

    def __str__(self):
        return f"{self.nev} - {self.mennyiseg} - {self.ar} Ft/kg - {self.termesztes_ev}"

zoldsegek = []

with open('zoldsegek.txt', 'r', encoding='utf-8') as file:
    for line in file:
        nev, mennyiseg, ar, termesztes_ev = line.strip().split(';')
        zoldsegek.append(Zoldseg(nev, mennyiseg, ar, termesztes_ev))

print("A teljes fájl tartalma:")
for zoldseg in zoldsegek:
    print(zoldseg)

print("\n2015 utáni zöldségek:")
zoldsegek_2015_utan = [zoldseg for zoldseg in zoldsegek if zoldseg.termesztes_ev > 2015]
for zoldseg in zoldsegek_2015_utan:
    print(zoldseg)

legolcsobb = min(zoldsegek, key=lambda zoldseg: zoldseg.ar)
print(f"\nA legolcsóbb zöldség:\n{legolcsobb.nev} - {legolcsobb.ar} Ft/kg")

paprika_zoldsegek = [zoldseg for zoldseg in zoldsegek if zoldseg.nev.lower().startswith("paprika")]
print(f"\n'Paprika'-val kezdődő zöldségek száma: {len(paprika_zoldsegek)}")

print("\nEzek a zöldségek 'paprika'-val kezdődnek:")
for zoldseg in paprika_zoldsegek:
    print(zoldseg)

with open('paprika_zoldsegek.txt', 'w', encoding='utf-8') as file:
    for zoldseg in paprika_zoldsegek:
        file.write(str(zoldseg) + '\n')

print("\nA paprika_zoldsegek.txt fájlba kiírásra kerültek az adatok.")
