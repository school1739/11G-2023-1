# создал переменные
a = int(input())
b = 0
c = 0
# написал условие для нуля
if a == 0:
    print("ValueError")
else:
    while a != 0:           # написал цикл
        a = int(input())
        b+=1
        c+=a
print(c/b)
