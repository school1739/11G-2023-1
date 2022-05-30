import random

from rich.console import Console
from rich.table import Table

console = Console()
# Некоторый диапазон
range_numbers = [-1000, 1000]


def cheat(probabilty_cheat, amount_fails):
    # Активированность чита
    cheat = False
    probabilty = random.randint(0, 100)
    # Вероятность срабатывания чита после 3 проигрышей подряд
    if probabilty <= probabilty_cheat and amount_fails >= 3:
        cheat = True
        # print("---Чит активирован---")
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

    def number(self, fails_in_a_row):  # Функция для числа, которое получает игрок
        self.num = random.randint(*range_numbers)
        if fails_in_a_row == 3:
            self.probability_cheat += 5
            if self.probability_cheat == 100:  # Если вероятность чита равна 100%, то она обнуляется, т.к. иначе было бы не честно
                self.probability_cheat = 0
        is_cheat = "✖"
        if cheat(self.probability_cheat, fails_in_a_row) == True:  # Чит
            self.num += 1000
            is_cheat = "✔"
        return self.num, is_cheat


gamer_1 = Gamer("1")
gamer_2 = Gamer("2")

# Название таблицы и её столбцов
table = Table(title="Game progress")
table.add_column("Раунд", justify="center", style="blue")
table.add_column("Число 1 игрока", justify="center")
table.add_column("Число 2 игрока", justify="center")
table.add_column("Счёт 1 игрока", justify="center")
table.add_column("Счёт 2 игрока", justify="center")
table.add_column("Чит 1?", justify="center", style="yellow")
table.add_column("Чит 2?", justify="center", style="yellow")
table.add_column("Победитель", justify="center", style="green", no_wrap=True)


class Referee:
    def __init__(self):
        print("Судья появился и готов следить за игрой")

    def Game(self, i):  # Игра
        global fails1_in_a_row, winner
        global fails2_in_a_row
        global score_1, score_2
        num_1 = gamer_1.number(fails1_in_a_row)
        num_2 = gamer_2.number(fails2_in_a_row)
        if num_2[0] == num_1[0]:
            score_1 += 1
            score_2 += 1
            fails1_in_a_row, fails2_in_a_row = 0, 0
            winner = "Ничья"
        elif num_2[0] > num_1[0]:
            score_1 -= 1
            score_2 += 1
            fails1_in_a_row += 1
            fails2_in_a_row = 0
            winner = "Второй"
        elif num_2[0] < num_1[0]:
            score_1 += 1
            score_2 -= 1
            fails1_in_a_row = 0
            fails2_in_a_row += 1
            winner = "Первый"

        # Добавляем значения в столбцы
        table.add_row(str(i + 1), str(num_1[0]), str(num_2[0]), str(score_1), str(score_2), str(num_1[1]),
                      str(num_2[1]),
                      str(winner))


Referee = Referee()

# Раунды
for i in range(10000):
    Referee.Game(i)  # Раунд одной игры
    if score_1 == 50:
        print(f'Первый победил в игре')
        break
    elif score_2 == 50:
        print(f'Второй победил в игре')
        break
console.print(table)

if score_1 < 50 and score_2 < 50:
    print(f'Никто не дошел до победого счета')

# OK