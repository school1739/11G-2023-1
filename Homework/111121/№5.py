a = input("Введите 8 бит : ")
if a=="0":
    b=0
elif a=="1":
    b=1
else:
    print("Введите числа 1 или 0")
while a!="":
    a=input()
    if a=="":
        b+=0
    else:
        if a=="1":
            b+=1
        else:
            b+=0
if b%2==0:
    print("1")
else:
    print("0")