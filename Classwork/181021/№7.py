dlina1 = int(input("Введите длину первой стороны:"))
dlina2 = int(input("Введите длину второй стороны:"))
dlina3 = int(input("Введите длину третьей стороны:"))
if dlina1 == dlina2 == dlina3:
    print("Трейгольник равносторонний")
elif dlina1 == dlina2 or dlina1 == dlina3 or dlina2 == dlina3:
    print("Трейгольник равнобедренный")
else:
    print("Трейгольник разносторонний")
