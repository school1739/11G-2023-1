s = open('24-1.txt').read()

max_count = 0
count = 1
last_symbol = ''
currently_symbol = ''

for i in range(len(s)):
    last_symbol = s[i-1]
    currently_symbol = s[i]
    if last_symbol != currently_symbol:
        count += 1
    else:
        if max_count <= count:
            max_count = count
        count = 1

    print('count={}, max_count={}'.format(count, max_count))
print(max_count)

# OK