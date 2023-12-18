zdanie = input("Podaj zdanie: ")
zdanie = zdanie.lower().replace(" ", "")
litery_w_kolejnosci = sorted(zdanie)
print("Litery w kolejności alfabetycznej:", ", ".join(litery_w_kolejnosci))
brakujace_litery = [litera for litera in "abcdefghijklmnopqrstuvwxyz" if litera not in zdanie]
print("Litery, których brakuje:", ", ".join(brakujace_litery))
