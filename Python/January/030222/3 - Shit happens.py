# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Под смайликом сделать подпись "Shit happens"

smile_radius = 200


def draw_face(x, y):
    center = sd.get_point(x, y)
    sd.circle(center, smile_radius, sd.COLOR_YELLOW, 0)

    sd.polygon([
        sd.get_point(center.x - smile_radius // 2, center.y - smile_radius // 10),
        sd.get_point(center.x - smile_radius // 4, center.y - smile_radius // 2),
        sd.get_point(center.x + smile_radius // 4, center.y - smile_radius // 2),
        sd.get_point(center.x + smile_radius // 2, center.y - smile_radius // 10),
    ], sd.COLOR_BLACK, 0)
    sd.circle(center, smile_radius // 3, sd.COLOR_YELLOW, 0)

    eyes_y = center.y + smile_radius // 2
    eyes_shift_x = smile_radius // 2
    eyes_radius = smile_radius // 6
    sd.circle(sd.get_point(center.x - eyes_shift_x, eyes_y), eyes_radius, sd.COLOR_BLACK, 0)
    sd.circle(sd.get_point(center.x + eyes_shift_x, eyes_y), eyes_radius, sd.COLOR_BLACK, 0)


draw_face(300, 300)

sd.pause()
