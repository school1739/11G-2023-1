
a = int(input())
b = 0
c = 0
if a == 0:
    print("ValueError")
else:
    while a != 0:
        a = int(input())
        b+=1
        c+=a
print(c/b)

# Evaluation: NOT OK. 0 считается только концом строки, не входит в подсчёт среднего.