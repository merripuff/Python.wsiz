#zad4
dlugosc_drogi = float(input("Podaj długość drogi (w km): "))
spalanie = float(input("Podaj średnie spalanie (w litrach na 100 km): "))
cena_paliwa = 6.5
zuzyte_paliwo = (dlugosc_drogi / 100) * spalanie
koszty_podrozy = zuzyte_paliwo * cena_paliwa
print(f"Przewidziane zużycie paliwa: {zuzyte_paliwo:.2f} litrów")
print(f"Koszty podróży wyniosą: {koszty_podrozy:.2f} zł")
