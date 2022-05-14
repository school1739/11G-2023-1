import math
import random

# Функция для расёта выплаты
def tariff(km):
    coeff = random.uniform(1, 2.5)#Повышение кооф
    summa = 4 * coeff + math.ceil(km / 1000 / 150) * 0.25#Сумма
    return f"Вы должны заплатить: {round(summa, 3)}Р"#Чек
print(tariff(float(input("Введите пройденное расстояние в километрах: "))))
