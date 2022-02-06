# (цикл for)
import simple_draw as sd
from random import randint

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

brick_size = (100, 50)
background_color = (100,) * 3
space_width = 10
rows = 10
bricks_in_row = 10
brick_color_difference = 30

# Задаём цвет заднего фона
sd.background_color = background_color
# Рисуем стену
for x in range(bricks_in_row):
    for y in range(rows):
        # Начало прямоугольника
        brick_x = (brick_size[0] + space_width) * x
        brick_y = (brick_size[1] + space_width) * y
        # Рассчитываем сдвиг
        if y % 2 == 1:
            brick_x -= (brick_size[0] + space_width) / 2
        # Рассчитываем начало и конец прямоугольника
        brick_start = sd.get_point(brick_x, brick_y)
        brick_end = sd.get_point(brick_x + brick_size[0], brick_y + brick_size[1])
        # Рандомизируем цвет кирпичей
        brick_color = (255 - randint(0, brick_color_difference),
                       127 + randint(-brick_color_difference // 2, brick_color_difference // 2),
                       randint(0, brick_color_difference))
        # Рисуем кирпич
        sd.rectangle(brick_start, brick_end, brick_color)

# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

sd.pause()
