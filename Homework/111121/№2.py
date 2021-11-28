print("Введите все цены в долларах:")
prices = []
while (price := input()) !='':
    prices.append(float(price))
s = sum(prices)*100
s = round(s/5)*5
print(f'Округленная сумма:{s/100}')