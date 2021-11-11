a=int(input("Введите число"))
b=0
c=a
if a==0:
    print("ERROR")
else:
    while a !=0:
        a=int(input())
        b+=1
        c+=a
print(c/b)