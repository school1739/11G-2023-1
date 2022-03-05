import math
print('1 - Формула Виета для приближения числа π')
print('2 - Формула Валлиса')
print('3 - Ряд Лейбница')
n = int(input("Введите число,в зависимости от того, какой формулой вы хотите получить число π: "))
m = input("Введите число, сколько знаков после запятой вы хотите видеть (лучше 4): ")
π = int(0)
if n == 1:
    π = math.sqrt(2) * (math.sqrt(2 + math.sqrt(2))) * math.sqrt(2 + (math.sqrt(2 + math.sqrt(2)))) * math.sqrt(2 + math.sqrt(2 + (math.sqrt(2 + math.sqrt(2)))))
    print("%.4f" % π)

# Evaluation: NOT OK