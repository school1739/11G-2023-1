# https://inf-ege.sdamgia.ru/problem?id=35915

numset = list(open('26.txt').read().split())  # прочитал файл
nums_count = int(numset.pop(0))  # зачем-то выделил количество
numset_set = set([int(i) for i in numset])  # конвертировал str в int, закинул в сет

odd_numset = set()  # сет для нечётных
avg_numset = set()  # сет для подходящих средних

for num in range(nums_count):  # итерируемся зачем-то по количеству
    if int(numset[num]) % 2 == 1:  # проверяем на нечётность
        odd_numset.add(int(numset[num]))  # если нечётный - кидаем в сет нечётных

odd_list = list(odd_numset)  # возвращаем в список, чтобы потом обращаться к элементам

for oddNum in range(len(odd_list) - 1):  # -1 потому что не до последнего, иначе сам с собой сравнивается в конце
    for oddNum2 in range(oddNum + 1, len(odd_list)):  # +1 чтобы не сравнивать с самим собой в начале
        current_avg = (odd_list[oddNum] + odd_list[oddNum2]) / 2  # нашел среднее
        if int(current_avg) in numset_set:  # проверил наличие в изначальном сете из списка
            avg_numset.add(current_avg)  # если да, добавил в сет средних

print(int(len(avg_numset)))  # длина списка подходящих средних = количество подходящих пар
print(int(max(avg_numset)))  # максимальное из списка подходящих средних