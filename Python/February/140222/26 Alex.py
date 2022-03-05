s = open("26 (1).txt").read()
time_start = 1633305600
time_end = time_start + 7 * 24 * 60 * 60
count = 0
time_process = [int(i) for i in range(7 * 24 * 60 * 60 + 1)]
for i in range(0, len(s), 2):
    if (int(s[i]) < time_start or int(s[i]) == 0) and (int(s[i + 1]) > time_end or int(s[i + 1]) == 0):
        count += 1
    elif int(s[i + 1]) >= time_start and int(s[i + 1]) <= time_end:
        time_process[int(s[i + 1]) - int(s[i])] = time_process[int(s[i + 1]) - int(s[i])] - 1

# print(time_end)
# if (int(s[i]) >= time_start or int(s[i])==0) and \
#             (int(s[i+1])<=time_end or int(s[i+1])==0):

#   File "\February\140222\26 Alex.py", line 7, in <module>
#     if (int(s[i]) < time_start or int(s[i]) == 0) and (int(s[i + 1]) > time_end or int(s[i + 1]) == 0):
# ValueError: invalid literal for int() with base 10: '\n'