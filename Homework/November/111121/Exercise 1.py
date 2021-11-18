# Ввод чисел
a=int(input())
b = 0
c = 0
# Вводим условие
if a==0:
    print("Ошибка")
else:
# Вводим цикл
    while a!=0:
        b= b + a
        c= c + 1
        a=int(input())
# Ввыводим результат
print(b / c)