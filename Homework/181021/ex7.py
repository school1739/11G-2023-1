print("Введите значения 3 сторон треугольника")
a = int(input())
b = int(input())
c = int(input())
if a == b and b == c:
    print("Это равносторонний треугольник")
elif a == b or b == c or c == a:
    print("Это равнобедренный треугольник")
else:
    print("Это разносторонний треугольник")
