"""Напишите функцию, принимающую на вход длины двух катетов прямо-
угольного треугольника и возвращающую длину гипотенузы, рассчитан-
ную по теореме Пифагора. В главной программе должен осуществляться
запрос длин сторон у пользователя, вызов функции и вывод на экран
полученного результата."""

from random import randint

# Specifying initial values
number_of_rounds = 0
player1_points = 0
player2_points = 0

SCORE = 'score'
DEFEATS_IN_A_RAW = 'defeat_in_a_raw'
CHEAT_PROB = 'cheat_prob'
LAST_MOVE = 'last_move'

players = [
    {
        SCORE: 0,
        DEFEATS_IN_A_RAW: 0,
        CHEAT_PROB: 0,
        LAST_MOVE: None
    },
    {
        SCORE: 0,
        DEFEATS_IN_A_RAW: 0,
        CHEAT_PROB: 0,
        LAST_MOVE: None
    }
]


# player move function
def player(index):
    players[index][LAST_MOVE] = randint(-1000, +1000) if randint(0, 99) > players[index][CHEAT_PROB] else randint(1000,
                                                                                                                  1000)


def referee(players):
    if players[0][LAST_MOVE] == players[1][LAST_MOVE]:
        print("Draw")
        players[0][SCORE] += 1
        players[1][SCORE] += 1
        players[0][DEFEATS_IN_A_RAW] = players[1][DEFEATS_IN_A_RAW] = 0
        return None

    if players[0][LAST_MOVE] < players[1][LAST_MOVE]:
        won_index, lose_index = 1, 0
    else:
        won_index, lose_index = 0, 1

    players[won_index][SCORE] += 1
    players[won_index][DEFEATS_IN_A_RAW] = 0
    players[won_index][CHEAT_PROB] = 0

    players[lose_index][SCORE] -= 1
    players[lose_index][DEFEATS_IN_A_RAW] += 1
    players[lose_index][CHEAT_PROB] += 5 if players[lose_index][DEFEATS_IN_A_RAW] % 3 == 0 else 0

    return won_index + 1


exit_flag = False

# Process of The Game
while not exit_flag:
    number_of_rounds += 1

    player(0)
    player(1)

    print("Move: player1={}, player2={}".format(players[0][LAST_MOVE], players[1][LAST_MOVE]))

    # Calling the Function
    won_player = referee(players)

    print("Round {} stats: player1={}, player2={}".format(number_of_rounds, players[0], players[1]))

    # if the the rounds are over
    if number_of_rounds > 99:
        print()
        print("The rounds are over.")
        if players[0][SCORE] == players[1][SCORE]:
            print("Draw!")
        elif players[0][SCORE] > players[1][SCORE]:
            print("Player1 finally won!")
        else:
            print("Player2 finally won!")
        exit_flag = True

    if players[0][SCORE] == 50:
        print("Player1 finally won!")
        exit_flag = True

    if players[1][SCORE] == 50:
        print("Player2 finally won!")
        exit_flag = True

# OK