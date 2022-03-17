# Нейросеть из стаканов

# Правила игры
"""
На столе 11 палочек, два игрока ходят по очереди. За каждый ход можно взять 1 или 2 палочки.
Проиграл тот, кто взял последнюю палочку.

Пользователь играет против компьютера. Первый ход определяется случайным образом, далее первым ходит игрок,
проигравший в предыдущем раунде.

Игра IRL:
На столе стоят 10 стаканов (можно 11, но стакан для хода на последнюю палочку никогда не используется,
т.к. в этом нет смысла). В каждом стакане ("нейроне") содержится по 5 бумажек с цифрами 1 и 2.
Каждый свой ход "нейросеть" выбирает из стакана с номером, соответствующим числу палочек на столе,
случайную бумажку с цифрой, затем берёт со стола количество палочек == числу на бумажке, затем передаёт
ход игроку.

В случае проигрыша "нейросети", из всех стаканов, которые принимали участие в раунде, убирается бумажка,
которую "нейронка" выбрала для хода. В случае выигрыша - добавляется новая бумажка с тем же значением, что
у использованной.

Если в "нейроне" остаётся последняя бумажка любого значения, она не удаляется при следующей
неудачной итерации -- на случай, если "нейросеть" попала в цикл неудачных решений на других "нейронах".
Поэтому бумажка с неправильным решением удаляется только после 10 подряд неудачных раундов.
Если несколько "нейронов" одновремено принимают неверные решения, удаляются не все сразу, а нейрон
с минимальным номером, через 10 неудач -- следующий минимальный и т.д..

Выполнение программы продолжается до 5 подряд побед "нейросети". После победы "нейросеть" показывает
содержимое стаканов -- сколько и каких бумажек в них содержится, какова вероятность принятия того или
иного решения в каждом "нейроне".

Использование сторонних библиотек (pybrain, pygame, numpy и т.п.) запрещено. Можно использовать только random.
"""
import enum
import random


# Класс нейрона (стаканчика)
class Neuron:
    # Положить бумажки в стаканчик
    def __init__(self):
        self.values = [1] * 5 + [2] * 5
        self.last_value = 0
        self.fails_in_row = 0

    # Взять случайную бумажку
    def choose(self):
        self.last_value = random.choice(self.values)
        return self.last_value

    # Убрать последнюю выбранную бумажку при проигрыше, если их больше одной
    def fail(self):
        assert self.last_value != 0
        if len(self.values) > 1:
            self.values.remove(self.last_value)
        else:
            self.fails_in_row += 1

    # Добавить новую бумажку с тем же значением, что и на выбранной
    def success(self):
        assert self.last_value != 0
        self.values.append(self.last_value)
        self.fails_in_row = 0

    # Ресетнуть нейрон, если всё плохо
    def reset(self):
        self.__init__()


# Класс "искусственного интеллекта"
class AI:
    # Подготовить стаканчики
    def __init__(self):
        self.neurons = [Neuron() for _ in range(10)]
        self.used_neurons = []

    # Выбрать число палочек
    def choose_number(self, sticks_left):
        neuron = self.neurons[sticks_left - 2]
        self.used_neurons.append(neuron)
        return neuron.choose()

    # Нейросеть проиграла
    def fail(self):
        for neuron in self.used_neurons:
            neuron.fail()
            if neuron.fails_in_row >= 10:
                neuron.reset()
        self.used_neurons.clear()

    # Нейросеть выиграла
    def win(self):
        for neuron in self.used_neurons:
            neuron.success()
        self.used_neurons.clear()


class Color(str, enum.Enum):
    RESET = "\u001B[0m",
    BLACK = "\u001B[30m",
    RED = "\u001B[31m",
    GREEN = "\u001B[32m",
    YELLOW = "\u001B[33m",
    BLUE = "\u001B[34m",
    PURPLE = "\u001B[35m",
    CYAN = "\u001B[36m",
    WHITE = "\u001B[37m"


def colored(value, color):
    return color + str(value) + Color.RESET


def player_turn():
    choice = int(input('Сколько возьмёте палочек: 1 или 2?: '))
    if choice not in (1, 2):
        print('ಠ╭╮ಠ')
        exit(-666)
    return choice


def bot_turn(ai, sticks_left):
    choice = ai.choose_number(sticks_left)
    print(f'Я возьму столько палочек: {colored(choice, Color.BLUE)}')
    return choice


def random_turn():
    choice = random.randint(1, 2)
    print(f'Рандомно выбрал число: {colored(choice, Color.YELLOW)}')
    return choice


# Создаём объект "искусственного интеллекта"
bot = AI()

# Количество рандомных раундов
random_play_rounds = int(input('Сколько раундов сыграть рандомно? (Можно 0): '))

# Цикл раундов
while True:
    # Оставшиеся палочки
    sticks_left = 11
    # 0 - ход игрока, 1 - нейросети
    turn = random.randint(0, 1)
    # Если надо, сыграть рандомно
    random_play = False
    if random_play_rounds > 0:
        random_play = True
        random_play_rounds -= 1
    # Цикл игры
    while sticks_left > 1:
        print(f'Палочек осталось: {colored(sticks_left, Color.RED)}')
        if turn == 0:
            if random_play:
                sticks_left -= random_turn()
            else:
                sticks_left -= player_turn()
        else:
            sticks_left -= bot_turn(bot, sticks_left)
        turn = 1 - turn
    print(colored('Осталась последняя палочка!', Color.CYAN))
    # Проверяем, кто проиграл
    if turn == 0:
        print('Ха-ха-ха! Я умнее тебя! У меня памяти 16 мегабайт!')
        bot.win()
    else:
        print('Ты победил :(')
        bot.fail()
    # Выводим состояние нейросети
    print('\nСтаканчики:')
    print('1: Не используется')
    for i, neuron in enumerate(bot.neurons):
        chance_one = neuron.values.count(1) / len(neuron.values) * 100
        print(f'{i + 2}: '
              f'Шансы - {chance_one:.2f}%, {100 - chance_one:.2f}%;\t'
              f'Бумажки - {sorted(neuron.values)}')
    print()
