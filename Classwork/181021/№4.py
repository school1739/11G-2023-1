stor = int(input("Введиете кол-во сторон:"))
if stor>10 or stor<3:
    print("Вы вышли из допустимого диапазона!")
else:
    if stor==3:
        print("Треугольник, 3 стороны")
    elif stor ==4:
        print("Четырехугольник, 4 стороны")
    elif stor == 5:
        print("Пятиуголник, 5 сторон")
    elif stor== 6:
        print("Шестиугольник, 6 сторон")
    elif stor == 7:
        print("Семиугольник, 7 сторон")
    elif stor ==8:
        print("Восьмиугольник, 8 сторон")
    elif stor==9:
        print("Девятиугольник, 9 сторон")
    else:
        print('Десятиугольник, 10 сторон')

# Evaluation: OK