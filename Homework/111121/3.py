x0 = 0
y0 = 0
xa = 0
ya = 0
p = 0

print("Введите первую координату X:", end=" ")
x0 = float(input())
print("Введите первую координату Y:", end=" ")
y0 = float(input())

xa = x0
ya = y0
xb = x0
yb = y0

entering = True
while entering:
    print("Введите следующую координату X (Enter для окончания ввода):", end=" ")
    s = input()
    if s == "":
        entering = False
    else:
        xb = float(s)
        print("Введите следующую координату Y:", end=" ")
        yb = float(input())
        p += ((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5
        xa = xb
        ya = yb

p += ((x0 - xa) ** 2 + (y0 - ya) ** 2) ** 0.5

print("Периметр многоугольника равен %.2f" % p)
