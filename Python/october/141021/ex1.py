print("Введите сумму заказа")
a=int(input())
n=0.18*a
c=0.18*a
print("Налог:+"+ str(round(n,2)) + "\nИтог:" +" "+str(round(c+n+a,2)))

# Evaluation: Не отображается сумма чаевых. Нет форматирования.