f = open('26.txt')
data = f.readlines()
s = data[0].split()
s = int(s[0])
del (data[0])
for i in range(0, len(data)):
    data[i] = int(data[i])
data = sorted(data)
sum = 0
for count in range(0, len(data)):
    if sum + data[count] > s: break
    sum += data[count]
print(count)
zapas = s - sum
for i in range(0, len(data)):
    if data[i] - data[count - 1] <= zapas:
        result = data[i]
print(result)