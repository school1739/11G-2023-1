
old = int(input("Возраст человека: "))
sum = 0
if 3 <= old <= 12:
    sum += 150
elif 12 <= old <= 65:
    sum += 450
elif old > 65:
    sum += 250
else:
    sum = sum
while old != '':
    old = int(input())
    if 3 <= old <= 12:
        sum += 150
    elif 12 <= old <= 65:
        sum += 450
    elif old>65:
        sum += 250
    else:
        sum = sum

print(sum)