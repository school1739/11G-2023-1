# (цикл for)
from typing import Any

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
  startx: Any = 50
  endx = 350
  starty = 50
  endy = 450
  for i in range(7):
      time.sleep(0.3)
      startx +=5
      endx +=+5
      sd.line(start_point=sd.get_point(startx,starty),end_point=sd.get_point(endx,endy),color = rainbow_colors[i],width=5)
# Подсказка: цикл нужно делать сразу по кортежу с цветами радуги.


# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
point = sd.get_point(600,-500)
r = 900
q = 0
for r in range(900,600,-10):
    time.sleep(0.3)
    sd.circle(center_position=point,radius=r,color=rainbow_colors[q],width=10)
    q +=1
    if q==7:
        break


sd.pause()
