import simple_draw as sd
import random
import math

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


def create_screen():
    sd.set_screen_size(width=1500, height=800)
    sd._init()


class DrawObject:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        pass


class SmallFirework(DrawObject):  # Основной класс фейерверка
    def __init__(self, x, y, color):
        super(SmallFirework, self).__init__(x, y, color)

    def draw(self):
        self.circles = [
            sd.circle(center_position=(sd.get_point(self.x + random.randint(2, 100), self.y + random.randint(1, 100))),
                      radius=5, color=self.color, width=0)
            for i in range(30)]


class BigFirework(DrawObject):
    def __init__(self, x, y, color):
        super(BigFirework, self).__init__(x, y, color)

    def draw(self):
        sd.circle(center_position=(sd.get_point(self.x, self.y)), radius=10, color=self.color, width=0)


class Balloon(DrawObject):  # Класс для шарика
    def __init__(self, x, y, color):
        super(Balloon, self).__init__(x, y, color)

    def draw(self):
        sd.ellipse(sd.get_point(self.x - 15, self.y - 20),
                   sd.get_point(self.x + 15, self.y + 20),
                   color=self.color,
                   width=0)

        sd.polygon(
            [sd.get_point(self.x - 5, self.y - 20),
             sd.get_point(self.x + 5, self.y - 20),
             sd.get_point(self.x, self.y - 32)],
            width=0)

        sd.line(sd.get_point(self.x, self.y - 32), sd.get_point(self.x, self.y - 37), color=sd.COLOR_WHITE)
        sd.line(sd.get_point(self.x, self.y - 37), sd.get_point(self.x - 3, self.y - 45), color=sd.COLOR_WHITE)
        sd.line(sd.get_point(self.x - 3, self.y - 45), sd.get_point(self.x - 3, self.y - 50), color=sd.COLOR_WHITE)
        sd.line(sd.get_point(self.x - 3, self.y - 50), sd.get_point(self.x - 6, self.y - 60), color=sd.COLOR_WHITE)


create_screen()

balloons = [Balloon(random.randint(100, 800), random.randint(100, 300), sd.random_color()) for i in range(5)]

for balloon in balloons:
    balloon.draw()

small_fireworks = [SmallFirework(random.randint(300, 1200), random.randint(500, 600), sd.random_color()) for i in
                   range(5)]

for firework in small_fireworks:
    firework.draw()

big_firework = [BigFirework(random.randint(650, 850), random.randint(570, 630), sd.random_color())
                for i in range(15)]

for firework in big_firework:
    firework.draw()

sd.pause()