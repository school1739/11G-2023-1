from math import sqrt
x = []
y = []
# Добавление начальных координат в списки координат
x.append(input("Введите первую координату X: "))
y.append(input("Введите первую координату y: "))
# Счётчик
i = 0
# Периметр
res = 0
while True:
    vvodx = input("Введите координату X: ")
    # Проверка на ввод пустого значения
    if vvodx == '' or vvodx == ' ':
        break
    vvody = input("Введите координату y: ")
    # Проверка на ввод пустого значения
    if vvody == '' or vvody == ' ':
        break
    x.append(vvodx)
    y.append(vvody)
    i += 1
    # Вычисление длины стороны и прибаление её к периметру
    res += sqrt((int(x[i]) - int(x[i - 1])) ** 2 + (int(y[i]) - int(y[i - 1])) ** 2)
# Вычисление длины последней стороны и прибаление её к периметру
res += sqrt((int(x[0]) - int(x[-1])) ** 2 + (int(y[0]) - int(y[-1])) ** 2)
print(res)