import math

# задал прайс лист
price_list = [0, 150, 250, 450]

bill = 0
age = int(input("возраст = (0 - окончание ввода)"))

# проверка возраста и прибавление цены за человека
while age != 0:
    if age < 3:
        None

    elif 2 < age < 13:
        bill += price_list[1]

    elif 12 < age < 65:
        bill += price_list[3]

    else:
        bill += price_list[2]

    age = int(input("возраст = "))

print("total bill:", bill, "rubles")

# вычисление сдачи с ближайшей тысячи
change = math.ceil(bill / 1000) * 1000 - bill

print("Ur change from 1000 rubles:", change, "rubles")
