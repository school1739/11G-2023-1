import math

# Константа отвечающая за режим отладки
DEBUG_MODE = False


# Функция отладочного вывода для функций расчета
def debug_print(pi, diff):
    if DEBUG_MODE:
        print("PI={}, Difference={:.20f}".format(pi, diff))


# Вычисление по формуле Виетта
def viet(eps):
    a = math.sqrt(2)
    p = a / 2.
    pi = 2 / p
    diff = 2 * eps

    while diff > eps:
        a = math.sqrt(2 + a)
        p *= a / 2.
        _pi = 2 / p
        diff = abs(pi - _pi)
        pi = _pi

        debug_print(pi, diff)

    return pi


# Вычисление по формуле Валлиса
def vallis(eps):
    n = 1
    k = 4 / 3.
    p = 1
    pi = 2 * p

    while k - 1 > eps:
        k = 4. * n * n / (4. * n * n - 1)
        p *= k
        _pi = 2 * p
        diff = abs(pi - _pi)
        pi = _pi
        n += 1

        debug_print(pi, diff)

    return pi


# Вычисление по формуле Лейбница
def leibniz(eps):
    n = 0.
    k = 1
    s = 0
    diff = 1

    while diff > eps:
        a = k / (2 * n + 1)
        s += a
        pi = 4 * s
        diff = abs(4 * a)
        n += 1
        k *= -1

        debug_print(pi, diff)

    return pi


# Вычисление числа Пи для по заданной формуле и заданной точностью
def calculate_pi(formula, epsilon):
    if formula == 1:
        return viet(epsilon)
    elif formula == 2:
        return vallis(epsilon)
    elif formula == 3:
        return leibniz(epsilon)
    # Если номер формулы некорректен
    else:
        print("Wrong formula.")
        return -1


# Ввод пользователем номера формулы
formula = int(input("Formula (1-Viet, 2-Vallis, 3-Leibniz):"))

# Задаем число знаков после запятой
digits = int(input("PI value precision (in digits after the point):"))

if digits < 1:
    print("Wrong precision value. Number of digits must be greater than zero")
    exit()

# Вычисляем точность (нужно сделать разную в зависимости от формулы)
epsilon = 0.5 * 0.1 ** (digits)
print('Epsilon={:.20f}'.format(epsilon))

pi = calculate_pi(formula, epsilon)

if pi == -1:
    exit()

output_format = 'PI = {:.' + str(digits + 1) + 'f}'
print(output_format.format(pi))

# Evaluation: +-OK. Респект за подробное описание алгоритмов решения и наглядный вывод. Ну и за режим отладки, конечно.
# Но таки есть косяк:
# > Formula (1-Viet, 2-Vallis, 3-Leibniz):2
# > PI value precision (in digits after the point):2
# > Epsilon=0.00500000000000000097
# > PI = 3.051
# Пользователь просит точность до N знаков после запятой, программа возвращает с точностью до N+1