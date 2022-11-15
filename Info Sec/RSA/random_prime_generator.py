# Генерация больших простых чисел
# https://ru.wikipedia.org/wiki/%D0%A2%D0%B5%D1%81%D1%82_%D0%9C%D0%B8%D0%BB%D0%BB%D0%B5%D1%80%D0%B0_%E2%80%94_%D0%A0%D0%B0%D0%B1%D0%B8%D0%BD%D0%B0

import random


def _prime_test(n, k):
    if n & 1 == 0:
        return False

    t = n - 1
    s = 0
    while t & 1 == 0:
        t //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, t, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False
    return True


def random_prime(start, stop):
    while True:
        n = random.randrange(start, stop)
        if _prime_test(n, 40):
            return n
