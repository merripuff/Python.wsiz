import random

a = random.randint(3, 7)
b = random.randint(3, 7)

X = set(random.randint(0, 10) for _ in range(a))
Y = set(random.randint(0, 10) for _ in range(b))

print(f"a) Zbiór X zawiera liczbę 5: {5 in X}")

print(f"b) Zbiór X jest podzbiorem zbioru Y: {X.issubset(Y)}")

print(f"c) Zbiór Y jest podzbiorem zbioru X: {Y.issubset(X)}")

print(f"d) Zbiór X jest nadzbiorem zbioru Y: {X.issuperset(Y)}")

print(f"e) Zbiór Y jest nadzbiorem zbioru X: {Y.issuperset(X)}")

suma_zbiorow = X.union(Y)
print(f"f) Suma zbiorów X i Y: {suma_zbiorow}")

roznica_X_Y = X.difference(Y)
print(f"g) Różnica zbiorów X i Y: {roznica_X_Y}")

roznica_Y_X = Y.difference(X)
print(f"h) Różnica zbiorów Y i X: {roznica_Y_X}")

iloczyn_zbiorow = X.intersection(Y)
print(f"i) Iloczyn zbiorów X i Y: {iloczyn_zbiorow}")

roznica_symetryczna = X.symmetric_difference(Y)
print(f"j) Różnica symetryczna zbiorów X i Y: {roznica_symetryczna}")

max_wartosc_X = max(X)
max_wartosc_Y = max(Y)
print(f"k) Najwyższa wartość w zbiorze X: {max_wartosc_X}")
print(f"   Najwyższa wartość w zbiorze Y: {max_wartosc_Y}")

pierwszy_element_X = X.pop()
Y.add(pierwszy_element_X)

Y.update(X.copy())

X.clear()
Y.clear()
