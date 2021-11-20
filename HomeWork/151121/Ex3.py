import random

average_counter = 0
for i in range(10):
    counter = 0
    lst = []
    while "ООО" not in lst and "РРР" not in lst:
        coin = random.choice(['e', 't'])
        if coin == 'e':
            lst += "О"
        else:
            lst += "Р"
        lst = "".join(lst)
        counter += 1
        average_counter += 1
    print(f"{' '.join([str(i) for i in lst])} (Попыток: {counter})")
print(f'Среднее количество попыток: {average_counter / 10}')