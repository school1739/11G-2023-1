length = float(input('Длина: '))
width = float(input('Ширина: '))
height = float(input('Высота: '))

print(f'Площадь комнаты: {length * width}')
print(f'Площадь стен: {(width + length) * height * 2}')
