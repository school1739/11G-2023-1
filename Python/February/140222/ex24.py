result = 0

with open('24-1.txt') as file:
    while string := file.readline():
        countA, countE = 0, 0
        for char in string:
            if char == 'A':
                countA += 1
            elif char == 'E':
                countE += 1
        if countA > countE:
            result += 1

print(result)
