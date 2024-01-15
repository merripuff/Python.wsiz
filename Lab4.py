# zad1
# listaImion = ["Asia", "Bartek", "Zosia", "Waldek"]
# posortowana = sorted(listaImion)
# print("a) ", posortowana)
# posortowana.append("Mateusz")
# posortowana.append("Dorota")
# print("b) ", posortowana, posortowana.pop())
# posortowana.insert(3, "Kasia")
# print("c) ", posortowana)
# posortowana.reverse()
# print("d) ", posortowana)
# listax2 = posortowana*2
# print(listax2)


# zad2
# tekst = "Rzeszów jest piękny"
# print("a)", tekst[0])
# print("b)", tekst[6:12:3], tekst[1])


# zad3
# tekst ="Python test super"
# print("a)", tekst[0], tekst[-1])
# print("b)", tekst[0::2])
# print("c)", tekst[1::3])
# print("d)", tekst[10:])
# print("e)", tekst[::-1])


# zad4
# imię = input("Podaj swoje imię: ")
# print("Witaj, ", imię)
#
# wiek = input("Podaj swój wiek: ")
# print("Twój wiek to: ", wiek)
#
# nazwisko = input("Podaj nazwisko: ")
# print("Twoje iniciały: ", imię[0], nazwisko[0])
#
# łańcuch = input("Podaj łańcuch: ")
# łańcuchx5 = łańcuch*5
# print(łańcuchx5)
# drugi_łańcuch = input("Podaj drugi łańcuch: ")
# print(łańcuch, drugi_łańcuch)


# zad1 po lab4
# def generuj_liste(n, x):
#     lista = ["".join(random.choice(string.ascii_lowercase) for _ in range(x)) for _ in range(n)]
#     return lista
# def konwertuj_na_krotke(lista):
#     return tuple(lista)
#
# import random
# import string
#
# n = int(input("Podaj wartość n: "))
# x = int(input("Podaj wartość x: "))
#
# lista_ciagow = generuj_liste(n, x)
#
# krotka_ciagow = konwertuj_na_krotke(lista_ciagow)
#
# ilosc_znakow = sum(len(ciag) for ciag in lista_ciagow)
# print(f"a) Ilość znaków w liście: {ilosc_znakow}")
#
# ilosc_k = sum(ciag.count('k') for ciag in lista_ciagow)
# print(f"b) Ilość liter 'k' w liście: {ilosc_k}")
#
# ilosc_kt = sum(ciag.count('kt') for ciag in lista_ciagow)
# print(f"c) Ilość ciągów 'kt' w liście: {ilosc_kt}")
#
# s = int(input("Podaj wartość s dla sprawdzenia długości ciągów: "))
# ilosc_dluzszych_niz_s = sum(1 for ciag in lista_ciagow if len(ciag) > s)
# print(f"d) Ilość ciągów dłuższych niż {s}: {ilosc_dluzszych_niz_s}")


# zad2 po lab4
# listaZakupów = {"Paprika": 6.99, "Rys": 9.99, "Piwo": 3.59}
# print(listaZakupów)
# suma = 0
# for item in listaZakupów:
#     suma += listaZakupów[item]
#     print(item)
# print(suma)


# zad3 po lab4
# rachunki_za_prad = {
#     'styczeń': 250,
#     'luty': 280,
#     'marzec': 220,
#     'kwiecień': 300,
#     'maj': 260,
#     'czerwiec': 240,
#     'lipiec': 280,
#     'sierpień': 310,
#     'wrzesień': 270,
#     'październik': 290,
#     'listopad': 250,
#     'grudzień': 300
# }
#
# lista_rachunkow = list(rachunki_za_prad.values())
#
# maksymalna_wartosc = max(lista_rachunkow)
# minimalna_wartosc = min(lista_rachunkow)
# suma_wartosci = sum(lista_rachunkow)
# srednia_wartosc = suma_wartosci / len(lista_rachunkow)
#
# print(f"Maksymalna wartość: {maksymalna_wartosc}")
# print(f"Minimalna wartość: {minimalna_wartosc}")
# print(f"Suma wartości: {suma_wartosci}")
# print(f"Średnia wartość: {srednia_wartosc}")
#
# ostatni_miesiac = list(rachunki_za_prad.keys())[-1]
# ostatni_rachunek = rachunki_za_prad[ostatni_miesiac]
#
# if ostatni_rachunek > srednia_wartosc:
#     print("Zacznij oszczędzać.")
# else:
#     print("Jesteś bezpieczny.")


# zad dodatk1
# zdanie = input("Podaj zdanie: ")
# zdanie = zdanie.lower().replace(" ", "")
# litery_w_kolejnosci = sorted(zdanie)
# print("Litery w kolejności alfabetycznej:", ", ".join(litery_w_kolejnosci))
# brakujace_litery = [litera for litera in "abcdefghijklmnopqrstuvwxyz" if litera not in zdanie]
# print("Litery, których brakuje:", ", ".join(brakujace_litery))


# zad dodatk2
# zdanie = input("Podaj zdanie: ")
# zdanie_po_usunieciu = ''.join(zdanie[i] for i in range(len(zdanie)) if i % 2 == 0)
# print("Tekst po usunięciu znaków o nieparzystych indeksach:", zdanie_po_usunieciu)


# zad dodatk3
# zdanie = input("Podaj zdanie: ")
# wyrazy = zdanie.split()
# zdanie_sformatowane = ' '.join(word.capitalize() for word in wyrazy)
# print("Zdanie z każdym wyrazem zaczynającym się i kończącym wielką literą:")
# print(zdanie_sformatowane)


# zad dodatk4
# ciag_znakow = input("Podaj ciąg znaków: ")
# licznik_znakow = {}
# ciag_zmieniony = ''
# for znak in ciag_znakow:
#     if znak in licznik_znakow:
#         ciag_zmieniony += '@'
#     else:
#         licznik_znakow[znak] = 1
#         ciag_zmieniony += znak
# print("Zmieniony ciąg znaków:", ciag_zmieniony)


# zad dodatk5
# zdanie = input("Podaj zdanie: ")
# slowa = zdanie.split()
# najdluzsze_slowo = max(slowa, key=len)
# print("Najdłuższe słowo:", najdluzsze_slowo)
# print("Długość najdłuższego słowa:", len(najdluzsze_slowo))



