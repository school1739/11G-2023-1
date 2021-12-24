import random
x=0
b = ["O","P"]#орла и решку в список запихал
for i in range(10):
    a = 0
    c = []  # список для победы
    while "OOO" not in c and "PPP" not in c:#цикл для победы
        v = random.choice(b)
        if v == "O":
            c+="O"
        else:
            c+="P"
            # проверка списка
        c = "".join(c)
        x+=1# счетчик для среднего значения
        a += 1  # счетчик
    print(f"{' '.join([str(i) for i in c])} (Попыток: {a})")
print(f"Среднее кол-во попыток- {x//10}")

# Evaluation: OK