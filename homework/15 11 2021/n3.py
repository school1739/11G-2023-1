import random
total = 0

for i in range(10):
    attempts = []# (попытки)
    # Добавляем в попытки решку или орла пока 3 последних элемента не будут равны
    while len(attempts) < 3 or len(set(attempts[-3:])) != 1:

        attempts += random.choice(('О', 'Р'))
    print(f'> {" ".join(attempts)} (попыток: {len(attempts)})')# Выводим все попытки и их количество
    total += len(attempts) # Прибавляем количество попыток к их общему количеству

print(f'Среднее количество попыток: {total / 10}')

# ps: (I did my best)

# ищем наименьшее общее кратное
while m % d != 0 or n % d != 0:
    d = d - 1
print("Наименьший общий множитель:", d)