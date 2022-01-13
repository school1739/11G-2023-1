import simple_draw as sd

def bubble(point, step):
    radius = 50
    for i in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2)
point = sd.get_point(100, 100)
bubble(point=point, step=10)

sd.resolution = (1200, 600)
# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(300, 300)
radius = 50
for i in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius, width=2)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг

# Нарисовать 10 пузырьков в ряд

# Нарисовать три ряда по 10 пузырьков

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами


sd.pause()
