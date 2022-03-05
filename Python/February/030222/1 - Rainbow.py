# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_PURPLE, sd.COLOR_BLUE, sd.COLOR_CYAN, sd.COLOR_GREEN,
                  sd.COLOR_YELLOW, sd.COLOR_ORANGE, sd.COLOR_RED)

screen = sd.set_screen_size(width=1500, height=800)
screen_init = sd._init()


# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
def rainbow(x1, y1):
    indent = 5
    for i in range(7):
        sd.line(sd.get_point(x1, y1 + i * indent), sd.get_point(x1 + 300, y1 + i * indent), width=4,
                color=rainbow_colors[i])


# Подсказка: цикл нужно делать сразу по кортежу с цветами радуги.


# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

def rainbow_circle(radius, step, width):
    point = sd.get_point(750, -200)
    for color in rainbow_colors:
        radius += step
        sd.circle(center_position=point, radius=radius, color=color, width=width)


# Calling teh Functions with given parameters
rainbow_circle(500, 15, 15)
rainbow(50, 600)

sd.pause()

# OK