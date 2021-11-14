#Ввод цены
a = int(input("Цена: "))
b = 0
с = ''
#Вводим цикл
while a!=с:
    b += int(a)
    a = str(input("Цена: "))
#Ввывод суммы
print(b)
#Округление суммы
d = int(5 * round(b / 5))
#Ввывод результата
print(d)