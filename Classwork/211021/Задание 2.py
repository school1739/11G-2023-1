import random
n = random.choice([0, 00, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36])

col = 0
number = 0
bet = 0

if n == 1 or 3 or 5 or 7 or 9 or 12 or 14 or 16 or 18 or 19 or 21 or 23 or 25 or 27 or 30 or 32 or 34 or 36 and n != 0 and n != 00:
    col = "красное"
if n == 2 or 4 or 6 or 8 or 10 or 11 or 13 or 15 or 17 or 20 or 22 or 24 or 26 or 28 or 29 or 31 or 33 or 35 and n != 0 and n != 00:
    col = "чёрное"
if n % 2 == 0 and n != 0 and n != 00:
    number = "чётное"
if n % 2 != 0 and n != 0 and n != 00:
    number = "нечётное"
if n <= 18 and n != 0 and n != 00:
    bet = "от 1 до 18"
if n > 18 and n != 0 and n != 00:
    bet = "от 19 до 36"

if n == 0 or n == 00:
    print("Выпавший номер:", n, "...")
    print("Выйгравшая ставка:", n)
if n != 0 and n != 00:
    print("Выпавший номер:", n, "...")
    print("Выйгравшая ставка:", n)
    print("Выйгравшая ставка:", col)
    print("Выйгравшая ставка:", number)
    print("Выйгравшая ставка:", bet)
