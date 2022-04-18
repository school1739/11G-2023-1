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

#Условия

cheat_chances = [0] * 2
points = [0] * 2
defeats_in_row = [0] * 2
ranges = [[-1000, 1000], [-1000, 1000]]

max_rounds = 10000
max_points = 50

#Как работают эти ваши читы

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

#Как работают выигрыш и проигрыш

def player_win(player_num):
    defeats_in_row[player_num] = 0
    points[player_num] += 1

def player_lost(player_num):
    defeats_in_row[player_num] += 1
    points[player_num] -= 1

#Делаем судью, расписал кто как и почему выигрывает

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

#Как присуждают эти ваши очки

for i in range(max_rounds):
     judge(player(0), player(1))
     print(f'Ход {i + 1}. Очки: {points}. Ranges: {ranges}')
     if points[0] >= max_points and points[1] >= max_points:     #Выводим результат игры
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