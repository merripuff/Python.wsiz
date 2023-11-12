#zad1
wiek = int(input("Podaj wiek: "))
if wiek < 0:
    print("Niepoprawne dane")
elif wiek <= 4:
    print("Wejście za darmo")
elif wiek <= 18:
    print("Cena biletu: 10zł")
else:
    print("Cena biletu: 20zł")

