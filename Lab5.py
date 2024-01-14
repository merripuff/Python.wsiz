def potega(a, n):
    p = a**n
    if n == 0:
        print(1)
    elif n < 0:
        print(1/p)
    else:
        print(p)
potega(a=2, n=-2)
