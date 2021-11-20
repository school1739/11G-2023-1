n = int(input("Введите число, до которого хотите увидеть таблицу умножения: "))
# Выводим номера столбцов
print(' ', end='\t')
for i in range(1, n+1): #Номера столбцов
    print(i, end='\t')
print()

for i in range(1, n+1):
    print(i, end='\t') #Номер строки
    for m in range(1, n+1):
        print(i * m, end='\t')
    print()