import random

# Некоторый диапазон
range_numbers = [-1000, 1000]


def cheat(probabilty_cheat, amount_fails):
    # cheat on
    cheat = False
    probabilty = random.randint(0, 100)
    # Вероятность срабатывания чита, после 3 проигрышей подряд
    if probabilty <= probabilty_cheat and amount_fails >= 3:
        cheat = True
        print("Чит активирован")
    return cheat


# Счет
score_1 = 0
score_2 = 0
# Проигрыши и кол-во проигрышей подряд
fails1_in_a_row = 0
fails2_in_a_row = 0


class Gamer:
    def __init__(self, name):
        print("Конструктор создал игрока")
        self.name = name
        self.probability_cheat = 0

    # Функция для числа, которое получает игрок
    def number(self, fails_in_a_row):
        self.num = random.randint(*range_numbers)
        if fails_in_a_row == 3:
            self.probability_cheat += 5
            if self.probability_cheat == 100:  # Если вероятность включения чита 100, то она обнулится, иначе будет не интересно
                self.probability_cheat = 0
        if cheat(self.probability_cheat, fails_in_a_row) is True:
            self.num += 1000
        return self.num


gamer_1 = Gamer("1")
gamer_2 = Gamer("2")


class Referee:
    def __init__(self):
        print("Судья будет наблюдать за вашей игрой")
    # сама игра
    def Game(self):
        global fails1_in_a_row
        global fails2_in_a_row
        global score_1, score_2
        num_1 = gamer_1.number(fails1_in_a_row)
        num_2 = gamer_2.number(fails2_in_a_row)
        if num_2 == num_1:
            score_1 += 1
            score_2 += 1
            fails1_in_a_row, fails2_in_a_row = 0, 0
            print("Ничья")
        elif num_2 > num_1:
            score_1 -= 1
            score_2 += 1
            fails1_in_a_row += 1
            fails2_in_a_row = 0
            print("Второй выиграл")
        elif num_2 < num_1:
            score_1 += 1
            score_2 -= 1
            fails1_in_a_row = 0
            fails2_in_a_row += 1
            print("Первый выиграл")


Referee = Referee()

# Раунды
for i in range(10000):
    Referee.Game()  # Раунд одной игры
    print(f"Счёт 1 игрока:", score_1)
    print(f"Счёт 2 игрока:", score_2)
    if score_1 == 50:
        print(f'Первый победил в игре')
        break
    elif score_2 == 50:
        print(f'Второй победил в игре')
        break
    print()
if score_1 < 50 and score_2 < 50:
    print(f'Никто не дошел до победого счета')

# OK