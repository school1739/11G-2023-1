# округляем сумму до 5 %

# находим цены и сумму в центах

print("Введите цены в долларах")
prices = []
while (price := input()) != '':
    prices.append(float(price))
# округляем до 5%
summa = round(summa / 5) * 5
# выводим сумму в долларах
print(f'Округленная сумма: {summa/100}' )

# Evaluation: NOT OK
# Traceback (most recent call last):
#   File "/python.21-22-1/homework/11112021/n2.py", line 10, in <module>
#     summa = round(summa / 5) * 5
# NameError: name 'summa' is not defined