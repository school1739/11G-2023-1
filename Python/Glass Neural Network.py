# Нейросеть из стаканов

#Правила игры
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

Использование сторонних библиотек (pybrain, pygame, numpy и т.п.) запрещено. Можно использовать только random."""



import random

class neurone:
    def __init__(self):
        self.values = [1] * 5 + [2] * 5
        self.last_value = 0
        self.fails_in_row = 0

    # Взять случайную палочку
    def choose(self):
        self.last_value = random.choice(self.values)
        return self.last_value

    # Убрать последнюю выбранную палоку при проигрыше, если их больше одной
    def fail(self):
        assert self.last_value != 0
        if len(self.values) > 1:
            self.values.remove(self.last_value)
        else:
            self.fails_in_row += 1

    # Добавить новую палочку
    def success(self):
        assert self.last_value != 0
        self.values.append(self.last_value)
        self.fails_in_row = 0

    def reset(self):
        self.__init__()

# Класс для искуственного интелекта
class artificial_intelligence:
    def __init__(self):
        self.neurons = [neurone() for _ in range(10)]
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


# Ход игрока
def player_turn():
    choice = int(input('Сколько возьмёте палочек: 1 или 2?: '))
    if choice not in (1, 2):
        print("Вы можете взять только одну или две палочки")
        choice = player_turn()
    return choice


# Ход искуственного интелекта
def bot_turn(ai, sticks_left):
    choice = ai.choose_number(sticks_left)
    print(f'Число палочек, которое я возьму:')
    return choice


# Рандом
def random_turn():
    choice = random.randint(1, 2)
    return choice

bot = artificial_intelligence()

# Количество рандомных раундов
random_play_rounds = int(input('Сколько раундов сыграть рандомно? : '))

# Цикл раундов
while True:
    # Оставшиеся палочки
    sticks_left = 11

    turn = random.randint(0, 1)
    # Если нужно, сыграть рандомно
    random_play = False
    if random_play_rounds > 0:
        random_play = True
        random_play_rounds -= 1
    # Цикл игры
    while sticks_left > 1:
        print(f'Палочек осталось: ')
        if turn == 0:
            if random_play:
                sticks_left -= random_turn()
            else:
                sticks_left -= player_turn()
        else:
            sticks_left -= bot_turn(bot, sticks_left)
        turn = 1 - turn
    print('Остается одна палочка')
    # Результаты
    if turn == 0:
        print('Выиграл искуственный интелект')
        bot.win()
    else:
        print('Выиграл пользователь')
        bot.fail()
    # Состояние нейросети
    print('\nСтаканчики:')
    print('1: Не используется')
    for i, neuron in enumerate(bot.neurons):
        chance_one = neuron.values.count(1) / len(neuron.values) * 100
        print(f'{i + 2}: '
              f'Шансы - {chance_one:.2f}%, {100 - chance_one:.2f}%;\t'
              f'Палочки - {sorted(neuron.values)}')
    print()

#OK