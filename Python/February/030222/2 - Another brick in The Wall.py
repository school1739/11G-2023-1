# (цикл for)
import simple_draw
background_color = (200, 120, 0)
step = 0
for y in range(0, 1000, 50):
    y1 = y + 50
    step -= 50
    for x in range(step, 1000, 100):
        x1 = x + 100
        point = sd.get_point(x, y)
        point1 = sd.get_point(x1, y1)
        sd.rectangle(point, point1, color=sd.random_color(), width=0)
sd.pause()
simple_draw.pause()

# NOT OK