
result = 0
with open('24-1.txt') as file:  # Читаем строки в файле
    for string in file:
        # Счётчик букв "A" и "E"
        countA, countE = 0, 0
        for char in string:
            if char == 'A':
                countA += 1
            elif char == 'E':
                countE += 1
        if countA > countE:
            result += 1

print(result) #Вывод результата

# OK