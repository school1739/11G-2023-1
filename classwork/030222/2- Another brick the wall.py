# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

import simple_draw as sd

sd.resolution = 600, 600

# цикл отрисовывает шесть строчек, в каждой по шесть кирпичей
for y in range(0, 600, 100):
    x = 0
    # цикл рисут шесть кирпичей в строчке
    for x in range(x, 600, 100):
        start_point = sd.get_point(x, y)
        end_point = sd.get_point(x + 100, y + 50)
        sd.rectangle(start_point, end_point, width=1)
# цикл отрисовывает следующие шесть строчек, в каждой по шесть кирпичей
for y in range(50, 600, 100):
    x = -50
    # цикл рисует кирпичи в строке
    for x in range(x, 600, 100):
        start_point = sd.get_point(x, y)
        end_point = sd.get_point(x + 100, y + 50)
        sd.rectangle(start_point, end_point, width=1)

sd.pause()