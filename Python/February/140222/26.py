with open('26.txt') as file:
    # коррекция
    listm = list(map(int, file.read().split()))
    S, N = listm.pop(0), listm.pop(0)
    listm.sort()

    summary = 0

    # расчет максимального количества людей
    for i in range(N):
        summary += listm[i]
        if summary > S:
            break

    summary -= listm[i] + listm[i - 1]

    edge = S - summary
    last = i
    R = N

    # подбор максимального размера файла
    while R - last > 1:
        m = (R + last) // 2
        if listm[m] > edge:
            R = m
        else:
            last = m

    print(i, listm[last])