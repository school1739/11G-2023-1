for row in range(1, maximum + 1):# составляем таблицу умножения от единицы до десяти.
    for column in range(row, row * maximum + 1, row):
        print("%4i" % column, end='\t')
    print()
    # column(столбик)
    # row(ряд)

# Evaluation: NOT OK
#Traceback (most recent call last):
# File "/python.21-22-1/homework/15 11 2021/n1.py", line 1, in <module>
#     for row in range(1, maximum + 1):# составляем таблицу умножения от единицы до десяти.
# NameError: name 'maximum' is not defined