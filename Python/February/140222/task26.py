# чтение файла
f = open('26.txt')
data = f.readlines()
f.close()

# получение информации о значениях S (объём хранилища) и N (число польз-лей)
head_info = data[0].split()
s = int(head_info[0])
n = int(head_info[1])

# составление массива объёмов
volumes = []
for i in range(1, n + 1):
    volumes.append(int(data[i]))

# сортировка массива объёмов по возрастанию
volumes = sorted(volumes)

# определние максимального числа файлов и вычисление общего объёма
max_sum = 0
max_amount = 0
while max_amount < n and max_sum + volumes[max_amount] < s:
    max_sum += volumes[max_amount]
    max_amount += 1

print(max_amount)

# запас места
reserve = s - max_sum
# объём наибольшего файла из наименьших
biggest = volumes[max_amount - 1]
# максимальный размер файла
largest_volume = 0

for i in range(n):
    # раз-ца между размером текущ. файла и выбранного не должна превышать запас
    if volumes[i] - biggest <= reserve:
        largest_volume = volumes[i]

print(largest_volume)
