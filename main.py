#zad4
dlugosc_drogi = float(input("Podaj długość drogi (w km): "))
spalanie = float(input("Podaj średnie spalanie (w litrach na 100 km): "))
cena_paliwa = 6.5  # Cena paliwa (zł/l)
zuzyte_paliwo = (dlugosc_drogi / 100) * spalanie
koszty_podrozy = zuzyte_paliwo * cena_paliwa
print("Przewidziane zużycie paliwa: ",zuzyte_paliwo," litrów")
print("Koszty podróży wyniosą: koszty_podrozy zł")
