import random

average_counter = 0
for i in range(10):
    counter = 0
    # Список выпадения орлов и решек
    lst = []
    # Симуляция бросания монетки
    while "ООО" not in lst and "РРР" not in lst:
        coin = random.choice(['eagle', 'tails'])
        # Проверка на выпадение орла или решки
        if coin == 'eagle':
            lst += "О"
        else:
            lst += "Р"
        # Соединение элементов списка, чтобы цикл while смог их проверить
        lst = "".join(lst)
        # Счёт кол-ва попыток
        counter += 1
        average_counter += 1
    print(f"{' '.join([str(i) for i in lst])} (Попыток: {counter})")
print(f'Среднее количество попыток: {average_counter / 10}')

# Evaluation: OK