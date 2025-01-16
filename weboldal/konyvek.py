class Konyvek:
    def __init__(self):
        self.lista = []

    def beolvas(self):
        with open("konyvek.txt", "r", encoding="UTF8") as file:
            adatok = file.readlines()

            for adat in adatok[1:]:
                adat = adat.strip()
                adat = adat.split(";")

                cim = adat[0]
                ar = int(adat[1])
                eladott = int(adat[2])
                ev = int(adat[3])

                self.lista.append([cim, ar, eladott, ev])
            
            print("A könyvek listája:\n")
            for list in self.lista:
                print(f"{list[0]};{list[1]};{list[2]};{list[3]}\n")

    def utan(self):
        print("2010 után megjelent könyvek:\n")
        for u in self.lista:
            if u[3] > 2010:
                print(f"{u[0]};{u[1]};{u[2]};{u[3]};")

    def legolcsobb(self):
        legolcsobb = float("inf")
        legolcsobbkonyv = " "
        for olcso in self.lista:
            if olcso[1] < legolcsobb:
                legolcsobb = olcso[1]
                legolcsobbkonyv = olcso[0]
        print(f"\nA legolcsóbb könyv: {legolcsobbkonyv} {legolcsobb} Ft")

    def kezd(self):
        with open("HappyPotter_konyvek.txt", "w", encoding="UTF8") as fajl:
            megszamol = 0
            for kezdodik in self.lista:
                if kezdodik[0].startswith("Harry Potter"):
                    megszamol+=1
                    fajl.write(f"\n{kezdodik[0]}")
                    print(f"\n{kezdodik[0]}")
            print("\nHarry Potter könyvek kiírva a fájlba:")
                    

konyv = Konyvek()
konyv.beolvas()
konyv.utan()
konyv.legolcsobb()
konyv.kezd()