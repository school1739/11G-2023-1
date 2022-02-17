import simple_draw as sd

# установка размеров окна и заголовка
screen_w = 1280
screen_h = 720
sd.caption = "Bubbles"
sd.set_screen_size(screen_w, screen_h)

# параметры пузыря
bubble_step = 5
bubble_centre = sd.get_point(screen_w / 2, screen_h / 2)
bubble_radius = 40
bubble_color = sd.COLOR_WHITE
bubble_width = 1


# Написать функцию рисования пузырька, принимающую 2 (или более) параметра:
# точка рисовании и шаг
def bubble(pos, step=5, rad=bubble_radius, color=sd.COLOR_WHITE):
    _width = bubble_width
    for i in range(3):
        sd.circle(center_position=pos, radius=rad, color=color, width=_width)
        rad -= step


# функция рисования нескольких пузырей в ряд
def bubble_row(start_x, y, amount, step=5, rad=bubble_radius,
               color=sd.COLOR_WHITE):
    x = start_x
    dx = rad * 2    # смещение по X пузырей в ряду
    for k in range(amount):
        bubble(sd.get_point(x, y), step, rad, color)
        x += dx


# Нарисовать пузырек - три вложенных окружности с шагом 5 пикселей
bubble(sd.get_point(screen_w / 2, screen_h / 2))

# Нарисовать 10 пузырьков в ряд
bubble_row(30, 30, 10, 3, 30, sd.COLOR_CYAN)

# Нарисовать три ряда по 10 пузырьков

# положение и радиус пузырей
bubble_x = 128
bubble_y = 128
bubble_rad = 28
bubble_dy = bubble_rad * 2  # смещение по Y ряда пузырей

# рисование трёх рядов
for j in range(3):
    bubble_row(bubble_x, bubble_y, 10, 3, bubble_rad)
    bubble_y += bubble_dy

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for i in range(100):
    bubble(pos=sd.random_point(), color=sd.random_color())

sd.pause()
