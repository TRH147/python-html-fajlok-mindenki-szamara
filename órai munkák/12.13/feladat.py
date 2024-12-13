def set_alap(set2, a, b, c):
    set1 = list(set2)
    print(f"Függvényargumentumok: {set2}, {a}, {b}, {c}")
    db = 0
    for i in set1:
        if i == a or i == b or i == c:
            db += 1

    if db == 2:
        if a in set1 and b in set1:
            set1.remove(a)
            set1.remove(b)
            set1.append(a + b)
            set1.append(c)
        if a in set1 and c in set1:
            set1.remove(a)
            set1.remove(c)
            set1.append(a + c)
            set1.append(b)
        if b in set1 and c in set1:
            set1.remove(b)
            set1.remove(c)
            set1.append(b + c)
            set1.append(a)

    set1 = set(set1)
    print(f"Módosult halmaz: {set1}")
    if len(set2) == len(set1):
        return False
    else:
        return True
        

print(f"Return: {set_alap({1, 2, 3, 4, 5}, 2, 3, 6)}")
