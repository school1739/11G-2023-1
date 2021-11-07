import random

a = random.choice([00, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
     30, 31, 32, 33, 34, 35, 36])
print('Выпавшее число: ' + str(a))
print('Выиграшная ставка: ' + str(a))
if a == 1 or a == 3 or a == 5 or a == 7 or a == 9 or a == 12 or a == 14 or a == 16 or a == 18 or a == 19 or a == 21 or a == 23 or a == 25 or a == 27 or a == 30 or a == 32 or a == 34 or a == 36:
    print("Выиграшная ставка: красный")
elif a == 0 or 00:
    print("Выиграшная ставка: зелёный")
else:
    print("Выиграшная ставка: чёрный")
if a % 2 == 0 and a != 0 and a != 00:
    print("Выиграшная ставка: чётное")
elif a % 2 == 1 and a != 0 and a != 00:
    print("Выиграшная ставка: нечётное")
else:
    print()
if a == 1 or a == 2 or a == 3 or a == 4 or a == 5 or a == 6 or a == 7 or a == 8 or a == 9 or a == 10 or a == 11 or a == 12 or a == 13 or a == 14 or a == a == 15 or a == 16 or a == 17 or a == 18:
    print("Выигршная ставка: от 1 до 18")
if a == 19 or a == 20 or a == 21 or a == 22 or a == 23 or a == 24 or a == 25 or a == 26 or a==27 or a == 28 or a == 29 or a == 30 or a == 31 or a == 32 or a == 33 or a == 33 or a == 34 or a == 35 or a == 36:
    print("Выиграшная ставка: от 19 до 36")
if a == 0:
    print("Выигрышная ставка 0")
if a == 00:
    print("Выигрышная ставка 00")