#zad3
a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))
delta = b**2 - 4*a*c
print("Delta: ", delta)
if a != 0:
    if delta < 0:
        print("Równanie nie ma rozwiązań")
    elif delta > 0:
            x1 = (-b + delta**(1/2)) / (2*a)
            x2 = (-b - delta**(1/2)) / (2*a)
            print("Równanie ma dwa rozwiązania: ", x1, x2)
    else:
        x = -c/b
        print("Równanie ma jedno rozwiązanie: ", x)
else:
    x = -c/b
    print("Równanie nie jest kwadratowe i ma dwa rozwiązanie: ", x)
