# (определение функций)
import simple_draw

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Под смайликом сделать подпись "Shit happens"

sd.resolution = (700, 700)


def smile(x, y, color):
    start_point = sd.get_point(x, y)
    sd.circle(start_point, 50, color, width=4)
    sd.line(sd.get_point(x - 20, y - 5), sd.get_point(x - 10, y - 20), color, 2)
    sd.line(sd.get_point(x - 10, y - 20), sd.get_point(x + 10, y - 20), color, 2)
    sd.line(sd.get_point(x + 10, y - 20), sd.get_point(x + 20, y - 5), color, 2)
    sd.line(sd.get_point(x - 15, y + 20), sd.get_point(x - 15, y + 5), color, 2)
    sd.line(sd.get_point(x + 15, y + 20), sd.get_point(x + 15, y + 5), color, 2)


for i in range(10):
    point = sd.random_point()
    x = point.x
    y = point.y
    color = sd.random_color()
    smile(x, y, color)

simple_draw.pause()

# NOT OK

#  File "C:\Users\bormo\PycharmProjects\python.21-22-1\Python\February\030222\3 - Shit happens.py", line 9, in <module>
#     sd.resolution = (700, 700)
# NameError: name 'sd' is not defined. Did you mean: 'id'?