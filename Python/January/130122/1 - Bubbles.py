import simple_draw as sd

# Нарисовать пузырек - три вложенных окружности с шагом 5 пикселей
import simple_draw as sd
def puzyir(start, shag):
    center_position = sd.get_point(50, 60)
    COLOR_YELLOW = (255, 255, 0)
    sd.circle(center_position, radius=25, color=COLOR_YELLOW, width=1)
    sd.circle(center_position, radius=30, color=COLOR_YELLOW, width=1)
    sd.circle(center_position, radius=35, color=COLOR_YELLOW, width=1)
# Написать функцию рисования пузырька, принимающую 2 (или более) параметра: точка рисовании и шаг
center_position=sd.get_point(50,60 )
COLOR_GREEN = (0, 255, 0)
sd.circle(center_position, radius=25, color=COLOR_GREEN, width=1)
sd.circle(center_position, radius=30, color=COLOR_GREEN, width=1)
sd.circle(center_position, radius=35, color=COLOR_GREEN, width=1)
sd.pause()
# Нарисовать 10 пузырьков в ряд
for x in range(50, 550, 50):
    point = sd.get_point(x, 50)
    create_bubble(point, step=5, color = sd.COLOR_GREEN)
# Нарисовать три ряда по 10 пузырьков
for y in range (100, 301, 100):
    for x in range(50, 550, 50):
        point = sd.get_point(x, y)
        create_bubble(point, step=5, color = sd.COLOR_GREEN)
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for y in range (10, 1000, 50):
    for x in range(10, 1000, 50):
        point = sd.get_point(sd.random_number(10,1400), sd.random_number(10,800))
        create_bubble(point, step=5, color=sd.random_color())