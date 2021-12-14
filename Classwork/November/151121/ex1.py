# ввод пользователем числа
maximum = int(input("введите число - "))

# составляем таблицу умножения
for row in range(1, maximum + 1):
    for column in range(row, row * maximum + 1, row):
        print("%4i" % column, end='\t')
    print()

# Evaluation: OK