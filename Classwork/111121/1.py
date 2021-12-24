sum = 0
k =int(input("Введите любое число, кроме 0:"))
i = 0
# Проверяем первое введнное значение
if k==0:
    print("Первое число не должно быть 0!")
else:
    # Высчитываем ср.арифметическое
    while k !=0:
        sum+=k
        i+=1
        k = int(input())
    print(sum/(i))

# Evaluation: OK