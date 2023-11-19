number = int(input("Podaj liczbę naturalną: "))
def s(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * s(n - 1)
if number < 0:
    print("Podana liczba jest mniejszą od zera. Silnia nie istnieje dla liczb ujemnych.")
else:
    result = s(number)
    print(f"Silnia liczby {number} wynosi: {result}")
