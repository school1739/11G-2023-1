with open('26.txt') as file:
    # корректируем список
    list_of_memory = list(map(int, file.read().split()))
    S, N = list_of_memory.pop(0), list_of_memory.pop(0)
    list_of_memory.sort()

    summary = 0

    # расчет максимального количества людей
    for i in range(N):
        summary += list_of_memory[i]
        if summary > S:
            break

    summary -= list_of_memory[i] + list_of_memory[i - 1]

    edge = S - summary
    last = i
    R = N

    # подбор максимального размера файла
    while R - last > 1:
        m = (R + last) // 2
        if list_of_memory[m] > edge:
            R = m
        else:
            last = m

    print(i, list_of_memory[last])

