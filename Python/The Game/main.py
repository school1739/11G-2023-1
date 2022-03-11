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

points = [0] * 2
ranges = [[-1000, 1000], [-1000, 1000]]
defeats_in_row = [0] * 2
cheat_chances = [0] * 2

max_rounds = 10000
max_points = 50


def player(player_num):
    try_cheat(player_num)
    return randint(*(ranges[player_num]))


def try_cheat(player_num):
    if defeats_in_row[player_num] >= 3:
        defeats_in_row[player_num] = 0
        cheat_chances[player_num] += 5
        if cheat_chances[player_num] > 95:
            cheat_chances[player_num] = 95
        if randint(0, 100) <= cheat_chances[player_num]:
            ranges[player_num][0] += 1000
            ranges[player_num][1] += 1000


def player_win(player_num):
    defeats_in_row[player_num] = 0
    points[player_num] += 1


def player_lost(player_num):
    defeats_in_row[player_num] += 1
    points[player_num] -= 1


def judge(choice1, choice2):
    if choice1 == choice2:
        player_win(0)
        player_win(1)
    elif choice1 > choice2:
        player_win(0)
        player_lost(1)
    else:
        player_lost(0)
        player_win(1)


for i in range(max_rounds):
    judge(player(0), player(1))

    print(f'Ход {i + 1}. Очки: {points}. Ranges: {ranges}')

    if points[0] >= max_points and points[1] >= max_points:
        print('Ничья!')
        break
    elif points[0] >= max_points:
        print('1-ый игрок выиграл!')
        break
    elif points[1] >= max_points:
        print('2-ой игрок выиграл!')
        break
else:
    print('Раунды кончились!')

# NOT OK. При каждом запуске: Раунды закончились