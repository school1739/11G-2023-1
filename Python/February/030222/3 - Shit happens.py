# (определение функций)
import simple_draw

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Под смайликом сделать подпись "Shit happens"


# структура, содержащая информацию о координатах линий заданных символов
# координаты относительные (от 0 до 1)
glyphs_info = {
    's': [
        ((0, 0), (1, 0)),
        ((1, 0), (1, 0.5)),
        ((1, 0.5), (0, 0.5)),
        ((0, 0.5), (0, 1)),
        ((0, 1), (1, 1))
    ],
    'h': [
        ((0, 0), (0, 1)),
        ((1, 0), (1, 1)),
        ((0, 0.5), (1, 0.5))
    ],
    'i': [
        ((0.5, 0), (0.5, 1))
    ],
    't': [
        ((0.5, 0), (0.5, 1)),
        ((0, 1), (1, 1))
    ],
    'a': [
        ((0, 0), (0.5, 1)),
        ((0.5, 1), (1, 0)),
        ((0.25, 0.5), (0.75, 0.5))
    ],
    'p': [
        ((0, 0), (0, 1)),
        ((0, 1), (1, 1)),
        ((1, 1), (1, 0.5)),
        ((1, 0.5), (0, 0.5))
    ],
    'e': [
        ((0, 0), (0, 1)),
        ((0, 1), (1, 1)),
        ((0, 0.5), (1, 0.5)),
        ((0, 0), (1, 0))
    ],
    'n': [
        ((0, 0), (0, 1)),
        ((1, 0), (1, 1)),
        ((0, 1), (1, 0))
    ]
}


# функция отрисовка смайлика
# x, y - координаты центра смайлика
# color - цвет заливки смайлика
# r - радиус круга смайлика
def smile_icon(x, y, color, r=100):
    pos = simple_draw.get_point(x, y)   # центр круга смайлика
    # заливка
    simple_draw.circle(pos, r, color, 0)
    # граница
    simple_draw.circle(pos, r, simple_draw.COLOR_BLACK, 4)

    # координаты и размеры прищуренных глаз (прямая линия)
    eye_w = r / 3                   # ширина глаза
    eye_y = y + r / 3               # координата Y глаза
    eye1_x = x - r / 2 - eye_w / 2  # координата X левого конца левого глаза
    eye2_x = x + r / 2 - eye_w / 2  # координата X левого конца правого глаза

    # концы отрезка левого глаза
    eye1_p1 = simple_draw.get_point(eye1_x, eye_y)
    eye1_p2 = simple_draw.get_point(eye1_x + eye_w, eye_y)
    # рисуем левый глаз
    simple_draw.line(eye1_p1, eye1_p2, simple_draw.COLOR_BLACK, 2)

    # концы отрезка правого глаза
    eye2_p1 = simple_draw.get_point(eye2_x, eye_y)
    eye2_p2 = simple_draw.get_point(eye2_x + eye_w, eye_y)
    # рисуем правый глаз
    simple_draw.line(eye2_p1, eye2_p2, simple_draw.COLOR_BLACK, 2)

    # координаты и размеры рта (прямая линия)
    mouth_w = r
    mouth_x = x - mouth_w / 2
    mouth_y = y - r / 3

    # концы отрезка рта
    mouth_p1 = simple_draw.get_point(mouth_x, mouth_y)
    mouth_p2 = simple_draw.get_point(mouth_x + mouth_w, mouth_y)
    # рисуем рот
    simple_draw.line(mouth_p1, mouth_p2, simple_draw.COLOR_BLACK, 2)


# функция отрисовка символа
# glyph - символ
# x, y - положение символа (левый нижний угол)
# w, h - размеры символа
# color - цвет символа
def draw_glyph(glyph, x, y, w, h, color):
    # рисуем только, если есть информация о символе
    if glyph in glyphs_info.keys():
        # массив кортежей с координатами концов отрезков
        glyph_lines = glyphs_info[glyph]
        # в цикле по отрезкам
        for line in glyph_lines:
            # определяем координаты концов отрезков в соответсвие с заданными
            # координатами на холсте и размерами символа
            p1 = line[0]
            p2 = line[1]
            x1 = x + p1[0] * w
            y1 = y + p1[1] * h
            x2 = x + p2[0] * w
            y2 = y + p2[1] * h
            # формируем точки
            draw_p1 = simple_draw.get_point(x1, y1)
            draw_p2 = simple_draw.get_point(x2, y2)
            # рисуем
            simple_draw.line(draw_p1, draw_p2, color, 1)


# функция отрисовка текста
# txt - строка
# x, y - положение текста (левый нижний угол)
# w, h - размеры прямоугольника, в который вписан текст
# color - цвет текста
def draw_text(txt, x, y, w, h, color):
    space_w = max(1, w // 25)   # межсимвольное расстояние
    txt_len = len(txt)          # длина строки
    glyph_w = (w - space_w * (txt_len - 1)) / txt_len   # ширина символа
    # в цикле по символам рисуем символ, смещая положение символа по X на
    # ширину символа и межсимвольное расстояние
    for glyph in txt:
        glyph_h = h     # высота символа (увеличить на 50%, если заглавный)
        if glyph.isupper():
            glyph_h += glyph_h // 2

        draw_glyph(glyph.lower(), x, y, glyph_w, glyph_h, color)
        x += glyph_w + space_w


# установка размеров окна и заголовка
screen_w = 640
screen_h = 480
simple_draw.caption = "Smile"
simple_draw.set_screen_size(screen_w, screen_h)

# параметры смайлика
smile_x = screen_w // 2
smile_y = screen_h // 2 + 64
smile_r = 100

smile_icon(smile_x, smile_y, simple_draw.COLOR_YELLOW, smile_r)

# параметры текста
txt_h = 32
txt_w = screen_w * 3 // 4
txt_x = smile_x - txt_w // 2
txt_y = smile_y - smile_r // 2 - txt_h - 64

draw_text("Shit happens", txt_x, txt_y, txt_w, txt_h, simple_draw.COLOR_WHITE)

simple_draw.pause()

# OK