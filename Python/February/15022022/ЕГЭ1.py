'''
Текстовый файл состоит не более чем из 106 символов X, Y и Z. Определите длину самой длинной последовательности, состоящей из символов Y. Хотя бы один символ Y находится в последовательности.
Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
'''
s = open('24-1.txt').read()

last_symbol = ''
currently_symbol = ''
schetala = 1
maximal_schetala = 0

for i in range(len(s)):
    last_symbol = s[i-1]
    currently_symbol = s[i]
    if last_symbol != currently_symbol:
        schetala += 1
    else:
        if maximal_schetala <= schetala:
            maximal_schetala = schetala
        count = 1

    print('schetala={}, maximal_schetala={}'.format(schetala, maximal_schetala))
print(maximal_schetala)

