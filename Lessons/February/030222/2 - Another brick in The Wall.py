# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
sd.resolution=(1000,500)
START_X = 0
START_Y = 0
BRICK_WIDTH = 100
BRICK_HEIGHT = 50
ROW_BRICK_NUMBER = 10
ROW_NUMBER = 10
BRICK_OFFSET = int(0.5 * BRICK_WIDTH)

for current_row in range(ROW_NUMBER):
    # вот здесь определяется, сколько именно составит смещение.
    # для четного ряда будет 50, для нечетного - 0
    OFFSET = 50 if current_row % 2 == 0 else 0

    for current_brick in range(ROW_BRICK_NUMBER):
        # добавим смещение к началу отсчета для оси X
        left_bottom_x = START_X + OFFSET + BRICK_WIDTH * current_brick
        left_bottom_y = START_Y + BRICK_HEIGHT * current_row
        left_bottom = sd.get_point(left_bottom_x, left_bottom_y)
        right_top_x = left_bottom_x + BRICK_WIDTH
        right_top_y = left_bottom_y + BRICK_HEIGHT
        right_top = sd.get_point(right_top_x, right_top_y)
        sd.rectangle(left_bottom, right_top, sd.COLOR_WHITE, width=3)
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
