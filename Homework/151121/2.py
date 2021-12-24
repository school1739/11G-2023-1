print("Введите два положительных числа:")
n = int(input())
m = int(input())

d = n
if m < n:
    d = m
while n % d != 0 or m % d != 0:
    d -= 1

print("Наибольший общий делитель:", d)
# Evaluation: OK