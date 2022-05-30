import random

from rich.console import Console
from rich.table import Table
from rich.progress import track
from rich.progress import Progress


"""Перепишите The Game 2.0 с использованием библиотеки rich.
Использование классов обязательно. Количество раундов: >=1000.

В процессе игры отображается прогресс-бар, вывод игрового процесса на консоль не происходит.
По окончанию игры выводится таблица с результатами каждого раунда (см. ниже), ниже таблицы -- имя победителя.
То же самое записывается в файл game_log.txt с использованием export_text().

Пример таблицы:

                             The Game 3.0 Progress
┏━━━━━━━┳━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━┓
┃ Round ┃ P1 Move ┃ P2 Move ┃ P1 Cheat ┃ P2 Cheat ┃ P1 Sco… ┃ P2 Score ┃ Winn… ┃
┡━━━━━━━╇━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━┩
│  666  │   123   │   321   │    ✅    │    ❌    │   34    │    12    │ Dick  │
└───────┴─────────┴─────────┴──────────┴──────────┴─────────┴──────────┴───────┘

"""


class PlayerInfo:
    def __init__(self, name="", points=0, move=0, in_cheat=False):
        self.name = name
        self.points = points
        self.move = move
        self.in_cheat = in_cheat

    def copy_pre_round_info(self, info: 'PlayerInfo'):
        self.name = info.name
        self.in_cheat = info.in_cheat

    def copy_round_info(self, info: 'PlayerInfo'):
        self.points = info.points
        self.move = info.move


class Player(PlayerInfo):
    default_range = (-1000, 1000)
    cheat_range = (1000, 1000)

    def __init__(self, name):
        super().__init__(name, 0, 0, False)
        self.defeats = 0
        self.cheat_factor = 0
        self.range = (Player.default_range[0], Player.default_range[1])

    def try_cheat(self):
        if not self.in_cheat:
            roll_chance = random.randint(1, 100)
            if roll_chance <= self.cheat_factor:
                self.range = (Player.cheat_range[0], Player.cheat_range[1])
                self.in_cheat = True

    def roll(self):
        self.move = random.randint(self.range[0], self.range[1])

    def win(self):
        self.points += 1
        if self.in_cheat:
            self.in_cheat = False
            self.range = (Player.default_range[0], Player.default_range[1])

    def lose(self):
        self.points -= 1
        self.defeats += 1
        if self.defeats == 3:
            self.cheat_factor += 5


class Round:
    def __init__(self, no: int, p1: PlayerInfo, p2: PlayerInfo):
        self.no = no

        self.p1 = PlayerInfo()
        self.p2 = PlayerInfo()
        self.p1.copy_pre_round_info(p1)
        self.p2.copy_pre_round_info(p2)
        self.winner = ""

    def set_results(self, p1: PlayerInfo, p2: PlayerInfo, winner):
        self.p1.copy_round_info(p1)
        self.p2.copy_round_info(p2)
        self.winner = winner

    def add_info_to_table(self, table: Table):
        table.add_row(
            str(self.no), str(self.p1.move), str(self.p2.move),
            "✔" if self.p1.in_cheat else "✘",
            "✔" if self.p2.in_cheat else "✘",
            str(self.p1.points), str(self.p2.points),
            self.winner
        )


class Game:
    def __init__(self, p1: Player, p2: Player, max_points=100,
                 max_rounds=1000):
        self.rounds = []
        self.max_points = max_points
        self.max_rounds = max_rounds
        self.p1 = p1
        self.p2 = p2
        self.winner = "Tie"

    def set_winner(self, player: Player):
        self.winner = player.name

    def set_tie(self):
        self.winner = "Tie"

    def judge(self):
        if self.p1.move > self.p2.move:
            self.p1.win()
            self.p2.lose()
            return self.p1.name

        if self.p1.move < self.p2.move:
            self.p1.lose()
            self.p2.win()
            return self.p2.name

        self.p1.win()
        self.p2.win()
        return "Tie"

    def is_game_over(self):
        pts1_reached_max = self.p1.points >= self.max_points
        pts2_reached_max = self.p2.points >= self.max_points

        return pts1_reached_max or pts2_reached_max

    def define_winner(self):
        pts1 = self.p1.points
        pts2 = self.p2.points

        if pts1 > pts2:
            self.set_winner(self.p1)
        elif pts1 < pts2:
            self.set_winner(self.p2)
        else:
            self.set_tie()

    def play_round(self, round_no: int):
        self.p1.try_cheat()
        self.p2.try_cheat()

        round_info = Round(round_no, self.p1, self.p2)

        self.p1.roll()
        self.p2.roll()
        winner = self.judge()

        round_info.set_results(self.p1, self.p2, winner)
        self.rounds.append(round_info)

    def play(self):
        with Progress() as progress:
            task = progress.add_task("[green]Playing...",
                                     total=self.max_rounds)
            cur_round = 1
            while not progress.finished:
                self.play_round(cur_round)
                if self.is_game_over():
                    progress.advance(task, advance=self.max_rounds)
                else:
                    progress.advance(task, advance=1)
                    cur_round += 1
                progress.refresh()

        self.define_winner()

    def show_results(self):
        table = Table(show_header=True, header_style="bold magenta")

        table.add_column("Round", width=10)
        table.add_column("P1 Move", width=10, justify="right")
        table.add_column("P2 Move", width=10, justify="right")
        table.add_column("P1 Cheat", width=10, justify="center")
        table.add_column("P2 Cheat", width=10, justify="center")
        table.add_column("P1 Score", width=10, justify="center")
        table.add_column("P2 Score", width=10, justify="center")
        table.add_column("Winner", width=16, justify="center")

        for cur_round in self.rounds:
            cur_round.add_info_to_table(table)

        return table


def play():
    console = Console(record=True)

    target_pts = int(input("Enter target amount of points: "))
    max_rounds = int(input("Enter max amount of rounds: "))
    p1_name = input("Enter Player 1 name: ")
    p2_name = input("Enter Player 2 name: ")

    player1 = Player("Player 1" if p1_name == "" else p1_name)
    player2 = Player("Player 2" if p2_name == "" else p2_name)
    game = Game(player1, player2, target_pts, max_rounds)

    game.play()
    console.print(game.show_results())
    console.print("Winner: " + game.winner)
    console.save_text("game_log.txt")

    console.input("Enter any key to exit...")


if __name__ == '__main__':
    play()
