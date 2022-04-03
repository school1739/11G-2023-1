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


class Firework:  # Основной класс фейерверка
    def __init__(self, center: sd.Point, radius: int, circle_radius: int):
        for _ in range(15):
            angle = 2 * math.pi * random.random()
            r = radius * math.sqrt(random.random())
            x = r * math.cos(angle) + center.x
            y = r * math.sin(angle) + center.y

            sd.circle(sd.get_point(x, y), circle_radius, sd.random_color())


class FireworkCenter(Firework):  # Подкласс для большой центральной части фейерверка
    def __init__(self, center: sd.Point):
        super().__init__(center, 200, 100)


class FireworkAround(Firework):  # Подкласс для маленьких фейерверков вокруг основного
    def __init__(self, center: sd.Point):
        super().__init__(center, 100, 50)


class Balloon:  # Класс для шарика
    def __init__(self, center: sd.Point, width: int, height: int):
        left_bottom = sd.Point(center.x - width / 2, center.y - height / 2)
        right_top = sd.Point(center.x + width / 2, center.y + height / 2)
        sd.ellipse(left_bottom, right_top, sd.random_color())
        sd.polygon([sd.Point(center.x, left_bottom.y),
                    sd.Point(center.x - width / 5, left_bottom.y - height / 5),
                    sd.Point(center.x + width / 5, left_bottom.y - height / 5)])



sd.pause()
