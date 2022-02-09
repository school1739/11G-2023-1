"""Написать программу, где две функции -- "Игрок 1" и "Игрок 2"
играют в игру, а третья функция -- "Судья" -- следит за ходом игры
и ведёт счёт.

Правила игры:
Оба игрока кажый раунд выдают случайное целое число
в некотором диапазоне. Судья сравнивает эти числа и начисляет игрокам очки:
Если числа равны, оба игрока получают 1 очко (+1). Когда число одно из игроков
больше другого, игрок, который выдал большее число, получает 1 очко (+1),
другой игрок штрафуется на 1 очко (-1). Игра продолжается до тех пор, пока
один из игроков не наберёт 50 очков, но не более 100 раундов."""

"""1. Основные правила (range: -1000, 1000)
2. Режим "Читера": после 3 проигрышей увеличивается вероятность "чита".
Чит: range(+1000, +1000). Изначальная вероятность считерить: 0%.
Увеличение вероятности: +5%. После первой победы с читом чит отключается.
Вероятность чита сохраняется."""

import random

# Некоторый диапазон
range_numbers = [-1000, 1000]


def cheat(fails,amount_fails):
    # Активированность чита
    cheat = False

    probabilty = random.randint(0, 100)
    # Вероятность срабатывания чита
    if probabilty <= fails * 5 and amount_fails>=3:
        cheat = True
        print("Cheat active")
    return cheat


def gamer_1(fails1):
    num1 = random.randint(*range_numbers)
    # Активированность чита
    if cheat(fails1,fails1_in_a_row) is True:
        num1 += 1000
    return num1


def gamer_2(fails2):
    num2 = random.randint(*range_numbers)
    # Активированность чита
    if cheat(fails2,fails2_in_a_row) is True:
        num2 += 1000
    return num2


# Счет
score_1 = 0
score_2 = 0
# Проигрыши и кол-во проигрышей подряд
fails1, fails1_in_a_row = 0, 0
fails2, fails2_in_a_row = 0, 0


def referee():
    global fails1, fails1_in_a_row
    global fails2, fails2_in_a_row
    global score_1, score_2

    num_1 = gamer_1(fails1)
    num_2 = gamer_2(fails2)
    if num_2 == num_1:
        score_1 += 1
        score_2 += 1
        fails1_in_a_row,fails2_in_a_row=0,0
        print("Ничья")
    elif num_2 > num_1:
        score_1 -= 1
        score_2 += 1
        fails1 += 1
        fails1_in_a_row+=1
        fails2_in_a_row=0
        print("Второй выиграл")

    elif num_2 < num_1:
        score_1 += 1
        score_2 -= 1
        fails2 += 1
        fails1_in_a_row=0
        fails2_in_a_row+=1
        print("Первый выиграл")



# Раунды
for i in range(10000):
    referee()
    if score_1 == 50:
        print(f'Первый победил в игре')
        break
    elif score_2 == 50:
        print(f'Второй победил в игре')
        break

if score_1 < 50 and score_2 < 50:
    print(f'Никто не дошел до победого счета')

# Надеюсь, что я правильно понял правила этой игры, т.к. меня не было на первом уроке, когда выполнялось это задание
