# Чтение файла
f = open('26.txt')
data = f.readlines()
f.close()

# Получение информации об объеме хранилища и числе пользователей
head = data[0].split()
s = int(head[0])
n = int(head[1])

# Составление массива
volumes = []
for i in range(1, n + 1):
    volumes.append(int(data[i]))

# Сортировка массива по возрастанию
volumes = sorted(volumes)

# Определние максимального числа файлов и вычисление общего объёма
max_1 = 0
max_2 = 0
while max_2 < n and max_1 + volumes[max_2] < s:
    max_1 += volumes[max_2]
    max_2 += 1
print(max_2)
reserve = s - max_1
biggest = volumes[max_2 - 1]
max_volume = 0

for i in range(n):
    if volumes[i] - biggest <= reserve:
        max_volume = volumes[i]

print(max_volume)
