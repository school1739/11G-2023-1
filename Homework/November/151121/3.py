import random
total = 0                    # Сколько попыток

for i in range(10):          # Выполняем 10 симуляций
    attempts = []
    while len(attempts) < 3 or len(set(attempts[-3:])) != 1:   # 3 последних элемента не должны будыть равны
        attempts += random.choice(('О', 'Р'))
    print(f'> {" ".join(attempts)} (попыток: {len(attempts)})') # Все попытки и их количество
    total += len(attempts)   # Складываем количество попыток и их общее количество
print(f'Среднее количество попыток: {total / 10}')# Выводим среднее значение