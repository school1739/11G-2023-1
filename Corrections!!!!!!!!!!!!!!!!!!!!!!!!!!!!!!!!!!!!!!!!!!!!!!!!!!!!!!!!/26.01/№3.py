import math
import random

# Функция для расёта выплаты
def delivery(x):
    summa = (10.95 + (x-1) * 2.95) * 75 # Сумма выплаты с переводом в рубли
    return f"Сколько должны заплатить рублями: {round(summa, 4)}Р"


print(delivery( int( input( "Кол-во товаров: "))))
