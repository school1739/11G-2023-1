
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

# Evaluation: NOT OK
#   File "/Homework/November/111121/ex4.py", line 13, in <module>
#     old = int(input())
# ValueError: invalid literal for int() with base 10: ''