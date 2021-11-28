a=int(input())
b = 0
c = 0
while a!=0:
    b = b + a
    c = c + 1
    a = int(input())
print(b / c)
if a==0:
    print("Ошибка")