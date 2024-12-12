
alma=150
körte= 200
gyumolcs=input("Kérem válassza ki a gyümölcsöt(A/K): ").strip().lower()


if gyumolcs not in ["alma", "körte"]:
        print("Hiba! Csak alma és körte választható!")
   

mennyiseg=int(input(f"Hány db {gyumolcs} gyümölcsöt szeretne?"))
if mennyiseg<= 0:
            print("Hiba! A mennyiségnek pozitív számnak kell lennie")
       
if gyumolcs=="alma":
        fizetendo= mennyiseg*alma
if gyumolcs == "körte":
        fizetendo= mennyiseg*körte

print(f"\nVálasztott gyümölcs: {gyumolcs}")
print(f"Mennyiség: {mennyiseg} darab")
print(f"Fizetendő összeg: {fizetendo} Ft")

