import math

print("1) Формула Виета для приближения числа π"
      "\n2) Формула Валлиса"
      "\n3) Ряд Лейбница")
choice, rounding = int(input("Напишите номер фомрулы для числа π: ")), int(input("До скольки знаков после запятой округлять: "))
kol = int(input("Введите кол-во повторения циклов(если ввести большое значение, программа будет долго выполняться): "))
# Формула Виета для приближения числа π
if choice == 1:
    sqrt2 = math.sqrt(2)
    pi = 2 / sqrt2
    for i in range(kol*100):
        sqrt2 = math.sqrt(2 + sqrt2)
        pi = pi * 2 / sqrt2
# Формула Валлиса
    print(round((pi * 2), rounding))
elif choice == 2:
    pi = (2 / 1) * (2 / 3)
    for i in range(2, kol*1000000, 2):
        pi = pi * ((2 + i) / (1 + i)) * ((2 + i) / (3 + i))
    print(round((pi * 2), rounding))
# Ряд Лейбница
else:
    pi = 1 - 1 / 3 + 1 / 5
    for i in range(4, kol* 1000000, 4):
        pi += -1 / (3 + i) + 1 / (5 + i)
    print(round((pi * 4), rounding))