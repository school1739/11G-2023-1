# (определение функций)
import simple_draw as sd

sd.set_screen_size(1500, 700)
sd._init()


# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Под смайликом сделать подпись "Shit happens"

def smile(x, y, clr):
    # Лицо
    sd.circle(sd.get_point(x, y), 300, clr, 0)
    # Улыбка
    sd.circle(sd.get_point(x, y - 100), 150, (255, 0, 0), 0)
    sd.circle(sd.get_point(x, y - 50), 150, clr, 0)
    # Нос
    sd.ellipse(sd.get_point(x - 50, y - 100), sd.get_point(x + 50, y), (255, 0, 0))
    # Глаза
    sd.rectangle(sd.get_point(x - 150, y), sd.get_point(x + 150, y + 200), (0, 0, 0))
    sd.rectangle(sd.get_point(x - 80, y), sd.get_point(x + 80, y + 200), clr)


smile(1500 / 2, 700 / 2, (255, 255, 255))

sd.pause()

# Здесь должны были быть фунции рисования букв, но они убежали :(
# Как найду их, напишу