a=int(input("Podaj wysokość choinki: "))
for i in range(1, a + 1):
    print("* " * i)

a=int(input("Podaj wysokość choinki: "))
for i in range(1, a + 1):
    print(" " * (a - i) + "* " * i)

