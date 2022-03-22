import random

glasses = {1: [1] * 5 + [2] * 5,  # Стаканчики с бумажками
           2: [1] * 5 + [2] * 5,
           3: [1] * 5 + [2] * 5,
           4: [1] * 5 + [2] * 5,
           5: [1] * 5 + [2] * 5,
           6: [1] * 5 + [2] * 5,
           7: [1] * 5 + [2] * 5,
           8: [1] * 5 + [2] * 5,
           9: [1] * 5 + [2] * 5,
           10: [1] * 5 + [2] * 5}

# Функция для изменения содержимого стаканов
def game_lost(num_of_glas):
    num_of_glas_list = list(num_of_glas)
    for i in num_of_glas_list:
        if len(glasses[i]) > 1:
            glasses[i].remove(num_of_glas[i])


# def game_win(num_of_glas):
#     num_of_glas_list = list(num_of_glas)
#
#     for i in num_of_glas_list:
#         glasses[i].append(num_of_glas[i])
#         print("    " , num_of_glas[i])

wins = 0  # кол-во побед подряд
while wins <= 5:  # игра до пяти побед включительно
    current_glasses = 10
    num_of_glas = {}
    print(wins)  # выводит кол-во побед подряд

    while True:
        user_stiks = random.randrange(1, 2)  # Сколько палочек выбирает пользователь
        current_glasses -= user_stiks

        if current_glasses == 1:  # Проверка на проигрыш
            wins = 0
            # print("NN lost")
            game_lost(num_of_glas)  # Изменение содержимого стаканов, если сеть проиграла
            break

        # Из задания непонятно, как ходит игрок: случайно или пытается выиграть?
        # Я сделал так, что он ходит случайно
        elif current_glasses <= 0:  # Проверка на выигрыш
            wins += 1
            # print("NN win")
            # game_win(num_of_glas)
            break

        num_from_glas = random.choice(glasses[current_glasses])
        num_of_glas[current_glasses] = num_from_glas
        current_glasses -= num_from_glas

        if current_glasses == 1:  # Проверка на выигрыш
            wins += 1
            # print("NN win")
            # game_win(num_of_glas)
            break

        elif current_glasses == 0:  # Проверка на проигрыш
            wins = 0
            game_lost(num_of_glas)
            # print("NN lost")
            break

for i in range(1, 11):  # Содержимое стаканов
    print(glasses[i])

#  К сожалению, я пока не до конца понял, что это означает и как это сделать: "Поэтому бумажка с неправильным решением удаляется только после 10 подряд неудачных раундов.
# Если несколько "нейронов" одновремено принимают неверные решения, удаляются не все сразу, а нейрон
# с минимальным номером, через 10 неудач -- следующий минимальный и т.д..".
# Но видимо из-за этого моя программа иногда зацикливается и не выдает правилный ответ.
# Буду искать решение
