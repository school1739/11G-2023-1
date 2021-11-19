# Ввод данных
a = int(input("Введите мининамальное значение: "))
b = int(input("Введите максимальное значение: "))
print('', end="\t")
# Ввод цикла
for i in range(a, b + 1):
    print(i, end="\t")
print()
# Ввод цикла
for i in range(a, b + 1):
    print(i, end="\t")
    for с in range(a, b + 1):
        print(с * i, end="\t")
    print() #Вывод таблицы умножения