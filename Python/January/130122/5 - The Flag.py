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
    sd.line(sd.get_point(490, 100), sd.get_point(490, 649), color=sd.COLOR_BLACK, width=20)


# рисуем шарик
def get_balloon(x, y, color):
    # рисуем шарики в разных местах
    center_of_ellipse = (x, y)
    x1_of_ellipse, y1_of_ellipse = x - 25, y - 35
    x2_of_ellipse, y2_of_ellipse = x + 25, y + 35
    x1_of_triangle, y1_of_triangle = (x1_of_ellipse + x2_of_ellipse) // 2, y1_of_ellipse - 7
    x2_of_triangle, y2_of_triangle = x1_of_triangle - 5, y1_of_ellipse
    x3_of_triangle, y3_of_triangle = x1_of_triangle + 5, y1_of_ellipse
    x1_of_line, y1_of_line = x1_of_triangle, y1_of_triangle
    x2_of_line, y2_of_line = x1_of_triangle, y1_of_triangle - 100
    sd.ellipse(sd.get_point(x1_of_ellipse, y1_of_ellipse), sd.get_point(x2_of_ellipse, y2_of_ellipse), color, width=0)
    sd.polygon(point_list=[sd.get_point(x1_of_triangle, y1_of_triangle), sd.get_point(x2_of_triangle, y2_of_triangle),
                           sd.get_point(x3_of_triangle, y3_of_triangle)],
               color=sd.COLOR_WHITE, width=0)
    sd.line(sd.get_point(x1_of_line, y1_of_line), sd.get_point(x2_of_line, y2_of_line), color=sd.COLOR_WHITE, width=2)


# рисуем фейерверки
def get_fireworks():
    for i in range(150):
        # рисуем круги в каждой из областей
        sd.circle(center_position=(sd.get_point(sd.random_number(50, 1400), sd.random_number(670, 770))), radius=2,
                  color=sd.random_color(), width=1)
        sd.circle(center_position=(sd.get_point(sd.random_number(175, 470), sd.random_number(470, 670))), radius=2,
                  color=sd.random_color(), width=1)
        sd.circle(center_position=(sd.get_point(sd.random_number(1010, 1290), sd.random_number(470, 670))), radius=2,
                  color=sd.random_color(), width=1)


# вызываем функции
print()
print(
    "Чтобы программа нарисовала шарик, вам нужно ввести следующие параметры:\n"
    "1) Положение шарика по горизонтали. (если вы хотите точное расположение, напишите цифрами от 0 до 1500,\n"
    "если же хотите рандомное расположение - введите 0")
x = int(input("Ввод: "))
print(
    "2) Положение шарика по вертикали. (если вы хотите точное расположение, напишите цифрами от 0 до 800,\n"
    "если же хотите рандомное расположение - введите 0")
y = int(input("Ввод: "))

if x == 0 and y != 0:
    random_x1 = int(input("введите границы рандомного расположения по горизонтали\nПервая:"))
    random_x2 = int(input("Вторая:"))
    get_balloon(sd.random_number(random_x1, random_x2), y, sd.random_color())

elif x != 0 and y == 0:
    random_y1 = int(input("введите границы рандомного расположения по вертикали\nПервая: "))
    random_y2 = int(input("Вторая:"))
    get_balloon(x, sd.random_number(random_y1, random_y2), sd.random_color())

elif x == 0 and y == 0:
    random_x1 = int(input("введите границы рандомного расположения по горизонтали\nПервая:"))
    random_x2 = int(input("Вторая:"))
    random_y1 = int(input("введите границы рандомного расположения по вертикали\nПервая: "))
    random_y2 = int(input("Вторая:"))
    get_balloon(sd.random_number(random_x1, random_x2), sd.random_number(random_y1, random_y2), sd.random_color())

elif x != 0 and y != 0:
    get_balloon(x, y, sd.random_color())

get_flag()
get_fireworks()

sd.pause()

# Чота ничо не работает. Вводи, не вводи -- пустой синий экран.