result = ''
q = int(input("Введите десятичное число: "))
# Построение двоичной записи числа
while q!=0:
    result =str(q%2)+result
    print(f"Остаток от деления: {q%2}\t Результат: {result}")
    q = q//2
print(f"Двоичное значение ввеленного числа: {result}")

# Evaluation: OK