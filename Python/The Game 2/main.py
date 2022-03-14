"""
Написать программу, где две функции -- "Игрок 1" и "Игрок 2"
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
Вероятность чита сохраняется.
"""

from random import randint

points = [0] * 2
ranges = [[-1000, 1000], [-1000, 1000]]
defeats_in_row = [0] * 2
cheat_chances = [0] * 2

max_rounds = 10000
max_points = 50


class Player:
    def __init__(self):
        self.points = 0
        self.range = [-1000, 1000]
        self.defeats_in_row = 0
        self.cheat_chance = 0

    def make_turn(self):
        self.try_cheat()
        return randint(*self.range)

    def try_cheat(self):
        if self.defeats_in_row >= 3:
            self.defeats_in_row = 0
            self.cheat_chance += 5
            if self.cheat_chance > 95:
                self.cheat_chance = 95
            if randint(0, 100) <= self.cheat_chance:
                self.range[0] += 1000
                self.range[1] += 1000

    def win(self):
        self.defeats_in_row = 0

    def draw(self):
        self.win()

    def lose(self):
        self.defeats_in_row += 1


class Judge:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def iteration(self):
        choice1 = self.player1.make_turn()
        choice2 = self.player2.make_turn()
        if choice1 == choice2:
            self.player1.draw()
            self.player2.draw()
            self.points1 += 1
            self.points2 += 1
        elif choice1 > choice2:
            self.player1.win()
            self.player2.lose()
            self.points1 += 1
            self.points2 += 1
        else:
            self.player1.lose()
            self.player2.win()
            self.points1 += 1
            self.points2 += 1

    @staticmethod
    def player_win(winner, loser):
        winner.win()
        loser.lose()
        winner.points += 1
        loser.points -= 1

    @staticmethod
    def draw(player1, player2):
        player1.draw()
        player2.draw()
        player1.points += 1
        player2.points += 1




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
