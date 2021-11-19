binary_number = int(input('ENTER THE NUMBER IN BINARY VIEW:'))

# разбиение числа на элементы, перемещенные в список
x = [int(a) for a in str(binary_number)]

dlina_of_list = len(x)
result = 0
number_in_list = 0

# цикл для подсчета числа
for i in range(0, dlina_of_list):
    dlina_of_list -= 1
    result = result + x[number_in_list] * 2 ** dlina_of_list
    number_in_list += 1

print(binary_number, "(2)", "=", result, "(10)")
