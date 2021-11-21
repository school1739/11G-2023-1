import random

# Количество симуляций
SIMULATIONS = 100
# Всего попыток
total_attempts = 0

# Выполняем симуляции
for i in range(SIMULATIONS):
    current_attempts = 0
    last = None
    in_a_row = 1
    # Выполняем, пока не будет 3 одинаковых подряд
    while in_a_row != 3:
        # Бросаем монетку
        attempt = random.choice(('О', 'Р'))
        if attempt == last:
            in_a_row += 1
        else:
            in_a_row = 1
        last = attempt
        print(attempt, end=' ')
        current_attempts += 1
    # Выводим количество попыток в симуляции
    print(f'(попыток: {current_attempts})')
    total_attempts += current_attempts

# Выводим среднее значение
print(f'Среднее количество попыток: {total_attempts / SIMULATIONS}')
