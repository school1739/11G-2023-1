import random
a = 0#количество обновлений
b = 0#максимум
for i in range(100):#цикл для cоздания числа
    num = random.randint(1,100)
    if num > b:
        print(num, "<=update")
        b = num
        a +=1
        #проверка на новый максимум
    else:
        print(num)
        i+=1
print(f"Макс значение в ряду:100"f"\кол-во смен макс значения:{a}")
