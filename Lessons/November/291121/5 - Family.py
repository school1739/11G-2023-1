# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ["Папа", 190],
    ["я", 182],
    ["Мама", 170],
    ["Брат", 180],

]


# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# TODO Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
# Пример вывода на консоль:
# Общий рост моей семьи - ХХ см
print(f"Общий рост моей семьи-{sum([i[1] for i in my_family_height])}")