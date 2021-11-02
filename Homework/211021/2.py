import random
red_list = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black_list = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
green_list = [0, 00]
num = random.choice(red_list + black_list + green_list)
print("Выпавший номер: " + str(num) +
        "\nВыигравшее ставка: " + str(num))
if num in red_list or num in black_list:
    if num in red_list:
        print("Выигравшая ставка: красное")
    elif num in black_list:
        print("Выигравшая ставка: черное")
    if num % 2 == 0:
        print("Выигравшая ставка: Четное")
    else:
        print("Выигравшая ставка: Нечетное")
    if 1 <= num <= 18:
        print("Выигравшая ставка: от 1 до 18")
    else:
        print("Выигравшая ставка: от 19 до 36")