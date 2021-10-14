print("Введите сумму заказа")
_1sum = int(input())
nalog = 0.18*_1sum
chay = 0.18*_1sum
print("Налог:" + str(round(nalog, 2)) + "\nЧаевые:"+ str(round(chay, 2)) + "\nИтог" + str(round(nalog + chay+_1sum, 2)))