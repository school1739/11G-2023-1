a=int(input())
b=0
c=0
if a ==0:
    print("ошибочка")
else:
    while a !=0:
        a=int(input())
        b+=1
        c+=a
print(c/b)                                       

# Evaluation: NOT OK.
# 5
# 5
# 5
# 0
# 3.3333333333333335