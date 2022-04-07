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

player1_points = 0
player2_points = 0
number_of_rounds = 0

cheat_probability = 'cheat_probability'
last_move = 'last_move'
score = 'score'
defeats_in_a_raw = 'defeat_in_a_raw'


players = [
    {
        score: 0,
        defeats_in_a_raw: 0,
        cheat_probability: 0,
        last_move: None
    },
    {
        score: 0,
        defeats_in_a_raw: 0,
        cheat_probability: 0,
        last_move: None
    }
]


def player(index):
    players[index][last_move] = randint(-1000, +1000) if randint(0, 99) > players[index][cheat_probability] else randint(10000,
                                                                                                                         10000)


def referee(players):
    if players[0][last_move] == players[1][last_move]:
        print("Draw")
        players[0][score] += 1
        players[1][score] += 1
        players[0][defeats_in_a_raw] = players[1][defeats_in_a_raw] = 0
        return None

    if players[0][last_move] < players[1][last_move]:
        won_index = 1
        lose_index = 0
    else:
        won_index = 0
        lose_index = 1

    players[won_index][score] += 1
    players[won_index][defeats_in_a_raw] = 0
    players[won_index][cheat_probability] = 0

    players[lose_index][score] -= 1
    players[lose_index][defeats_in_a_raw] += 1
    players[lose_index][cheat_probability] += 5 if players[lose_index][defeats_in_a_raw] % 3 == 0 else 0

    return won_index + 1


while True:
    number_of_rounds += 1

    player(0)
    player(1)

    won_player = referee(players)


    if number_of_rounds > 99:
        print("ну типо раунды закончились")
        if players[0][score] == players[1][score]:
            print("ничья")
        elif players[0][score] > players[1][score]:
            print("игрок 1 выиграл")
        else:
            print("игрок 2 выиграл")
        break

    if players[0][score] == 50:
        print("игрок 1 выиграл")
        break

    if players[1][score] == 50:
        print("игрок 2 выиграл")
        break


# NOT OK. При каждом запуске: Раунды закончились