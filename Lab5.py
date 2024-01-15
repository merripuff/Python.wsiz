# zad1
# def pole(r):
#     pole_koła= 3.14 * r*r
#     print("Pole koła=", pole_koła)
# pole(2)


# zad2
# def pole(a,b,h):
#     pole_t= h*(a+b)/2
#     print("Pole=", pole_t)
# pole(a=4, b=5, h=2)


# zad3
# def dane(imie, wiek=20):
#     print(f"Imię: {imie}, Wiek: {wiek}")
# dane("Anna", 25)
# dane("Jan")


# zad4
# def liczba(x):
#     if x<0:
#         print("Liczba x jest ujemna")
#     else:
#         print( "Liczba x lest dodatnia")
# liczba(12)


# zad5
# def BMI(waga, wzrost):
#     bmi= waga/(wzrost*wzrost)
#     if bmi<=18.5:
#         print("Niedowaga, BMI=", bmi)
#     elif 18.5 <bmi < 24.9:
#         print("Norma, BMI=", bmi)
#     elif 25< bmi< 30:
#         print("Nadwaga, BMI=", bmi)
#     else:
#         print("Otyłość, BMI=", bmi)
# BMI(90, 1.6)


# zad6
# def PoleTr(a, b, c):
#     if a<=0 or b<=0 or c<=0:
#         print("Podane dane są niepoprawne")
#     else:
#         if a+b<=c or b+c<=a or c+a<=b:
#             print("Z podanych danych nie uda się utworzyć trójkąt")
#         else:
#             p=(a+b+c)/2
#             pole=(p*(p-a)*(p-b)*(p-c))**0.5
#             print("Pole trójkąta to:", pole)
# PoleTr(a=2, b=4, c=5)


# zad7
# def odwroc_string(tekst):
#     return tekst[::-1]
# przyklad_string = "Hello, World!"
# odwrocony_string = odwroc_string(przyklad_string)
# print(odwrocony_string)


# zad8
# def potega(a, n):
#     p = a**n
#     if n == 0:
#         print(1)
#     elif n < 0:
#         print(1/p)
#     else:
#         print(p)
# potega(a=2, n=-2)


# zad9
def fibonacci(n):
    if n <= 0:
        return "Błąd: n powinno być liczbą naturalną większą od zera."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
numer_wyrazu = 12
wynik = fibonacci(numer_wyrazu)
print(f"{numer_wyrazu}-ty wyraz ciągu Fibonacciego: {wynik}")
