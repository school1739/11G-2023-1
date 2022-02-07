import simple_draw as sd
import random

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг

# Нарисовать 10 пузырьков в ряд

# Нарисовать три ряда по 10 пузырьков

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

# Экран
screen = sd.set_screen_size(width=1500, height=800)
screen_init = sd._init()


# Пузырь
def new_bubble(point, step, color):
    radius = 5
    for i in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=color, width=1)


# Ряд из 11 пузырей
for x in range(50, 550, 50):
    point = sd.get_point(x, 50)
    new_bubble(point, step=3, color=sd.COLOR_WHITE)

# 3 ряда из 10 пузырей
for y in range(100, 301, 100):
    for x in range(50, 550, 50):
        point = sd.get_point(x, y)
        new_bubble(point, step=3, color=sd.COLOR_BLACK)

# 100 случайных пузырей с рандомным цветом
for y in range(10, 1000, 50):
    for x in range(10, 1000, 50):
        point = sd.get_point(sd.random_number(10, 1400), sd.random_number(10, 800))
        new_bubble(point, step=3, color=sd.random_color())

sd.pause()
