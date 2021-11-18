# Вводим двоичное число
binary_num = input('Введите число в двоичном виде: ')
print('Переводим это число в десятичную систему счисления: ')

# Списки с частями формул
formula1 = []
formula2 = []
# Результат
result = 0

for index, n in enumerate(reversed(binary_num)):
    # Составляем первую формулу
    formula1.insert(0, f'{n}∙2^{index}')

    a = int(n) * (2 ** index)
    # Составляем вторую формулу
    formula2.insert(0, str(a))
    # Находим результат
    result += a

# Преобразовываем списки в строки
formula1 = '+'.join(formula1)
formula2 = '+'.join(formula2)
# Выводим результат
print(f'{binary_num}(2) = {formula1} = {formula2} = {result}(10)')
