fail = open('26.txt')
data = fail.readlines()
s = data[0].split()
s = int(s[0])
del(data[0])
for i in range (0, len(data)):
    data[i] = int(data[i])
data = sorted(data)
summa = 0
for count in range (0, len(data)):
    if summa + data[count] > s: break
    summa += data[count]
print(count)
zapas = s - summa
for i in range (0, len(data)):
    if data[i] - data[count-1] <= zapas:
        itog = data[i]
print(itog)

# OK