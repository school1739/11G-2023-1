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

width = 1500
height = 700
sd.set_screen_size(width, height)
sd._init()

center = sd.get_point(width / 2, height / 2) #центр


class Firework:  # Основной класс фейерверка
    def fireworks(x, y):
        sd.circle(sd.get_point(x, y), 10, sd.random_color(), 0)


class FireworkCenter(Firework): # Подкласс для большой центральной части фейерверка
        for i in range(1000):
            Firework.fireworks(center.x + random.randint(-150, 150), center.y + random.randint(-150, 150))


class FireworkAround(Firework):  # Подкласс для маленьких фейерверков вокруг основного
    for indent in range(3):
        for i in range(300):
            Firework.fireworks(center.x + random.randint(-450, -350) + 400 * indent,
                               center.y + random.randint(250, 350))
    for indent in range(2):
        for i in range(300):
            Firework.fireworks(center.x + random.randint(-250, -150) + 400 * indent,
                               center.y + random.randint(-350, -250))


class Balloon:  # Класс для шарика
    def __init__(self):
        pass

    def balloon(self):
        sd.ellipse(sd.get_point(self.x - 20, self.y - 30), sd.get_point(self.x + 20, self.y + 30),
                   sd.random_color())

        sd.polygon(point_list=[sd.get_point(self.x, self.y - 30), sd.get_point(self.x - 5, self.y - 40),
                               sd.get_point(self.x + 5, self.y - 40)], color=sd.random_color(), width=0)

        sd.line(sd.get_point(self.x, self.y - 40), sd.get_point(self.x - 5, self.y - 60))
        sd.line(sd.get_point(self.x - 5, self.y - 60), sd.get_point(self.x + 5, self.y - 80))
        sd.line(sd.get_point(self.x + 5, self.y - 80), sd.get_point(self.x - 5, self.y - 100))
        sd.line(sd.get_point(self.x - 5, self.y - 100), sd.get_point(self.x + 5, self.y - 120))


for i in range(5): # 5 шариков
    Balloon.balloon(sd.random_point())

sd.pause()

