# Находим периметр многоугольника
#
import math


# Класс точки
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Метод для определения расстояния между этой и другой точкой
    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


print('Введите все точки, x и y через пробел')
perimeter = 0
start = None
prev = None
# Вводим точки пока строка не пустая
while (str_point := input()) != '':
    point = Point(*map(int, str_point.split()))
    # Если это первая точка, сохраняем её
    if start is None:
        start = point
        prev = point
    # Иначе прибавляем к периметру расстояние
    else:
        perimeter += point.distance(prev)
        prev = point
# Добавляем расстояние между первой и последней точками
perimeter += start.distance(prev)

# Выводим периметр
print(f'Периметр = {perimeter:.2f}')
