a=int(input())
b=0
c=a
# условие вывода ошибки
if a==0:
   print(ValueError)
else:
# цикл ввода новых переменных
    while a!=0:
        a=int(input())
        b+=1
        c+=a
print(c/b)