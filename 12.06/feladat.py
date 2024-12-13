import csv
import datetime as dt

def load_data(file_path):
    with open(file_path, "r", encoding="UTF-8-sig") as file:
        reader = csv.DictReader(file, delimiter=";")
        return [row for row in reader]

def main():
    file_path = "autoverseny.csv"
    data = load_data(file_path)

    # for sor in data:
    #     print(sor["csapat"])
    
    print(f"3. feladat: {len(data)}")

    for i in data:
        if i["versenyzo"] == "Fürge Ferenc" and i["palya"] == "Gran Prix Circuit" and i["kor"] == "3":
            time = dt.datetime.strptime(i["korido"], "%H:%M:%S")
            print(f"4. fleadat: {time.hour*3600 + time.minute*60 + time.second} másodperc")

    print("5. feladat:")
    valasz = input("Kérem egy versenyző nevét:\n")

    go = True
    minimum = None
    gyors = None
    for i in data:
        if i["versenyzo"] == valasz:
            if go == True:
                minimum = i["korido"]
                gyors = i
                go = False
            else:
                if minimum > i["korido"]:
                    minimum = i["korido"]
                    gyors = i

    if gyors == None:
        print("Nincs ilyen versenyző az álloményban!")
    else:
        print(f"6. feladat: {gyors["palya"]}, {gyors["korido"]}")



if __name__ == "__main__":
    main()