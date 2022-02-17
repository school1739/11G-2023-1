import random

import simple_draw as sd

# Нарисовать флаг России с древком

# Вокруг флага добавить не менее пяти воздушных шариков
# (эллипс + треугольник "хвостик" + прямая линия "ниточка")

# На заднем фоне нарисовать не менее трёх феерверков (группы разноцветных
# кругов разного относительно маленького диаметра, не менее 15 штук)

# Hint: для рисования однотипных объектов проще всего использовать функцию
# и цикл

# установка размеров окна и заголовка
screen_w = 1280
screen_h = 720
sd.caption = "The Flag"
sd.set_screen_size(screen_w, screen_h)


# функция отрисовки флага
# pole_pos - точка основания древка
# width - длина полотна
# height - ширина полотна
# pole_height - высота древка от основания до нижней части полотна
def flag(pole_pos, width, height, pole_height):
    # высота древка от основания до верхушки
    total_pole_height = pole_height + height

    # положение конечных точек отрезка древка
    pole_x = pole_pos.x
    pole_y = pole_pos.y
    pole_top = sd.get_point(pole_x, pole_y + total_pole_height)

    # высота и цвета полос флага
    height /= 3
    colors = [sd.COLOR_WHITE, sd.COLOR_BLUE, sd.COLOR_RED]

    # координаты вершин полос флага (первой полосы)
    strip_x1 = pole_top.x
    strip_x2 = strip_x1 + width
    strip_y1 = pole_top.y
    strip_y2 = strip_y1 - height

    # в цикле по цветам флага рисуем полосу и смещаем координаты Y
    # на высоту полосы
    for i in range(len(colors)):
        sd.rectangle(sd.get_point(strip_x1, strip_y2),
                     sd.get_point(strip_x2, strip_y1), colors[i])
        strip_y1 -= height
        strip_y2 -= height

    # рисуем древко
    sd.line(pole_pos, pole_top, sd.COLOR_DARK_ORANGE, 4)


# функция отрисовки воздушного шарика
def balloon(pos, width=40, height=80, color=sd.COLOR_RED):
    # координаты точки, где шарик "завязан"
    start_x = pos.x
    start_y = pos.y

    # координаты вершин прямоугольника, в который вписан эллипс шарика
    e_top_left = sd.get_point(start_x - width / 2, start_y)
    e_bottom_right = sd.get_point(start_x + width / 2, start_y + height)
    # рисуем эллипс
    sd.ellipse(e_top_left, e_bottom_right, color, 0)

    # размер "хвостика" и координата Y его нижней части
    tail_size = 12
    t_bottom_y = start_y - tail_size / 2

    # параметры и координаты нитки шарика
    tail_line_length = 30
    l_start = sd.get_point(start_x - 1, t_bottom_y)
    l_end = sd.get_point(start_x - 1, t_bottom_y - tail_line_length)
    # рисуем нитку
    sd.line(l_start, l_end, sd.COLOR_BLACK, 2)

    # координаты вершин "хвостика"
    t_top = pos
    t_bottom_left = sd.get_point(start_x - tail_size / 2, t_bottom_y)
    t_bottom_right = sd.get_point(start_x + tail_size / 2, t_bottom_y)
    # рисуем "хвостик"
    sd.polygon([t_top, t_bottom_left, t_bottom_right], color, 0)


# функция отрисовки фейерверка
def firework(pos):
    # опредение числа кругов в фейерверке
    min_amount = 15
    max_amount = 30
    k = sd.random_number(min_amount, max_amount)

    # в цикле отрисовываем круги случайных цвета и радиуса
    for i in range(k):
        color = sd.random_color()
        rad = sd.random_number(15, 60)
        sd.circle(pos, rad, color, 1)


# рисуем фейерверки в случайных местах по всему экрану
firework_amount = sd.random_number(3, 25)
for k in range(firework_amount):
    x = sd.random_number(0, screen_w)
    y = sd.random_number(0, screen_h)
    firework(sd.get_point(x, y))

# параметры флага
flag_w = 480        # длина полотна
flag_h = 240        # ширина полотна
flag_pole_h = 240   # высота древка от основания до нижней части полотна
flag_x = (screen_w - flag_w) / 2
flag_y = (screen_h - flag_h - flag_pole_h) / 2
# рисуем флаг
flag(sd.get_point(flag_x, flag_y), flag_w, flag_h, flag_pole_h)

# координаты сторон флага для определения пространства, где нужно рисовать
# воздушные шарики
flag_left_x = flag_x
flag_right_x = flag_x + flag_w
flag_top_y = flag_y + flag_h + flag_pole_h
flag_bottom_y = flag_y

# в цикле рисуем шарики
balloons_amount = sd.random_number(5, 20)
for k in range(balloons_amount):
    # случайно выбираем координату X шарика слева и справа от флага
    dx = 0      # расстояние от краёв экрана и флага по X
    x1 = sd.random_number(dx, flag_left_x - dx)
    x2 = sd.random_number(flag_right_x + dx, screen_w - dx)
    x = random.choice([x1, x2])

    # случайно выбираем координату Y шарика сверху и снизу от флага
    dy = 0      # расстояние от краёв экрана и флага по Y
    y1 = sd.random_number(dy, flag_bottom_y - dy)
    y2 = sd.random_number(flag_top_y + dy, screen_h - dy)
    y = random.choice([y1, y2])

    # определяем случайно параметры шарика (размеры и цвет)
    w = sd.random_number(30, 90)
    h = w + sd.random_number(0, 60)
    color = sd.random_color()

    # рисуем шарик
    balloon(sd.get_point(x, y), w, h, color)

sd.pause()
