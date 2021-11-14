length = float(input("Длина:"))
width = float(input("Ширина:"))
height = float(input("Высота:"))

print("Площадь комнаты:" ,length * width)
print("Площадь стен:" ,(width + length) * height * 2)