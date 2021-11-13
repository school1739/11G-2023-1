d = int(input("Длина первой стороны "))
d2 = int(input("Длина второй стороны "))
d3 = int(input("Длина третьей стороны "))
if d1 == d2 == d3:
    print("Равносторонний ")
elif d1 == d2 or d1 == d3 or d2 == d3:
    print("Равнобедренный")
else:
    print("разносторонний ")

# Evaluation: NameError: name 'd1' is not defined