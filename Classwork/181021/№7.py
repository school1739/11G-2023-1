a=int(input("Введите пожалуйста длины сторон: "))
b=int(input())
c=int(input())
if a==b==c:
    print("Треугольник равносторонний")
elif a==b or b==c or c==a:
    print("Треугольник равнобедренный")
else:
    print("Треугольник разносторонний")