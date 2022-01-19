import simple_draw as sd

# Нарисовать флаг России с древком

# Вокруг флага добавить не менее пяти воздушных шариков (эллипс + треугольник "хвостик" + прямая линия "ниточка")

# На заднем фоне нарисовать не менее трёх феерверков (группы разноцветных кругов разного
# относительно маленького диаметра, не менее 15 штук)

# Hint: для рисования однотипных объектов проще всего использовать функцию и цикл

import random

import simple_draw as sd

sd.background_color = (0, 0, 0)

# На заднем фоне нарисовать не менее трёх феерверков (группы разноцветных кругов разного
# относительно маленького диаметра, не менее 15 штук)
# 1-й феерверк
for m in range(25):
    point = sd.get_point(200, 550)
    colour = sd.random_color()
    radius = random.randint(3, 60)
    sd.circle(center_position=point, radius=radius, color=colour, width=3)
# 2-й феерверк
for m in range(25):
    point = sd.get_point(500, 300)
    colour = sd.random_color()
    radius = random.randint(3, 60)
    sd.circle(center_position=point, radius=radius, color=colour, width=3)
# 3-й феерверк
for m in range(25):
    point = sd.get_point(300, 100)
    colour = sd.random_color()
    radius = random.randint(3, 60)
    sd.circle(center_position=point, radius=radius, color=colour, width=3)
# Нарисовать флаг России с древком
# 1-я полоса
left_bottom = sd.get_point(125, 425)
right_top = sd.get_point(475, 500)
COLOR_WHITE = (255, 255, 255)
sd.rectangle(left_bottom, right_top, color=COLOR_WHITE, width=0)
# 2-я полооса
left_bottom = sd.get_point(125, 350)
right_top = sd.get_point(475, 425)
COLOR_BLUE = (0, 0, 250)
sd.rectangle(left_bottom, right_top, color=COLOR_BLUE, width=0)
# 3-я полоса
left_bottom = sd.get_point(125, 275)
right_top = sd.get_point(475, 350)
COLOR_RED = (255, 0, 0)
sd.rectangle(left_bottom, right_top, color=COLOR_RED, width=0)
# древко
left_bottom = sd.get_point(115, 100)
right_top = sd.get_point(125, 500)
COLOR_DARK_YELLOW = (127, 127, 0)
sd.rectangle(left_bottom, right_top, color=COLOR_DARK_YELLOW, width=0)
# Вокруг флага добавить не менее пяти воздушных шариков (эллипс + треугольник "хвостик" + прямая линия "ниточка")
# 1-й шарик
left_bottom = sd.get_point(50, 500)
right_top = sd.get_point(80, 550)
colour = sd.random_color()
sd.ellipse(left_bottom, right_top, color=colour, width=0)
# 2-й шарик
left_bottom = sd.get_point(500, 450)
right_top = sd.get_point(530, 500)
colour = sd.random_color()
sd.ellipse(left_bottom, right_top, color=colour, width=0)
# 3-й шарик
left_bottom = sd.get_point(250, 220)
right_top = sd.get_point(280, 270)
colour = sd.random_color()
sd.ellipse(left_bottom, right_top, color=colour, width=0)
# 4-й шарик
left_bottom = sd.get_point(60, 100)
right_top = sd.get_point(90, 150)
colour = sd.random_color()
sd.ellipse(left_bottom, right_top, color=colour, width=0)
# 5-й шарик
left_bottom = sd.get_point(420, 130)
right_top = sd.get_point(450, 180)
colour = sd.random_color()
sd.ellipse(left_bottom, right_top, color=colour, width=0)
# 1-й хвостик
colour = sd.random_color()
sd.polygon(point_list=[sd.get_point(65, 500),
                       sd.get_point(62, 490),
                       sd.get_point(68, 490)],
           color=colour, width=0)
# 2-й хвостик
colour = sd.random_color()
sd.polygon(point_list=[sd.get_point(515, 450),
                       sd.get_point(512, 440),
                       sd.get_point(518, 440)],
           color=colour, width=0)
# 3-й хвостик
colour = sd.random_color()
sd.polygon(point_list=[sd.get_point(265, 220),
                       sd.get_point(262, 210),
                       sd.get_point(268, 210)],
           color=colour, width=0)
# 4-й хвостик
colour = sd.random_color()
sd.polygon(point_list=[sd.get_point(75, 100),
                       sd.get_point(72, 90),
                       sd.get_point(78, 90)],
           color=colour, width=0)
# 5-й хвостик
colour = sd.random_color()
sd.polygon(point_list=[sd.get_point(435, 130),
                       sd.get_point(432, 120),
                       sd.get_point(438, 120)],
           color=colour, width=0)
# 1-я верёвочка
start_point = sd.get_point(65, 490)
end_point = sd.get_point(65, 450)
colour = sd.random_color()
sd.line(start_point=start_point, end_point=end_point, color=colour, width=1)
# 2-я верёвочка
start_point = sd.get_point(515, 440)
end_point = sd.get_point(515, 400)
colour = sd.random_color()
sd.line(start_point=start_point, end_point=end_point, color=colour, width=1)
# 3-я верёвочка
start_point = sd.get_point(265, 210)
end_point = sd.get_point(265, 170)
colour = sd.random_color()
sd.line(start_point=start_point, end_point=end_point, color=colour, width=1)
# 4-я верёвочка
start_point = sd.get_point(75, 90)
end_point = sd.get_point(75, 40)
colour = sd.random_color()
sd.line(start_point=start_point, end_point=end_point, color=colour, width=1)
# 5-я верёвочка
start_point = sd.get_point(435, 120)
end_point = sd.get_point(435, 80)
colour = sd.random_color()
sd.line(start_point=start_point, end_point=end_point, color=colour, width=1)

sd.pause()