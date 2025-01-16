nev = input("Adja meg az üzlet nevét: ")

arak=[]
db=0
while True:
    ar = int(input("Adja meg termék árát: "))
    arak.append(ar)
    db+=1

    if db >=4:
        meg = input("Szeretne még egy termék árát megadni? (igen/nem): ")
        if meg == "nem":
            break

print(f"Üzlet neve: {nev}")
print(f"Átlagos költség: {round(sum(arak)/len(arak))} Ft")