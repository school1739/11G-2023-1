# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Под смайликом сделать подпись "Shit happens"

# Словарь со списками точек начала и конца линий каждой буквы
symbols = {
    's': [((1, 0.7), (0.5, 1)),
          ((0.5, 1), (0, 0.7)),
          ((0, 0.7), (1, 0.3)),
          ((1, 0.3), (0.5, 0)),
          ((0.5, 0), (0, 0.3))],
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

sd.background_color = sd.COLOR_WHITE
sd.set_screen_size(1000, 600)
smile_radius = 200


# Функция для рисования смайлика
def draw_smile(x, y):
    # Круг
    center = sd.get_point(x, y)
    sd.circle(center, smile_radius, sd.COLOR_YELLOW, 0)
    # Улыбка
    sd.polygon([
        sd.get_point(center.x - smile_radius // 2, center.y - smile_radius // 10),
        sd.get_point(center.x - smile_radius // 4, center.y - smile_radius // 2),
        sd.get_point(center.x + smile_radius // 4, center.y - smile_radius // 2),
        sd.get_point(center.x + smile_radius // 2, center.y - smile_radius // 10),
    ], sd.COLOR_BLACK, 0)
    sd.circle(center, smile_radius // 3, sd.COLOR_YELLOW, 0)
    # Глаза
    eyes_y = center.y + smile_radius // 2
    eyes_shift_x = smile_radius // 2
    eyes_radius = smile_radius // 6
    sd.circle(sd.get_point(center.x - eyes_shift_x, eyes_y), eyes_radius, sd.COLOR_BLACK, 0)
    sd.circle(sd.get_point(center.x + eyes_shift_x, eyes_y), eyes_radius, sd.COLOR_BLACK, 0)


# Функция для рисования символа
def draw_symbol(symbol, start, width, height, thickness):
    # Рисуем каждую линию
    for line in symbols[symbol]:
        line_start = sd.get_point(line[0][0] * width + start.x, line[0][1] * height + start.y)
        line_end = sd.get_point(line[1][0] * width + start.x, line[1][1] * height + start.y)
        sd.line(line_start, line_end, sd.COLOR_BLACK, thickness)


# Функция для рисования текста
def draw_text(text, left_bottom, right_top, thickness):
    # Рассчитываем общую ширину и ширину и высоту символов
    width = right_top.x - left_bottom.x
    height = right_top.y - left_bottom.y
    symbol_width = width // len(text)
    # Рисуем каждый символ
    for i, symbol in enumerate(text):
        # Увеличиваем высоту символа в 2 раза если это заглавная буква
        symbol_height = height
        if symbol.isupper():
            symbol_height *= 2
        draw_symbol(symbol.lower(), sd.get_point(left_bottom.x + symbol_width * i, left_bottom.y),
                    symbol_width // 2, symbol_height, thickness)


draw_smile(500, 300)
draw_text('Shit happens', sd.get_point(50, 50), sd.get_point(1000, 100), 5)

sd.pause()

# OK