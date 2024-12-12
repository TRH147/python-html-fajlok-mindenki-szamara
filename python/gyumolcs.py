a = 150
k = 200

print("Üdvözöljük a gyümölcsboltban!\nKétféle gyümölcs kapható:\n1. Alma - 150 Ft/db\n2. Körte - 200Ft/db")
gyumi = input("Kérem, válassza ki a gyümölcsöt (alma/körte): ").lower()
menny = int(input("Kérem, adja meg, hány darabot szeretne vásárolni: "))

if gyumi == "alma":
    print("A választott gyümölcs: Alma")
    print(f"Mennyiség: {menny} darab")
    print(f"Fizetendő összeg: {menny * a} Ft")
else:
    print("A választott gyümölcs: Körte")
    print(f"Mennyiség: {menny} darab")
    print(f"Fizetendő összeg: {menny * k} Ft")