# (определение функций)
import simple_draw as sd

sd.set_screen_size(1900, 900)
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


# "Координата" для каждой буквы в "Shit happens"
letters = {
    's': [((1, 0.7), (0.5, 1)),
          ((0.5, 1), (0, 0.7)),
          ((0, 0.7), (1, 0.3)),
          ((1, 0.3), (0.5, 0)),
          ((0.5, 0), (0, 0.3))],
    'S': [((2, 1.4), (1, 2)),
          ((1, 2), (0, 1.4)),
          ((0, 1.4), (2, 0.6)),
          ((2, 0.6), (1, 0)),
          ((1, 0), (0, 0.6))],
    'h': [((0, 1), (0, 0)),
          ((0, 0.5), (1, 0.5)),
          ((1, 0.5), (1, 0))],
    'i': [((0.5, 0), (0.5, 0.8)),
          ((0.5, 0.9), (0.5, 1))],
    't': [((0, 1), (1, 1)),
          ((0.5, 1), (0.5, 0))],
    'a': [((0, 0.7), (0.5, 1)),
          ((0.5, 1), (1, 0.7)),
          ((1, 0.7), (1, 0)),
          ((1, 0.5), (0, 0.5)),
          ((0, 0.5), (0, 0)),
          ((0, 0), (1, 0))],
    'p': [((0, 0), (0, 1)),
          ((0, 1), (1, 1)),
          ((1, 1), (1, 0.5)),
          ((1, 0.5), (0, 0.5))],
    'e': [((1, 0.3), (0.5, 0)),
          ((0.5, 0), (0, 0.3)),
          ((0, 0.3), (0, 0.7)),
          ((0, 0.7), (0.5, 1)),
          ((0.5, 1), (1, 0.5)),
          ((1, 0.5), (0, 0.5))],
    'n': [((0, 0), (0, 1)),
          ((0, 0.8), (0.5, 1)),
          ((0.5, 1), (1, 0.8)),
          ((1, 0.8), (1, 0))],
    ' ': []
}


def drawletter(letter, start, width, height, depth):
    # Рисуем линии буквы с помощью словаря letters
    for line in letters[letter]:
        line_start = sd.get_point(line[0][0] * width + start.x, line[0][1] * height + start.y)
        line_end = sd.get_point(line[1][0] * width + start.x, line[1][1] * height + start.y)
        sd.line(line_start, line_end, sd.COLOR_ORANGE, depth)


smile(1900 / 2, 700 / 2, (255, 255, 255))

for i, lttr in enumerate("Shit happens"):
    # Проверка на заглавную букву
    if lttr.istitle():
        drawletter(lttr, sd.get_point(130 * i + 200 - 100, 700), 100, 100, 10)
    else:
        drawletter(lttr, sd.get_point(130 * i + 200, 700), 100, 100, 10)

sd.pause()

# OK