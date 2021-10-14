dep = int(input("Начальный депозит: "))
cash1 = dep*0.4 + dep
cash2 = cash1*0.4 + cash1
cash3 = cash2*0.4 + cash2
print("Сумма в конце 1 года: ", "%.2f" % cash1 )
print("Сумма в конце 2 года: ", "%.2f" % cash2)
print("Сумма в конце 3 года: ", "%.2f" % cash3)