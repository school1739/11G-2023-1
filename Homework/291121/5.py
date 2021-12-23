# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ["мама", "папа", "брат"]


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['мама', 160],
    ['папа', 180],
    ['брат', 140]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
dad_index = -1
i = 0
max_i = len(my_family_height)
while dad_index == -1 and i < max_i:
    if my_family_height[i][0] == "папа":
        dad_index = i
if dad_index != -1:
    print("Рост отца - %d см" % my_family_height[dad_index][1])

sum = 0
for x in my_family_height:
    sum += x[1]
print("Общий рост моей семьи - %d см" % sum)
# Пример вывода на консоль:
# Общий рост моей семьи - ХХ см

# Evaluation: NOT OK. Бесконечный цикл.