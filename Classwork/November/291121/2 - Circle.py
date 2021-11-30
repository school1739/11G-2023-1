import math

# Есть значение радиуса круга
radius = 42

# расчитываем площадь круга и выводим округленное значение
square = round(3.1415926 * float(radius ^ 2), 4)
print(square)

# Далее, пусть есть координаты точки
point_1 = (23, 34)
# где 23 - координата х, 34 - координата у

# создаем словать точек
points = {}
center = (0, 0)
points["center"] = center
points["point_1"] = point_1

# высчитываем расстояние от центра до точки
distance = math.sqrt((center[0] - point_1[0]) ** 2 + (center[1] - point_1[1]) ** 2)

# проверяем входит ли точка в круг
if distance <= radius:
    print(True)
else:
    print(False)

# Аналогично для другой точки
point_2 = (30, 30)

points["point_2"] = point_2
# расчитываем расстояние от центра до 2 точки
distance = math.sqrt((center[0] - point_2[0]) ** 2 + (center[1] - point_2[1]) ** 2)

# проверяем входит ли точка в круг
if distance <= radius:
    print(True)
else:
    print(False)

# Пример вывода на консоль:
#
# 77777.7777
# False
# False
