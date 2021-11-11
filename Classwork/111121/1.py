sum = 0
k =int(input())
i = 0
# Проверяем первое введённое число
if k==0:
    print("Первое число не должно быть 0!")
else:
    # Высчитываем ср.арифметическое
    while k !=0:
        sum+=k
        i+=1
        k = int(input())
    print(sum/(i))