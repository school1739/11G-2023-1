cost = input("Введите все цены в центах: ")
sum = int(cost)
while cost!=" ":
    cost = input()
    sum+=int(cost)
print("Общая сумма покупки в долларах: ", sum/100)
if sum%5 <= 2.5:
    print("К оплате налом: ", (sum-(sum%5))/100)
else:
    print("К оплате налом: ", (sum + 10-(sum%5))/100)
