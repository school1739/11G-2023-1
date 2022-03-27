"""Написать программу, где две функции -- "Игрок 1" и "Игрок 2"
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
Вероятность чита сохраняется."""


import enum
import random
import os


# Класс нейрона "стаканчик"
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

    # Добавить новую бумажку с параметрами соответсвующими выбранной
    def success(self):
        assert self.last_value != 0
        self.values.append(self.last_value)
        self.fails_in_row = 0


    def reset(self):
        self.__init__()


# Класс для искуственного интелекта
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


# Ход чувачка
def player_turn():
    choice = int(input('Сколько возьмёте палочек: 1 или 2?: '))
    if choice not in (1, 2):
        print('Why dude? That wont do dude')
        choice = player_turn()
    return choice


# Ход машины (бота)
def bot_turn(ai, sticks_left):
    choice = ai.choose_number(sticks_left)
    print(f'Я возьму столько палочек:')
    return choice


# Рандом
def random_turn():
    choice = random.randint(1, 2)
    print(f'Рандомно выбрал число:')
    return choice


# Создаём объект "искусственного интеллекта"
bot = AI()

# Количество рандомных раундов
random_play_rounds = int(input('Сколько раундов сыграть рандомно? : '))

# Цикл раундов
while True:
    # Оставшиеся палочки
    sticks_left = 11
    # если 0 - ход чувачка, если 1, то нейронка
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
    # Подводим итоги
    if turn == 0:
        print('Востание машин не за горами чувак')
        bot.win()
    else:
        print('А ты хорош чувак')
        bot.fail()
    # Состояние нейросети
    print('\nСтаканчики:')
    print('1: Не используется')
    for i, neuron in enumerate(bot.neurons):
        chance_one = neuron.values.count(1) / len(neuron.values) * 100
        print(f'{i + 2}: '
              f'Шансы - {chance_one:.2f}%, {100 - chance_one:.2f}%;\t'
              f'Бумажки - {sorted(neuron.values)}')
    print()
