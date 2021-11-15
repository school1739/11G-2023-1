d, m, y = input('Текущая дата: ').split('.')
d, m, y = int(d), int(m), int(y)

v = y

if v % 400 == 0 or (v % 4 == 0 and v % 100 != 0):
    print('високосный год')
else:
    print('не високосный год')

if m == 4 or m == 6 or m == 9 or m == 11:
    h == 30
if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    h == 31
if y < 0:
    print('Ошибка ввода даты.')
    if m < 0 or m > 12:
        print('Ошибка ввода даты.')
    if d < 0 or d > 31:
        print('Ошибка ввода даты.')
    if h == 0 and d > 30:
        print('Ошибка ввода даты.')
    if m == 2 and v == 0 and d > 29:
        print('Ошибка ввода даты.')
    if m == 2 and v < 0 and d > 28:
        print('Ошибка ввода даты.')

if d == 31 and m == 12:
    d1 == 1, m1 == 1, y1 == y + 1
if d == 31:
    d1 == 1, m1 == m + 1, y1 == y + 1,
if d == 30 and h == 30:
    d1 == 1, m1 == m + 1, y1 == y
if d == 29 and m == 2:
    d1 == 1, m1 == 3, y1 == y
if d == 28 and m == 2 and v < 0:
    d1 == 1, m1 == 3, y1 == y
else:
    d1 == d + 1, m1 == m, y1 == y

print('Следующая дата {:0>2}:{:0>2}:{:0>4}'.format(d1, m1, y1))