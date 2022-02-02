"""Интернет-магазин предоставляет услугу экспресс-доставки для части
своих товаров по цене $10,95 за первый товар в заказе и $2,95 – за все
последующие. Напишите функцию, принимающую в качестве единствен-
ного параметра количество товаров в заказе и возвращающую общую
сумму доставки. В основной программе должны производиться запрос
количества позиций в заказе у пользователя, и отображаться на экране
сумма доставки (сумму перевести в рубли по курсу $1 = 75₽."""

def value_of_delivery(number_of_items):
    payment_for_delivery = 10.95 * 75 + 2.95 * (number_of_items - 1) * 75
    return payment_for_delivery

round_of_value_delivery = round(value_of_delivery(number_of_items=int(input("enter the number of items - "))), 2)

print("payment for delivery - ", round_of_value_delivery, "rubles")