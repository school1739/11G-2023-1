summary = 0
price = None

# ввод цен и расчет суммы пока введенная цена не равна нулю
while price != 0:
    price = int(input("Вводите цену целым числом центов!"))
    summary += price

print("total price:", summary, "cents")

# округление суммы для оплаты наличными
summary = int(summary / 5) * 5 + (5 if (summary % 5) > 2.5 else 0)

print("for payment by cash:", summary, "cents")

# Evaluation: OK