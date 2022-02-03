# (цикл for)

import simple_draw as sd
sd.set_screen_size(1500,700)

sd._init()

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)



# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

def raduga(clr,step):
    sd.line(sd.get_point(50,50+step),sd.get_point(350,450+step),clr,4)
k1=0
for clr in rainbow_colors:
    raduga(clr,k1)
    k1-=5

# Подсказка: цикл нужно делать сразу по кортежу с цветами радуги.


# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

def raduga_circle(clr,step):
    sd.circle(sd.get_point(750,0),500 - step,clr,15)

k2=0
for clr in rainbow_colors:
    raduga_circle(clr,k2)
    k2+=15

sd.pause()
