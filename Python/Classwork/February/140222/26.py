file = open('26.txt')
data = file.readlines()
a = data[0].split()
a = int(a[0])
del (data[0])

for i in range(0, len(data)):
    data[i] = int(data[i])
data = sorted(data)
sum = 0

for count in range(0, len(data)):
    if sum + data[count] > a: break
    sum += data[count]
print(count)
costyl = a - sum

for i in range(0, len(data)):
    if data[i] - data[count - 1] <= costyl:
        result = data[i]
print(result)
