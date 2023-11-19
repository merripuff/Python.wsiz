dane = int(input("Wprowadź liczbę całkowitą: "))
while True:
    if dane >= 0:
        print("To jest liczba")
        continue
    else:
        print(f"Pierwiastek kwadratowy z {dane} wynosi: {0.5*dane}")
        print("Dziękujemy za skorzystanie z naszej aplikacji")
    break
    print("Wprowadź poprawną liczbę całkowitą.")
