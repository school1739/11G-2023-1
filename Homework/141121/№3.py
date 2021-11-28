import random
m = [1, 2]
a = 0
t = 0
while a != 3:
    ran = random.choice(m)
    if ran==1:
        a += 1
        print("Р", end=" ")
        tries += 1
    else:
        a += 0
        print("О", end=" ")
        tries += 1

print("Попытки: ", t)