a = int(input("Введите человеческий возраст "))
b = 0
if a >= 0:
    if a <= 2:
        b = a * 10.5
        print(b, "лет")
    else:
        b = 2 * 10.5 + (a - 2) * 4
        print(b, "лет")
else:
    print("Ошибка")
