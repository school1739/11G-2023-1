# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Под смайликом сделать подпись "Shit happens"

sd.background_color = (128, 128, 128)  # Серый фон
sd.set_screen_size(width=1600, height=900)  # Разрешение моего экрана :(


def facik(x, y):  # Делаем функцию (потому так написано в задании, а без неё всё пишется в 5 строчек)
    # Главный шарик, сам смайлик
    sd.circle(center_position=sd.get_point(x, y), radius=200, color=sd.COLOR_DARK_YELLOW, width=0)
    # Улыбка (чёрный эллпис)
    sd.ellipse(left_bottom=sd.get_point(x - 125, y - 150), right_top=sd.get_point(x + 125, y), color=sd.COLOR_BLACK,
               width=0)
    # Улыбка (жёлтый эллипс перекрывает чёрный, выходит улыбка)
    sd.ellipse(left_bottom=sd.get_point(x - 125, y - 125), right_top=sd.get_point(x + 125, y + 25),
               color=sd.COLOR_DARK_YELLOW,
               width=0)
    # Левый глаз
    sd.ellipse(left_bottom=sd.get_point(x - 100, y + 15), right_top=sd.get_point(x - 50, y + 85), color=sd.COLOR_BLACK,
               width=0)
    # Правый глаз
    sd.ellipse(left_bottom=sd.get_point(x + 50, y + 15), right_top=sd.get_point(x + 100, y + 85), color=sd.COLOR_BLACK,
               width=0)


facik(800, 500)


def shit_happens(x, y):  #625 125

    #  S
    sd.line(start_point=sd.get_point(x - 575, y - 25), end_point=sd.get_point(x - 525, y - 75), color=sd.COLOR_BLACK, width=5)
    sd.line(start_point=sd.get_point(x - 525, y - 75), end_point=sd.get_point(x - 475, y - 25), color=sd.COLOR_BLACK, width=5)
    sd.line(start_point=sd.get_point(x - 475, y - 25), end_point=sd.get_point(x - 575, y + 75), color=sd.COLOR_BLACK, width=5)
    sd.line(start_point=sd.get_point(x - 575, y + 75), end_point=sd.get_point(x - 525, y + 125), color=sd.COLOR_BLACK, width=5)
    sd.line(start_point=sd.get_point(x - 525, y + 125), end_point=sd.get_point(x - 475, y + 75), color=sd.COLOR_BLACK, width=5)

    #  h
    sd.line(start_point=sd.get_point(x - 425, y - 75), end_point=sd.get_point(x - 425, y + 125), color=sd.COLOR_BLACK, width=4)
    sd.line(start_point=sd.get_point(x - 425, y + 25), end_point=sd.get_point(x - 375, y + 25), color=sd.COLOR_BLACK, width=4)
    sd.line(start_point=sd.get_point(x - 375, y + 25), end_point=sd.get_point(x - 375, y - 75), color=sd.COLOR_BLACK, width=4)

    #  i
    sd.line(start_point=sd.get_point(x - 325, y - 75), end_point=sd.get_point(x - 325, y + 75), color=sd.COLOR_BLACK, width=4)
    sd.circle(center_position=sd.get_point(x - 324, y + 85), radius=5, color=sd.COLOR_BLACK, width=0)

    #  t
    sd.line(start_point=sd.get_point(x - 250, y - 75), end_point=sd.get_point(x - 250, y + 125), color=sd.COLOR_BLACK, width=4)
    sd.line(start_point=sd.get_point(x - 250, y - 75), end_point=sd.get_point(x - 225, y - 75), color=sd.COLOR_BLACK, width=4)
    sd.line(start_point=sd.get_point(x - 275, y + 50), end_point=sd.get_point(x - 225, y + 50), color=sd.COLOR_BLACK, width=4)

    #  625  125

    # H
    sd.line(start_point=sd.get_point(x - 25, y - 75), end_point=sd.get_point(x - 25, y + 125), color=sd.COLOR_BLACK, width=4)
    sd.line(start_point=sd.get_point(x - 25, y + 25), end_point=sd.get_point(x + 25, y + 25), color=sd.COLOR_BLACK, width=4)
    sd.line(start_point=sd.get_point(x + 25, y - 75), end_point=sd.get_point(x + 25, y + 125), color=sd.COLOR_BLACK, width=4)

    #  a
    sd.ellipse(left_bottom=sd.get_point(x + 75, y - 75), right_top=sd.get_point(x + 125, y + 25), color=sd.COLOR_BLACK, width=4)
    sd.line(start_point=sd.get_point(x + 125, y - 75), end_point=sd.get_point(x + 125, y + 25), color=sd.COLOR_BLACK, width=4)

    #  p
    sd.line(start_point=sd.get_point(x + 175, y - 110), end_point=sd.get_point(x + 175, y), color=sd.COLOR_BLACK, width=4)
    sd.ellipse(left_bottom=sd.get_point(x + 175, y - 50), right_top=sd.get_point(x + 225, y + 25), color=sd.COLOR_BLACK, width=4)

    #  p
    sd.line(start_point=sd.get_point(x + 275, y - 110), end_point=sd.get_point(x + 275, y), color=sd.COLOR_BLACK, width=4)
    sd.ellipse(left_bottom=sd.get_point(x + 275, y - 50), right_top=sd.get_point(950, y + 25), color=sd.COLOR_BLACK, width=4)

    #  e
    sd.rectangle(left_bottom=sd.get_point(x + 375, y), right_top=sd.get_point(x + 425, y + 25), color=sd.COLOR_BLACK, width=4)
    sd.line(start_point=sd.get_point(x + 375, y - 75), end_point=sd.get_point(x + 375, y + 25), color=sd.COLOR_BLACK, width=4)
    sd.line(start_point=sd.get_point(x + 375, y - 75), end_point=sd.get_point(x + 425, y - 75), color=sd.COLOR_BLACK, width=4)

    #  n
    sd.line(start_point=sd.get_point(x + 475, y - 75), end_point=sd.get_point(x + 475, y + 25), color=sd.COLOR_BLACK, width=4)
    sd.line(start_point=sd.get_point(x + 475, y + 10), end_point=sd.get_point(x + 525, y + 10), color=sd.COLOR_BLACK, width=4)
    sd.line(start_point=sd.get_point(x + 525, y + 10), end_point=sd.get_point(x + 525, y - 75), color=sd.COLOR_BLACK, width=4)

    #  s
    sd.line(start_point=sd.get_point(x + 575, y - 50), end_point=sd.get_point(x + 600, y - 75), color=sd.COLOR_BLACK, width=5)
    sd.line(start_point=sd.get_point(x + 600, y - 75), end_point=sd.get_point(x + 625, y - 50), color=sd.COLOR_BLACK, width=5)
    sd.line(start_point=sd.get_point(x + 625, y - 50), end_point=sd.get_point(x + 575, y), color=sd.COLOR_BLACK, width=5)
    sd.line(start_point=sd.get_point(x + 575, y), end_point=sd.get_point(x + 600, y + 25), color=sd.COLOR_BLACK, width=5)
    sd.line(start_point=sd.get_point(x + 600, y + 25), end_point=sd.get_point(x + 625, y), color=sd.COLOR_BLACK, width=5)

shit_happens(625, 125)


sd.pause()
