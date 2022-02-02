# Делаем функцию
def f(n):
    return ((10.95 + (2.95 * (n - 1))) * 75)


# Спрашиваем кол-во товаров (ввод)
n = int(input("Количество заказанных товаров: "))

# Костыль
if n == 0:
    print("Сумма доставки: 0 рублей (чел, ты)")
elif n < 0:
    print("Отдал магазину вещи, маладесь")
else:
    # Вывод
    print(f"Сумма доставки: {f(n)} рублей")

# +-OK.
# Количество заказанных товаров: 13
# Сумма доставки: 3476.2500000000005 рублей