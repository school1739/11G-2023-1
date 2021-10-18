old = int(input("Введите свой возраст:"))
if old >= 0:
    if old >= 2:
        print("Ваш возраст:", " ", 21 + (old - 2) * 4)
    else:
        print("Ваш возраст:", " ", 7 * old)
else:
    print("Неправильное число")
