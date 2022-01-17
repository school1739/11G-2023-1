import simple_draw as sd


# Функция для рисования пузырька
def draw_bubble(center, radius, step, color):
    for i in range(3):
        sd.circle(center, radius - i * step * 2, color)


# Функция для рисования 10 пузырьков в ряд
def draw_bubble_row(y, radius, step, color):
    for i in range(10):
        draw_bubble(sd.get_point(radius * 2 * (i + 1), y), radius, step, color)


# Размер окна
sd.set_screen_size(1500, 800)
sd.start_drawing()

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
draw_bubble(sd.get_point(100, 100), 30, 5, sd.COLOR_YELLOW)


# Написать функцию рисования пузырька, принимающую 2 (или более) параметра: точка рисовании и шаг
# draw_bubble


# Нарисовать 10 пузырьков в ряд
draw_bubble_row(200, 30, 5, sd.COLOR_GREEN)


# Нарисовать три ряда по 10 пузырьков
colors = [sd.COLOR_RED, sd.COLOR_BLUE, sd.COLOR_WHITE]
for i in range(3):
    draw_bubble_row(300 + i * 60, 30, 5, colors[i])


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for i in range(100):
    draw_bubble(sd.random_point(), 30, 5, sd.random_color())


sd.finish_drawing()
sd.pause()
