import simple_draw as sd

sd.set_screen_size(width=1400, height=700)
sd._init()
# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

bubble_center = sd.get_point(700, 500)

sd.circle(bubble_center, 60)
sd.circle(bubble_center, 55)
sd.circle(bubble_center, 50)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг

# def bubble(position,radius,color):
#     sd.circle(position,radius,color)

# Нарисовать 10 пузырьков в ряд

for i in range(100, 400, 30):
    bubble_center = sd.get_point(i, 550)
    sd.circle(bubble_center, 15)

# Нарисовать три ряда по 10 пузырьков
for j in range(100, 400, 100):
    for i in range(100, 400, 30):
        bubble_center = sd.get_point(i, j)
        sd.circle(bubble_center, 15)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for i in range(100):
    sd.circle(sd.random_point(), 30, sd.random_color())
# Переделать
# Пузырь это 3 круга, один в другом
sd.pause()
