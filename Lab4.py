def generuj_liste(n, x):
    lista = ["".join(random.choice(string.ascii_lowercase) for _ in range(x)) for _ in range(n)]
    return lista
def konwertuj_na_krotke(lista):
    return tuple(lista)

import random
import string

n = int(input("Podaj wartość n: "))
x = int(input("Podaj wartość x: "))

lista_ciagow = generuj_liste(n, x)

krotka_ciagow = konwertuj_na_krotke(lista_ciagow)

ilosc_znakow = sum(len(ciag) for ciag in lista_ciagow)
print(f"a) Ilość znaków w liście: {ilosc_znakow}")

ilosc_k = sum(ciag.count('k') for ciag in lista_ciagow)
print(f"b) Ilość liter 'k' w liście: {ilosc_k}")

ilosc_kt = sum(ciag.count('kt') for ciag in lista_ciagow)
print(f"c) Ilość ciągów 'kt' w liście: {ilosc_kt}")

s = int(input("Podaj wartość s dla sprawdzenia długości ciągów: "))
ilosc_dluzszych_niz_s = sum(1 for ciag in lista_ciagow if len(ciag) > s)
print(f"d) Ilość ciągów dłuższych niż {s}: {ilosc_dluzszych_niz_s}")


