# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450):
x = 50  # Переменная, чтобы смещать линии радуг по горизонтали (начало)
y = 350  # Переменная, чтобы смещать линии радуг по горизонтали (конец)
for i in rainbow_colors:
    sd.line(start_point=sd.get_point(x, 50), end_point=sd.get_point(y, 450), color=i, width=4)
    x = x + 5
    y = y + 5

# Подсказка: цикл нужно делать сразу по кортежу с цветами радуги.


# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
z = 150  # Переменная, чтобы менять радиус радуг
for i in rainbow_colors:
    sd.circle(center_position=sd.get_point(500, -50), radius=z, color=i, width=10)
    z = z + 10

sd.pause()
