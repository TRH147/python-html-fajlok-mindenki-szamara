
tabor_neve = input("Add meg a tábor nevét: ")
kaloriak = []  

while len(kaloriak) < 5:
    napi_kaloria = input(f"Add meg az elégetett kalóriák számát a(z) {len(kaloriak) + 1}. napon: ")
    
    if napi_kaloria.isdigit():
        kaloriak.append(int(napi_kaloria))

    if len(kaloriak) >= 5:
        tovabb = input("Szeretnél még kalóriákat hozzáadni? (i/n): ")
        if tovabb == "n":
            break
        elif tovabb =="i":
            napi_kaloria = input(f"Add meg az elégetett kalóriák számát a(z) {len(kaloriak) + 1}. napon: ")


atlag_kaloria = sum(kaloriak) / len(kaloriak)

print("\n  ===== Heti Kalóriaösszeg =====")
print(f"\n Tábor neve: {tabor_neve}")
print(f"\n Átlagosan elégetett kalória naponta: {int(atlag_kaloria)} kcal")
