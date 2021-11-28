# Ввод минимального и максимального значения
min = int(input("Введите мин. значение: "))
max = int(input("Введите макс. значение: "))
print('', end="\t")
# Первая строка таблици умножения
for i in range(min, max + 1):
  print(i, end="\t")
print()
  # Таблица умножения
for i in range(min, max + 1):
   print(i, end="\t")
   for j in range(min, max + 1):
       print(j * i, end="\t")
   print()