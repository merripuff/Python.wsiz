#zad4
a = int(input("Podaj pierwszą liczbę całkowitą: "))
b = int(input("Podaj drugą liczbę całkowitą: "))
# Wybór początkowej i końcowej liczby do wypisania
p = min(a, b)
k = max(a, b)
print("Liczby parzyste od {p} do {k}: ")
for liczba in range(p, k + 1):
    if liczba % 2 == 0:
        print(liczba)
    else:
        continue
