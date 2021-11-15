print("Введите все цены в долларах")
prices = []
while (price := input()) !='':
    prices.append(float(price))
summa = sum(prices)*100
summa = round(summa/5)*5
print(f'Округленная сумма:{summa/100}')