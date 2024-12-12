viragok = []

with open("viragok.txt", "r", encoding="UTF-8") as file:
    for sor in file:
        adat = sor.strip().split(", ")
        viragok.append([adat[0], int(adat[1]), int(adat[2]), adat[3]])

print("A fájl tartalma:")
for i in viragok:
    print(f"{i[0]}, {i[1]} Ft, {i[2]} darab, Szállítás: {i[3]}")

eladott_db = 0
legdragabb_ar = viragok[0][1]
legdragabb_virag = None
R_db = 0
for i in viragok:
    if legdragabb_ar < i[1]:
        legdragabb_ar = i[1]
        legdragabb_virag = i

    
    if i[0][0] == "R":
        R_db += 1
    
    eladott_db += i[2]

print(f"\nA legdrágább virág: {legdragabb_virag[0]} - {legdragabb_ar:.1f} Ft")
print(f"Az eladott virágok átlagos darabszáma: {round(eladott_db / len(viragok))} darab\n")

print(f"\nAz 'R'-rel kezdődő virágok száma: {R_db}")

print("\nAz 'R'-rel kezdődő virágok:")
for i in viragok:
    if i[0][0] == "R":
        print(f"{i[0]}, {i[1]} Ft, {i[2]} darab, Szállítás: {i[3]}")

with open("R_betus_viragok.txt", "w", encoding="UTF-8") as fajl:
    for i in viragok:
        if i[0][0] == "R":
            fajl.writelines(f"{i[0]}, {i[1]} Ft, {i[2]} darab, Szállítás: {i[3]}\n")
