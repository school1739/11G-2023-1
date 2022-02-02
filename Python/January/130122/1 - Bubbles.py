import simple_draw as sd
screen=sd.set_screen_size(width=1500, height=800)
screen_init=sd.init()
# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
def create_buble(point, step, color):
    radius=5
    for i in range(3):
        radius +=step
        sd.circle(center_position=point, radius=radius, color=color, width=1)

# Написать функцию рисования пузырька, принммающую 2 (или более) sd.circle(center_position, radius=50, color=(0, 255, 0), width=1)параметра: точка рисовании и шаг
for x in range(50, 550, 50):
    point=sd.get_point(x, 50)
    create_bubble(point, step=3, color=sd.COLOR_GREEN)

# Нарисовать 10 пузырьков в ряд
for x in range(50,550,50):
        point=sd.get_point(x,50)
        create_bubble(point,step=3,color=sd.COLOR_WHITE)

# Нарисовать три ряда по 10 пузырьков
for y in range (100,301,100):
    for x in range(50,550,50):
        point=sd.get_point(x,y)
        create_bubble(point, step=3, color=sd.COLOR_BLUE)
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for y in range (10,1000,50):
    for x in range (10,1000,50):
        poin=sd.get_point(sd.random_number(10,1400),sd.random_number(10,800))
        create_bubble(point, step=3, color=sd.random_color())

sd.pause()

# AttributeError: module 'simple_draw' has no attribute 'init'. Did you mean: '_init'?