zdanie = input("Podaj zdanie: ")
zdanie_po_usunieciu = ''.join(zdanie[i] for i in range(len(zdanie)) if i % 2 == 0)
print("Tekst po usunięciu znaków o nieparzystych indeksach:", zdanie_po_usunieciu)
