# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Под смайликом сделать подпись "Shit happens"


screen = sd.set_screen_size(width=1500, height=800)
screen_init = sd._init()

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

radius_of_smile = 100


# Drawing Smile
def draw_smile(x, y):
    center_of_smile = sd.get_point(x, y)
    sd.circle(center_of_smile, radius_of_smile, sd.COLOR_YELLOW, 0)

    sd.polygon([
        sd.get_point(center_of_smile.x + radius_of_smile / 2, center_of_smile.y - radius_of_smile / 2),
        sd.get_point(center_of_smile.x - radius_of_smile / 2, center_of_smile.y - radius_of_smile / 2),
        sd.get_point(center_of_smile.x - radius_of_smile / 4, center_of_smile.y - radius_of_smile / 8),
        sd.get_point(center_of_smile.x + radius_of_smile / 4, center_of_smile.y - radius_of_smile / 8),

    ],
        sd.COLOR_BLACK, 0)

    sd.circle(center_of_smile, radius_of_smile // 3, sd.COLOR_YELLOW, 0)
    sd.line(sd.get_point(center_of_smile.x, center_of_smile.y - radius_of_smile // 8),
            sd.get_point(center_of_smile.x, center_of_smile.y + radius_of_smile // 8), color=sd.COLOR_BLACK, width=10)

    x = radius_of_smile // 3
    y = center_of_smile.y + radius_of_smile // 3

    eyes = sd.get_point(x, y)
    radius_of_eyes = radius_of_smile // 8

    sd.circle(sd.get_point(center_of_smile.x - eyes.x, eyes.y), radius_of_eyes, sd.COLOR_BLACK, 0)
    sd.circle(sd.get_point(center_of_smile.x + eyes.x, eyes.y), radius_of_eyes, sd.COLOR_BLACK, 0)


# drawing one Letter
def draw_letter(symbol, start_point, width, height):
    for segment in symbols[symbol]:
        start_of_line = sd.get_point(segment[0][0] * width + start_point.x, segment[0][1] * height + start_point.y)
        end_of_line = sd.get_point(segment[1][0] * width + start_point.x, segment[1][1] * height + start_point.y)
        sd.line(start_of_line, end_of_line, sd.COLOR_RED, 7)


# Drawing inscription
def draw_inscription(left_bottom, right_top, inscription):
    # The markup of inscription
    width_of_inscription = right_top.x - left_bottom.x
    height_of_inscription = right_top.y - left_bottom.y
    symbol_width = width_of_inscription // len(inscription)
    # The rendering every letter in inscription
    for i, symbol in enumerate(inscription):
        draw_letter(symbol, sd.get_point(left_bottom.x + symbol_width * i, left_bottom.y),
                    symbol_width // 2, height_of_inscription)


# The calling of Functions
draw_smile(500, 500)
draw_inscription(sd.get_point(50, 50), sd.get_point(700, 300), 'shit happens')

sd.pause()

# OK. Stalin happens