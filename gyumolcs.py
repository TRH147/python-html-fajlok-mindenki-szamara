print("Üdvözöljük a gyümölcsboltban!")
print("Kétféle gyümölcs kapható:")
print("1. Alma - 150 Ft/db")
print("2. Körte - 200 Ft/db")
gyumolcs = input("Kérem válasza ki a gyümölcsöt (alma/körte): ").lower()

if gyumolcs == "alma":
    ar = 150
elif gyumolcs == "körte":
    ar = 200

mennyiseg = int(input(f"Kérem, adja meg, hány darabot szeretne vásárolni:  "))

fizetendo = ar * mennyiseg

print(f"A választott gyümölcs: {gyumolcs}")
print(f"Mennyiség: {mennyiseg} darab")
print(f"Fizetendő összeg: {fizetendo} Ft")
