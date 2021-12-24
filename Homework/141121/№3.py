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

# Evaluation: NOT OK
# О Traceback (most recent call last):
#   File "/Users/bormotoon/PycharmProjects/python.21-22-1/Homework/141121/№3.py", line 14, in <module>
#     tries += 1
# NameError: name 'tries' is not defined