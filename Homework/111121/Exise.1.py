# Сумма и количество чисел
total = 0
n = 0
# Считываем числа,пока пользователь не введёт 0
print('Вводите числа:')
while (num := float(input())) != 0:
    total += num
    n += 1

if n == 0:
    # Сразу введён 0
    print('Error')
else:
    # Выводим среднее значение
    print(total / n)

# Evaluation: OK