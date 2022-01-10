a = int(input())
sum = 0
while a != "":
    if 0 <= int(a) < 3:
        sum = sum + 0
        a = input()
    elif 3 <= int(a) < 12:
        sum = sum + 150
        a = input()
    elif 12 <= int(a) < 65:
        sum = sum + 450
        a = input()
    elif int(a) >= 65:
        sum = sum + 250
        a = input()
print("Стоимость билетов:", sum, "рублей")
if sum%1000 == 0:
    print("Сдача с ближайшей 1000 рублей: 0 рублей")
else:
    print("Сдача с ближайшей 1000 рублей:", (1000 - sum % 1000), "рублей")

# Evaluation:OK. Пользователю не понятно, что нужно вводить и ч