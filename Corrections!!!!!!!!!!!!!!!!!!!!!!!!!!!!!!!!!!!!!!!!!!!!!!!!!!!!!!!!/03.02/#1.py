import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


start_x, start_y = 50, 50      # кординаты
end_x, end_y = 350, 450
sd.resolution = (500, 500)

for current_color in rainbow_colors:
    start_point = sd.get_point(start_x, start_y)
    end_point = sd.get_point(end_x, end_y)
    start_x += 5
    end_x += 5
    sd.line(start_point=start_point, end_point=end_point, color=current_color,width=4)

start_x, start_y = 250, 0
sd.resolution = (500, 500)

for current_color in rainbow_colors:
    center_position = sd.get_point(start_x, start_y)
    sd.circle(center_position=center_position, radius=400, color=current_color, width=15)
    start_y -= 15

sd.pause()
