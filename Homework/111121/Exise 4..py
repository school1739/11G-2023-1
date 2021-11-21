total = 0
# Вводим возраст пока не будет пустая строка
while (age := input()) != '':
    age = int(age)
    # Прибавляем к общей сумме стоимость билета в зависимости от возраста
    if age > 65:
        total += 250
    elif age > 12:
        total += 450
    elif age > 2:
        total += 150
# Выводим общую цену и сдачу с ближайшей тысячи рублей
print(f'Общая цена: {total}')
if total % 1000 == 0:
    change = 0
else:
    change = 1000 - total % 1000
print(f'Сдача с ближайшей тысячи рублей: {change}')
# total (подсчет суммы)
# age (возраст)
# change (сдача)
