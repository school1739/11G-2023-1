import simple_draw as sd
sd.set_screen_size(1000, 600)
# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
center_position=sd.random_point()

sd.circle(center_position, radius=50, color=(0, 255, 0), width=1)
sd.circle(center_position, radius=45, color=(0, 255, 0), width=1)
sd.circle(center_position, radius=40, color=(0, 255, 0), width=1)
# Написать функцию рисования пузырька, принммающую 2 (или более) sd.circle(center_position, radius=50, color=(0, 255, 0), width=1)параметра: точка рисовании и шаг

# Нарисовать 10 пузырьков в ряд

# Нарисовать три ряда по 10 пузырьков

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
sd.pause()