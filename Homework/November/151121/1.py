# Ввод мин. и макс. значений
min = int(input("Введите мин. значение: "))
max = int(input("Введите макс. значение: "))
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

# Evaluation: OK
# Обрати внимание на подчёркнутые переменные min и max -- это т.н. shadowed names -- это переменные, названные так,
# что имя совпадает с названием какой-нибудь функции или метода. Такой ситуации лучше избегать.