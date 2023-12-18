listaImion = ["Asia", "Bartek", "Zosia", "Waldek"]
posortowana = sorted(listaImion)
print("a) ", posortowana)
posortowana.append("Mateusz")
posortowana.append("Dorota")
print("b) ", posortowana, posortowana.pop())
posortowana.insert(3, "Kasia")
print("c) ", posortowana)
posortowana.reverse()
print("d) ", posortowana)
listax2 = posortowana*2
print(listax2)

