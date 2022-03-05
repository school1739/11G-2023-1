"""Написать программу, где две функции -- "Игрок 1" и "Игрок 2"
играют в игру, а третья функция -- "Судья" -- следит за ходом игры
и ведёт счёт.

Правила игры:
Оба игрока каждый раунд выдают случайное целое число
в некотором диапазоне. Судья сравнивает эти числа и начисляет игрокам очки:
Если числа равны, оба игрока получают 1 очко (+1). Когда число одно из игроков
больше другого, игрок, который выдал большее число, получает 1 очко (+1),
другой игрок штрафуется на 1 очко (-1). Игра продолжается до тех пор, пока
один из игроков не наберёт 50 очков, но не более 100 раундов.

1. Основные правила (range: -1000, 1000)
2. Режим "Читера": после 3 проигрышей увеличивается вероятность "чита".
Чит: range(+1000, +1000). Изначальная вероятность считерить: 0%.
Увеличение вероятности: +5%. После первой победы с читом чит отключается.
Вероятность чита сохраняется."""

from random import randint

# начальные значения
number_of_rounds = 0
player1_points = 0
player2_points = 0

# игрок 1
def First_Player():
    return randint(0, 150)

# игрок 2
def Second_Player():
    return randint(0, 150)
# Рефери
def Referee(first_peek, second_peek):
    global player1_points, player2_points

    if first_peek == second_peek:
        player1_points += 1
        player2_points += 1
    elif first_peek < second_peek:
        player1_points -= 1
        player2_points += 1
    else:
        player1_points += 1
        player2_points -= 1
while True:
    # функция
    Referee(First_Player(), Second_Player())

    # исход если закончаться раунды
    number_of_rounds += 1
    if number_of_rounds > 100:
        print('Раунды закончились')
        exit()

    # Результат игры
    if player1_points == 50 and player2_points < 50:
        print('Первый игрок победил')
        exit()

    elif player2_points == 50 and player1_points < 50:
        print('Второй игрок победил')
        exit()

    elif player1_points == 50 and player2_points == 50:
        print('Ничья, идем по домам')
        exit()

# NOT OK. При каждом запуске: Раунды закончились