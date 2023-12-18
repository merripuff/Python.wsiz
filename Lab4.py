listaZakupów = {"Paprika": 6.99, "Rys": 9.99, "Piwo": 3.59}
print(listaZakupów)
suma = 0
for item in listaZakupów:
    suma += listaZakupów[item]
    print(item)
print(suma)

