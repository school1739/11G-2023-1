# ввод сторон треугольника
a = int(input("введите первую сторону"))
b = int(input("введите вторую сторону"))
c = int(input("введите третью сторону"))

if a == b == c:
    print("треугольник - равносторонний")
elif a == b != c or a == c !=b or b == c != a:
    print("треугольник - равнобедренный")
else:
    print("треугольник - разносторонний")