import simple_draw as sd

# Нарисовать флаг России с древком

# Вокруг флага добавить не менее пяти воздушных шариков (эллипс + треугольник "хвостик" + прямая линия "ниточка")

# На заднем фоне нарисовать не менее трёх феерверков (группы разноцветных кругов разного
# относительно маленького диаметра, не менее 15 штук)

# Создание экрана
sd.set_screen_size(width=1500, height=800)
sd._init()


# рисуем флаг
def get_flag():
    # рисуем прямоугольник
    sd.rectangle(sd.get_point(500, 400), sd.get_point(1000, 600), color=sd.COLOR_WHITE, width=1)
    # закрашиваем флаг
    sd.line(sd.get_point(500, 400), sd.get_point(1000, 400), color=sd.COLOR_RED, width=100)
    sd.line(sd.get_point(500, 500), sd.get_point(1000, 500), color=sd.COLOR_BLUE, width=100)
    sd.line(sd.get_point(500, 600), sd.get_point(1000, 600), color=sd.COLOR_WHITE, width=100)
    # рисуем древко
    sd.line(sd.get_point(490, 100), sd.get_point(490, 649), color=sd.COLOR_WHITE, width=20)


# рисуем шарики
def get_balloons():
    # рисуем шарики в разных местах
    sd.ellipse(sd.get_point(100, 500), sd.get_point(150, 570), color=sd.COLOR_ORANGE, width=0)
    sd.polygon(point_list=[sd.get_point(120, 500), sd.get_point(130, 500), sd.get_point(125, 493)],
               color=sd.COLOR_WHITE, width=0)
    sd.line(sd.get_point(125, 400), sd.get_point(125, 500), color=sd.COLOR_WHITE, width=2)

    sd.ellipse(sd.get_point(200, 400), sd.get_point(250, 470), color=sd.COLOR_GREEN, width=0)
    sd.polygon(point_list=[sd.get_point(220, 400), sd.get_point(230, 400), sd.get_point(225, 393)],
               color=sd.COLOR_WHITE, width=0)
    sd.line(sd.get_point(225, 300), sd.get_point(225, 400), color=sd.COLOR_WHITE, width=2)

    sd.ellipse(sd.get_point(300, 300), sd.get_point(350, 370), color=sd.COLOR_DARK_YELLOW, width=0)
    sd.polygon(point_list=[sd.get_point(320, 300), sd.get_point(330, 300), sd.get_point(325, 293)],
               color=sd.COLOR_WHITE, width=0)
    sd.line(sd.get_point(325, 200), sd.get_point(325, 300), color=sd.COLOR_WHITE, width=2)

    sd.ellipse(sd.get_point(1100, 300), sd.get_point(1150, 370), color=sd.COLOR_RED, width=0)
    sd.polygon(point_list=[sd.get_point(1120, 300), sd.get_point(1130, 300), sd.get_point(1125, 293)],
               color=sd.COLOR_WHITE, width=0)
    sd.line(sd.get_point(1125, 200), sd.get_point(1125, 300), color=sd.COLOR_WHITE, width=2)

    sd.ellipse(sd.get_point(1200, 400), sd.get_point(1250, 470), color=sd.COLOR_DARK_PURPLE, width=0)
    sd.polygon(point_list=[sd.get_point(1220, 400), sd.get_point(1230, 400), sd.get_point(1225, 393)],
               color=sd.COLOR_WHITE, width=0)
    sd.line(sd.get_point(1225, 300), sd.get_point(1225, 400), color=sd.COLOR_WHITE, width=2)

    sd.ellipse(sd.get_point(1300, 500), sd.get_point(1350, 570), color=sd.COLOR_CYAN, width=0)
    sd.polygon(point_list=[sd.get_point(1320, 500), sd.get_point(1330, 500), sd.get_point(1325, 493)],
               color=sd.COLOR_WHITE, width=0)
    sd.line(sd.get_point(1325, 400), sd.get_point(1325, 500), color=sd.COLOR_WHITE, width=2)


# рисуем фейерверки
def get_fireworks():
    for i in range(700):
        # рисуем круги в каждой из областей
        sd.circle(center_position=(sd.get_point(sd.random_number(50, 1400), sd.random_number(670, 770))), radius=2,
                  color=sd.random_color(), width=1)
        sd.circle(center_position=(sd.get_point(sd.random_number(175, 470), sd.random_number(470, 670))), radius=2,
                  color=sd.random_color(), width=1)
        sd.circle(center_position=(sd.get_point(sd.random_number(1010, 1290), sd.random_number(470, 670))), radius=2,
                  color=sd.random_color(), width=1)


# вызываем функции
get_balloons()
get_flag()
get_fireworks()

sd.pause()
