a = int(input("Введите 1-ое положительное число"))
b = int(input("Введите 2-ое положительное число"))
if a <=0 or b <=0:
#проверка
    print("ерор")
else:
    delitel = min(a,b)
    #меньшее число
    while a % delitel !=0 or b % delitel !=0:
        delitel-=1
    #проверка на делитель
    print(delitel)

# Evaluation: OK