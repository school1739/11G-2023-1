a = 0
# Ввод возраста, проверка на пустой ввод
while (b := input()) != '':
    b = int(b)
    # Прибавление к общей сумме стоимость билета
    if b > 65:
        a += 250
    elif b > 12:
        a += 450
    elif b > 2:
        a += 150
# Вывод общую цену и сдачу с ближайшей тысячи рублей
print(f'Общая цена: {a}')
if a % 1000 == 0:
    c = 0
else:
    c = 1000 - a % 1000
print(f'Сдача с ближайшей тысячи рублей: {c}')

# Evaluation: +- OK. Пользователю не понятно, что от него хотят. Ни подсказки для ввода, ни для ответа.