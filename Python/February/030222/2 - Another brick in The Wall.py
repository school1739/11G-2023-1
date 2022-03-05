# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# установка размеров окна и заголовка
screen_w = 640
screen_h = 480
simple_draw.caption = "Wall"
simple_draw.set_screen_size(screen_w, screen_h)


# функция отрисовки кирпича
def brick(x, y, w, h):
    # координаты вершин
    p1 = simple_draw.get_point(x, y)
    p2 = simple_draw.get_point(x + w, y + h)
    # заливка
    simple_draw.rectangle(p1, p2, simple_draw.COLOR_DARK_RED, 0)
    # границы (соединения кирпичей)
    simple_draw.rectangle(p1, p2, simple_draw.COLOR_WHITE, 4)


# размеры кирпича
brick_w = 100
brick_h = 50

# варианты начального положения ряда кирпичей
# нечётный ряд рисуется с координаты X = 0
# чётный - X = -половина ширины кирпича
brick_start_x = [0, -brick_w // 2]
brick_start_x_idx = 0   # индекс текущего варианта

brick_y = 0     # Y текущего рядя кирпичей
# в цикле по Y до высоты окна
while brick_y < screen_h:
    # задаём начальный X кирпича в соответствии с вариантом
    brick_x = brick_start_x[brick_start_x_idx]

    # в цикле по X до ширины окна рисуем кирпич и смещаемся на ширину кирпича
    while brick_x < screen_w:
        brick(brick_x, brick_y, brick_w, brick_h)
        brick_x += brick_w

    # смещаем ряд на высоту
    brick_y += brick_h
    # меняем вариант начальной координаты X
    brick_start_x_idx = not brick_start_x_idx


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

# OK. Отдельный респект за правильный "цемент"!