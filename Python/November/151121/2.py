# Ввод чисел
first_num = int(input("Введите положительное число: "))
second_num = int(input("Введите положительное число: "))
# Проверка на ввод неположитеьных чисел
if first_num <= 0 or second_num <= 0:
    print("Ошибка!")
else:
    # Выбор меньшего из чисел
    divider = min(first_num, second_num)
    # Проверка на наибольший общий делитель
    while first_num % divider != 0 or second_num % divider != 0:
        divider -= 1
    print(divider)

# Evaluation: OK