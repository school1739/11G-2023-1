# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
a1 = 0
a2 = 50
b1 = 100
b2 = 155
sd.background_color = (128, 128, 128)
for i in range(10):
    sd.rectangle(left_bottom=sd.get_point(a1, 0), right_top=sd.get_point(b1, 50), color=sd.COLOR_ORANGE, width=0)
    a1 = a1 + 105
    b1 = b1 + 105
sd.rectangle(left_bottom=sd.get_point(0, 55), right_top=sd.get_point(45, 105), color=sd.COLOR_ORANGE, width=0)
for i in range(10):
    sd.rectangle(left_bottom=sd.get_point(a2, 55), right_top=sd.get_point(b2, 105), color=sd.COLOR_ORANGE, width=0)
    a2 = a2 + 110
    b2 = b2 + 110
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
