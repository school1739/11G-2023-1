import random
a = 0
b = 0
for i in range(100):
    num = random.randint(1,100)
    if num > b:
        print(num, "<=update")
        b = num
        a +=1
    else:
        print(num)
        i+=1
print(f"Макс значение в ряду:100"f"\кол-во смен макс значения:{a}")