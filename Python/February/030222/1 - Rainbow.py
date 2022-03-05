# (цикл for)

import simple_draw as sd

# установка размеров окна и заголовка
screen_w = 640
screen_h = 480
sd.caption = "Rainbow"
sd.set_screen_size(screen_w, screen_h)

# кортеж с цветами радуги
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5
# из точки (50, 50) в точку (350, 450)

# параметры линий радуги
x1 = 50
x2 = 350
y1 = 50
y2 = 450
w = 4
dx = 4

# в цикле по цветам рисуем линии, сдвигая координаты X на заданный шаг
for color in rainbow_colors:
    start_point = sd.get_point(x1, y1)
    end_point = sd.get_point(x2, y2)
    sd.line(start_point, end_point, color, w)
    x1 += dx
    x2 += dx

# Подсказка: цикл нужно делать сразу по кортежу с цветами радуги.

# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем
# экрана, поэкспериментировать с параметрами, что бы было красиво

rainbow_arc_pos = sd.get_point(screen_w / 2, -32)   # центр дуг радуги
w = 16                      # ширина дуг радуги
r = screen_w / 2 * 1.5      # начальный радиус дуг радуги
# в цикле по цветам рисуем окружности, уменьшая радиус на ширину дуги
for color in rainbow_colors:
    sd.circle(rainbow_arc_pos, r, color, w)
    r -= w

sd.pause()

# OK