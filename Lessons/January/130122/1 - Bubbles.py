import simple_draw as sd
import random
sd.resolution = (1280, 800)
random

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(400, 400)
rad = 50
for _ in range(3):
    rad += 5
    sd.circle(center_position=point, radius=rad)
# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def bubble(point, step):
    rad = 50
    for _ in range(3):
        rad += step
        sd.circle(center_position = point, radius = rad)

point = sd.get_point(400, 300)
bubble(point = point, step = 10)

# Нарисовать 10 пузырьков в ряд
for i in range(100, 1001, 100):
    point = sd.get_point(i, 100)
    bubble(point = point, step = 5)

# Нарисовать три ряда по 10 пузырьков
for a in range(100, 301, 100):
   for i in range(100, 1001, 100):
       point = sd.get_point(i, a)
       bubble(point = point, step = 5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for i in range(100):
    sd.circle(sd.random_point(), 30, sd.random_color())

    sd.pause()

# NOT OK. Вместо 100 пузырьков рисуется только один, а выход из окна
# только с ошибкой.