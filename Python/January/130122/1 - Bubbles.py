import simple_draw as sd

sd.set_screen_size(width=1500, height=700)
sd._init()


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

def draw_bub(center, step, color):
    for i in range(0, 15, 5):
        sd.circle(center, step + i, color)


draw_bub(sd.Point(500, 100), 5, (255, 255, 0))


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг

def bubble(center, step):
    draw_bub(center, step, (255, 255, 0))


# Нарисовать 10 пузырьков в ряд

for i in range(10, 40, 3):
    bubble_center = sd.get_point(i * 10, 550)
    bubble(bubble_center, 5)

# Нарисовать три ряда по 10 пузырьков
for j in range(1, 4, 1):
    for i in range(10, 40, 3):
        bubble_center = sd.Point(i * 10, j * 100)
        bubble(bubble_center, 5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for i in range(100):
    draw_bub(sd.random_point(), 30, sd.random_color())

sd.pause()
