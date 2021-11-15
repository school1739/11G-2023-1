# С какого по какое число будет таблица (включительно)
FROM = 1
TO = 10

# Ширина поля для вывода числа
width = len(str(TO ** 2)) + 1


# Функция для вывода чисел с выравниванием
def print_formatted(a):
    print(str(a).rjust(width), end='')


# Выводим номера столбцов
print_formatted('')
for i in range(FROM, TO + 1):
    print_formatted(i)
print()

# Создаём таблицу
for i in range(FROM, TO + 1):
    # Выводим номер строки
    print_formatted(i)
    # Выводим всю строку
    for j in range(FROM, TO + 1):
        print_formatted(i * j)
    print()
