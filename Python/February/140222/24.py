from math import fmod
s = open('24-1.txt').read()
count = 0
max_count = 0

for i in range(len(s)):
    if (s[i] == 'Y' and fmod(count, 3) == 0) or \
            (s[i] == 'Y' and fmod(count, 3) == 1) or \
            (s[i] == 'Z' and fmod(count, 3) == 2):
        count += 1

        if count > max_count:
            max_count = count
    elif s[i] == 'X':
        count = 1
    else:
        count = 0
    print(max_count)