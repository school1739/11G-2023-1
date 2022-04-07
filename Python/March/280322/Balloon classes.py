import math
import simple_draw as sd
import random

"""
Задача: написать программу, выводящую на экран праздничный салют
и воздушные шарики, используя классы.
Салюты (5 салютов): 6 фейерверков (1 большой в центре, 5 в два раза
меньших вокруг). Фейерверк: не менее 15 закрашенных окружностей,
расположенных группой.
Шарик: основной овал, треугольник-пуцка, ломанная линия (не менее
4 отрезков) - верёвочка.
Фейерверки и шарики описываются в классах (обратите внимание на наследование!).
Постарайтесь максимально часто использовать рандом с небольшим разбросом,
чтобы не было одинаковых фигур.

Использование предопределенных классов обязательно. Дополнительные классы,
инкапсуляция, функции и классовые методы - произвольно.
Использование pygame и/или иных библиотек, кроме SD и random не допускается.
"""

sd.background_color = sd.COLOR_WHITE
sd.resolution = (1500, 1000)


# Основной класс фейерверка
class Firework:
    def __init__(self, center: sd.Point, radius: int, circle_radius: int):
        # Рисуем 15 окружностей в рандомном месте окружности
        for _ in range(15):
            angle = 2 * math.pi * random.random()
            r = radius * math.sqrt(random.random())
            x = r * math.cos(angle) + center.x
            y = r * math.sin(angle) + center.y

            sd.circle(sd.get_point(x, y), circle_radius, sd.random_color(), 0)


# Подкласс для большой центральной части фейерверка
class FireworkCenter(Firework):
    def __init__(self, center: sd.Point):
        super().__init__(center, 100, 50)


# Подкласс для маленьких фейерверков вокруг основного
class FireworkAround(Firework):
    def __init__(self, center: sd.Point):
        super().__init__(center, 50, 25)


# Класс салюта
class Salute:
    def __init__(self, center: sd.Point, radius: int):
        FireworkCenter(center)
        for _ in range(5):
            angle = 2 * math.pi * random.random()
            x = radius * math.cos(angle) + center.x
            y = radius * math.sin(angle) + center.y
            FireworkAround(sd.Point(x, y))


# Класс для шарика
class Balloon:
    def __init__(self, center: sd.Point, width: int, height: int):
        left_bottom = sd.Point(center.x - width / 2, center.y - height / 2)
        right_top = sd.Point(center.x + width / 2, center.y + height / 2)
        sd.ellipse(left_bottom, right_top, sd.random_color())
        sd.polygon([sd.Point(center.x, left_bottom.y),
                    sd.Point(center.x - width / 5, left_bottom.y - height / 5),
                    sd.Point(center.x + width / 5, left_bottom.y - height / 5)],
                   sd.random_color(), 0)
        sd.lines([sd.Point(center.x, left_bottom.y - height / 5),
                  sd.Point(center.x - width / 10, left_bottom.y - height / 5 * 2),
                  sd.Point(center.x + width / 10, left_bottom.y - height / 5 * 3),
                  sd.Point(center.x - width / 10, left_bottom.y - height / 5 * 4)],
                 sd.random_color(), width=3)


for _ in range(20):
    Balloon(sd.random_point(), sd.random_number(50, 100), sd.random_number(100, 150))

for _ in range(3):
    Salute(sd.random_point(), sd.random_number(200, 300))

sd.pause()