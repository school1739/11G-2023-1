import simple_draw as sd
import random


def draw_bubble(center, radius, step, color=sd.COLOR_WHITE):
    for i in range(3):
        sd.circle(center, radius - i * step * 2, color)


def draw_bubble_row(y, radius, step):
    for i in range(10):
        draw_bubble(sd.Point(radius * 2 * (i + 1), y), radius, step)


sd.resolution = (1500, 800)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
draw_bubble(sd.Point(100, 100), 30, 5)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# готово


# Нарисовать 10 пузырьков в ряд
draw_bubble_row(200, 30, 5)


# Нарисовать три ряда по 10 пузырьков
for i in range(3):
    draw_bubble_row(300 + i * 60, 30, 5)


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for i in range(100):
    draw_bubble(sd.random_point(), 30, 5, sd.random_color())


sd.pause()
