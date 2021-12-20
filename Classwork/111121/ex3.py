##########################################
#   Задание 3. Периметр многоугольника   #
##########################################

import math


# Класс точки
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Метод для определения расстояния между этой и другой точками
    def distance(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)


print('Введите все точки, x и y через пробел')
perimeter = 0
start = None
prev = None
# Вводим точки пока строка не пустая
while (point := input()) != '':
    point = Point(*map(int, point.split()))
    # Если это первая введённая точка, сохраняем её
    if start is None:
        start = point
        prev = point
    # Иначе прибавляем к периметру расстояние до предыдущей
    else:
        perimeter += point.distance(prev)
        prev = point
# Добавляем расстояние между первой и последней точками
perimeter += start.distance(prev)

# Выводим периметр
print(f'Периметр = {perimeter:.2f}')

# Evaluation: NOT OK. Перемудрил, и получилось не оч. Классы это круто, но не нужно на нашем уровне.
# 1 2 3 4
# Traceback (most recent call last):
#   File "\python.21-22-1\Classwork\111121\ex3.py", line 25, in <module>
#     point = Point(*map(int, point.split()))
# TypeError: Point.__init__() takes 2 positional arguments but 5 were given