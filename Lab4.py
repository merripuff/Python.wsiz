
rachunki_za_prad = {
    'styczeń': 250,
    'luty': 280,
    'marzec': 220,
    'kwiecień': 300,
    'maj': 260,
    'czerwiec': 240,
    'lipiec': 280,
    'sierpień': 310,
    'wrzesień': 270,
    'październik': 290,
    'listopad': 250,
    'grudzień': 300
}

lista_rachunkow = list(rachunki_za_prad.values())

maksymalna_wartosc = max(lista_rachunkow)
minimalna_wartosc = min(lista_rachunkow)
suma_wartosci = sum(lista_rachunkow)
srednia_wartosc = suma_wartosci / len(lista_rachunkow)

print(f"Maksymalna wartość: {maksymalna_wartosc}")
print(f"Minimalna wartość: {minimalna_wartosc}")
print(f"Suma wartości: {suma_wartosci}")
print(f"Średnia wartość: {srednia_wartosc}")

ostatni_miesiac = list(rachunki_za_prad.keys())[-1]
ostatni_rachunek = rachunki_za_prad[ostatni_miesiac]

if ostatni_rachunek > srednia_wartosc:
    print("Zacznij oszczędzać.")
else:
    print("Jesteś bezpieczny.")
