n=int(input("Введите первое число: "))
m=int(input("Введите второе число: "))
d=0
if n>=m:
    d=m
else:
    d=n
while m%d != 0 or n%d != 0:
    d=d-1
print("Наименьший общий множитель: ", d)