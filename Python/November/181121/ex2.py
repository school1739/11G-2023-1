# Вводим двоичное число
binary_num = input('Введите число в двоичном виде: ')
print('Переводим это число в десятичную систему счисления: ')

# Списки с частями формул
output1 = ''
output2 = ''
# Результат
result = 0

for index, n in enumerate(reversed(binary_num)):
    # Добавляем "+" между слагаемыми
    if index != 0:
        output1 = ' + ' + output1
        output2 = ' + ' + output2
    # Составляем первую формулу
    output1 = f'{n}∙2^{index}' + output1
    a = int(n) * (2 ** index)
    # Составляем вторую формулу
    output2 = str(a) + output2
    # Находим результат
    result += a

# Выводим красивый результат
print(f'\033[93m{binary_num}(2) \033[39m= \033[94m{output1} \033[39m= \033[92m{output2} \033[39m= \033[93m{result}(10)')

# Evaluation: OK. Отдельный мегареспект за форматированный вывод!