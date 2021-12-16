import math

# Есть значение радиуса круга
radius = 42

# расчитываем и округляем площадь круга
sq= round(3.1415926 * float(radius ^ 2), 4)
print(sq)

# есть координаты точки
point_1 = (23, 34)
# где 23 - а х, 34 -  у

# создаем словать точек
points = {}
center = (0, 0)
points["center"] = center
points["point_1"] = point_1

# расстояние от центра до точки
distance = math.sqrt((center[0] - point_1[0]) ** 2 + (center[1] - point_1[1]) ** 2)

# являетс яли точка частью круга
if distance <= radius:
    print(True)
else:
    print(False)

# Аналогично для другой точки
point_2 = (30, 30)

points["point_2"] = point_2
# расстояние от центра до 2 точки
distance = math.sqrt((center[0] - point_2[0]) ** 2 + (center[1] - point_2[1]) ** 2)

# принадлежит ли тточка кругу
if distance <= radius:
    print(True)
else:
    print(False)

# Пример вывода на консоль:
#
# 77777.7777
# False
# False