n = 0
total = 0
entering = True

print("Введите числа")
while entering:
    x = float(input())
    if x == 0:
        entering = False
    else:
        total += x
        n += 1

if n == 0:
    print("Не было введено чисел.")
else:
    avg = total / n
    print("Среднее значение введённых чисел: %.4f" % avg)

# Evaluation: +-OK. Многовато цифр после запятой.