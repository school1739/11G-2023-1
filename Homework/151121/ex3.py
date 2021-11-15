import random

# Всего попыток
total = 0

# Выполняем 10 симуляций
for i in range(10):
    attempts = []
    # Добавляем в попытки решку или орла пока 3 последних элемента не будут равны
    while len(attempts) < 3 or len(set(attempts[-3:])) != 1:
        attempts += random.choice(('О', 'Р'))
    # Выводим все попытки и их количество
    print(f'> {" ".join(attempts)} (попыток: {len(attempts)})')
    # Прибавляем количество попыток к их общему количеству
    total += len(attempts)

# Выводим среднее значение
print(f'Среднее количество попыток: {total / 10}')
