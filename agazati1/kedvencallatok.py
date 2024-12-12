import random

def kedvenc_allatok():
    allatok = []  
    print("Adj meg 3 kedvenc állatodat!")

    while len(set(allatok)) < 3:  
        allat = input("Kedvenc állat: ").strip()
        if allat in allatok:
            print(f"'{allat}' már szerepel a listában, adj meg egy másikat!")
        else:
            allatok.append(allat)
            print(f"'{allat}' bekerült a listába.")

    print(f"\nÖsszesen {len(allatok)} állatnév került hozzáadásra.")
    print("Az összegyűjtött kedvenc állatok: " + ", ".join(allatok))

  
    legjobb_kedvenc = random.choice(allatok)
    print(f"A legjobb kedvenced: {legjobb_kedvenc}")


if __name__ == "__main__":
    kedvenc_allatok()





