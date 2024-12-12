import random

allatok = []
print("Add meg a 3 kedvenc állatodat!")

for i in range(3):
    allat = input("Adj meg egy kedvenc állatot: ")
    allatok.append(allat)
    print(f"{i + 1} állat került hozzáadásra a listához.")

print(f"\nA kedvenc állataid:\n{", ".join(map(str, allatok))}")

print(f"\nA kiválasztott kedvenc állat: {random.choice(allatok)}")
