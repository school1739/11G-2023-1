print("Введите сумму заказа")
f = int(input())
n = 0.18*f
c = 0.18*f
print("Налог:"+ str(round(n,2)) + "\nИтог:" + " "+str(round(c+n+f,2)))

# Evaluation: OK. Не показана сумма чаевых.