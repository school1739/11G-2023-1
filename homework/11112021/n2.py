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