# сделать через count не получилось, не работало

a = input("Введите 8 бит (0/1): ")
if a == "0":
    b = 0
elif a == "1":
    b = 1
else:
    print("это не 0 или 1")
while a != "":
    a = input()
    if a == " ":
        b+=0
    else:
        if a == "1" :
            b += 1
        else:
            b += 0
if b % 2 == 0:
    print("1")
else:
    print("0")