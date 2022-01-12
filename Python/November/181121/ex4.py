from math import sqrt
from decimal import Decimal, getcontext


# Формула Виета для приближения числа π
def viet_formula(iters):
    result = Decimal(1)
    a = Decimal(0)
    for _ in range(iters):
        a = (2 + a).sqrt()
        result *= a / 2
    result = 2 / result
    return result


# Формула Валлиса
def wallis_formula(iters):
    result = Decimal(1)
    for i in range(1, iters + 1):
        a = Decimal(4 * (i ** 2))
        result *= a / (a - 1)
    result *= 2
    return result


# Ряд Лейбница
def leibniz_formula(iters):
    result = Decimal(0)
    for i in range(iters):
        result += (-1) ** i / Decimal(2 * i + 1)
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

# Не знаю как производить вычисления до определённого знака после запятой, поэтому вводить надо количество итераций
# и знаков после запятой при вычислениях
iterations = int(input('Количество итераций: '))
precision = int(input('Знаков после запятой при вычислениях: '))
getcontext().prec = precision + 1
# Берём из словаря функцию по введённому номеру и выводим результат
print(formulas[formula](iterations))

# Evaluation: OK