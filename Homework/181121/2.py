print("Введите число в двоичном форме:", end=" ")
x = input()

print()
print("Вы ввели число %s в двоичной системе счисления "
      "и хотите перевести его в десятичную." % x)
print("Для этого переведем его сначала в десятичную вот так:")
print(x, "(2) = ", sep="", end="")

digits = len(x)
degree = digits - 1
i = 0
result = 0
log1 = []
log2 = []

while degree >= 0:
    digit = int(x[i])
    a = digit * 2 ** degree

    log1.append("%d∙2^%d" % (digit, degree))
    log2.append(str(a))

    result += a
    i += 1
    degree -= 1

log1 = '+'.join(log1)
log2 = '+'.join(log2)

print("%s(2) = %s = %s = %d(10)" % (x, log1, log2, result))

# Evaluation: OK