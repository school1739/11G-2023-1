bottle_s = int(input("Введите количество бутылок 1 литр и меньше "))
bottle_b = int(input("Введите количество бутылок, которые больше одного литра "))
cost_bottle_small=bottle_s*0.10
cost_bottle_big=bottle_b*0.25
print(str(cost_bottle_small+cost_bottle_big)+"₽")