with open("24-1.txt") as f:
    s = f.read().strip()
seq = list(map(len, s.split("A")))
result = max(map(sum, zip(seq, seq[1:])))+1 if len(seq) > 1 else len(s)

print(result)