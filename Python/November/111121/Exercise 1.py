# Ввод чисел
a=int(input())
b = 0
c = 0
# Вводим условие
if a==0:
    print("Ошибка")
else:
# Вводим цикл
    while a!=0:
        b= b + a
        c= c + 1
        a=int(input())
# Ввыводим результат
print(b / c)

# Evaluation: +- OK. Пользователю не понятно, что от него хотят. Ни подсказки для ввода, ни для ответа.
# Also, в строках 11-13 отступы косячные. Должно быть 4 пробела или 1 Tab.