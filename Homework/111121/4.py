from math import ceil
price = 0
while True:
    # Ввод возраста
    years = input("Введите возраст посетителя: ")
    # Проверка на ввод пустого значения
    if years == '' or years == ' ':
        break
    # Сопоставление возраста с ценой билета
    elif 3 <= int(years) <= 12:
        price += 150
    elif 65 <= int(years):
        price += 250
    elif 12 < int(years) < 65:
        price += 450
print(f'Цена за билеты: {price}')
print(f"Сдача: {ceil(price/1000)*1000-price}")