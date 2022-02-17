# https://inf-ege.sdamgia.ru/problem?id=41001
numset = []
with open('26.txt') as file:
    n = int(file.readline())
    for string in file:
        numset.extend(map(int, string.split()))

print(numset)