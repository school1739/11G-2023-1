import simple_draw as sd

# Зададим размер окна для рисования
sd.set_screen_size(1600, 900)
sd.start_drawing()


# Написать функцию рисования пузырька, принимающую 2 (или более) параметра: точка рисовании и шаг
def draw_bubble(center, radius, step, color):
    for i in range(3):
        sd.circle(center, radius - i * step * 2, color)


# Нарисовать пузырек - три вложенных окружности с шагом 5 пикселей
draw_bubble(sd.get_point(120, 120), 35, 7, sd.COLOR_GREEN)


# Нарисовать 10 пузырьков в ряд
def draw_bubble_row(x, radius, step, color):
    for i in range(10):
        draw_bubble(sd.get_point(radius * 2 * (i + 1), x), radius, step, color)


# Нарисовать три ряда по 10 пузырьков
draw_bubble_row(200, 30, 5, sd.COLOR_CYAN)
colors = [sd.COLOR_RED, sd.COLOR_BLUE, sd.COLOR_WHITE]
for i in range(3):
    draw_bubble_row(300 + i * 60, 30, 5, colors[i])

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for i in range(100):
    draw_bubble(sd.random_point(), 30, 5, sd.random_color())

sd.finish_drawing()
sd.pause()

# OK