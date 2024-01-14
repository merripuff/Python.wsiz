def PoleTr(a, b, c):
    if a<=0 or b<=0 or c<=0:
        print("Podane dane są niepoprawne")
    else:
        if a+b<=c or b+c<=a or c+a<=b:
            print("Z podanych danych nie uda się utworzyć trójkąt")
        else:
            p=(a+b+c)/2
            pole=(p*(p-a)*(p-b)*(p-c))**0.5
            print("Pole trójkąta to:", pole)
PoleTr(a=2, b=4, c=5)
