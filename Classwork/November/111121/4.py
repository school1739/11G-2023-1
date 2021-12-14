a = int(input("Сколько <2 лет:"))    # Переменные из условия
b = int(input("Сколько от 3 до 12:"))
c = int(input("Сколько взрослых:"))
d = int(input("Сколько >65:"))
A = a*0                              # Цена билетов из дано
B = b*150
C = c*450
D = d*250
Sum = A+B+C+D                        # Сумма всех билетов
i = 1000                             # Сумма от куда считаетсь сдача
if Sum < i:
    print(Sum, "Цена")
    print(i - Sum, "Сдача")
else:
    S = (Sum // i + 1) * i
    print(Sum, "Цена")
    print(S-Sum, "Сдача")

# Evaluation: OK