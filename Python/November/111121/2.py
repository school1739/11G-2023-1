# Ввод цен
price = [float(i) for i in input("Введите цены в центах через пробел: ").split()]
# Сумма цен в долларах
print(f'Сумма цен в долларах: {sum(price)/100}')
# Округление числа до ближайших 5 центов
if sum(price)%5>2.5 and sum(price)%5!=0:
    print(f'Сумма к оплате в долларах: {(sum(price) + (5 - sum(price) % 5))/100}')
elif sum(price)%5!=0:
    print(f'Сумма к оплате в долларах: {(sum(price) - sum(price) % 5)/100}')

# Evaluation: OK