import random
changes = 0
max_num = 0
i = 0
while max_num != 100:
    # Вывод рандомных чисел
    num = random.randint(0, 100)
    # Поиск максимального числа. "i" нужно для того, чтобы первое число не считалось обновлением
    if num > max_num and i != 0:
        max_num = num
        changes += 1
        print(f"{num} <== Обновление")
    else:
        print(num)
    i += 1
print(f"Максимальное значение в ряду: 100 "
      f"\nКоличество смен максимального значения: {changes}")




