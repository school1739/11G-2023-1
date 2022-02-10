"""Напишите функцию, принимающую на вход длины двух катетов прямо-
угольного треугольника и возвращающую длину гипотенузы, рассчитан-
ную по теореме Пифагора. В главной программе должен осуществляться
запрос длин сторон у пользователя, вызов функции и вывод на экран
полученного результата."""


import random
from random import randint


 #Условия

 chances = [0] * 2
 points = [0] * 2
 defeats_in_row = [0] * 2
 ranges = [[-1000, 1000], [-1000, 1000]]

 max_rounds = 10000
 max_points = 50

 #Читы

 def player(player_num):
    try_cheat(player_num)
    return randint(*(ranges[player_num]))

 def player1():
     return randint(0, 10)
 def try_cheat(player_num):
      if defeats_in_row[player_num] >= 3:
           defeats_in_row[player_num] = 0
           chances[player_num] += 5
           if chances[player_num] > 95:
                chances[player_num] = 95
           if randint(0, 100) <= chances[player_num]:
                ranges[player_num][0] += 1000
                ranges[player_num][1] += 1000

 #Выигрыш и проигрыш

 def player2():
     return randint(0, 10)
 def player_win(player_num):
     defeats_in_row[player_num] = 0
     points[player_num] += 1

 def player_lost(player_num):
     defeats_in_row[player_num] += 1
     points[player_num] -= 1

 #Судья

 def judge(choice1, choice2):
     global points1, points2
     if choice1 == choice2:
         points1 += 1
         points2 += 1
         player_win(0)
         player_win(1)
     elif choice1 > choice2:
         points1 += 1
         points2 -= 1
         player_win(0)
         player_lost(1)
     else:
         points1 -= 1
         points2 += 1


 rounds = 0
 while True:
     judge(player1(), player2())
     rounds += 1
     if points1 >= 50 and points2 >= 50:
         print('Ничья!')
         break
     elif points1 >= 50:
         print('1-ый игрок выиграл!')
         break
     elif points2 >= 50:
         print('2-ой игрок выиграл!')
         break
     rounds += 1
     if rounds >= 1000000:
         print('Раунды кончились!')
         break
         player_lost(0)
         player_win(1)

 #Очки
 for i in range(max_rounds):
      judge(player(0), player(1))
      print(f'Ход {i + 1}. Очки: {points}. Ranges: {ranges}')
      if points[0] >= max_points and points[1] >= max_points:     #Вывод результатов игры
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