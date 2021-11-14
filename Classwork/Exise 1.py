#Условие
a=int(input())
b=0
c=a
if a==0:
   print(ValueError)
else:
    while a!=0:
        a=int(input())
        b+=1
        c+=a
print(c/b)