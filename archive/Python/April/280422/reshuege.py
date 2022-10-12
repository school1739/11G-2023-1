"""current = 1
maximum = 1

with open("zadanie24_2.txt", "r") as the_file:
    text = the_file.read()
    for L in range(len(text) - 1):
        if text[L] == "L" and text[L] == text[L + 1]:
            current += 1
            maximum = max(current, maximum)
        else:
            current = 1
print(maximum)
the_file.close()"""

with open("27886.txt", "r") as the_file:
    lines = the_file.readlines()
    first_line = lines.pop(0).split()
    print(first_line)

    disk_size = int(first_line[0])
    user_count = int(first_line[1])

    backup_size = 0
    backup_count = 0
    max_line = 0

    lines = [int(i) for i in lines]
    lines.sort()

    for line in lines:
        if backup_size + line <= disk_size:
            backup_size += line
            backup_count += 1
            max_line = line
            print(backup_count, backup_size, max_line)

    for line in lines:
        if (backup_size - max_line) + line <= disk_size:
            biggest_backup = line

    print(backup_count, biggest_backup)