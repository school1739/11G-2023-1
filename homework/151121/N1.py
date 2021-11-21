a = int(input("Введите максимальное значение"))
b = int(input("Введите мнимальное значение"))
print("", end="\t")
for i in range(b,a +1):
    print(i, end="\t")
print()
for j in range(b,a+1):
    print(j, end="\t")
    for k in range(b,a+1):
        print(k * j, end="\t")
    print()