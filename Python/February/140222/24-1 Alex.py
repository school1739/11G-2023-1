from math import fmod

s = open("24-1.txt")
count = 0
maxcount =0
for i in range(len(s)):
    if (s[i] == 'A' and fmod(count, 3) == 0) or \
            (s[i] == 'B' and fmod(count, 3) == 1) or \
            (s[i] == 'c' and fmod(count, 3) == 2):
        count += 1
        if count> maxcount:
            maxcount=count
    elif s[i]=='A':
        count+=1
    else:
        count=0

    print(count)