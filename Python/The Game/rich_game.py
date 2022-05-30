from random import randint
import sys
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.progress import Progress, track
import time

score_table = Table(title="Game Data", title_style='bold italic green1',
                    header_style='blue bold',
                    border_style='aquamarine3')
score_table.add_column("Round", style='green')
score_table.add_column("P1_move", style='yellow')
score_table.add_column("P2_move", style='yellow')
score_table.add_column("Score of P1", style='dark_slate_gray1')
score_table.add_column("Score of P2", style='dark_slate_gray1')
score_table.add_column("Cheat_P1", justify='center')
score_table.add_column("Cheat_P2", justify='center')
score_table.add_column("Winner", justify='center', style='bold gold1')


class Player:
    name = None
    last_move = None
    cheat_probability = 0
    score = 0
    defeats_in_a_raw = 0

    def __init__(self, name):
        self.name = name

    def make_move(self):
        self.last_move = randint(-1000, +1000) if randint(0, 99) > self.cheat_probability else 1000

    def update_winner(self, reset_cheat=True):
        self.score += 1
        self.defeats_in_a_raw = 0
        self.cheat_probability = 0 if reset_cheat else self.cheat_probability

    def update_loser(self):
        self.score -= 1
        self.defeats_in_a_raw += 1
        self.cheat_probability += 5 if self.defeats_in_a_raw % 3 == 0 else 0


class Referee:
    player1 = None
    player2 = None

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def make_judge(self):
        if self.player1.last_move == self.player2.last_move:
            self.player1.update_winner(False)
            self.player2.update_winner(False)
            return None
        elif self.player1.last_move < self.player2.last_move:
            winner, loser = self.player2, self.player1
        else:
            winner, loser = self.player1, self.player2

        winner.update_winner()
        loser.update_loser()

        return winner


def main():
    console = Console()
    exit_flag = False

    player1 = Player("Peter")
    player2 = Player("John")

    referee = Referee(player1, player2)

    number_of_rounds = 0

    result_text = Text()

    # Process of The Game
    for i in track(range(500), description="Processing..."):
        number_of_rounds = i + 1

        player1.make_move()
        player2.make_move()

        # Calling the Function
        winner = referee.make_judge()

        score_table.add_row(str(number_of_rounds), str(player1.last_move), str(player2.last_move), str(player1.score),
                            str(player2.score),
                            str(player1.cheat_probability), str(player2.cheat_probability), str(winner.name))

        # if the the rounds are over
        if number_of_rounds > 500 or player1.score == 100 or player2.score == 100:
            if player1.score == player2.score:
                result_text = "никто"
            else:
                if player1.score > player2.score:
                    result_text = "первый игрок"
                else:
                    result_text.append("второй игрок")

    result_panel = Panel.fit("!!! Победил {} со счетом ({}:{}) !!!".format(result_text, player1.score, player2.score),
                             title="Итог игры",
                             subtitle="спасибо за игру :)",
                             border_style='red')
    console.print(score_table)
    console.print(result_panel)

    file_path = 'total_of_game.txt'
    sys.stdout = open(file_path, "w")
    console.print(score_table)
    console.print(result_panel)

if __name__ == "__main__":
    main()

# OK