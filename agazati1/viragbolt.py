import csv


class Virag:
    def __init__(self, nev, ar, eladott_mennyiseg, szallitas_datuma):
        self.nev = nev
        self.ar = int(ar)
        self.eladott_mennyiseg = int(eladott_mennyiseg)
        self.szallitas_datuma = szallitas_datuma

    def __str__(self):
        return f"{self.nev}, {self.ar} Ft, {self.eladott_mennyiseg} db, {self.szallitas_datuma}"


def beolvas(fajlnev):
    viragok = []
    with open(fajlnev, "r", encoding="utf-8") as fajl:
        reader = csv.reader(fajl)
        for sor in reader:
            viragok.append(Virag(*sor))
    return viragok


def legdragabb_virag(viragok):
    return max(viragok, key=lambda v: v.ar)


def eladott_atlag(viragok):
    osszes_mennyiseg = sum(v.eladott_mennyiseg for v in viragok)
    return osszes_mennyiseg / len(viragok)


def r_betusviragok(viragok):
    return [v for v in viragok if v.nev.startswith("R")]


def main():
    fajlnev = "viragok.txt"
    viragok = beolvas(fajlnev)

  
    print("A virágbolt teljes kínálata:")
    for virag in viragok:
        print(virag)

  
    legdragabb = legdragabb_virag(viragok)
    print(f"\nA legdrágább virág: {legdragabb.nev}, {legdragabb.ar} Ft")

    
    atlag = eladott_atlag(viragok)
    print(f"\nAz eladott virágok darabszámának átlaga: {atlag:.2f}")

    
    r_viragok = r_betusviragok(viragok)
    print("\nR-rel kezdődő virágok:")
    for virag in r_viragok:
        print(virag)

   
    with open("R_betus_viragok.txt", "w", encoding="utf-8") as fajl:
        for virag in r_viragok:
            fajl.write(str(virag) + "\n")
    print("\nAz R-rel kezdődő virágok mentve a 'R_betus_viragok.txt' fájlba.")


if __name__ == "__main__":
    main()
