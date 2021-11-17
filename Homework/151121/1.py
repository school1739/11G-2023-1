# Ввод мин. и макс. значений
min = int(input())
max = int(input())
# Отступ
print('', end="\t")
# Первая строчка табл. умножения
for i in range(min, max + 1):
    print(i, end="\t")
print()
# Табл. умножения
for i in range(min, max + 1):
    print(i, end="\t")
    for j in range(min, max + 1):
        print(j * i, end="\t")
    print()