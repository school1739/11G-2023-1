a = int(input("Введите 1-ое положительное число"))
b = int(input("Введите 2-ое положительное число"))
if a <=0 or b <=0:
    print("ерор")
else:
    delitel = min(a,b)
    while a % delitel !=0 or b % delitel !=0:
        delitel-=1
    print(delitel)
