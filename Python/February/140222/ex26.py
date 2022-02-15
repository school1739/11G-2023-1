from itertools import groupby
from operator import itemgetter

tickets = []
with open('26.txt') as file:
    n = int(file.readline())
    for _ in range(n):
        tickets.append(tuple(map(int, file.readline().split())))

tickets.sort(key=lambda ticket: (-ticket[0], ticket[1]))

for row, seats in ((row, list(map(itemgetter(1), tickets)))
                   for row, tickets
                   in groupby(tickets, itemgetter(0))):
    for i in range(len(seats) - 1):
        if seats[i + 1] - seats[i] == 3:
            print(row, seats[i] + 1)
            exit(0)
