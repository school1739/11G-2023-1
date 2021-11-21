# Вводим значения
n, m = int(input('n: ')), int(input('m: '))

# import math
# print(math.gcd(n, m))

d = min(n, m)
while n % d != 0 or m % d != 0:
    d -= 1
print(f'НОД n и m = {d}')
