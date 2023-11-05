#zad4.1
import random

# Generowanie losowej długości drogi (liczba całkowita z zakresu <1, 100000>)
dlugosc_drogi = random.randint(1, 100000)

# Średnie spalanie (wprowadź dowolne wartości)
spalanie = float(input("Podaj średnie spalanie (w litrach na 100 km): "))

# Cena paliwa
cena_paliwa = 6.5  # Cena paliwa (zł/l)

# Obliczanie zużycia paliwa
zuzyte_paliwo = (dlugosc_drogi / 100) * spalanie

# Obliczanie kosztów podróży
koszty_podrozy = zuzyte_paliwo * cena_paliwa

# Wyświetlanie wyników
print(f"Przewidziane zużycie paliwa: {zuzyte_paliwo:.2f} litrów")
print(f"Koszty podróży wyniosą: {koszty_podrozy:.2f} zł")
