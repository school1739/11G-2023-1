import random

red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
zero = 0
double_zero = -1

random_number = random.choice([zero, double_zero] + red + black)

str_random_number = str(random_number)
if random_number == double_zero:
    str_random_number = '00'

print(f'Выпавший номер: {str_random_number}')

print(f'Выигравшая ставка: {str_random_number}')

if random_number not in (zero, double_zero):
    if random_number in red:
        print('Выигравшая ставка: Красное')
    else:
        print('Выигравшая ставка: Чёрное')

    if random_number % 2 == 0:
        print('Выигравшая ставка: Чётное')
    else:
        print('Выигравшая ставка: Нечётное')

    if 1 <= random_number <= 18:
        print('Выигравшая ставка: 1 - 18')
    else:
        print('Выигравшая ставка: 19 - 36')

# Evaluation: OK. Подозрительно изящное решение с использованием команд, которые мы не проходили. Где списал?