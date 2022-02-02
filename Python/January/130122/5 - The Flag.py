import simple_draw as sd

width = 1500
height = 700
sd.set_screen_size(width, height)
sd._init()
# центр экрана
center = sd.get_point(width / 2, height / 2)

tricolor = [
    (255, 255, 255),
    (0, 0, 255),
    (255, 0, 0)
]


# Нарисовать флаг России с древком

def flag(center):
    # Флаг
    sd.line(sd.get_point(center.x - 200, center.y - 300), sd.get_point(center.x - 200, center.y + 200), (255, 127, 0),
            5)

    # K - высота флага. Нужна, чтобы последовательно нарисовать три прямоугольника
    k = 0
    for i in tricolor:
        sd.rectangle(sd.get_point(center.x - 200, center.y + 150 - k), sd.get_point(center.x + 200, center.y + 200 - k),
                     i)
        k += 50


# Вокруг флага добавить не менее пяти воздушных шариков (эллипс + треугольник "хвостик" + прямая линия "ниточка")

# Шарики
def balloon(x_y):
    sd.ellipse(sd.get_point(x_y.x - 20, x_y.y - 30), sd.get_point(x_y.x + 20, x_y.y + 30), sd.random_color())
    sd.polygon(point_list=[sd.get_point(x_y.x, x_y.y - 30), sd.get_point(x_y.x - 5, x_y.y - 40),
                           sd.get_point(x_y.x + 5, x_y.y - 40)])
    sd.line(sd.get_point(x_y.x, x_y.y - 40), sd.get_point(x_y.x, x_y.y - 100))


# На заднем фоне нарисовать не менее трёх феерверков (группы разноцветных кругов разного
# относительно маленького диаметра, не менее 15 штук)

# Фейрверки
def fireworks():
    for i in range(5):
        sd.circle(sd.get_point(sd.random_number(100, 300) + i * 270, sd.random_number(500, 700)), 4, sd.random_color())


# Вызываем ф-ции
for i in range(100):
    fireworks()
for i in range(20):
    balloon(sd.random_point())

# Функции "flag" даётся аргумент, центр экрана
flag(sd.get_point(width / 2, height / 2))

# !задний фон рисуется самым первым
# !К каждому пункту функцию
sd.pause()

# OK