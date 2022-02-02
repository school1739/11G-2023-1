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


# First player
def First_Player():
    return randint(0, 150)


# Second player
def Second_Player():
    return randint(0, 150)


# The Function of Referee
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


# Process of The Game
while True:
    # Calling the Function
    Referee(First_Player(), Second_Player())

    # if the the rounds are over
    number_of_rounds += 1
    if number_of_rounds > 100:
        print('The rounds are over')
        exit()

    # The results of The Game

    if player1_points == 50 and player2_points < 50:
        print('First player won!')
        exit()

    elif player2_points == 50 and player1_points < 50:
        print('Second player won!')
        exit()

    elif player1_points == 50 and player2_points == 50:
        print('Draw!')
        exit()
