a = int(input())
if a < 0:
    print('Введите неотрицательное чило!')
    exit(-1)

if a <= 2:
    print(a / 10.5)
else:
    print((a - (10.5 * 2)) / 4 + 2)


