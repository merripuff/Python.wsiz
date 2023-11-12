#zad6
n = int(input("Podaj liczbę studentów w grupie: "))
suma_punktow = 0
licznik_studentow = 0
while licznik_studentow < n:
    punkty = float(input(f"Podaj liczbę punktów dla studenta {licznik_studentow + 1}: "))
    if 0 <= punkty <= 100:
        suma_punktow += punkty
        licznik_studentow += 1
    else:
        print("Błędna wartość! Wprowadź liczbę punktów z zakresu 0-100.")
        continue
srednia = suma_punktow / n
print("Średnia liczba punktów w grupie to: ", srednia)
