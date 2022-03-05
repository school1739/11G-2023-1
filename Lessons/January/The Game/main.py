"""Напишите функцию, принимающую на вход длины двух катетов прямо-
угольного треугольника и возвращающую длину гипотенузы, рассчитан-
ную по теореме Пифагора. В главной программе должен осуществляться
запрос длин сторон у пользователя, вызов функции и вывод на экран
полученного результата."""

import random


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
    rounds += 1
    if points1 >= 50 and points2 >= 50:
        print('Победила дружба!')
        break
    elif points1 >= 50:
        print('1-ый игрок молодец!')
        break
    elif points2 >= 50:
        print('2-ой игрок молодец!')
        break
    rounds+=1
    if rounds >= 1000000:
        print('Раунды кончились!')
        break

# +-OK. Где читы?