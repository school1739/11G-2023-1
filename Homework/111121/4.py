entering = True
total = 0

print("Введите возраст всех посетителей в группе (по одному в строке):")
while entering:
    s = input()
    if s == "":
        entering = False
    else:
        age = int(s)
        if age > 2:
            if age <= 12:
                total += 150
            elif age > 65:
                total += 250
            else:
                total += 450

print("Общая сумма билетов: ₽", total, sep="")
remainder = 1000 - total % 1000
print("Сдача с тысячи: ₽", remainder, sep="")
