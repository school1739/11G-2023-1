import random


class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.loses = 0

    def make_move(self, sticks):
        return 1

    def on_win(self):
        self.wins += 1

    def on_lose(self):
        self.loses += 1


class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def make_move(self, sticks):
        while True:
            print("{}, please make your move (1 or 2) ...".format(self.name))
            move = int(input())

            if move == 1 or move == 2:
                return move

            print("You made incorrect move. Are you dummy?")


class RandomComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def make_move(self, sticks):
        move = random.randint(1, 2)
        return move


class GlassNNComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

        self.glasses = [[1, 2] for glass in range(11)]
        self.move_history = [None] * 11

    def make_move(self, sticks):
        index = sticks - 1
        # take the glass according to the number of sticks on the table
        glass = self.glasses[index]

        if len(glass) == 1:
            move = glass[0]
        else:
            sheet_index = random.randint(0, len(glass) - 1)
            move = glass.pop(sheet_index)
            self.move_history[index] = move

        return move

    def on_win(self):
        super().on_win()

        # print("I, {}, win again!".format(self.name))
        # print(self.move_history)

        for index in range(11):
            move = self.move_history[index]
            self.move_history[index] = None

            if move is not None:
                self.glasses[index].append(move)
                self.glasses[index].append(move)

        # print(self.glasses)

    def on_lose(self):
        super().on_lose()
        # print("I, {}, lose :(".format(self.name))
        # print(self.glasses)


class Game:
    def __init__(self, player1, player2):
        self.sticks = 11
        self.active_player = player1
        self.next_player = player2

    def play(self):
        while self.sticks > 0:
            # print("Now, there are {} sticks on the table.".format(self.sticks))

            move = self.active_player.make_move(self.sticks)

            # print("{} took {}".format(self.active_player, move))

            self.sticks -= move
            self.active_player, self.next_player = self.next_player, self.active_player

        # return winner, loser
        return self.active_player, self.next_player


def main():
    exit_flag = False
    number_of_round = 1

    # player1, player2 = HumanPlayer("Vlad"), RandomComputerPlayer("Dummy Computer")
    player1, player2 = GlassNNComputerPlayer("GlassNet"), RandomComputerPlayer("Dummy Computer")

    game = Game(player1, player2)

    while not exit_flag:

        print("===== Round {} =====".format(number_of_round))

        winner, loser = game.play()

        winner.on_win()
        loser.on_lose()

        # print("Game is over. Player {} win".format(winner.name))

        print("{}: wins={}, loses={}".format(player1.name, player1.wins, player1.loses))
        print("{}: wins={}, loses={}".format(player2.name, player2.wins, player2.loses))

        number_of_round += 1

        if number_of_round == 100000:
            exit_flag = True

        game = Game(loser, winner)

    return 0


if __name__ == "__main__":
    main()

# MEGAOK