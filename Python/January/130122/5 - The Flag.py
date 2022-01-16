import math

import simple_draw as sd

# Нарисовать флаг России с древком

# Вокруг флага добавить не менее пяти воздушных шариков (эллипс + треугольник "хвостик" + прямая линия "ниточка")

# На заднем фоне нарисовать не менее трёх феерверков (группы разноцветных кругов разного
# относительно маленького диаметра, не менее 15 штук)


# Функция для рисования флага
def draw_flag(center, width, height):
    start = sd.Point(center.x - width / 2, center.y - height / 2)
    colors = [sd.COLOR_WHITE, sd.COLOR_BLUE, sd.COLOR_RED]
    line_height = height / 6
    # Линии флага
    for i, color in enumerate(colors):
        line_top_y = start.y + height - line_height * i
        sd.rectangle(sd.Point(start.x, line_top_y - line_height), sd.Point(start.x + width, line_top_y), color)
    # Древко
    sd.rectangle(sd.Point(start.x, start.y), sd.Point(start.x + 10, start.y + height), (133, 133, 133))


# Функция для рисования шарика
def draw_balloon(center, width, height):
    start = sd.Point(center.x - width / 2, center.y - width / 2)
    # Шарик
    sd.ellipse(start, sd.Point(start.x + width, start.y + height), sd.random_color())
    # Хвостик
    sd.polygon([sd.Point(center.x - 20, start.y - 20),
                sd.Point(center.x, start.y),
                sd.Point(center.x + 20, start.y - 20)],
               sd.random_color(), 3)
    # Ниточка
    sd.line(sd.Point(center.x, start.y - 20), sd.Point(center.x, start.y - 100))


# Функция для рисования фейерверка
def draw_firework(center, size):
    start = sd.Point(center.x - size / 2, center.y - size / 2)
    for _ in range(15):
        sd.circle(sd.Point(sd.random_number(start.x, start.x + size), sd.random_number(start.y, start.y + size)),
                  sd.random_number(size // 10, size // 5), sd.random_color())


window_size = (1800, 1000)
flag_size = (200, 200)
balloon_size = (70, 100)
balloon_count = 10
balloon_circle_radius = 300
firework_count = 20
firework_size = 100

sd.set_screen_size(*window_size)

window_center = sd.Point(window_size[0] / 2, window_size[1] / 2)
sd.start_drawing()

# Рисуем фейерверки
for i in range(firework_count):
    draw_firework(sd.random_point(), firework_size)

# Рисуем флаг
draw_flag(window_center, *flag_size)

# Рисуем шарики
for i in range(balloon_count):
    t = math.pi * 2 / balloon_count * i
    draw_balloon(sd.Point(balloon_circle_radius * math.cos(t) + window_center.x,
                          balloon_circle_radius * math.sin(t) + window_center.y), *balloon_size)

sd.finish_drawing()
sd.pause()
