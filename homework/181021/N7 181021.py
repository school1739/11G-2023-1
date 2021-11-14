a = int(input("введите 1 сторону"))
b = int(input("введите 2 сторону"))
c = int(input("введите 3 сторону"))
if a == b == c:
    print("Треугольник равносторонний")
elif a == b !=c or a == c !=b or c == b != a:
    print("Треугольник равнобедренный")
else:
    print("Треугольник разносторонний")

# Evaluation: OK