valuta = input("Milyen valutáról szeretne átváltani? ").upper()
db = int(input("Adja meg az átváltandó összeget: "))
if valuta == "USD":
    osszeg = db*360
    print(f"Az átváltott összeg eredménye: {osszeg} HUF")
if valuta == "EUR":
    osszeg = db*400
    print(f"Az átváltott összeg eredménye: {osszeg} HUF")