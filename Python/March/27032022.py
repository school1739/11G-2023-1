import random
# import os

glasses = {1: [1] * 5 + [2] * 5,  # Стаканчики с бумажками
           2: [1] * 5 + [2] * 5,
           3: [1] * 5 + [2] * 5,
           4: [1] * 5 + [2] * 5,
           5: [1] * 5 + [2] * 5,
           6: [1] * 5 + [2] * 5,
           7: [1] * 5 + [2] * 5,
           8: [1] * 5 + [2] * 5,
           9: [1] * 5 + [2] * 5,
           10: [1] * 5 + [2] * 5,
           11: [1] * 5 + [2] * 5}


# Функция для изменения содержимого стаканов
def game_lost(num_of_glass):
    num_of_glass_list = list(num_of_glass)
    for i in num_of_glass_list:
        if len(glasses[i]) > 1:  # Убираем листочек
            glasses[i].remove(num_of_glass[i][0])
        elif num_of_glass[i][1] == 10:  # Убираем последний листочек, если кол-во проигрышей на нём равно 10
            glasses[i].remove(num_of_glass[i][0])

wins = 0  # кол-во побед подряд
while wins <= 5:  # игра до пяти побед включительно
    current_glasses = 10
    num_of_glass = {}
    loss = 0  # Кол-во проигрышей
    # print(wins)  # выводит кол-во побед подряд

    while True:
        user_sticks = random.randrange(1, 2)  # Сколько палочек выбирает пользователь
        current_glasses -= user_sticks  # Игрок берёт....
        if current_glasses == 1:  # Проверка на проигрыш
            wins = 0
            game_lost(num_of_glass)  # Изменение содержимого стаканов, если сеть проиграла
            break

        #ходит случайно
        elif current_glasses <= 0:  # Проверка на выигрыш
            wins += 1
            break

        num_from_glass = random.choice(glasses[current_glasses])
        num_of_glass[current_glasses] = num_from_glass, loss
        current_glasses -= num_from_glass  # Нейросеть берёт....

        if current_glasses == 1:  # Проверка на выигрыш
            wins += 1
            break

        elif current_glasses == 0:  # Проверка на проигрыш
            wins = 0
            game_lost(num_of_glass)
            break

# os.system('shutdown /s /t 0')
for i in range(1, 12):  # Содержимое стаканов
    print(f"В {i} содержится {glasses[i]}.")
    probability_1 = glasses[i].count(1) / len(glasses[i])
    print(f"Вероятность достать 1 из стакана: {probability_1}.")
    print(f"Вероятность достать 2 из стакана: {1 - probability_1}.")
    print()
