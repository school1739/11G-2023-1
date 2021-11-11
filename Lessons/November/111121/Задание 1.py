sum = 0
i = 0
n = int(input())
if sum == 0 and i == 0 and n == 0:
    print("Ошибка! 0 не может быть первым числом!")
else:
    while n != 0:
        sum = sum + n
        i = i + 1
        n = int(input())
print("%.2f" % (sum / i))
