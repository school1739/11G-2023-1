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
import random

default_range = (-1000, 1000)
cheat_range = (1000, 1000)
cheat_factor = 5
cheat_min_defeats = 3


def init_player():
    return {
        "points": 0,
        "cur_number": 0,
        "defeats": 0,
        "cheat_factor": 0,
        "in_cheat": False,
        "range": (default_range[0], default_range[1])
    }


def try_cheat(player):
    if not player["in_cheat"]:
        roll_chance = random.randint(1, 100)
        if roll_chance <= player["cheat_factor"]:
            player["range"] = (cheat_range[0], cheat_range[1])
            player["in_cheat"] = True


def player_roll(player):
    try_cheat(player)
    player["cur_number"] = random.randint(
        player["range"][0], player["range"][1])


def player_win(player):
    player["points"] += 1
    if player["in_cheat"]:
        player["in_cheat"] = False
        player["range"] = (default_range[0], default_range[1])


def player_lose(player):
    player["points"] -= 1
    player["defeats"] += 1
    if player["defeats"] == cheat_min_defeats:
        player["cheat_factor"] += cheat_factor


def judge(p1, p2):
    if p1["cur_number"] > p2["cur_number"]:
        player_win(p1)
        player_lose(p2)
        return 1, -1
    if p1["cur_number"] < p2["cur_number"]:
        player_lose(p1)
        player_win(p2)
        return -1, 1
    player_win(p1)
    player_win(p2)
    return 1, 1


def print_info(player, no):
    print("Игрок %d" % no)
    print("Диапазон: %s" % str(player["range"]))
    print("Выпало: %d" % player["cur_number"])
    print("--------")


def play(max_points=50, max_rounds=100):
    player1 = init_player()
    player2 = init_player()
    cur_round = 1

    while cur_round <= max_rounds:
        print("Раунд %d" % cur_round)
        print("========")

        player_roll(player1)
        player_roll(player2)

        print_info(player1, 1)
        print_info(player2, 2)

        print("Итог раунда")
        p1_res, p2_res = judge(player1, player2)

        pts1 = player1["points"]
        pts2 = player2["points"]

        print("Игрок 1: %d (%+d), Игрок 2: %d (%+d)" % (
            pts1, p1_res, pts2, p2_res))

        pts1_reached_max = pts1 >= max_points
        pts2_reached_max = pts2 >= max_points

        print("========\n")

        if pts1_reached_max and pts2_reached_max:
            print("Ничья!")
            return

        if pts1_reached_max:
            print("Победил игрок 1!")
            return

        if pts2_reached_max:
            print("Победил игрок 2!")
            return

        cur_round += 1

    print("Превышено максимальное число раундов!")


if __name__ == '__main__': # Прикольно, конечно, но, так-то, попахивает "помощью друга".
    play()

# OK