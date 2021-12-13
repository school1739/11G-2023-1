# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб
# ---- ДЛЯ СТОЛОВ ----

# общее количества столов
tables_quantity = store[goods['Стол']][0]['quantity'] + store[goods['Стол']][1]['quantity']
# общая стоимости столов
tables_cost = tables_quantity * store[goods['Стол']][0]['price'] + tables_quantity * store[goods['Стол']][1]['price']
# вывод
print('Стол -', tables_quantity, 'шт, стоимость', tables_cost, 'руб')

# ---- ДЛЯ СТУЛЬЕВ ----
# общее количества стульев
chears_quantity = store[goods['Стул']][0]['quantity'] + store[goods['Стул']][1]['quantity'] + store[goods['Стул']][2]['quantity']
# общая стоимости стульев
chears_cost = chears_quantity * store[goods['Стул']][0]['price'] + chears_quantity * store[goods['Стул']][1]['price'] + chears_quantity * store[goods['Стул']][2]['price']
# вывод
print('Стул -', chears_quantity, 'шт, стоимость', chears_cost, 'руб')

# ---- ДЛЯ ДИВАНОВ ----

# общее количества диванов
sofas_quantity = store[goods['Диван']][0]['quantity'] + store[goods['Диван']][1]['quantity']
# общая стоимости диванов
sofas_cost = sofas_quantity * store[goods['Диван']][0]['price'] + sofas_quantity * store[goods['Диван']][1]['price']
# вывод
print('Диван -', sofas_quantity, 'шт, стоимость', sofas_cost, 'руб')
