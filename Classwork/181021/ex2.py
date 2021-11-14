a = int(input())
if a < 0:
    print("Введите неотрицательное число")
    exit(-1)
elif a <= 2:
    print(a * 10.5)
else:
    print ((a - 2) * 4 + (10.5 * 2))

# Evaluation: OK. Зачем дробная часть?