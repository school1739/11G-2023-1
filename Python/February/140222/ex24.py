"""
Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт.
Строки содержат только заглавные буквы латинского алфавита (ABC...Z).
Определите количество строк, в которых буква A встречается чаще, чем буква E.
"""

result = 0

# Читаем строки в файле
with open('24-1.txt') as file:
    for string in file:
        # Считаем количество букв "A" и "E"
        countA, countE = 0, 0
        for char in string:
            if char == 'A':
                countA += 1
            elif char == 'E':
                countE += 1
        if countA > countE:
            result += 1

print(result)
