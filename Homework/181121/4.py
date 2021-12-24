def pi_viet(it):
    result = 1
    a = 0
    for i in range(it):
        a = (2 + a) ** 0.5
        result *= a / 2
    return 2 / result


def pi_wallis(it):
    result = 2
    for i in range(1, it + 1):
        a = 4 * (i ** 2)
        result *= a / (a - 1)
    return result


def pi_leibniz(it):
    result = 0
    sign = 1
    for i in range(it):
        result += sign / (2 * i + 1)
        sign *= -1
    return 4 * result


algs = [
    pi_viet,
    pi_wallis,
    pi_leibniz
]

alg_index = int(input('''
Выберите алогритм вычисления:
1. Формула Виета для приближения числа π
2. Формула Валлиса
3. Ряд Лейбница
'''))
e = int(input("Введите точность (число знаков после запятой): "))
iters = int(input("Введите количестве итераций: "))

pi = algs[alg_index - 1](iters)
print("π ≈", round(pi, e))
