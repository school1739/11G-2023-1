print("Введите целое число:", end=" ")
x = int(input())

result = ""
while x > 1:
    remainder = x % 2
    result = str(remainder) + result
    x = x // 2
    print("Результат: %d, остаток от деления: %d" % (x, remainder))
result = str(x) + result

print("Двоичное представление:", result)

# Evaluation: OK