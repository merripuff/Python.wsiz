#zad1
a = float(input("Podaj pierwszą liczbę całkowitą: "))
b = float(input("Podaj drugą liczbę całkowitą: "))
if(a>b):
    k=a
    p=b
elif(b>a):
    k=b
    p=a
else:
    print("Nie mogę obliczyć liczb")
if a != b:
    while p<=k:
        print(p)
        p+=1
else:
    print("Koniec")

