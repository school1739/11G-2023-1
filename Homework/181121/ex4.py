from math import sqrt


# Формула Виета для приближения числа π
def viet_formula(prec):
    result = 1
    a = 0
    for _ in range(prec):
        a = sqrt(2 + a)
        result *= a / 2
    result = 2 / result
    return result


# Формула Валлиса
def wallis_formula(prec):
    result = 1
    for i in range(1, prec + 1):
        a = 4 * (i ** 2)
        result *= a / (a - 1)
    result *= 2
    return result


# Ряд Лейбница
def leibniz_formula(prec):
    result = 0
    for i in range(prec):
        result += ((-1) ** i) / (2 * i + 1)
    result *= 4
    return result


# Составляем словарь с функциями формул и их номерами
formulas = {
    '1': viet_formula,
    '2': wallis_formula,
    '3': leibniz_formula
}

# Получаем номер формулы
formula = input('''
Выберите формулу (напишите номер)
1. Формула Виета для приближения числа π
2. Формула Валлиса
3. Ряд Лейбница
''')

# Не знаю, как производить вычисления до определённого знака после запятой, поэтому вводить надо количество итераций
iterations = int(input('Количество итераций (чем больше, тем точнее): '))

# Берём из словаря функцию с введённым номером и выводим результат
print(formulas[formula](iterations))
