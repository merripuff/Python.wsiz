def fibonacci(n):
    if n <= 0:
        return "Błąd: n powinno być liczbą naturalną większą od zera."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
numer_wyrazu = 12
wynik = fibonacci(numer_wyrazu)
print(f"{numer_wyrazu}-ty wyraz ciągu Fibonacciego: {wynik}")
