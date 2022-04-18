
import random
# Задача диапазона
range_numbers = [-1000, 1000]

# Вероятность срабатывания чита
chance_cheat_1 = 0
chance_cheat_2 = 0

def cheat(chance_cheat, amount_fails):
    # Активированность чита
    cheat = False
    chance = random.randint(0, 100)
    # Вероятность срабатывания чита после 3 проигрышей подряд
    if chance <= chance_cheat and amount_fails >= 3:
        cheat = True
    return cheat

# Счёт
score_1 = 0
score_2 = 0
# Количество проигрышей подряд
fails1, fails1_in_a_row = 0, 0
fails2, fails2_in_a_row = 0, 0
#Класс для игрока
class Gamer:
    def __init__(self, name):
        print("Конструктор создал игрока")
        self.name = name
        self.probability_cheat = 0

    def number(self, fails_in_a_row):
        self.num = random.randint(*range_numbers)
        if fails_in_a_row == 3:
            self.probability_cheat += 5
        if cheat(self.probability_cheat, fails_in_a_row) is True:
            self.num += 1000
        return self.num


gamer_1 = Gamer("1")
gamer_2 = Gamer("2")

#Класс для судьи
class Referee:
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

        elif num_2 < num_1:
            score_1 += 1
            score_2 -= 1
            fails1_in_a_row = 0
            fails2_in_a_row += 1
            print("Выиграл первый")
        elif num_2 > num_1:
            score_1 -= 1
            score_2 += 1
            fails1_in_a_row += 1
            fails2_in_a_row = 0
            print("Выиграл второй")

Referee = Referee()

# Раунды
for i in range(10000):
    Referee.Game()
    print(f"Счёт 1 игрока:", score_1)
    print(f"Счёт 2 игрока:", score_2)
    if score_1 == 50:
        print(f'Первый игрок победил в игре')
        break
    elif score_2 == 50:
        print(f'Второй  игрок победил в игре')
        break
    print()
if score_1 < 50 and score_2 < 50:
    print(f'Ничья')

# OK