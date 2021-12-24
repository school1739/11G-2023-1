print("Введите все цены в долларах:")
prices = []
while (price := input()) !='':
    prices.append(float(price))
s = sum(prices)*100
s = round(s/5)*5
print(f'Округленная сумма:{s/100}')

# Evaluation: NOT OK. Требовалось округлить до ближайших 5 центов, значит последняя цифра может быть только 5 или 0.