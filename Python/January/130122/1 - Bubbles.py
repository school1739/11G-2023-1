# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
import random

import simple_draw as sd
def bubble(point, step):
    radius = 50
    for i in range(1):
        radius += step
        sd.circle(center_position=point, color=(sd.COLOR_RED), radius=radius, width=2)
point = sd.get_point(100, 100)
bubble(point=point, step=10)

sd.resolution = (1200, 600)
# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(1100, -100)
radius = 50
for i in range(3):
    radius += 5
    sd.circle(center_position=point, color=(sd.COLOR_PURPLE), radius=radius, width=2)

# Нарисовать 10 пузырьков в ряд
for x in range(100, 1100, 101):
    point = sd.get_point(x, 500)
    bubble(point=point, step=5)

# Нарисовать три ряда по 10 пузырьков
for y in range(100, 301, 100):
    for x in range(100, 1001, 100):
        point = sd.get_point(x, y)
        sd.circle(center_position=point, color=(sd.COLOR_GREEN), width=2)
        bubble(point=point, step=5)
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
point = sd.random_point()
radius = 50
for i in range(100):
    color = random.randint(sd.COLOR_PURPLE, sd.COLOR_WHITE)
    sd.circle(center_position=point, radius=radius, width=2)
    bubble(point=point, step=step)
sd.pause()
