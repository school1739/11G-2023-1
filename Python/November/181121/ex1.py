# Рекурсивная функция для перевода из десятичной системы счисления в двоичную
def to_binary(decimal):
    if decimal == 0:
        return ''
    # Находим частное и остаток от деления decimal на 2
    quotient, mod = divmod(decimal, 2)
    # Выводим их
    print(f'{decimal} / 2 = {quotient}, остаток: {mod}')
    # Продолжаем рекурсию
    return to_binary(quotient) + str(mod)


# Вводим число
num = int(input('Введите число: '))
# Выводим результат
print(f'Число в двоичном представлении: {to_binary(num)}')

# Evaluation: OK