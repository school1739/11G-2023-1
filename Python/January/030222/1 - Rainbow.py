# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
point_from = sd.get_point(50, 50)
point_to = sd.get_point(350, 450)
width = 10
step = 5
for i, color in enumerate(rainbow_colors):
    shift = point_from.y - step * i
    start = sd.get_point(point_from.x + shift, point_from.y - shift)
    end = sd.get_point(point_to.x + shift, point_to.y - shift)
    sd.line(start, end, color, width)
# TODO нарисовать Nyan Cat и звёздочки
# Подсказка: цикл нужно делать сразу по кортежу с цветами радуги.


# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
center = sd.get_point(400, 0)
radius = 200
step = 10
width = 10
for i, color in enumerate(rainbow_colors):
    sd.circle(center, radius - step * i, color, width)

sd.pause()
