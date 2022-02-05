# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
sd.background_color = (128, 128, 128)
sd._to_screen(1600, 900)
sd.set_screen_size(width=1600, height=900)
x1 = -155
y1 = -55
x2 = -5
y2 = -5
for i in range(20):
    y1 = y1 + 55
    y2 = y2 + 55
    for i in range(20):
        x1 = x1 + 155
        x2 = x2 + 155
        sd.rectangle(left_bottom=sd.get_point(x1, y1), right_top=sd.get_point(x2, y2), color=sd.COLOR_ORANGE, width=0)

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
