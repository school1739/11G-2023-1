print("Введите цены товаров")
entering = True
total = 0

while entering:
    s = input()
    if s == "":
        entering = False
    else:
        x = float(s)
        if x > 0:
            total += x

print("Общая сумма: %.2f" % total)
cents_cost = total * 100
remainder = cents_cost % 5
if cents_cost % 5 < 2.5:
    cents_cost -= remainder
else:
    cents_cost += 5 - remainder
to_pay = cents_cost / 100
print("К оплате: %.2f" % to_pay)
