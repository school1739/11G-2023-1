import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# Задача размеров окна и заголовка
screen_w = 640
screen_h = 480
sd.caption = "Wall"
sd.set_screen_size(screen_w, screen_h)

# Кирпич
def brick(x, y, w, h):
    p1 = simple_draw.get_point(x, y)
    p2 = simple_draw.get_point(x + w, y + h)
    # Заливка кирпичец
    simple_draw.rectangle(p1, p2, simple_draw.COLOR_DARK_RED, 0)
    # Границы кирпичей
    simple_draw.rectangle(p1, p2, simple_draw.COLOR_WHITE, 4)
# Размеры кирпича
brick_w = 100
brick_h = 50

brick_start_x = [0, -brick_w // 2]
brick_start_x_idx = 0
brick_y = 0
# Ввод цикла по Y
while brick_y < screen_h:
    brick_x = brick_start_x[brick_start_x_idx]
while brick_x < screen_w:
    brick(brick_x, brick_y, brick_w, brick_h)
brick_x += brick_w

# Перенос ряда на высоту
brick_y += brick_h
# Замена координаты X
brick_start_x_idx = not brick_start_x_idx

sd.pause()

# NOT OK. Ничего не происходит, приходится останавливать программу:
# pygame 2.1.2 (SDL 2.0.18, Python 3.10.0)
# Hello from the pygame community. https://www.pygame.org/contribute.html
# Traceback (most recent call last):
#   File "\Python\February\030222\2 - Another brick in The Wall.py", line 28, in <module>
#     while brick_y < screen_h:
# KeyboardInterrupt
# Process finished with exit code -1073741510 (0xC000013A: interrupted by Ctrl+C)
