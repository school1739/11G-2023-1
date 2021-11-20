# составляем таблицу умножения
for row in range(1, 11):
    for j in range(row, row * 11, row):
        print("%4i" % j, end='\t')
    print()

