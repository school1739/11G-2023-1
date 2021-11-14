a = int(input("Введите день"))
b = int(input("Введите месяц"))
c = int(input("Введите год"))
if a <= 30 and b == 1 or a <= 30 and b == 3 or a <= 30 and b == 5 or a <= 30 and b == 7 or a <= 30 and b == 8 or a <= 30 and b == 10 or a <= 30 and b == 12:
    print(a + 1, b, c)
elif a == 31 and b == 1 or a == 31 and b == 3 or a == 31 and b == 5 or a == 31 and b == 7 or a == 31 and b == 8 or a == 31 and b == 10:
    print("1", b + 1, c)
elif a == 31 and b == 12:
    print("1", '1', c + 1)
elif a <= 29 and b == 4 or a <= 29 and b == 6 or a <= 29 and b == 9 or a <= 29 and b == 11:
    print(a + 1, b, c)
elif a == 30 and b == 4 or a == 30 and b == 6 or a == 30 and b == 9 or a == 30 and b == 11:
    print('1', b + 1, c)
elif a <= 27 and b == 2:
    print(a + 1, b, c)
elif a == 28 and b == 2 and c % 4 >= 1:
    print('1', b + 1, c)
elif a == 28 and b == 2 and c % 4 == 0:
    print(a + 1, b, c)
elif a == 29 and b == 2:
    print('1', b + 1, c)
else:
    print('Ошибка')
