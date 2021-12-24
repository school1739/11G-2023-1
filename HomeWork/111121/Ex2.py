print("Введите все цены в долларах")
prices = []
while (price := input()) !='':
    prices.append(float(price))
summa = sum(prices)*100
summa = round(summa/5)*5
print(f'Округленная сумма:{summa/100}')

# Evaluation: NOT OK. Требовалось округлить до 5 центов, а, значит, последняя цифра может быть 5 или 0.
# Введите все цены в долларах
# 12
# 13
# 14
#
# Округленная сумма:39.0