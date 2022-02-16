from datetime import datetime
from math import fmod

# Начало отсчёта времени
start = datetime.now()

s = open("24-2.txt").read()
count = 0
max_count = 0

for i in s:
    if (i == 'A' and fmod(count, 2) == 0) or \
            (i == 'B' and fmod(count, 2) == 1):
        count += 1
        # maxcount = max(count, max_count) - Занимает много времени поэтому отсавил вариантБ который списал у вас
        if count > max_count:
            max_count = count
    elif i == 'A':
        count += 1
    else:
        count = 0
print(max_count)

# Время выполнения программы
print("Time:  ", datetime.now() - start)
