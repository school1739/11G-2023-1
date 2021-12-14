min = int(input("Мин. значение: "))
max = int(input("Макс. значение: "))
print('', end="\t")
for i in range(min, max + 1):
    print(i, end="\t")
print()
for i in range(min, max + 1):
    print(i, end="\t")
    for g in range(min, max + 1):
        print(g * i, end="\t")
    print()

# Evaluation: OK