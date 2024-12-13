def beolvas(szoveg):
    lista = []
    with open(szoveg, "r", encoding="UTF-8") as file:
        for line in file:
            data = line.strip().split(";")
            lista.append({"szin":data[0], "meret":float(data[1]), "sebesseg":int(data[2])})
    return lista

pelda = beolvas("be.txt")

for i in pelda:
    print(i)
