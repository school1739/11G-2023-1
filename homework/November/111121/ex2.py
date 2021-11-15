print("Введите цены в долларах")
prices = []
while (price := input()) != '':
    prices.append(float(price))
summa = round(summa / 5) * 5
print(f'Округленная сумма: {summa/100}' )