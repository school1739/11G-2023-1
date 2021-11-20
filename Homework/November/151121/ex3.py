# сделал не до конца, так как находит просто 3 орла/решки НЕПОДРЯД


import random

mon = [1, 2]
a = 0
tries = 0
while a != 3:  # пока не наберется 3 орла/решки
    ran = random.choice(mon)
    if ran == 1:
        a += 1
        print("Р", end=" ")
        tries += 1
    else:
        a += 0
        print("О", end=" ")
        tries += 1


print("Попытки: ", tries)