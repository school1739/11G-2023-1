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

# # Evaluation: NOT OK. Бесконечный цикл.
# Возраст человека: 1
# 45
# 89
# 0
# 4
# 24
# авы
# Traceback (most recent call last):
#   File "/Homework/111121/№4.py", line 12, in <module>
#     a = int(input())
# ValueError: invalid literal for int() with base 10: 'авы'