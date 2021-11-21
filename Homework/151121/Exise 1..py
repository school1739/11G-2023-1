maximum = int(input("введите число - ")) # число введенное пользователем

for row in range(1, maximum + 1):# составляем таблицу умножения от единицы до десяти.
    for column in range(row, row * maximum + 1, row):
        print("%4i" % column, end='\t')
    print()
    # column(столбик)
    # row(ряд)