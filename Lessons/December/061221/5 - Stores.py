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

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

lamp_code = goods['Лампа'] #Переменная, которая является содердимым кода предмета мебели
lamps_item = store[lamp_code][0] #Переменная, которая является данными о предмете мебели на складе
lamps_quantity = lamps_item['quantity'] #Переменная численного количества предмета мебели
lamps_price = lamps_item['price'] #Переменная стоиомсти 1 предмета мебели
lamps_cost = lamps_quantity * lamps_price #Находим цену всех данных предметов мебели
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб') #Выводим
#В других частях хода комментирование тоже самое

table_code_0 = goods['Стол']
tables_item_0 = store[table_code_0][0]
tables_quantity_0 = tables_item_0['quantity']
tables_price_0 = tables_item_0['price']
tables_cost_0 = tables_quantity_0 * tables_price_0

table_code_1 = goods['Стол']
tables_item_1 = store[table_code_1][1]
tables_quantity_1 = tables_item_1['quantity']
tables_price_1 = tables_item_1['price']
tables_cost_1 = tables_quantity_1 * tables_price_1

tables_quantity = tables_quantity_0 + tables_quantity_1
tables_cost = tables_cost_0 + tables_cost_1
print('Стол -', tables_quantity, 'шт, стоимость', tables_cost, 'руб')


sofa_code_0 = goods['Диван']
sofas_item_0 = store[sofa_code_0][0]
sofas_quantity_0 = sofas_item_0['quantity']
sofas_price_0 = sofas_item_0['price']
sofas_cost_0 = sofas_quantity_0 * sofas_price_0

sofa_code_1 = goods['Диван']
sofas_item_1 = store[sofa_code_1][1]
sofas_quantity_1 = sofas_item_1['quantity']
sofas_price_1 = sofas_item_1['price']
sofas_cost_1 = sofas_quantity_1 * sofas_price_1

sofas_quantity = sofas_quantity_0 + sofas_quantity_1
sofas_cost = sofas_cost_0 + sofas_cost_1
print('Диван -', sofas_quantity, 'шт, стоимость', sofas_cost, 'руб')


chair_code_0 = goods['Стул']
chairs_item_0 = store[chair_code_0][0]
chairs_quantity_0 = chairs_item_0['quantity']
chairs_price_0 = chairs_item_0['price']
chairs_cost_0 = chairs_quantity_0 * chairs_price_0

chair_code_1 = goods['Стул']
chairs_item_1 = store[chair_code_1][1]
chairs_quantity_1 = chairs_item_1['quantity']
chairs_price_1 = chairs_item_1['price']
chairs_cost_1 = chairs_quantity_1 * chairs_price_1

chair_code_2 = goods['Стул']
chairs_item_2 = store[chair_code_2][2]
chairs_quantity_2 = chairs_item_2['quantity']
chairs_price_2 = chairs_item_2['price']
chairs_cost_2 = chairs_quantity_2 * chairs_price_2

chairs_quantity = chairs_quantity_0 + chairs_quantity_1 + chairs_quantity_2
chairs_cost = chairs_cost_0 + chairs_cost_1 + chairs_cost_2
print('Стул -', chairs_quantity, 'шт, стоимость', chairs_cost, 'руб')