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

p1_score, p2_score = 0, 0

def p1():
    return randint (0,10)
def p2():
    return randint (0,10)

def judge(option1, option2):
    global p1_score, p2_score
    if option1 == option2:
        p1_score +=1
        p2_score +=1
    elif option1 > option2:
        p1_score += 1
        p2_score -= 1
    else:
        p1_score -= 1
        p2_score += 1

rounds = 0
while True:
    judge(p1(), p2())

    if p1_score ==50 and p2_score ==50:
         print("TIE")
         break

    if p1_score ==50 and p2_score <50:
        print("Player 1 won")
        break

    if p2_score == 50 and p1_score <50:
        print("Player 2 won")
        break

    if rounds>100:
        print("the rounds are over")
        break

