name = input("Jak masz na imię? ")
print(f"Witaj, {name}!")

wiek = int(input("Podaj swój wiek: "))
if wiek <= 0:
     wiek = int(input("Podaj swój poprawny wiek: "))
     print("Twój wiek to: ", wiek)
elif wiek >= 0:
    print("Twój wiek to: ", wiek)

imie = input("Podaj swoje imię: ")
nazwisko = input("Podaj swoje nazwisko: ")
inicjaly = imie[0] + nazwisko[0]
print("Twoje inicjały to:", inicjaly)

lanuch = input("Podaj jakiś łańcuch: ")
for i in range(5):
    print(lanuch)

first = input("Podaj pierwszy łańcuch: ")
second = input("Podaj drugi łańcuch: ")
third = first + second
print("Połączone łańcuchy:", third)

one = input("Podaj pierwszy łańcuch: ")
two = input("Podaj drugi łańcuch: ")
h1 = one[:len(one)//2]
h2 = two[len(two)//2:]
three = h1 + h2
print("Połączone połowy:", three)

