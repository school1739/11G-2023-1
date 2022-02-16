file = open('24-2.txt')
s = fail.read()
zachem = s.split('E')
x =-1
for i in zachem:
    if i.count('A')>=3:
        x = max(len(i), x)
print(x)