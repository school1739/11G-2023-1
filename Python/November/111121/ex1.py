a = int(input())
b = 0
c = a

# условие на равенство и неравенство нулю
if a == 0:
    print("ValueError")
else:
    # цикл на добавление чисел
    while a != 0:
        a = int(input())
        b += 1
        c += a
print(c / b)

# Evaluation: +-OK. Пользователю не понятно, как пользоваться. Ни подсказок, ни ответа.