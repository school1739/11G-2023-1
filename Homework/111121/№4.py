a = int(input("Возраст человека: "))
sum = 0
if 3 <= a <= 12:
    sum += 150
elif 12 <= a <= 65:
    sum += 450
elif a > 65:
    sum += 250
else:
    sum = sum
while a != '':
    a = int(input())
    if 3 <= a <= 12:
        sum += 150
    elif 12 <= a <= 65:
        sum += 450
    elif a > 65:
        sum += 250
    else:
        sum = sum
print(sum)