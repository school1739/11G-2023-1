# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
start_x = 50
start_y = 50
end_x = 350
end_y = 450
step_x = 5
step_y = 5

for i in range(7):
    start_x += i * step_x
    start_y += i * step_y
    end_x += i * step_x
    end_y += i * step_y
    sd.line(start_point=sd.get_point(start_x, start_y), end_point=sd.get_point(end_x, end_y), color=rainbow_colors[i],
            width=4)


# Подсказка: цикл нужно делать сразу по кортежу с цветами радуги.


# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
start_x = 250
start_y = -200
sd.resolution = (500, 500)
for current_color in rainbow_colors:
    center_position = sd.get_point(start_x, start_y)
    sd.circle(center_position=center_position, radius=600, color=current_color, width=15)
    start_y -= 15

sd.pause()
