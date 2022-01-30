import simple_draw as sd
import random
sd.resolution = (1200, 600)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

COLOR_RED = (255, 0, 0)
COLOR_ORANGE = (255, 127, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_CYAN = (0, 255, 255)
COLOR_BLUE = (0, 0, 255)
COLOR_PURPLE = (255, 0, 255)

COLOR_DARK_YELLOW = (127, 127, 0)
COLOR_DARK_ORANGE = (127, 63, 0)
COLOR_DARK_RED = (127, 0, 0)
COLOR_DARK_GREEN = (0, 127, 0)
COLOR_DARK_CYAN = (0, 127, 127)
COLOR_DARK_BLUE = (0, 0, 127)
COLOR_DARK_PURPLE = (127, 0, 127)


point = sd.get_point(300,300)
sd.circle(center_position=point)
radius = 50

for i in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius)

def bubble(point, step):
    radius = 50
    for i in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2)





for i in range(100,1100,100):
    point = sd.get_point(i,300)
    bubble(point=point, step=5)


for x in range(100,301,100):
    for i in range(100,1100,100):
        point = sd.get_point(i,x)
        bubble(point=point, step=5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
    colors = [
        COLOR_RED,
        COLOR_ORANGE,
        COLOR_YELLOW,
        COLOR_GREEN,
        COLOR_CYAN,
        COLOR_BLUE,
        COLOR_PURPLE,
        COLOR_DARK_YELLOW,
        COLOR_DARK_ORANGE,
        COLOR_DARK_RED,
        COLOR_DARK_GREEN,
        COLOR_DARK_CYAN,
        COLOR_DARK_BLUE,
        COLOR_DARK_PURPLE,
    ]
for i in range(10,1100,50):
    for g in range(10,1100,50):
        point = sd.get_point(sd.random_number(10,1400),sd.random_number(10,800))
        bubble(point,step=3)





sd.pause()
