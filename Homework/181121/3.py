from random import randint

updates = 0
repeats = 100

numbers = []

x = randint(1, 100)
max_number = x
numbers.append(x)
print(x)

repeats -= 1
for k in (range(repeats)):
    x = randint(1, 100)
    numbers.append(x)
    end_str = "\n"

    if x > max_number:
        max_number = x
        updates += 1
        end_str = " <== Обновление\n"

    print(x, end=end_str)
print("Максимальное значение в ряду:", max_number)
print("Количество смен максимального значения:", updates)

# Evaluation: OK