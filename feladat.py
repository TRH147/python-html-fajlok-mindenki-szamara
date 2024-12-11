import csv

def load_data (file_path):
    with open(file_path, 'r', encoding='UTF-8') as file:
        reader =csv.DictReader(file, delimiter=';')
        return [row for row in reader]

def main():
    file_path='autoverseny.csv'
    data = load_data(file_path)


    for sor in data:
        if sor ['versenyzo'] == 'Szélsebes Szerpentínia' and sor ['palya'] == 'Gran Prix':
            print(sor)


if __name__ == "__main__":
    main()