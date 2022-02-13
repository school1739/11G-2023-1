# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


background_color = (225, 165, 0)
step = 0
for y in range(0, 1000, 50):
    y1 = y + 50
    step -= 50
    for x in range(step, 1000, 100):
        simple_draw.background_color = background_color
        x1 = x + 500
        point = simple_draw.get_point(x, y)
        point1 = simple_draw.get_point(x1, y1)
        simple_draw.rectangle(point, point1, color=simple_draw.COLOR_GREY, width = 3)
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
