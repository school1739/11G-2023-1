n = input("Введите двоичное число, которое хотите перевести в десятичное: ")
string = str(n)
i = len(string)
a = int(0)
b = int(string[a])
c = int(0)
d = int(0)
result = ""
print(n, "(2) =", end=" ")
if b == 0 or b == 1:
    while i > 0:
        b = int(string[a])
        i = i - 1
        c = b * (2 ** i)
        print(b, "*", "( 2 ^", i, ')', end=" ")
        a = a + 1
        d = c + d
        if i > 0:
            result = result + str(c) + "+"
            print("+", end=" ")
            c = 0
        else:
            result = result + str(c)
            c = 0
    print("=", result, "=", d, "(10)")
    print("Ответ:", d, "(10)")
else:
    print("Ошибка! Символы в строке не являются 1 или 0!")