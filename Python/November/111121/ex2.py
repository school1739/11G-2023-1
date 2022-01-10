print("Введите цены в долларах")
prices = []
while (price := input()) != '':
    prices.append(float(price))
summa = round(summa / 5) * 5
print(f'Округленная сумма: {summa/100}' )

# Evaluation: NOT OK
# Traceback (most recent call last):
#   File "python.21-22-1\Homework\November\111121\ex2.py", line 5, in <module>
#     summa = round(summa / 5) * 5
# NameError: name 'summa' is not defined