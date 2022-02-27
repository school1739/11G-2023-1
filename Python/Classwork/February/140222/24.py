with open("24-1.txt") as file:
    a = file.read().strip()
seq = list(map(len, a.split("A")))
result = max(map(sum, zip(seq, seq[1:]))) + 1 if len(seq) > 1 else len(a)

print(result)
