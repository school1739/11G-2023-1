s = open("24-1.txt").read()
count = 1
max_count = 0
count_of_a = 0
for symbol in s:
    if symbol == 'A':
        count_of_a += 1
        count += 1
    elif symbol != 'E':
        count +=1
    else:
        if count_of_a >= 3 and max_count < count:
            max_count = count
        count = 0
print(max_count)

# OK