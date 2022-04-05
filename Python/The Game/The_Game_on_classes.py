from random import randint


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
    exit_flag = False

    player1 = Player("Peter")
    player2 = Player("John")

    referee = Referee(player1, player2)

    number_of_rounds = 0

    # Process of The Game
    while not exit_flag:
        number_of_rounds += 1

        player1.make_move()
        player2.make_move()

        print("Move: {}={}, {}={}".format(player1.name, player1.last_move, player2.name, player2.last_move))

        # Calling the Function
        winner = referee.make_judge()

        print("Round {} stats: {}={}, {}={}".format(number_of_rounds, player1.name, player1.score,
                                                    player2.name, player2.score))

        # if the the rounds are over
        if number_of_rounds > 99 or player1.score == 50 or player2.score == 50:
            print("The rounds are over.")
            if player1.score == player2.score:
                print("Draw!")
            else:
                winner = player1 if player1.score > player2.score else player2
                print("Player {} finally won!".format(winner.name))

            exit_flag = True


if __name__ == "__main__":
    main()
