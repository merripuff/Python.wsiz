zdanie = input("Podaj zdanie: ")

slowa = zdanie.split()

najdluzsze_slowo = max(slowa, key=len)

print("Najdłuższe słowo:", najdluzsze_slowo)
print("Długość najdłuższego słowa:", len(najdluzsze_slowo))
