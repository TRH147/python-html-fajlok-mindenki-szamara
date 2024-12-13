import csv

data = []
with open("autoverseny.csv", "r", encoding='utf-8-sig') as file:
    reader = csv.DictReader(file, delimiter=";")
    
    for row in reader:
        data.append(row)
"""
print(data[len(data)-200]['csapat']+"\n"+data[len(data)-200]['versenyzo'])
"""
print(f"3. feladat: {len(data)}")

def idoSwitch(korido):
    ido_reszek = korido.split(":")
    ora = int(ido_reszek[0])
    perc = int(ido_reszek[1])
    masodperc = int(ido_reszek[2])
    return ora*3600 + perc*60 + masodperc

for i in data:
    if i['versenyzo'] == "Fürge Ferenc" and i['palya'] == "Gran Prix Circuit" and i['kor'] == "3":
          print(f"4. feladat: {idoSwitch(i["korido"])}")

beNev = input("Kerem egy versenyzo nevet:")

legjobbIdo = {}
"""
for row in data:
    if row['versenyzo'] == beNev:
        legjobbIdo[row['palya']] = []

for row in data:
    if row['versenyzo'] == beNev:
        legjobbIdo[row['palya']].append(idoSwitch(row['korido']))
"""

for row in data:
    if row['versenyzo'] == beNev:
        if row["palya"] not in legjobbIdo:
            legjobbIdo[row['palya']] = []
        legjobbIdo[row['palya']].append(idoSwitch(row['korido']))

def idoVissza(masodperc):
    ora = masodperc // 3600
    fennmarado = masodperc % 3600
    perc = fennmarado // 60
    masodperc = fennmarado % 60

    return f"{ora:02};{perc:02};{masodperc:02}"

min_dict = {}
for k, v in legjobbIdo.items():
    min_dict[k] = min(v)

legkisebb_ertek = min(min_dict, key=min_dict.get)
print(legkisebb_ertek +" "+ idoVissza(min_dict[legkisebb_ertek]))