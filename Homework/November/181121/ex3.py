import random

# list = [random.randint(1, 100) for i in range(100)]
#
# maximum = -1
# counter = 0
#
# for i in list:
#     if i > maximum:
#         maximum = i
#         counter += 1
#         print("{} <== new maximum".format(i))
#     else:
#         print(i)
# print(counter)
# exit()


number_of_update = 0
current_maximum = 0

# цикл создания случайного числа
for i in range(100):

    # генерируем случайное число от 1 до 100
    number = random.randint(1, 100)

    # определяем, является ли число новым максимумом
    if number > current_maximum:
        print(number, "<== update")
        number_of_update += 1
        current_maximum = number
    else:
        print(number)

print("max of numbers:", current_maximum)
print("number of updates:", number_of_update)
