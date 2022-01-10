n = int(input("enter the first number"))
m = int(input("enter the second number"))

d = 0

# выражаем значение d
if n >= m:
    d = m
else:
    d = n

# ищем наименьшее общее кратное
while m % d != 0 or n % d != 0:
    d = d - 1
print("Least common multiple:", d)

# Evaluation: +- OK. Мы, так-то, ищем наибольший общий делитель.