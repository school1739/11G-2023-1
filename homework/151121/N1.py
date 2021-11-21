a = int(input("Введите максимальное значение"))
b = int(input("Введите мнимальное значение"))
print("", end="\t")
#первая строчка таблицы
for i in range(b,a +1):
    print(i, end="\t")
print()
#таблица
for j in range(b,a+1):
    print(j, end="\t")
    for k in range(b,a+1):
        print(k * j, end="\t")
    print()