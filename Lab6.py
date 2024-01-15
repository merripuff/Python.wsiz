# zad 1a
# import random
# szczęśliwy_numerek = random.randint(1,49)
# print("Szczęśliwy numerek:", szczęśliwy_numerek)


# zad 1b
# import random
# roczniki = [2004,2003,2002,2005,2006,2001]
# szczęśliwy_rocznik = random.choice(roczniki)
# print("Szczęśliwy rocznik:", szczęśliwy_rocznik)


# zad2
# import math
# sqrt = math.sqrt(81)
# print(sqrt)
# pow = math.pow(8,10)
# print(pow)
# plus = math.sqrt(2) + math.sqrt(3) + math.sqrt(6)
# print(plus)
# sqrt3 = 125 ** (1/3)
# print(sqrt3)


# zad3
# import time
# t = int(input("Podaj sekundy: "))
# while t > 0:
#     print("Pozostało sekund:", t)
#     time.sleep(1)
#     t -= 1
# print("Koniec!")


# zad5
import keyword
words_to_check = ["for", "print", "break", "done", "bad"]
for word in words_to_check:
    if keyword.iskeyword(word):
        print(f"{word} jest słowem kluczowym w Pythonie.")
    else:
        print(f"{word} nie jest słowem kluczowym w Pythonie.")
