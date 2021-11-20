input_string = input('Input binary number:')

# Определяем наивысший показатель степени для двоичного числа
power = len(input_string)-1

# создаем переменные для хранения выходных результатов
output1 = []
output2 = []
result = 0

# цилк по каждой цифре двоичного числа начиная с высшего порядка
for char in input_string:
    # проверяем, что цифра двоичная
    if char != '0' and char != '1':
        print("Error!")
        exit()

    # добавляем результаты в переменные
    output1.append('{}*2^{}'.format(char, power))
    temp = int(char) * 2 ** power
    output2.append(str(temp))
    result += temp

    # уменьшаем показатель степени
    power -= 1

# Выводим результат
print('{}(2) = {} = {} = {}'.format(input_string, '+'.join(output1), '+'.join(output2), result))

exit()