#zad2
def dodawanie(a, b):
    return a + b
def odejmowanie(a, b):
    return a - b
def mnozenie(a, b):
    return a * b
def dzielenie(a, b):
    if b != 0:
        return a / b
    else:
        return "Błąd: Dzielenie przez zero"
def potegowanie(a, b):
    return a ** b
print("Jaką operację chcesz wykonać?")
print("1) dodawanie")
print("2) odejmowanie")
print("3) mnożenie")
print("4) dzielenie")
print("5) potęgowanie")
operacja = int(input("Wpisz numer operacji: "))
arg1 = float(input("Podaj argument 1: "))
arg2 = float(input("Podaj argument 2: "))
if operacja == 1:
    wynik = dodawanie(arg1, arg2)
elif operacja == 2:
    wynik = odejmowanie(arg1, arg2)
elif operacja == 3:
    wynik = mnozenie(arg1, arg2)
elif operacja == 4:
    wynik = dzielenie(arg1, arg2)
elif operacja == 5:
    wynik = potegowanie(arg1, arg2)
else:
    wynik = "Błąd: Nieprawidłowy numer operacji"
print("Wynik:", wynik)
