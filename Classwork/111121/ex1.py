n=int(input())
sum=0
k=0
if n==0:
    print("error")
else:
    while n !=0:
        sum+=k
        k+=1
        n = int(input())
print(sum/k)

# Evaluation: NOT OK
# 5
# 5
# 5
# 0
# 1.0