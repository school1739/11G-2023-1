n2 = input("Введите число в двоичной записи: ")
n10 = 0
length = len(n2)
for i in range(0, length):
    n10 = n10 + int(n2[i])*(2**(length - i - 1))
print("Введенное число в десятичной записи будет равно", n10)