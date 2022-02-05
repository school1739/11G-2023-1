# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Под смайликом сделать подпись "Shit happens"

sd.background_color = (128, 128, 128)
sd.set_screen_size(width=1600, height=900)  # Разрешение моего экрана :(

sd.circle(center_position=sd.get_point(800, 450), radius=200, color=sd.COLOR_DARK_YELLOW, width=0)
sd.ellipse(left_bottom=sd.get_point(675, 300), right_top=sd.get_point(925, 450), color=sd.COLOR_BLACK, width=0)
sd.ellipse(left_bottom=sd.get_point(675, 325), right_top=sd.get_point(925, 475), color=sd.COLOR_DARK_YELLOW, width=0)
sd.ellipse(left_bottom=sd.get_point(700, 465), right_top=sd.get_point(750, 535), color=sd.COLOR_BLACK, width=0)
sd.ellipse(left_bottom=sd.get_point(850, 465), right_top=sd.get_point(900, 535), color=sd.COLOR_BLACK, width=0)


sd.pause()
