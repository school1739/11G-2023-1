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

from random import randint

points1 = 0
points2 = 0


def player1():
    return randint(0, 10)


def player2():
    return randint(0, 10)


def judge(choice1, choice2):
    global points1, points2
    if choice1 == choice2:
        points1 += 1
        points2 += 1
    elif choice1 > choice2:
        points1 += 1
        points2 -= 1
    else:
        points1 -= 1
        points2 += 1


rounds = 0
while True:
    judge(player1(), player2())

    if points1 >= 50 and points2 >= 50:
        print('Победила бебра!')
        break
    elif points1 >= 50:
        print('1-ый игрок выиграл!')
        break
    elif points2 >= 50:
        print('2-ой игрок выиграл!')
        break

    rounds += 1
    if rounds >= 1000:
        print('Раунды кончились!')
        break

# NOT OK. При каждом запуске "Раунды кончились!" и больше ничего.