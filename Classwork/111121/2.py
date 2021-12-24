price = input("Введите цены:")
sum=0
while price !=' ':
    sum+=int(price)
print(sum)

# Evaluation: NOT OK. Бесконечный цикл
# Введите # цены: 12
# 13
# 1
#
# 0
# f
# 4e32
# vcas
# 1
# 3
# Traceback(most # recent # call # last):
# File # "/Classwork/111121/2.py", line # 4, in < module > # sum += int(price)
# KeyboardInterrupt
# # Process # finished
# with exit code 130 (interrupted by signal 2: SIGINT)