# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

point_from = sd.get_point(30, 30)
point_to = sd.get_point(400, 500)
width = 10
step = 5
for i, color in enumerate(rainbow_colors):
    shift = point_from.y - step * i
    start = sd.get_point(point_from.x + shift, point_from.y - shift)
    end = sd.get_point(point_to.x + shift, point_to.y - shift)
    sd.line(start, end, color, width)
center = sd.get_point(400, 0)
radius = 200
step = 10
width = 10
for i, color in enumerate(rainbow_colors):
    sd.circle(center, radius - step * i, color, width)

sd.pause()

