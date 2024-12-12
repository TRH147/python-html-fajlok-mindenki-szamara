import random

allatok = []

print("Add meg a 3 kedvenc állatodat!")

while len(set(allatok)) < 3:
    allat = input("Adj meg egy kedvenc állatot: ").lower()
    if allat not in allatok:
        allatok.append(allat)
        print(f"{len(allatok)} állat került hozzáadásra a listához")

print("\nA kedvenc állataid:")
print(", ".join(allatok))

legjobb_kedvenc = random.choice(allatok)

print(f"\nA kiválasztott kedvenc állat: {legjobb_kedvenc}")
