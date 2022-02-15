f = open("C:/Users/kaban_vovan/Downloads/26_demo.txt")
n = int(f.readline())
a = []
for s in f:
    start_process, end_process = map(int, s.split())
    print(start_process, end_process)
