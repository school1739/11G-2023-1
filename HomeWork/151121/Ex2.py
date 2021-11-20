fn = int(input("Первое положительное число: "))
sn = int(input("Второе положительное число: "))
if fn <= 0 or sn <= 0:
    print("ERROR!")
else:
    div = min(fn, sn)
    while fn % div != 0 or sn % div != 0:
        div -= 1
    print(div)