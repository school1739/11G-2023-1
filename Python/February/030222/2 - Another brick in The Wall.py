# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

brick_size = (100, 50)
backg_width = 10
rows = 10
bricks_in_row = 10

sd.rectangle(sd.get_point(0, 0), sd.get_point(*sd.resolution), background_color)
for x in range(bricks_in_row):
    for y in range(rows):
        brick_x = (brick_size[0] + space_width) * x
        brick_y = (brick_size[1] + space_width) * y
        if y % 2 == 1:
            brick_x -= (brick_size[0] + space_width) / 2
        start = sd.get_point(brick_x, brick_y)
        end = sd.get_point(brick_x + brick_size[0], brick_y + brick_size[1])
        sd.rectangle(start, end, sd.COLOR_ORANGE)
round_color = (100,) * 3
space
# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

simple_draw.pause()

# NOT OK.

#   File "C:\Users\bormo\PycharmProjects\python.21-22-1\Python\February\030222\2 - Another brick in The Wall.py", line 12, in <module>
#      sd.rectangle(sd.get_point(0, 0), sd.get_point(*sd.resolution), background_color)
#  NameError: name 'sd' is not defined. Did you mean: 'id'?