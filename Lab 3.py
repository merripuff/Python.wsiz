# zad1
# for i in range(1, 101, 1):
#     print(i)

# for i in range(20, -1, -2):
#    print(i)

# for i in range(100, -1, -1):
#     print(i)


# zad2
# a=int(input("Podaj liczbę linij i gwiazdek: "))
# for i in range(a):
#     for gwiazdka in range(a):
#          print("*", end="")
#     print()


# zad3
# a=int(input("Podaj wysokość choinki: "))
# for i in range(1, a + 1):
#     print("* " * i)
#
# a=int(input("Podaj wysokość choinki: "))
# for i in range(1, a + 1):
#     print(" " * (a - i) + "* " * i)


# zad4
# n=int(input("Który wyraz ciągu obliczyć: "))
# a=int(input("Podaj pierwszy wyraz ciągu: "))
# r=int(input("Podaj różnicę ciągu: "))
# for i in range(n):
#     x=a+i*r
#     print(x)


# zad5
# num = int(input("Podaj liczbę naturalną: "))
# def f(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * f(n - 1)
# if num < 0:
#     print("Podana liczba jest mniejszą od zera. Silnia nie istnieje dla liczb ujemnych.")
# else:
#     result = f(num)
#     print(f"Silnia liczby {num} wynosi: {result}")


# zad6
# dane = int(input("Wprowadź liczbę całkowitą: "))
# while True:
#     if dane >= 0:
#         print("To jest liczba")
#     else:
#         print(f"Pierwiastek kwadratowy z {dane} wynosi: {0.5*dane}")
#         print("Dziękujemy za skorzystanie z naszej aplikacji")
#     break
#     print("Wprowadź poprawną liczbę całkowitą.")


# zad6 const
# dane = int(input("Wprowadź liczbę całkowitą: "))
# while True:
#     if dane >= 0:
#         print("To jest liczba")
#         continue
#     else:
#         print(f"Pierwiastek kwadratowy z {dane} wynosi: {0.5*dane}")
#         print("Dziękujemy za skorzystanie z naszej aplikacji")
#     break
#     print("Wprowadź poprawną liczbę całkowitą.")


# zad1 po lab3
# tekst = "Rzeszów jest piękny"
# print("Pierwsza litera:", tekst[0])
#
# print("Siódma, dziesiąta, trzynasta oraz druga litera:", tekst[6], tekst[9], tekst[12], tekst[1])


# zad2 po lab3
# tekst = "Python jest super"
# print("Zerowy indeks:", tekst[0])
# print("Ostatni indeks:", tekst[-1])
# print("Co drugi, zaczynając od zerowego:", tekst[0:18:2])
# co_trzeci_pierwszy = tekst[1::3]
# print("Co trzeci zaczynając od pierwszego:", tekst[1:18:3])
# print("Od dziesiątego do ostatniego:", tekst[9:18])
# print("Od końca do początku:", tekst[::-1])


# zad3 po lab3
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
