#zad3
# Pobieranie długości boków od użytkownika
dlugosc = float(input("Podaj długość boku a: "))
szerokosc = float(input("Podaj długość boku b: "))

# Obliczanie pola prostokąta
pole = dlugosc * szerokosc

# Obliczanie obwodu prostokąta
obwod = 2 * (dlugosc + szerokosc)

# Wyświetlanie wyników
print(f"Pole prostokąta o bokach {dlugosc} i {szerokosc} wynosi {pole}")
print(f"Obwód prostokąta o bokach {dlugosc} i {szerokosc} wynosi {obwod}")

