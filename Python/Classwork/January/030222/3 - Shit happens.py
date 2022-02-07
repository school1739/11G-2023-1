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


sd.line(start_point=sd.get_point(50, 100), end_point=sd.get_point(100, 50), color=sd.COLOR_BLACK, width=5)
sd.line(start_point=sd.get_point(100, 50), end_point=sd.get_point(150, 100), color=sd.COLOR_BLACK, width=5)
sd.line(start_point=sd.get_point(150, 100), end_point=sd.get_point(50, 200), color=sd.COLOR_BLACK, width=5)
sd.line(start_point=sd.get_point(50, 200), end_point=sd.get_point(100, 250), color=sd.COLOR_BLACK, width=5)
sd.line(start_point=sd.get_point(100, 250), end_point=sd.get_point(150, 200), color=sd.COLOR_BLACK, width=5)

sd.line(start_point=sd.get_point(200, 50), end_point=sd.get_point(200, 250), color=sd.COLOR_BLACK, width=4)
sd.line(start_point=sd.get_point(200, 150), end_point=sd.get_point(300, 150), color=sd.COLOR_BLACK, width=4)
sd.line(start_point=sd.get_point(300, 150), end_point=sd.get_point(300, 50), color=sd.COLOR_BLACK, width=4)
sd.line(start_point=sd.get_point(350, 50), end_point=sd.get_point(350, 200), color=sd.COLOR_BLACK, width=4)
sd.circle(center_position=sd.get_point(351, 210), radius=5, color=sd.COLOR_BLACK, width=0)

sd.line(start_point=sd.get_point(425, 50), end_point=sd.get_point(425, 250), color=sd.COLOR_BLACK, width=4)
sd.line(start_point=sd.get_point(425, 50), end_point=sd.get_point(450, 50), color=sd.COLOR_BLACK, width=4)
sd.line(start_point=sd.get_point(400, 175), end_point=sd.get_point(450, 175), color=sd.COLOR_BLACK, width=4)




sd.pause()
