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
import enum
from random import randint

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

max_rounds = 10000
max_points = 50

score_table = Table(title='Очки игроков',
                    title_style='bold italic green1',
                    header_style='blue bold',
                    border_style='aquamarine3')
score_table.add_column('№', style='green')
score_table.add_column('Ход 1', style='yellow')
score_table.add_column('Ход 2', style='yellow')
score_table.add_column('Очки 1', style='dark_slate_gray1')
score_table.add_column('Очки 2', style='dark_slate_gray1')
score_table.add_column('Чит 1?', justify='center')
score_table.add_column('Чит 2?', justify='center')
score_table.add_column('Победитель', justify='center', style='bold gold1')


# Класс игрока
class Player:
    # Конструктор класса
    def __init__(self):
        self.points = 0
        self.range = [-1000, 1000]
        self.defeats_in_row = 0
        self.cheat_chance = 0

        self.last_move = 0
        self.is_cheat = 0
        self.total_cheats = 0

    # Имитация хода игрока
    def make_turn(self):
        self.try_cheat()
        self.last_move = randint(*self.range)
        return self.last_move

    # Попытка считерить, если проиграл 3 раза подряд
    def try_cheat(self):
        if self.defeats_in_row >= 3:
            self.defeats_in_row = 0
            self.cheat_chance += 5
            if self.cheat_chance > 95:
                self.cheat_chance = 95
            if randint(0, 100) <= self.cheat_chance:
                self.is_cheat = True
                self.total_cheats += 1
                self.range[0] += 1000
                self.range[1] += 1000
                return
        self.is_cheat = False

    # Игрок победил
    def win(self):
        self.defeats_in_row = 0

    # Ничья
    def draw(self):
        self.win()

    # Игрок проиграл
    def lose(self):
        self.defeats_in_row += 1


# Перечисление результата игры/раунда
class Result(enum.Enum):
    DRAW = 0
    PLAYER_1 = 1
    PLAYER_2 = 2


# Класс судьи
class Judge:
    # Конструктор класса
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    # Сыграть раунд
    def iteration(self):
        choice1 = self.player1.make_turn()
        choice2 = self.player2.make_turn()
        if choice1 == choice2:
            self.player1.draw()
            self.player2.draw()
            self.add_points(1, 1)
            return Result.DRAW
        elif choice1 > choice2:
            self.player1.win()
            self.player2.lose()
            self.add_points(1, -1)
            return Result.PLAYER_1
        else:
            self.player1.lose()
            self.player2.win()
            self.add_points(-1, 1)
            return Result.PLAYER_2

    def check_winner(self):
        if self.player1.points >= max_points and self.player2.points >= max_points:
            return Result.DRAW
        if self.player1.points >= max_points:
            return Result.PLAYER_1
        if self.player2.points >= max_points:
            return Result.PLAYER_2
        return None

    # Если раунды закончились
    def rounds_over(self):
        if self.player1.points == max_points and self.player2.points >= max_points:
            return Result.DRAW
        if self.player1.points > self.player2.points:
            return Result.PLAYER_1
        return Result.PLAYER_2

    # Добавить очки игрокам
    def add_points(self, p1, p2):
        self.player1.points += p1
        self.player2.points += p2


def bool2emoji(value):
    if value:
        return '[green]✔'
    return ''


# Создаём игроков и судью
player1 = Player()
player2 = Player()
judge = Judge(player1, player2)

rounds_over = False

# Цикл игры
for i in range(max_rounds):
    round_result = judge.iteration()

    table_result = {Result.DRAW: '-',
                    Result.PLAYER_1: '1',
                    Result.PLAYER_2: '2'}[round_result]

    score_table.add_row(str(i + 1),
                        str(player1.last_move), str(player2.last_move),
                        str(player1.points), str(player2.points),
                        bool2emoji(player1.is_cheat), bool2emoji(player2.is_cheat),
                        table_result)

    game_result = judge.check_winner()
    if game_result is not None:
        break
# Раунды закончились
else:
    rounds_over = True
    game_result = judge.rounds_over()

console = Console(record=True)
console.print(score_table)

result_text = Text()
if rounds_over:
    result_text.append('Раунды кончились!\n', style='yellow bold')
result_text.append({Result.DRAW: 'Ничья!',
                    Result.PLAYER_1: '1-ый игрок выиграл!',
                    Result.PLAYER_2: '2-ой игрок выиграл!'}[game_result],
                   style='green bold')

result_panel = Panel(result_text, title='Результат игры', expand=False, border_style='red')

console.print(result_panel)

with open('log.txt', mode='w', encoding='utf-8') as log:
    log.write(console.export_text())
