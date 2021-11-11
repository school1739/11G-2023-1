##
# Находим периметр многоугольника
#
#
perimeter = 0
x1, y1 = None
print('Введите координаты точек через пробел: ')
while (coords := input()) != '':
    x, y = map(int, coords.split())
    if x1 is None:

