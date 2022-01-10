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

# Evaluation: NOT OK. Что за числа 1 или 0? Почему вываливается с ошибкой?
# Введите 8 бит : 11001100
# Введите числа 1 или 0
# 1
# Traceback (most recent call last):
#   File "/Users/bormotoon/PycharmProjects/python.21-22-1/Homework/111121/№5.py", line 14, in <module>
#     b+=1
# NameError: name 'b' is not defined