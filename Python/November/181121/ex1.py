entered_number = int(input("enter the number"))
remnant = ''
result = ''

# цикл, определяющий остаток, результат от деления и число после деления на 2
while entered_number > 0:
    remnant = str(entered_number % 2)
    print(entered_number, "/ 2 =", entered_number // 2, "remnant:", remnant)

    result = remnant + result
    entered_number = entered_number // 2

print("finish = 0\nnumber in binary view:", result)

# Evaluation: OK